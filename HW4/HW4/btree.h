#pragma once

#ifndef BTREE_H
#define BTREE_H

#include "node.h"
#include "collisionexception.h"
#include <iostream>

using namespace std;

template<class Type>
class BTree{
private:
  int size;

  Node<Type>* tree;

  CollisionException except;

public:
  //Default constructor
  BTree();

  //Overloaded constructor 
  BTree(Type* item);
  
  //Destructor
  ~BTree();

  //Insert item into the tree
  void insert(Type* item, Node<Type>* subtree = tree);
  
  //Location an item in the tree
  Type* find(Type* item, Node<Type>* subtree = tree);

  //Check for two red nodes in a row
  void checkRotation(Node<Type>* node);

  //Rotate subtree left around pivot
  void rotateLeft(Node<Type>* pivot);

  //Rotate subtree right around pivot
  void rotateRight(Node<Type>* pivot);
  
  //Get the number of nodes in the tree
  int getSize();
  
  //Get the height of the tree
  int getHeight(Node<Type>* subtree = tree);
 
};

//Default constructor
template<class Type>
BTree<Type>::BTree() {
	size = 0;
	tree = nullptr;
}

//Overloaded constructor
template<class Type>
BTree<Type>::BTree(Type* item) {
	size = 1;
	tree = new Node<Type>(item, "Black");
}

//Insert item into the tree
template<class Type>
void BTree<Type>::insert(Type* item, Node<Type>* subtree = tree) {
	if (item = find(item)) {
		throw except.collision();
	}

	if (subtree == nullptr) { subtree = new Node<Type>(item, "Black"); }
	else {
		if (item >= subtree->value) {
			if (subtree->right == nullptr) { 
				subtree->right = new Node<Type>(item, "Red", subtree);
			}
			else { 
				insert(item, subtree->right); 
			}
		}
		else {
			if (subtree->left == nullptr) { 
				subtree->left = new Node < Type(item, "Red", subtree); 
			}
			else { 
				insert(item, subtree->left); 
			}
		}
	}
	size++;
	checkRotation(subtree);
	
}

//Locate an item in the tree
template<class Type>
Type* BTree<Type>::find(Type* item, Node<Type>* subtree = tree) {
	Node<Type>* search = nullptr;
	if (subtree != nullptr) {
		if (item == subtree->value) { search = new Node<Type>(subtree); }
		else if (item >= subtree->value) { search = find(item, subtree->right); }
		else if (item < subtree->value) { search = find(item, subtree->left); }
	}
	
	return search;
}

template<class Type>
void BTree<Type>::checkRotation(Node<Type>* node){
	if (node->color == "Red" && node != tree) {

		//4 cases for rotation to occur
		
		//Cases where node has left child
		if (node->left != nullptr) {
			//If the child isn't red, do nothing
			if (node->left->color == "Red") {

				//Case where node is also a left child
				if (node->isLeftChild()) {
					//Check if node has a red sibling
					if (node->parent->right != nullptr) {
						if (node->parent->right->color == "Red") {
							node->changeColor();
							node->parent->changeColor();
							node->parent->right->changeColor();
						}
						else {
							rotateRight(node);
						}
					}
					else {
						rotateRight(node);
					}
					

				}

				//Case where node is a right child
				else if (node->isRightChild()) {

					//Check if node has a red sibling
					if (node->parent->left != nullptr) {
						if (node->parent->left->color == "Red") {
							node->changeColor();
							node->parent->changeColor();
							node->parent->left->changeColor();
						}
						else {
							//Switch node with left child
							rotateRight(node->left);
							//Left child is now parent
							rotateLeft(node->parent);
						}
					}
					else {
						//Switch node with left child
						rotateRight(node->left);
						//Left child is now parent
						rotateLeft(node->parent);
					}
				}

			}
		}
		//Cases where node has a right child
		if (node->right != nullptr) {
			//If the child isn't red, do nothing
			if (node->right->color == "Red") {

				//Case where node is also a right child
				if (node->isRightChild()) {
					//Check for a red sibling
					if (node->parent->left != nullptr) {
						if (node->parent->left->color == "Red") {
							node->changeColor();
							node->parent->changeColor();
							node->parent->left->changeColor();
						}
						else {
							rotateLeft(node);
						}
					}
					else {
						rotateLeft(node);
					}

				}
				//Case where node is a left child
				if (node->isLeftChild) {
					//Check for a red sibling
					if (node->parent->right != nullptr) {
						if (node->parent->right->color == "Red") {
							node->changeColor();
							node->parent->changeColor();
							node->parent->right->changeColor();
						}
						else {
							rotateLeft(node->right);
							rotateRight(node->parent);
						}
					}
					else {
						rotateLeft(node->right);
						rotateRight(node->parent);
					}
				}
			}
		
		}

		checkRotation(node->parent);
	}
	else if (node->color == "Red" && node == tree) {
		tree->changeColor();
	}
}

//Rotate subtree left around pivot
template<class Type>
void BTree<Type>::rotateLeft(Node<Type>* pivot) {
	Node<Type>* temp = new Node<Type>(pivot->parent);
	if (temp->which = 1) {
		temp->parent->right = pivot;
		pivot->parent = temp->parent;
		temp->parent = pivot;
	}
	temp->right = pivot->left;
	pivot->left = temp;

}

//Rotate subtree right around pivot
template<class Type>
void BTree<Type>::rotateRight(Node<Type>* pivot) {
	Node<Type>* temp = pivot->left;
	temp->parent = pivot->parent;
	if (temp->parent->left == pivot) { temp->parent->left = temp; }
	else { temp->parent->right = temp; }
	pivot->parent = temp;
	pivot->left = temp->right;
	temp->right = pivot;
	temp->changeColor();
	pivot->changeColor();
}

//Return how many nodes are in the tree
template<class Type>
int BTree<Type>::getSize() {
	return size;
}

//Return how tall the tree is
template<class Type>
int BTree<Type>::getHeight(Node<Type>* subtree = tree) {
	if (subtree == nullptr) {
		return 0;
	}
	if (subtree->left->value == nullptr && subtree->right->value == nullptr) {
		return 1;
	}

	int lHeight = getHeight(subtree->left) + 1;
	int rHeight = getHeight(subtree->left) + 1;
	if (lHeight > rHeight) {
		return lHeight;
	}
	return rHeight;
	
}

template<class Type>
BTree<Type>::~BTree() {
	//Do deletion here
	//gotta go through the entire tree and delete each node
	delete tree;
}

#endif
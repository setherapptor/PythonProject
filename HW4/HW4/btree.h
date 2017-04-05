#pragma once

#include "node.h"
#include <iostream>

using namespace std;

template<class Type>
class BTree{
private:
  int size;
  int height;

  Node<Type>* tree;

public:
  BTree();

  BTree(Type* item);
  
  ~BTree();

  void insert(Type* item, Node<Type>* subtree = tree);
  
  Type* find(Type* item, Node<Type>* subtree = tree);

  Type* remove(Type* item);

  void checkRotation(Node<Type>* subtree = nullptr);

  void rotateLeft(Node<Type>* pivot);

  void rotateRight(Node<Type>* pivot);
  
  int getSize();
  
  int getHeight();
 
};

template<class Type>
BTree<Type>::BTree() {
	height = 0;
	size = 0;
	tree = nullptr;
}


template<class Type>
BTree<Type>::BTree(Type* item) {
	height = 0;
	size = 1;
	tree = new Node<Type>(item, "Black");
}

template<class Type>
void BTree<Type>::insert(Type* item, Node<Type>* subtree = tree) {
	if (tree == nullptr) {
		tree = new Node<Type>(item, "Black");
	}
	else {
		if (subtree->value == nullptr) {
			subtree->value = item;
			subtree->color = "Red";
			subtree->left = new Node<Type>(subtree);
			subtree->right = new Node<Type>(subtree);

		}
		else if (item >= subtree->value) {
			insert(item, subtree->right);
		}
		else {
			insert(item, subtree->left);
		}
	}
	size++;
	checkRotation(Node<Type>* subtree = nullptr);
}

template<class Type>
Type* BTree<Type>::find(Type* item, Node<Type>* subtree = tree) {
	Type* search = nullptr;
	if (item == subtree->value) { search = subtree->value; }
	else if (item >= subtree->value) { search = find(item, subtree->right); }
	else if (item < subtree->value) { search = find(item, subtree->left); }
	return search;
}

template<class Type>
Type* BTree<Type>::remove(Type* item) {
	Type* search = find(item);
	Type* temp = search;
	if (search != nullptr) {
		if (search->left->value == nullptr) {
			search->right->parent = search->parent;
			if (search->parent->left == search) { search->parent->left = search->right; }
			else { search->parent->right = search->right; }
			if (search->color == "Black" && search->right->color == "Red"){search->right->color = "Black"}
		}
		else {

		}
	}
	size--;
	search->parent = search->right = search->left = nullptr;
	//checkRotation(tree);
	return search;
}

template<class Type>
void BTree<Type>::checkRotation() {

}

template<class Type>
void BTree<Type>::rotateLeft(Node<Type>* pivot) {
	Node<Type>* temp = pivot->right;
	temp->parent = pivot->parent;
	if (temp->parent->left == pivot) { temp->parent->left = temp; }
	else { temp->parent->right = temp; }
	pivot->parent = temp;
	pivot->right = temp->left;
	temp->left = pivot;
	temp->changeColor();
	pivot->changeColor();
}

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


template<class Type>
int BTree<Type>::getSize() {
	return size;
}

template<class Type>
int BTree<Type>::getHeight() {
	return height;
}

template<class Type>
BTree<Type>::~BTree() {
	//Do deletion here
}

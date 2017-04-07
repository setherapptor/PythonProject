#pragma once
#ifndef BST_H
#define BST_H

#include "node.h"
#include "collisionexception.h"
#include <iostream>
#include <string>

using namespace std;

template<class Type>
class BST {
private:
	int size;

	CollisionException except;

public:
	Node<Type>* root;

	//Default constructor
	BST();

	//Overloaded constructor
	BST(Type* item);

	//Destructor
	~BST();

	//Insert item
	void insert(Type* item, Node<Type>* branch);

	//Locate item
	Type* find(Type* item, Node<Type>* branch);

	//Remove item
	Type* remove(Type* item, Node<Type>* branch);

	//Rotate around parent
	void rotateLeft(Node<Type>* parent);

	//Rotate right around parent
	void rotateRight(Node<Type>* parent);

	//Get all items from smallest to largest
	Type* getAllAscending();

	//Get all items from biggest to smallest
	Type* getAllDescending();

	//Get all items for two above functions
	Type* getAllItems();

	//Return size of the tree
	int getSize();

	//Return height of the tree
	int getHeight(Node<Type>* branch = root);
};

#endif

//Default constructor
template<class Type>
BST<Type>::BST() {
	size = 0;
	root = nullptr;
}

//Overloaded constructor
template<class Type>
BST<Type>::BST(Type* item) {
	size = 1;
	root = new Node<Type>(item);
}

//Insert item
template<class Type>
void BST<Type>::insert(Type* item, Node<Type>* branch) {
	if (root == nullptr) {
		root = new Node<Type>(item);
	}
	else {
		if (branch->left != nullptr) {
			if (item < branch->value) {
				insert(item, branch->left);
			}
		}
		else if (branch->right != nullptr) {
			if (item > branch->value) {
				insert(item, branch->right);
			}
		}
		else if (item < branch->value) {
			branch->left = new Node<Type>(item, branch);
		}
		else if (item > branch->value) {
			branch->right = new Node<Type>(item, branch);
		}
	}
	
}

//Find item
template<class Type>
Type* BST<Type>::find(Type* item, Node<Type>* branch) {
	if (root == nullptr) {
		return nullptr;
	}

	if (branch->value == item) {
		return branch->value;
	}
	else if(branch->left != nullptr && item < branch->value) {
		return find(item, branch->left);
	}
	else if (branch->right != nullptr && item > branch->value) {
		return find(item, branch->right);
	}
	else {
		return nullptr;
	}
}

template<class Type>
Type* BST<Type>::remove(Type* item, Node<Type>* branch) {

}

template<class Type>
void BST<Type>::rotateLeft(Node<Type>* parent) {

}

template<class Type>
void BST<Type>::rotateRight(Node<Type>* parent) {

}

template<class Type>
Type* BST<Type>::getAllAscending() {

}

template<class Type>
Type* BST<Type>::getAllDescending() {

}

template<class Type>
Type* BST<Type>::getAllItems() {
	return root->value;
}

template<class Type>
int BST<Type>::getSize() {
	return size;
}

template<class Type>
int BST<Type>::getHeight(Node<Type>* branch = root) {

}
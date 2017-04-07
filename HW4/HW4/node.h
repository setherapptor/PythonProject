#pragma once
#ifndef NODE_H
#define NODE_H

#include <string>

using namespace std;

template<class Type>
class Node {
public:
	Type* value; //Stored data
	Node* parent; //Pointers to other family members
	Node* left; 
	Node* right; 

	//Default constructor
	Node();

	//Copy constructor
	Node(Node<Type>* node);

	//Fill constructor
	Node(Type* item, Node<Type>* pa = nullptr);

	bool isLeftChild();

	bool isRightChild();

	//Destructor
	~Node();
};

//Default constructor
template<class Type>
Node<Type>::Node() {
	value = nullptr;
	parent = right = left = nullptr;
}

//Copy constructor
template<class Type>
Node<Type>::Node(Node<Type>* node) {
	value = node->value;
	parent = node->parent;
	left = node->left;
	right = node->right;
}

//Fill constructor
template<class Type>
Node<Type>::Node(Type* item, Node<Type>* pa = nullptr) {
	value = item;
	parent = pa;
	left = right = nullptr;
}

//Check if left child
template<class Type>
bool Node<Type>::isLeftChild() {
	return parent->left == this;
}

//Check if right child
template<class Type>
bool Node<Type>::isRightChild() {
	return parent->right == this;
}

template<class Type>
Node<Type>::~Node() {
	//Delete stuff
	parent = left = right = nullptr;
	value = nullptr;
	delete parent, left, right, value;
}

#endif
#pragma once
#include <iostream>
#include <cmath>

template<class Type>
class Node {
public:
	Type** value;
	Node** parent, left, right;
	string color;

	Node();

	Node(Type* item, string c);

	Node(Node<Type>* p);

	void changeColor();
};

//Default constructor
template<class Type>
Node<Type>::Node(){
	value = nullptr;
	parent = left = right = nullptr;
	color = '';
}

//Constructor for creating a node with leaves
template<class Type>
Node<Type>::Node(Type* item, string c) {
	value = item; //Initialize the data
	color = c; 
	parent = nullptr; //Start with no parent
	left->value = right->value = nullptr; //Initialize data of leaves
	left->color = right->color = "Black";
	left->left = left->right = right->left = right->right = nullptr; //The leaves don't have children
	left->parent = right->parent = this; //Be able to point to this from children
}

//Constructor for making leaves
template<class Type>
Node<Type>::Node(Node<Type>* p) {
	value = nullptr;
	color = "Black";
	parent = p;
	left = right = nullptr;
}

template<class Type>
void Node<Type>::changeColor() {
	if (color == "Black") {
		color = "Red";
	}
	else {
		color = "Black";
	}
}
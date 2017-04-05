#pragma once

template<class Type>
class Node {
public:
	Type** value; //Stored data
	Node** parent, left, right; //Pointers to other family members
	string color; //Color of the node

	//Default constructor
	Node();

	//Copy constructor
	Node(Node<Type>* node);

	//Fill constructor
	Node(Type* item, string c, Node<Type>* pa = nullptr);

	//Destructor
	~Node();

	//Change color
	void changeColor();

	bool isLeftChild();

	bool isRightChild();
};

//Default constructor
template<class Type>
Node<Type>::Node() {
	value = nullptr;
	parent = right = left = nullptr;
	color = "";
}

//Copy constructor
template<class Type>
Node<Type>::Node(Node<Type>* node) {
	value = node->value;
	parent = node->parent;
	left = node->left;
	right = node->right;
	color = node->color;
}

//Fill constructor
template<class Type>
Node<Type>::Node(Type* item, string c, Node<Type>* pa = nullptr) {
	value = item;
	color = c;
	parent = pa;
	left = right = nullptr;
}

//Change color
template<class Type>
void Node<Type>::changeColor() {
	if (color == "Red") { color = "Black"; }
	else { color = "Red"; }
}

//Check if left child
template<class Type>
bool Node<Type>::isLeftChild() {
	return this->parent->left == this;
}

//Check if right child
template<class Type>
bool Node<Type>::isRightChild() {
	return this->parent->right == this;
}

template<class Type>
Node<Type>::~Node() {
	//Delete stuff
}
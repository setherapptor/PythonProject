#pragma once
#include "operationcount.h"
#include <iostream>
#include <cmath>

template<class Type>
class Node {
public:
	OperationCount opCount;
	int order;
	int size;
	Type** value;
	Node** children;

	Node(int inOrder);

	Node(Type* item, int inOrder);

	void addItem(Type* item);

	Type* removeItem(Type* item);

	Type* findItem(Type* item);

	void split();

	void print(int level);
};

template<class Type>
Node<Type>::Node(int inOrder){
	order = inOrder;
	size = 0;
	value = new Type*[order];
	children = nullptr;
}

template<class Type>
Node<Type>::Node(Type* item, int inOrder) {
	order = inOrder;
	size = 1;
	value = new Type*[order];
	for (int i = 0; i < order; i++) {
		value[i] = nullptr;
	}
	children = nullptr;
	value[0] = item;
}

template <class Type> void Node<Type>::addItem(Type * item) {
	int iterator = 0; //To store prospective location of the item
	int ops = 0; // number of ops temporary
	while (value[iterator] != nullptr && iterator < order - 1 && *item > *value[iterator]) { //Find where the item should be placed
		iterator++;
	}
	ops = iterator; //Iterator is indicative of how many objects were compared
	for (int i = order - 1; i > iterator; i--) {
		value[i] = value[i - 1]; //Shift entire array one space to the right
	}
	ops += size - iterator; //Number of ops performed in the for loop (shifting items)
	opCount.addFunction += ops; //increment operations count for add functions
	value[iterator] = item;
	size++;
}

template <class Type> Type* Node<Type>::removeItem(Type * item) {
	int iterator = 0;
	int ops = 0;
	Type * retval = nullptr; //initialize return value as nullptr
	while (iterator < order - 1) { //find the location of the object
		if (value[iterator] && *item == *value[iterator]) {
			break;
		}
		iterator++;
	}
	ops += iterator;
	retval = value[iterator];
	for (int i = iterator; i < order - 1; i++) {
		value[i] = value[i + 1];
	}
	ops += size - iterator;
	opCount.removeFunction += ops; //increment operations count for remove function
	size--;
	return retval;
}

template<class Type>
Type* Node<Type>::findItem(Type* item) {
	int iterator = 0;
	int ops = 0;
	Type * retval = nullptr; //initialize return value as nullptr
	while (iterator < order - 1) { //find the location of the object
		if (value[iterator] && *item == *value[iterator]) {
			break;
		}
		iterator++;
	}
	ops += iterator;
	retval = value[iterator];
	return retval;
}

template <class Type> void Node<Type>::split() {
	Type* search;
	Node<Type>* left = new Node(order);
	Node<Type>* right = new Node(order);
	int* count = new int[order];
	for (int i = 0; i < order; i++) {
		search = value[i];
		count[i] = 0;
		for (int k = i; k < order; k++) {
			if (search < value[k]) {
				count[i]++;
			}
		}
	}
	search = nullptr;
	for (int i = 1; i < order - 1; i++) {
		if (abs(count[i] - count[i + 1]) && abs(count[i] - count[i] - 1)) {
			search = value[i];
		}
		else if (search == nullptr) {
			left->addItem(value[i-1]);
		}
		else {
			right->addItem(value[i]);
		}
	}
}

template<class Type>
void Node<Type>::print(int level) {
	for (int i = 0; i < order; i++) {
		if (value[i] != nullptr) {
			cout << "| " << *value[i] << " |";
		}
		else {
			cout << "|  |";
		}
	}
	for (int i = 0; i < level * 2; i++) {
		cout << " ";
	}
}
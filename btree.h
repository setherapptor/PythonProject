#pragma once

#include <iostream>
#include "node.h"
#include <iostream>

using namespace std;

template<class Type>
class BTree{
private:
  int order;
  int size;
  int height;

  Node<Type>* tree;
public:
  BTree(int inOrder = 3);
  
  ~BTree();
  
  void insert(Type* item) { insert(item, tree); }

  void insert(Type* item, Node<Type>* subtree);
  
  Type* remove(Type* item);
  
  Type* find(Type* item);
  
  int getSize();
  
  int getHeight();
  
  void printTree(int level, int currChild) {printTree(level, currChild, tree);}

  void printTree(int level, int currChild, Node<Type>* in);
};

template<class Type>
BTree<Type>::BTree(int inOrder) {
	order = inOrder;
	height = 0;
	size = 0;
	tree = nullptr;
}

template<class Type>
void BTree<Type>::insert(Type* item, Node<Type>* subtree) {
	if (tree == nullptr) {
		tree = new Node<Type>(item, order);
		size++;
		return;
	}
	if (subtree->children == nullptr && subtree->size < order-1) {
		subtree->addItem(item);
	}
	else if (subtree->children == nullptr && subtree->size+1 >= order - 1) {
		subtree->split();
	}
	size++;
}

template<class Type>
int BTree<Type>::getSize() {
	return size;
}

template<class Type>
void BTree<Type>::printTree(int level, int currChild, Node<Type>* in) {
	if (in != nullptr) {
		in->print(level);
		if (currChild < order-1 && in->children != nullptr) {
			printTree(level++, currChild++, in->children[currChild++]);
		}
		cout << endl;
	}
}

template<class Type>
BTree<Type>::~BTree() {
	//Do deletion here
}

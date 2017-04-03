#pragma once
#ifndef ORDEREDLIST_H
#define ORDEREDLIST_H

#include "listexception.h"
#include "operationcount.h"
#include <iostream>
#include <stdio.h>

using namespace std;

template <class Type>
class OrderedList {
protected:
  ListException exception; //Custom exception class
  OperationCount opCount = {0,0}; //For counting the number of operations for the add/remove methods
  int max_size; //maximum size possible
  int current_size; //current size
  Type ** data_array; //underlying data array of pointers
public:
  OrderedList();

  OrderedList(int size);

  virtual void AddItem(Type * item); //So that derived classes can override

  virtual Type*  RemoveItem(Type * item); //So that derived classes can override

  virtual Type* findItem(Type* item);

  int length();

  int getCapacity();

  OperationCount getOperations();

  bool isEmpty();

  bool isFull();

  Type* getParent();

  virtual void makeEmpty();
};

template <class Type> OrderedList<Type>::OrderedList(){
  max_size = 1;
  current_size = 0;
  data_array = new Type*[1];
}

template <class Type> OrderedList<Type>::OrderedList(int size){
  max_size = size;
  current_size = 0;
  data_array = new Type*[size];
  for(int i = 0; i < size;i ++){
    data_array[i] = nullptr;
  }
}

template <class Type> void OrderedList<Type>::AddItem(Type * item){
  int iterator = 0; //To store prospective location of the item
  int ops = 0; // number of ops temporary
  if(current_size == max_size){ //Make sure there is space in the list
    throw exception.overflow();
  }
  while(data_array[iterator] != nullptr && iterator < max_size-1 && *item > *data_array[iterator]){ //Find where the item should be placed
    iterator++;
  }
  ops = iterator; //Iterator is indicative of how many objects were compared
  for(int i = max_size-1;i > iterator;i--){
    data_array[i] = data_array[i-1]; //Shift entire array one space to the right
  }
  ops += current_size-iterator; //Number of ops performed in the for loop (shifting items)
  opCount.addFunction += ops; //increment operations count for add functions
  data_array[iterator] = item;
  current_size++;
}

template <class Type> Type* OrderedList<Type>::RemoveItem(Type * item){
  int iterator = 0;
  int ops = 0;
  Type * retval = nullptr; //initialize return value as nullptr
  if(current_size == 0){ //check for underflow case
    throw exception.underflow();
  }
  while(iterator < max_size-1){ //find the location of the object
    if(data_array[iterator] && *item == *data_array[iterator]){
      break;
    }
    iterator++;
  }
  ops += iterator;
  retval = data_array[iterator];
  for(int i = iterator;i < max_size-1;i++){
    data_array[i] = data_array[i+1];
  }
  ops += current_size-iterator;
  opCount.removeFunction += ops; //increment operations count for remove function
  current_size--;
  return retval;
}

template <class Type> Type* OrderedList<Type>::findItem(Type * item) {
	int iterator = 0;
	int ops = 0;
	Type * retval = nullptr; //initialize return value as nullptr
	if (current_size == 0) { //check for underflow case
		throw exception.underflow();
	}
	while (iterator < max_size - 1) { //find the location of the object
		if (data_array[iterator] && *item == *data_array[iterator]) {
			break;
		}
		iterator++;
	}
	ops += iterator;
	retval = data_array[iterator];
	return retval;
}

template <class Type> int OrderedList<Type>::length(){
  return current_size;
}

template <class Type> int OrderedList<Type>::getCapacity(){
  return max_size;
}

template <class Type> OperationCount OrderedList<Type>::getOperations(){
  return opCount;
}

template <class Type> bool OrderedList<Type>::isEmpty(){
  return current_size == 0;
}

template <class Type> bool OrderedList<Type>::isFull(){
  return current_size == max_size;
}

template <class Type> Type* OrderedList<Type>::getParent() {
	int order = max_size;
	Type* search;
	int count[order];
	for (int i = 0; i < order; i++) {
		search = data_array[i];
		count[i] = 0;
		for (int k = i; k < order; k++) {
			if (search < data_array[k]) {
				count[i]++;
			}
		}
	}

	for (int i = 1; i < order-1; i++) {
		if (abs(count[i] - count[i + 1]) && abs(count[i] - count[i] - 1) {
			return data_array[i]
		}
	}
}

template <class Type> void OrderedList<Type>::makeEmpty(){
  //Empty data_array
  for(int i = 0;i < current_size;i++){
    delete data_array[i];
  }
  delete [] data_array;
  current_size = 0;
}

#endif

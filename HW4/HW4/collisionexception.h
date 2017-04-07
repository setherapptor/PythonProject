#pragma once
#ifndef COLLISIONEXCEPTION_H
#define COLLISIONEXCEPTION_H
#include <exception>

class CollisionException : public std::exception {
public:
	virtual const char* collision() const throw(){
		return "Error: Attempt to insert an existing item.";
	}
};

#endif 
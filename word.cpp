#include "word.h"
#include <string>

using namespace std;

Word::Word() {
	s = "";
	i = 1;
}

Word::Word(string inString) {
	s = inString;
	i = 1;
}

int Word::getInt() {
	return i;
}

void Word::setInt(int inInt) {
	i = inInt;
}

string Word::getString() {
	return s;
}

void Word::setString(string inString) {
	s = inString
}

bool Word::operator<(Word inWord) {
	if (s.compare(inWord.getString()) < 0) {
		return true;
	}
	return false;
}

bool Word::operator==(Word inWord) {
	if (s.compare(inWord.getString()) == 0) {
		return true;
	}
	return false;
}

bool Word::operator==(string inString) {
	if (s.compare(inString) == 0) {
		return true;
	}
	return false;
}

bool Word::operator>(Word inWord) {
	if (s.compare(inWord.getString()) > 0) {
		return true;
	}
	return false;
}
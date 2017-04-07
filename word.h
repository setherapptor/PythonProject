#pragma once

#include <string>

using namespace std;

class Word {
private:
	string s;
	int i;
public:
	Word();
	Word(string);
	int getInt();
	void setInt(int);
	string getString();
	void setString(string);
	bool operator<(Word);
	bool operator==(Word);
	bool operator==(string);
	bool operator>(Word);
};
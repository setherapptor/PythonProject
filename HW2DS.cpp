// HW2DS.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "btree.h"
#include "word.cpp"
#include<fstream>
#include<iostream>
#include<stdio.h>

using namespace std;

fstream openFstream();

int main()
{
	char response;
	fstream stream = openFstream();
	char line[512];
	bool contents = false;
	while (stream.getline(line, 512)) {  
		if (!strcmp(line, "Contents:\r") || !strcmp(line, "Contents: ") || !strcmp(line, "Contents:")) {
			contents = true; //Signals start of char count
		}
		else if (contents) {
			TODO
		}
	}

    return 0;
}

fstream openFstream() {
	string fileName = "";
	cout << "Please enter the file name: ";
	cin >> fileName;

	fstream stream;
A:
	try {
		if (fileName.length() < 4) {
			throw 0;
		}
		if (fileName.length() >= 4 && fileName.substr(fileName.length() - 4, fileName.length()) != ".txt") {
			fileName += ".txt";
		}
		stream.open(fileName, ios::in | ios::out);
		if (stream.fail()) {
			throw 1;
		}
		cout << "---------------File Open Success!--------------" << endl << endl;
	}
	catch (int e) {
		cout << "Error " << e << ":" << getError(e) << endl;
		fileName = "";
		cout << "Please enter new file name: ";
		cin >> fileName;
		goto A;
	}
	return stream;
}

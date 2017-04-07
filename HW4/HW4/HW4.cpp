// HW4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "bst.h"
#include <iostream>

void clearScreen();

int main()
{
	
	BST<int>* t = new BST<int>;
	t = new BST<int>();
	
	int response = 0;

	while (response != 5) {
		cout << "Press 1 to insert a number" << endl;
		cout << "Press 2 to find a number" << endl;
		cout << "Press 3 to get the values is ascending order" << endl;
		cout << "Press 4 to get the values is descending order" << endl;
		cout << "Press 5 to quit" << endl;

		cin >> response;

		clearScreen();

		switch (response) {
			//Insert number
			case 1: {
				int p;
				cout << "Enter a number:";
				cin >> p;
				t->insert(&p, t->root);
				break;
			}
			//Find number
			case 2: {
				int p;
				cout << "Enter a number to find: ";
				cin >> p;
				int r = *(t->find(&p, t->root));
				cout << std::to_string(r);
				break;
			}
			//Print tree in ascending order
			case 3: {
				
				break;
			}
			//Print tree in descending order
			case 4: {

				break;
			}
			default: {
				cout << "Enter a number between 1-5" << endl;
				break;
			}
		}
		clearScreen();
			
	}






    return 0;

}

void clearScreen() {
	for (int i = 0; i < 10; i++) {
		cout << "\n\n\n\n\n\n\n\n\n\n";
	}
}
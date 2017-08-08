// 54 Spiral Matrix.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <stdio.h>
#include <vector>
#include <stdlib.h>


using namespace std;
class Solution {
public:

	vector<int> spiralOrder(vector<vector<int>>& matrix) {
		vector<int> spirals;
		int direction, north, south, west, east, m, n, x, y;
		m = matrix.size();
		n = matrix.front().size();
		north = 0;
		south = m - 1;
		west = 0;
		east = n - 1;
		x = 0;
		y = 0;
		direction = 0;
		for (int i = 0; i < m * n; i++ ){
			spirals.push_back(matrix[y][x]);
			switch (direction) {
				case 0: // move right
					if (x == east) {
						direction = 3;
						north++;
						y++;
					}
					else { // move down
						x++;
					}
					break;
				case 1: // move left
					if (x == west) {
						direction = 2;
						south--;
						y--;
					}
					else { //  move up
						x--;
					}
					break;
				case 2: // move up
					if (y == north) {
						direction = 0;
						west++;
						x++;
					}
					else { // move right
						y--;
					}
					break;
				case 3: // move down
					if (y == south) {
						direction = 1;
						east--;
						x--;
					}
					else  // move left
					{
						y++;
					}
					break;
			}
		}
		return spirals;
	}
};

void printResult(vector<int>& spiral) {
	for (int i = 0; i < spiral.size(); i++) {
		cout << spiral[i] << endl;
	}
}

int main() {
	vector<vector<int>> matrix;
	matrix.push_back({ 1,2,3 });
	matrix.push_back({ 4,5,6 });
	matrix.push_back({ 7,8,9 });
	Solution *sol = new Solution();
	printResult(sol->spiralOrder(matrix));
	system("pause");

}

void printMatrix(vector<vector<int>>& matrix) {
	for (int x = 0; x < matrix.size(); x++) {
		for (int y = 0; y < matrix.front().size(); y++) {
			cout << matrix[x][y] << endl;
		}
	}
}



// 36 Valid Sudoku.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <string>
#include <iostream>

using namespace std;
class Solution {
public:
	bool isValidSudoku(vector<vector<char>>& board) {
		if (board.front().size() != 9 || board.size() != 9) {
			return false;
		}
		vector<char> grid;
		vector<char> columns;
		for (int i = 0; i < 9; i++) { // iterate row
			if (!isValidRow(board[i])) { // check if row is balid
				return false;
			}
			for (int j = 0; j < 9; j++) { // iterate col
				if (i != 0 && (((i + 1) % 3) == 0) && ((j + 1) % 3 == 0)) { // checks for 3x3
					for (int k = i - 2; k < i + 1; k++) {  // creates a 3x3 grid in form of a vector of 9 chars
						grid.push_back(board[k][j - 2]);
						grid.push_back(board[k][j - 1]);
						grid.push_back(board[k][j]);
					}
					if (!isValidGrid(grid)) {
						return false;
					}
					grid.clear(); // clear the vector
				}
				columns.push_back(board[j][i]);
			}
			if (!isValidColumn(columns)) { // check if column is valid
				return false;
			}
			columns.clear(); // clear the column
		}
		return true;
	}
	// unneccessary wrappers, but good for understanding code
	bool isValidRow(vector<char>& row) { 
		return isValid(row);
	}
	bool isValidColumn(vector<char>& col) {
		return isValid(col);
	}
	bool isValidGrid(vector<char>& grid) {
		return isValid(grid);
	}

	bool isValid(vector<char>& input) {
		for (int i = 0; i < input.size(); i++) {
			for (int j = i + 1; j < input.size(); j++) {
				if (input[i] != '.'){ // if not empty
					if ((input[i] >= '1' && input[i] <= '9') && (input[i] != input[j])) { // check for duplicates and digit range (1-9)
						continue;
					}
					else {
						return false;
					}
				}
			}
		}
		return true;
	}
};


vector<vector<char>> generateSudoku(vector<char>& input) {
	vector<char> row;
	vector<vector<char>> sudoku;
	for (int i = 0; i < input.size(); i++) {
		if ((i + 1) % 9 == 0) {
			for (int j = i; j >= 0; j--) {
				row.push_back(input[j]);
			}
		}
		sudoku.push_back(row);
		row.clear();
	}
	return sudoku;
}
int main()
{
	vector<char> input = { '5', '3', '.', '.', '7', '.', '.' ,'.', '.',
							'6', '.', '.', '1', '9', '5', '.', '.', '.',
							'.', '9', '8', '.', '.', '.', '.', '6', '.',
							'8', '.', '.', '.', '6', '.', '.', '.', '3',
							'4', '.', '.', '8', '.', '3', '.', '.', '1',
							'7', '.', '.', '.', '2', '.', '.', '.', '6',
							'.', '6', '.', '.', '.', '.', '2', '8', '.',
							'.', '.', '.', '4', '1', '9', '.', '.', '5',
							'.', '.', '.', '.', '8', '.', '.', '7', '9'};
	vector<vector<char>> sudoku = generateSudoku(input);
	Solution *sol = new Solution();
	cout << sol->isValidSudoku(sudoku) << endl;
	system("pause");
    return 0;
}

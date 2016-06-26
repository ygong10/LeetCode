// 1 Two Sums.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		vector<int> result;
		for (int i = 0; i < nums.size(); i++) {
			for (int j = i + 1; j < nums.size(); j++) {
				if (nums[i] + nums[j] == target) {
					result.push_back(i);
					result.push_back(j);
					return result;
				}
			}
		}
		return result;
	}
};

int main()
{
	vector<int> input;
	input.push_back(0);
	input.push_back(4);
	input.push_back(3);
	input.push_back(0);
	int target = 0;
	Solution *sol = new Solution();

	vector<int> answer = sol->twoSum(input, target);

	cout << answer[0] << answer[1] << endl;

	system("pause");
    return 0;
}


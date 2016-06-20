#include <stdio.h>
#include <iostream>
#include <string>


class Solution {
public:
	std::string reverseString(std::string s) {
		for (int i = 0; i < s.length() / 2; i++) {
			char temp = s[i];
			s[i] = s[s.length() - i - 1];
			s[s.length() - i - 1] = temp;
		}
		return s;
	}
};

int main() {
	std::string input;
	Solution *solution = new Solution();
	while (std::getline(std::cin, input)) {
		std::cout << solution->reverseString(input) << std::endl;
	}
	return 0;
}


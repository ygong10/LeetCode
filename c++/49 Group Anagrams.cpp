// 49 Group Anagrams
// Time Complexity: O(NlogN)
// Space Complexity: O(N)

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, int> dict;
        vector<vector<string>> anagrams;
        
        for (string str : strs) {
            string sorted_str(str);
            sort(sorted_str.begin(), sorted_str.end());
            
            auto it = dict.find(sorted_str);
            
            if (it == dict.end()) {
                vector<string> new_vector;
                new_vector.push_back(str);
                dict[sorted_str] = anagrams.size();
                anagrams.push_back(new_vector);
            } else {
                anagrams[it->second].push_back(str);
            }       
        }
    
        return anagrams;
    }
};

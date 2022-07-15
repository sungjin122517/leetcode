#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

// My own solution
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        vector<int> temp;

        for (int i=0; i<nums.size(); i++) {
            if (find(temp.begin(), temp.end(), nums[i]) != temp.end())
                return true;
            temp.push_back(nums[i]);
        }
        return false;
    }
};


// Use of unordered set
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> temp(nums.begin(), nums.end());

        if (temp.size() == nums.size())
            return false;
        else
            return true;
    }
};


// Use of sort
bool containsDuplicate(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i=0; i<nums.size()-1; i++) {
        if (nums[i]==nums[i+1])
            return true;
    }
    return false;
}


// Use of adjacent_find
bool containsDuplicate(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    
    if (adjacent_find(nums.begin(), nums.end()) != nums.end())
        return true;
    else 
        return false;
}


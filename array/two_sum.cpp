#include <iostream>   
#include <vector>
#include <algorithm>
using namespace std;

/* 
벡터에서 합이 target이 되는 두 개의 element의 index들을 찾는 문제.
두 개의 for loop (Brute Force method)을 쓰지 않고 할 수 있는 방법을 생각해 내지 못 하겠다.
참고로 Brute Force의 time complexity는 O(n^2).

결국 인터넷에 algorithm for two sum을 검색해서 time complexity가 O(n)인 hashmap을 이용한 알고리즘을 찾아냈다.
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        unordered_map<int, int> hash;
        
        for (int i=0; i<nums.size(); i++) {
            int temp = target - nums[i];
            
            if (hash.find(temp) != hash.end()) {
                result.push_back(i);
                result.push_back(hash[temp]);
                return result;
            }
            hash[nums[i]] = i;
        }
        return {};
    }
};

/*
일반 벡터가 아닌 unordered_map이라는 것을 사용했다.
unordered_map은 key와 value로 이루어진 hash map이다.
위에 문제 풀이와 같이 key와 value를 지정할 수 있다.

find(): returns an iterator to the first element in the range [first, last) that compares equal to value.
If no such element is found, it returns last.
*/
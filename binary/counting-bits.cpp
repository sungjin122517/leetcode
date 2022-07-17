#include <iostream>
#include <vector>

using namespace std;

/*
Topic: binary
Difficulty: easy



1. time complexity: O(nlogn) 
runtime: 16 ms (상위 87%)
memory usage: 8.7 MB (상위 70%)
*/

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> arr;
        arr.push_back(0);
        if (n==0) {return arr;}
        arr.push_back(1);
        
        for (int i=2; i<n+1; i++) {
            int temp=i;
            int count=0;
            while (temp) {
                if (temp%2==1) {count++;}
                temp /= 2;
            }
            arr.push_back(count);
        }
        return arr;
        
    }
};


/* 
2. Dynamic programming
time complexity: O(n)  
runtime: 8 ms (상위 40%)
memory usage: 7.9 MB (상위 30%)  
*/

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> arr(n+1, 0);

        for (int i=1; i<n+1; i++) {
            int part1 = arr[i/2];   // == arr[i>>1] (right-shift)
            int part2 = i&1;    // LSB of i

            arr[i]=part1+part2;
        }
        return arr;
        
    }
};
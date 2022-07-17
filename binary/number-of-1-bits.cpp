#include <iostream>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count=0;
        while (n>0) {
            if (n%2==1) {
                count++; 
            }
            // right shift operator
            n = n >> 1;
        }
        return count;
    }
};

/*
Topic: binary
Difficulty: easy

Runtime: 4 ms (상위 60%)
Memory usage: 5.8 MB (상위 20%)

Input of uint32 can be represented in binary form.
However, if printed out, it is represented in decimal form.


Refer to geeksforgeeks: Count set bits in an integer.

1. simple method: my method.
Time complexity: O(log n)
*/

// 2. Brian Kernighan's algorithm
int hammingWeight(uint32_t n) {
    int count=0;
    while (n) {
        n = n && (n-1);
        count++;
    }
    return count;
}

/*
e.g.
n = 9;
count = 0;

n = 9&8 (1001 & 1000)
n = 8 (1000)
count = 1;

n = 8&7 (1000 & 0111)
n = 0
count = 2;

therefore, return count = 2;
*/
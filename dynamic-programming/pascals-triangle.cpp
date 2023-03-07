#include <iostream>
#include <vector>

using namespace std;

/*
dynamic programming 문제이다. array에 무엇을 저장해야할까?

time complexity: O(N^2), since there are two for loops.
space complexity: O(1). One 2D vector output created as result.

solved using dp.
dp에 사용되는 vector 자체를 2d vector로 지정하면 된다.
*/

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> dp;
        // dp[0].push_back({1});
        for (int i=0; i<numRows; i++) {
            dp.push_back(vector<int>(i+1, 1));
            for (int j=1; j<i; j++) {
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            }
        }

        return dp;
    }
};
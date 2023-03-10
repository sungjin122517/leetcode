#include <iostream>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        bool dp[n][n];
        int start = 0;
        int maxLen = 0;

        memset(dp, 0, sizeof(dp));

        if (n==1) return s;

        for (int i=0; i<n; i++) {
            dp[i][i] = true;
            if (i == n-1) break;
            if (s[i] == s[i+1]) {
                dp[i][i+1] = true;
                maxLen = 2;
                start = i;
            }
        }

        for (int k=3; k<=n; k++) {
            for (int i=0; i<n-k+1; i++) {
                int j = i+k-1;
                if (s[i] == s[j] && dp[i+1][j-1]) {
                    dp[i][j] = true;
                    if (k>maxLen) {
                        maxLen = k;
                        start = i;
                    }
                }
            }
        }

        return s.substr(start, maxLen);
    }
};
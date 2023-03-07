#include <iostream>

using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int index = 0;
        for (int i=0; i<t.length(); i++) {
            if (s[index] == t[index]) index++;
        }
        
        if (index == s.length()-1) return true;
        else return false;
    }
};
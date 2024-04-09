#include <iostream>

using namespace std;

// [easy] Valid palindrome

bool isPalindrome(string s) {
    // convert upper to lower char, remove space, remove comma/fullstop -> no need!!
    int start = 0, end = s.length()-1;
    while (start <= end) {
        if (!isalnum(s[start])) {
            start++;
            continue;
        }
        if (!isalnum(s[end])) {
            end--;
            continue;
        }
        if (tolower(s[start]) != tolower(s[end])) return false;
        start++;
        end--;
    }

    return true;

}

/*
Time Complexity: O(n)
Space Complexity: O(1), since only use two pointers
*/
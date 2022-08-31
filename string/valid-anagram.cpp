#include <iostream>

using namespace std;

bool isAnagram(string s, string t) {
    if (s.length() != t.length())
        return false;

    int arr1[26] = { };
    int arr2[26] = { };

    for (int i=0; i<s.length(); i++) {
        arr1[s[i]-'a']++;
        arr2[t[i]-'a']++;
    }

    for (int j=0; j<26; j++) {
        if (arr1[j] != arr2[j])
            return false;
    }

    return true;
}
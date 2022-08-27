#include <iostream>
#include <unordered_set>
#include <vector>
// #include <math>

using namespace std;


/* time complexity: O(n^2) */
int lengthOfLongestSubstring(string s) {
    if (s.length()==0)
        return 0;

    int max = -1;
    int num = 0;
    for (int i=0; i<s.length(); i++) {
        unordered_set<char> set;
        num = 0;
        // vector<bool> set(26);   // default values in set are false
        for (int j=i; j<s.length(); j++) {
            // if (set[s[j]-'a'])
            //     break;
            // set[s[j]-'a']=true;
            if (set.find(s[j]) != set.end())
                break;
            set.insert(s[j]);
            num++;
        }
        cout << num << endl;
        if (max<num)
            max = num;
    }
    return max;
}

// time complexity: O(n)
int lengthOfLongestSubstring(string s) {
    int result = 0;

    // last index of all characters is initialized as -1
    vector<int> lastIndex(256, -1); // number of chars = 256

    int i = 0;  // start of window
    for (int j=0; j<s.length(); j++) {
        i = max(i, lastIndex[s[j]+1]);

        // update result if we get a larger window
        result = max(result, j-i+1);

        // update last index of j
        lastIndex[s[j]] = j;
    }
    return result;
}

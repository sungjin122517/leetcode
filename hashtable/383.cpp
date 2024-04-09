#include <iostream>
#include <unordered_map>

using namespace std;

// [easy] Ransom note

bool canConstruct(string ransomNote, string magazine) {
    unordered_map<char, int> map;

    // ransomNote map
    for (int i=0; i<magazine.length(); i++) {
        if (map.find(magazine[i]) == map.end()) {
            map[magazine[i]] = 1;
        }
        else {
            map[magazine[i]]++;
        }
    }

    for (int j=0; j<ransomNote.length(); j++) {
        if (map.find(ransomNote[j]) != map.end() && map[ransomNote[j]] > 0) {
            map[ransomNote[j]]--;
        }
        else return false;
    }

    return true;
}

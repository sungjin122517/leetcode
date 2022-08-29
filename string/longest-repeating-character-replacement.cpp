#include <iostream>
#include <algorithm>

using namespace std;

/* 
apple
banana
carrot
environment, k=3

1. 일단 제일 길게 만들수 있는 substring의 길이를 찾는다.
2. 그 두 알파벳 사이에서 바꿔야하는 알파벳의 갯수를 찾는다.
3. 갯수가 k보다 크면, 첫번째 index부터 다시 시작해서 다른 알파벳이 나올때마다 1씩 감소.
4. 모든 char에 대해서 이 과정을 반복한다.


*/

int characterReplacement(string s, int k) {
    int result = 0;
    int leftInd = 0;
    int arr[26] = { };
    int windowSize;

    for (int j=0; j<s.length(); j++) {
        arr[s[j]-'A']++;
        int newlyAddedCharNum = j-leftInd+1 - *max_element(arr, arr+26);
        if (newlyAddedCharNum > k) {
            arr[s[leftInd]-'A']--;
            leftInd++;
        }

        result = max(result, j-leftInd+1);
    }
    return result;

    // while (rightInd<k) {
    //     windowSize = rightInd+leftInd-1;

    //     if (windowSize - *max_element(arr, arr+26) <= k) {
    //         arr[s[rightInd]-'A']++;
    //         max = windowSize;
    //         rightInd++;
    //     }
    //     else {
    //         arr[s[leftInd]-'A']--;
    //         leftInd++;
    //     }
    // }
}
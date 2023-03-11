#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

/*
Topic: Dynamic Programming
전혀 감을 잡지 못 하였다. Solution을 봐도 거의 다 backtracking으로 풀었다.

답을 보니 생각보다 간단했다.
Recursion을 이용해서 괄호 앞, 사이, 뒤에 ()을 넣어주면 된다.
아직 바로 생각해내기엔 한계가 있다.

Parenthesis 문제의 dp 방법은 사이사이에 () 추가하기.

메모리는 확실히 적게 먹지만 (Beats 94.2%) 런타임이 길다 (Beats 39.3%).
*/

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if (n<1) return {""};
        else if (n == 1) return {"()"};
        else {
            vector<string> ans;
            unordered_set<string> strs;
            for (string str : generateParenthesis(n-1)) {
                int len = str.length();
                for (int i=0; i<len; i++) {
                    string temp = str.substr(0, i) + "()" + str.substr(i, len-i);
                    strs.insert(temp);
                }
            }
            
            for (string str : strs) ans.push_back(str);
            return ans;
        }
    }
};
#include <iostream>   
#include <vector>
#include <algorithm>
using namespace std;

// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
//         int max_profit = 0;
//         for (int i=0; i<prices.size()-1; i++) {
//             int max = *max_element(prices.begin()+i+1, prices.end());
//             if (max_profit<max-prices[i])
//                 max_profit = max - prices[i];
//         }
//         return max_profit;
//     }
// };

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // map<int, int> map;
        // for (int i=0; i<prices.size(); i++) {
        //     map[prices[i]]=i;
        // }
        // sort(prices.begin(), prices.end());
        // for (int i=prices.size()-1; i>0; i--) {
        //     if (map[prices[i]] > map[prices[0]]) {
        //         return prices[i]-prices[0];
        //     }
        // }
        // return 0;


        // return index of minimum value
        // int min_it = min_element(prices.begin(), prices.end()) - prices.begin();
        // int max_it = max_element(prices.begin()+min_it, prices.end()) - prices.begin();
        // if (max_it>min_it)
        //     return prices[max_it]-prices[min_it];
        // else
        //     return 0;

        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i=1; i<prices.size(); i++) {
            if (minPrice > prices[i]) {
                minPrice = prices[i];
            }
            else if (maxProfit < prices[i]-minPrice) {
                maxProfit = prices[i]-minPrice;
            }
        }
        return maxProfit;
    }
};


/* 
By default, map is sorted in increasing order based on its key.

첫번째 solution:
1. for loop을 이용해서 첫번째 숫자부터 각 숫자를 기준으로 둔다. max라는 int variable을 만든다.
2. 기준 숫자보다 뒤에 있는 숫자들중에 maximum를 찾는다.
3. maximum-기준이 max보다 작으면 max=maximum-기준.

결과: time-limit exceeded.

두번째 solution:
1. min_element 함수를 이용해서 제일 작은 숫자의 인덱스를 찾는다.
2. 그 인덱스 이후에 숫자들 중에서 제일 큰 숫자를 찾아서 profit을 찾는다.

하지만 문제점: 이렇게 찾은 profit이 항상 max라는 보장은 없다. 밑과 같은 test case도 존재한다.

굉장히 간단한 문제였다,,
loop을 한 번만 돌고도 찾을 수 있었다.
일단 2개의 변수, minPrice와 maxProfit을 만든다.
loop을 돌면서 minPrice와 maxProfit을 동시에 업데이트 해주면 된다.
minPrice는 return되지 않는 값이기 때문에 그냥 비교 용도로만 사용될 수 있기 때문이다.

*/
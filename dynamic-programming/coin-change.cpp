#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// class Solution {
// public:
//     int coinChange(vector<int>& coins, int amount) {
//         sort(coins.begin(), coins.end());
//         vector<int> temp;
//         vector<int>::reverse_iterator p;
//         int count = 0;
//         int total=amount;
//         for (p=coins.rbegin(); p != coins.rend(); p++) {
//             if (*p<amount) {
//                 temp.push_back(*p);
//                 count++;
//                 total -= *p;
//             }
//             vector<int>::reverse_iterator reit = p;
//             while (reit != coins.rend()) {
//                 if (*reit < amount) {

//                 }
//             }
//         }
        
//     }
// };

// 1. Recursion
int coinChange(vector<int>& coins, int amount) {
    // base case
    if (amount==0) return 0;

    // initialize result
    int result = INT_MAX;

    // try every coin that has smaller value than amount
    vector<int>::iterator p;
    for (p=coins.begin(); p != coins.end(); p++) {
        if (*p <= amount) {
            int sub_result = coinChange(coins, amount-*p);

            // Check for INT_MAX to avoid overflow
            // && see if result can be minimized
            if (sub_result != INT_MAX && sub_result+1 < result)
                result = sub_result+1;
            
            if (sub_result == -1) {
                return -1;
            }
        }
    }
    if (result == INT_MAX) 
        return -1;
    return result;
}


// 2. Dynamic programming
int coinChange(vector<int>& coins, int amount) {
    // table[i] for storing the minimum number of coins to get the amount i
    int table[amount+1];

    // base case
    table[0]=0;

    // initialize all table values as infinite
    for (int i=1; i<=amount; i++)
        table[i] = INT_MAX;
    
    // compute minimum coins required for all values from 1 to V.
    vector<int>::iterator p;
    for (int i=1; i<=amount; i++) {
        for (p=coins.begin(); p != coins.end(); p++) {
            if (*p <= i) {
                int sub_result = table[i-*p];
                // check whether the sub_result can be made with given coins
                // && see if results can be minimized.
                if (sub_result != INT_MAX && sub_result+1 < table[i]) {
                    table[i]=sub_result+1;
                }
            }
        }
    }

    if (table[amount] == INT_MAX)
        return -1;
    
    return table[amount];
}
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// class Solution {
// public:
//     int lengthOfLIS(vector<int>& nums) {
//         int len = nums.size();
//         int arr[len];
//         for (int i=0; i<len; i++) {
//             arr[i]=0;
//         }

//         for (int i=0; i<len; i++) {
//             if (arr[i] == 0) { arr[i]=1; }
//             else { continue; }

//             vector<int>::iterator p = nums.begin()+i+1;
//             int p_arr = i+1;
//             vector<int>::iterator mark=p-1;
//             int mark_arr = p_arr-1;

//             for (p; p!=nums.end(); p++) {
//                 if (*p > *mark) {
//                     if (arr[p_arr] < arr[mark_arr]+1) {
//                         arr[p_arr] = arr[mark_arr]+1;
//                         mark_arr = p_arr;
//                         mark = p;
//                     }
//                 }
//                 p_arr++;
//             }
//         }

//         return *max_element(arr, arr+len);
//     }
// };

// Dynamic programming
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int len = nums.size();
        int arr[len];
        for (int i=0; i<len; i++) {
            arr[i]=1;
        }
        if (len==1) { return 1; }

        vector<int>::iterator p;
        int p_arr = 1;
        for (p=nums.begin()+1; p != nums.end(); p++) {
            vector<int>::iterator mark;
            int mark_arr = 0;
            for (mark=nums.begin(); mark != p; mark++) {
                if (*p > *mark) {
                    if (arr[p_arr] < arr[mark_arr]+1) {
                        arr[p_arr] = arr[mark_arr]+1;
                    }
                }
                mark_arr++;
            }
            p_arr++;
        }

        return *max_element(arr, arr+len);
    }
};


// Use of lower_bound
int lengthOfLIS(vector<int>& nums) {
    vector<int> arr;
    int len = nums.size();
    for (int i=0; i<len; i++) {
        // lower_bound searches for nums[i] by binary search.
        // if nums[i] doesn't exist in arr, p=nums[i]보다 큰 값 중에 가장 작은 값의 위치.
        vector<int>::iterator p = lower_bound(arr.begin(), arr.end(), nums[i]);
        // p==nums.end() if all values of arr < nums[i]
        if (p==nums.end()) { arr.push_back(nums[i]); }
        else { *p = nums[i]; }

        return arr.size();
    }
}


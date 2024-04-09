#include <iostream>

using namespace std;

// [medium] Product of array except itself

vector<int> productExceptSelf(vector<int>& nums) {
    vector<int> result(nums.size(), 1);

    int pre = 1;
    for (int i=0; i<nums.size(); i++) {
        result[i] *= pre;
        pre *= nums[i];
    }

    int post = 1;
    for (int j=nums.size()-1; j>=0; j--) {
        result[j] *= post;
        post *= nums[j];
    }

    return result;
}
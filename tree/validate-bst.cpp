#include <iostream>
#include <vector>

using namespace std;


// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

bool isFirstVisit = true;
int lastVisitedVal;

bool isValidBST(TreeNode* root) {
    if (!root) { return true; }

    if (!isValidBST(root->left)) {
        return false;
    }

    if (isFirstVisit && lastVisitedVal >= root->val) {
        return false;
    }

    isFirstVisit = false;
    lastVisitedVal = root->val;

    if (!isValidBST(root->right)) {
        return false;
    }

    return true;

}

// bool isValidBST(TreeNode* root) {
//     if (!root) { return true; }
//     if (!root->left && !root->right) { return true; }

//     if (!root->left) { isValidBST(root->right); }
//     else if (root->left->val < root->val) {
//         isValidBST(root->left);
//     } else {
//         return false;
//     }

//     if (!root->right) { return true; }
//     if (root->right->val > root->val) {
//         isValidBST(root->right);
//     } else {
//         return false;
//     }

//     return true;

// }
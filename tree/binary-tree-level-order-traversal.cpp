#include <iostream>
#include <vector>
#include <queue>

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


vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> ans;
    if (!root) { return ans; }

    // vector<int> start;
    // start.push_back(root->val);
    // ans.push_back(start);

    queue<TreeNode *> q;
    q.push(root);
    while (!q.empty()) {
        vector<int> temp;
        int qSize = q.size();
        while(qSize>0) {
            temp.push_back(q.front()->val);
            if (q.front()->left) { q.push(q.front()->left); }
            if (q.front()->right) { q.push(q.front()->right); }
            q.pop();
            qSize--;
        }
        ans.push_back(temp);
    }

    return ans;
}
#include <iostream>
#include <queue>

using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


// think about the perspective of subtree
int maxDepth(TreeNode* root) {
    if (!root)
        return 0;
    
    int leftDepth = maxDepth(root->left);
    int rightDepth = maxDepth(root->right);

    if (leftDepth>rightDepth)
        return leftDepth+1;
    else 
        return rightDepth+1;
}

// BFS: level order traversal
int maxDepth(TreeNode* root) {
    if (!root)
        return 0;
    
    queue<TreeNode*> q;
    q.push(root);
    int depth = 1;

    while (!q.empty()) {
        TreeNode* temp = q.front();
        q.pop();

        for (int i=0; i<q.size(); i++) {
            if (temp->left)
                q.push(temp->left);
            if (temp->right)
                q.push(temp->right);
        }
        depth++;
    }
    
    return depth;
}

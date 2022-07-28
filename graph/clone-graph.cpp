#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;


// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};


class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (node==nullptr)
            return nullptr;
        
        // map to keep track of all the nodes which have already been created
        map<Node*, Node*> copies;
        queue<Node*> q;

        q.push(node);
        // copy without its neighbours
        Node* copy = new Node(node->val, {});

        // key = address of original node
        // value = address of new node
        copies[node] = copy;
        while (!q.empty()) {
            Node* u = q.front();
            q.pop();
            vector<Node*> v = u->neighbors;
            for (int i=0; i<v.size(); i++) {
                if (copies[v[i]]==nullptr) {
                    // copy = new Node(v[i]->val, {});
                    copies[v[i]] = new Node(v[i]->val, {});
                    q.push(v[i]);
                }
                copies[u]->neighbors.push_back(copies[v[i]]);
            }
        }
        return copies[node];
    }
};
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;


class Solution {
public:
    int getParent(unordered_map<int, int> nodes, int x) {
        if (nodes[x] == x) return x;
        return nodes[x] = getParent(nodes, nodes[x]);
    }

    // void createGraph(unordered_map<int, int> nodes, int a, int b) {
    //     a = getParent(nodes, a);
    //     b = getParent(nodes, b);
    //     if (a<b) {
    //         nodes.at(b) = a;
    //         cout << b << ' ' << nodes.at(b) << endl;
    //     }
    //     else {
    //         nodes.at(a) = b;
    //         cout << a << ' ' << nodes.at(a) << endl;
    //     }
    // }

    bool findParent(unordered_map<int, int> nodes, int a, int b) {
        a = getParent(nodes, a);
        b = getParent(nodes, b);
        if (a==b) return true;
        else return false;
    }

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        
        /*
        1. create parent array
        Which data structure to use? unordered map
        */
        unordered_map<int, int> nodes;

        for (int i=0; i<edges.size(); i++) {
            nodes[edges[i][0]] = edges[i][0];
            nodes[edges[i][1]] = edges[i][1];
        }

        // for (int i=0; i<edges.size(); i++) {
        //     cout << nodes.at(i) << endl;
        // }

        for (int i=0; i<edges.size(); i++) {
            int a = edges[i][0];
            int b = edges[i][1];

            a = getParent(nodes, a);
            b = getParent(nodes, b);
            if (a<b) {
                nodes.at(b) = a;
                // cout << b << ' ' << nodes.at(b) << endl;
            }
            else {
                nodes.at(a) = b;
                // cout << a << ' ' << nodes.at(a) << endl;
            }
            // createGraph(nodes, edges[i][0], edges[i][1]);
        }

        return findParent(nodes, source, destination);
    }
};

/*
Map을 쓰면 일일이 맵을 다 형성해줘야 하기 때문에 time limit을 넘긴다.
그리고 map은 array처럼 주소가 있지 않아서 함수 내에서 변경해도 적용이 되지 않는다.
*/

bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
    unordered_map<int, vector<int>> nodes;
    for (int i=0; i<edges.size(); i++) {
        nodes[edges[i][0]].push_back(edges[i][1]);
        nodes[edges[i][1]].push_back(edges[i][0]);
    }

    bool visited[n];
    for (int i=0; i<n; i++) visited[i] = false;
    visited[source] = true;
    // vector<bool> visited; 여기서 벡터 쓰면 맨 첨에 initialize 안 해줘도 된다.

    queue<int> q;
    q.push(source);

    while (!q.empty()) {
        int currNode = q.front();
        q.pop();
        if (currNode == destination) return true;

        for (int i=0; i<nodes[currNode].size(); i++) {
            int adjNode = nodes[currNode][i];
            if (!visited[adjNode]) {
                q.push(adjNode);
                visited[adjNode] = true;
            }
        }
    }

    return false;
}



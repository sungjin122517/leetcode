#include <iostream>
#include <vector>

using namespace std;

/*
1. Need to determine the paths, since the paths are not given. Just the points

*/

class Solution {
public:
    int parent[1001];

    int getParent(int index) {
        if (parent[index] < 0) return index;
        return parent[index] = getParent(parent[index]);
    }

    bool merge(int a, int b) {
        a = getParent(a);
        b = getParent(b);
        if (a==b) return false;
        parent[a] = b;
        return true;
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        for (int i=0; i<points.size(); i++) parent[i] = -1;

        // create edges
        vector<pair<int, pair<int, int>>> edges;
        for (int i=0; i<points.size(); i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j=i+1; j<points.size(); j++) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                int dist = abs(x2-x1) + abs(y2-y1);
                edges.push_back({dist, {i, j}});
            }
        }

        // sort edges in ascending order
        sort(edges.begin(), edges.end());

        int ans = 0;
        for (int i=0; i<edges.size(); i++) {
            int cost = edges[i].first;
            int x = edges[i].second.first;
            int y = edges[i].second.second;
            if (merge(x, y)) ans += cost;

            // int a = getParent(x);
            // int b = getParent(y);
            // if (a != b) {
            //     Union(a, b);
            //     ans += cost;
            // }
        }

        return ans;
    }
};
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    class Graph {
        public:
            vector<vector<pair<int, int>>> adj;  // adjacent nodes (distance, target)
            int numNodes;
        
        void generateGraph(vector<vector<int>> &input, int n) {
            numNodes = n;
            adj.resize(n+1);    // n+1 because node value starts from 1 to n
            for (int i=0; i<input.size(); i++) 
                adj[input[i][0]].push_back({input[i][2], input[i][1]});
        }

        void clear() { adj.clear(); }

    };

    vector<int> dijkstraSingleTarget(Graph g, int source) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        vector<int> dist(g.numNodes+1, 1000);
        vector<bool> visited(g.numNodes+1, false);
        // visited[0] = true;
        
        dist[source] = 0;
        minHeap.push({0, source});

        while (!minHeap.empty()) {
            int time = minHeap.top().first;
            int currInd = minHeap.top().second;
            minHeap.pop();
            if (time > dist[currInd]) continue;
            // if (visited[currInd]) continue;

            for (pair<int, int> path : g.adj[currInd]) {   // curr node에 인접한 모든 노드 iterate
                int nextTime = time + path.first;
                int nextInd = path.second;
                if (nextTime < dist[nextInd]) {
                    dist[nextInd] = nextTime;
                    minHeap.push({nextTime, nextInd}); 
                }
            }
        }

        // if (count(visited.begin(), visited.end(), false)) return -1;
        // else return *max_element(dist.begin(), dist.end());
        return dist;


    }

    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        Graph g;
        g.generateGraph(times, n);
        vector<int> timeVec = dijkstraSingleTarget(g, k);
        int maxTime = 0;

        for (int i=1; i<=n; i++) {
            if (timeVec[i] == 1000) return -1;
            if (timeVec[i] > maxTime) maxTime = timeVec[i];
        }

        return maxTime;
    }
};

/*
vector<int> dist -> 모든 shortest distance 저장
bool<int> visited
다익스트라 이용해서 dist vector 업데이트
하나라도 inf 있으면 return -1
없으면 그 중에서 제일 큰 숫자 return

---
저번에 풀어봤던 path with maximum probability와 유사한 문제.
queue(minHeap)을 이용한 구현은 방문 여부를 굳이 체크하지 않아도 된다.
방문 했으면 nextTime이 이미 업데이트 되었기 때문에 while loop 안에 for loop 안에 if문을 들어가지 않기 때문이다. 


*/
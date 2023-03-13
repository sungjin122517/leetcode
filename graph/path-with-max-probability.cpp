#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    class Graph {
        public:
            vector<vector<pair<int, double>>> adj;  // adjacent nodes
            int nodes;  // number of nodes

            void generateGraph(vector<vector<int>> &input, vector<double> &w, int n) {
                nodes = n;
                adj.resize(nodes+1);
                for (int i=0; i<input.size(); i++) {
                    adj[input[i][0]].push_back({input[i][1], w[i]});
                    adj[input[i][1]].push_back({input[i][0], w[i]});
                }
            }

            void clear() { adj.clear(); }
    };

    double dijkstraSingleTarget(Graph g, int source, int target) {
        // create minheap of pairs <distance, node> sorted by distance
        priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> minHeap;   // minHeap in ascending order of pair.first
        vector<double> dist(g.nodes+1, 0);
        vector<bool> visited(g.nodes+1, false);

        /*
        minHeap is in ascending order (smallest at the top).
        Since we need to get max probability, we prioritize probability with max modulus by multiplying with -1.
        */
        dist[source] = -1;  
        minHeap.push({-1, source});

        while (!minHeap.empty()) {
            double prob = minHeap.top().first;
            int curr = minHeap.top().second;
            minHeap.pop();
            if (dist[curr] < prob) continue;
            if (visited[curr]) continue;    // unnecessary
            visited[curr] = true;

            for (pair<int, double> path : g.adj[curr]) {
                int next = path.first;
                double nextProb = prob * path.second;
                if (nextProb < dist[next]) {
                    dist[next] = nextProb;
                    minHeap.push(make_pair(nextProb, next));
                }
            }
        }

        return -dist[target];
    }

    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        Graph g;
        g.generateGraph(edges, succProb, n);
        return dijkstraSingleTarget(g, start, end);
    }
};
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

/*
Dijkstra Algorithm
- shortest path 탐색
- negative weight 포함 불가능
- dynamic programming을 활용
    - 최단거리를 구할 때 그 이전까지 구했던 최단거리 정보를 그대로 사용한다

과정:
1. 시작 노드 설정
2. 시작 노드를 기준으로 각 노드의 minimum weight 저장
3. unvisited node 중에서 minimum weight의 노드를 선택
4. 해당 노드를 거쳐서 특정 노드로 가는 경우를 고려하여 min cost 갱신
5. 3 & 4 반복
*/



vector<pair<int, int>> a[6];    // 간선 정보
int d[6];   // 최소 비용

void dijkstra(int start) {
    d[start] = 0;
    priority_queue<pair<int, int>, greater<int>> pq;  // pair: distance, index 순으로. pair.first에 따라서 내림차순 정렬이 된다.
    pq.push(make_pair(0, start));

    while (!pq.empty()) {
        int curr = pq.top().second;
        int dist = pq.top().first;
        pq.pop();
        if (d[curr] < dist) continue;

        for (int i=0; i<a[curr].size(); i++) {
            int next = a[curr][i].second;   // curr 노드의 인접 노드
            int nextDist = dist + a[curr][i].first; // curr 노드를 거쳐서 인접 노드로 가는 거리
            if (nextDist < d[next]) // 최소 비용 업데이트
                d[next] = nextDist;
                pq.push(make_pair(nextDist, next));
        }
    }
}

int main() {
    /*
    initialize array d[6] with all infinity.
    a[6]에 간선 정보 업데이트.
    다익스트라 함수 구현.
    */
    
}
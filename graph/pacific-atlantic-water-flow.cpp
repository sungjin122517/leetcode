#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
//     vector<vector<int>> result;

//     for (int i=0; i<heights.size(); i++) {
//         for (int j=0; j<heights[i].size(); j++) {
//             if (dfsPacific(i, j, heights))   //
//                 if (dfsAtlantic(i, j, heights))
//                     result.push_back({i, j});
//         }
//     }

//     return result;
// }

// bool dfsPacific(int row, int col, vector<vector<int>>& heights) {
//     // bool temp = false;

//     if (row <= 0 || col <= 0)
//         return true;
//     if (heights[row][col] < heights[row][col-1])
//         return false;
//     if (heights[row][col] < heights[row-1][col])
//         return false;
    
//     // if (dfsPacific(row, col-1, heights))
//     //     return true;
//     // if (dfsPacific(row-1, col, heights))
//     //     return true;

//     if (dfsPacific(row, col-1, heights))
//         return true;
//     if (dfsPacific(row-1, col, heights))
//         return true;
    
//     return false;
// }

// bool dfsAtlantic(int row, int col, vector<vector<int>>& heights) {
//     // bool temp = false;

//     if (row >= heights.size()-1 || col >= heights[row].size()-1)
//         return true;
//     if (heights[row][col] < heights[row][col+1])
//         return false;
//     if (heights[row][col] < heights[row+1][col])
//         return false;

//     if (dfsAtlantic(row, col+1, heights))
//         return true;
//     if (dfsAtlantic(row+1, col, heights))
//         return true;
    
//     return false;
// }

vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
    vector<vector<int>> result;
    queue<pair<int, int>> qPac, qAtl;
    int row = heights.size();
    int col = heights[0].size();

    for (int i=0; i<row; i++) {
        qPac.push({0, i});
        qAtl.push({col-1, i});
    }
    for (int j=0; j<col-1; j++) {
        qPac.push({j+1, 0});
        qAtl.push({j, row-1});
    }

    vector<vector<bool>> visitedP(row, vector<bool>(col, false));
    vector<vector<bool>> visitedA(row, vector<bool>(col, false));

    BFS(heights, visitedP, qPac, row, col);
    BFS(heights, visitedA, qAtl, row, col);

    for (int i=0; i<col; i++) {
        for (int j=0; j<row; j++) {
            if (visitedP[i][j] && visitedA[i][j]) {
                result.push_back({i, j});
            }
        }
    }

    return result;
}

// function to check if coordinate (i, j) lies inside N*M matrix
bool safe(int i, int j, int row, int col) {
    if (i<0 || j<0 || i>=col || j>=row)
        return false;
    return true;
}

// perform BFS traversal and mark visited cells
void BFS(vector<vector<int>> heights, vector<vector<bool>> &visited, queue<pair<int, int>> q, int row, int col) {
    while (!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();
        visited[cur.first][cur.second] = true;

        // check right side of the cell and see if right cell can reach the current cell
        if (safe(cur.first+1, cur.second, row, col) && heights[cur.first+1][cur.second] >= heights[cur.first][cur.second]
        && visited[cur.first+1][cur.second]==false) {
            q.push({cur.first+1, cur.second});
            visited[cur.first+1][cur.second] = true;
        }
        // check left ...
        if (safe(cur.first-1, cur.second, row, col) && heights[cur.first-1][cur.second] >= heights[cur.first][cur.second]
        && visited[cur.first-1][cur.second]==false) {
            q.push({cur.first-1, cur.second});
            visited[cur.first-1][cur.second] = true;
        }
        // check down ...
        if (safe(cur.first, cur.second-1, row, col) && heights[cur.first][cur.second-1] >= heights[cur.first][cur.second]
        && visited[cur.first][cur.second-1]==false) {
            q.push({cur.first, cur.second-1});
            visited[cur.first][cur.second-1] = true;
        }
        // check up ...
        if (safe(cur.first, cur.second+1, row, col) && heights[cur.first][cur.second+1] >= heights[cur.first][cur.second]
        && visited[cur.first][cur.second+1]==false) {
            q.push({cur.first, cur.second+1});
            visited[cur.first][cur.second+1] = true;
        }
    }
}


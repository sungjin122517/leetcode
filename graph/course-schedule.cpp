#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adjacencyList(numCourses);
        vector<int> visited(numCourses, 0);
        // vector<int> visited;

        // make list of prerequisites of all courses and add to a map.
        for (int i=0; i<prerequisites.size(); i++) {
            adjacencyList[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        // since there may be more than one graph, loop is required.
        for (int i=0; i<numCourses; i++) {
            if (!dfs(i, adjacencyList, visited))
                return false;
        }

        return true;
    }

    bool dfs(int course, unordered_map<int, vector<int>>& adjacencyList, vector<int> visited) {
        // return false if the node is already visited
        if (visited[course]==1)
            return false;
        // if (find(visited.begin(), visited.end(), course) != visited.end())
        //     return false;
        if (adjacencyList[course].size()==0)
            return true;

        visited[course]=1;     // mark node as visiting
        // visited.push_back(course);
        for (int i=0; i<adjacencyList[course].size(); i++) {
            if (!dfs(adjacencyList[course][i], adjacencyList, visited))
                return false;
        }
        // visited.pop_back();
        adjacencyList[course] = {};
        return true;
    }
};





// class Solution {
// public:
//     bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {        
                
//         unordered_map<int, vector<int>> um;
//         vector<int> visited(numCourses, 0);
        
//         //Make list of prerequisites of all courses and add to a map
//         for (auto p: prerequisites)
//         {
//             um[p[0]].push_back(p[1]);
//         }
        
//         //Traverse each course, return true if each prerequisite of the course can be traversed
//         for (int i=0; i<numCourses; i++)
//         {
//             if (!traverse(visited, um, i))
//                 return false;
//         }
        
//         return true;
//     }
    
//     bool traverse (vector<int>& visited, unordered_map<int, vector<int>>& um, int i)
//     {
        
//         if (visited[i]==10) //Already visiting (a cycle exists)
//             return false;
//         if (visited[i]==1)
//             return true;
//         visited[i]=10;      //Mark as visiting
//         for (auto c: um[i])
//         {
//             if (!traverse(visited, um, c))
//                 return false;
//         }
//         visited[i] = 1;     //Visited
//         return true;
//     }
    
// };
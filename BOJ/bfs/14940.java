/* 
14940. 쉬운 최단거리

n=1 000 000 -> O(n)
bfs? dp?
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int m;
    static int[][] map;
    static boolean isStartChecked = false;

    static int[][] distance;
    static boolean[][] isVisited;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};


    public static void main(String[] args) throws IOException {

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
    
        map = new int[n][m];
        int row = 0;
        int col = 0;
    
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(in.readLine());
            for (int j=0; j<m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                
                if (!isStartChecked) {
                    if (map[i][j] == 2) {
                        isStartChecked = true;
                            row = i;
                            col = j;
                    }
                }
            }
        }
    
        distance = new int[n][m];
        isVisited = new boolean[n][m];
        
        bfs(row, col);
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (!isVisited[i][j]) {
                    distance[i][j] = -1;
                }
                System.out.print(distance[i][j] + " ");
            }
            System.out.println();
        }
        
    }
    
    private static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        isVisited[x][y] = true;
        
        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            
            for (int i=0; i<4; i++) {
                int nx = temp[0] + dx[i];
                int ny = temp[1] + dy[i];
                
                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    if (!isVisited[nx][ny]) {
                        isVisited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                        distance[nx][ny] = distance[x][y] + 1;
                    }
                }
            }
        }
    }
}
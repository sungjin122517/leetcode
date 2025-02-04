/*
14888. 연산자 끼워넣기

브루트포스 + 백트래킹


*/

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    public static int MAX = Integer.MIN_VALUE;
    public static int MIN = Integer.MAX_VALUE;
    public static int n;
    public static int[] number;
    public static int[] operator = new int[4];
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        number = new int[n];
        for (int i=0; i<n; i++) {
            number[i] = Integer.parseInt(st.nextToken());
        }
        
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<4; i++) {
            operator[i] = Integer.parseInt(st.nextToken());
        }
        
        dfs(number[0], 1);
        
        System.out.println(MAX);
        System.out.println(MIN);
        
    }
    
    public static void dfs(int num, int idx) {
        
        if (idx == n) {
            MAX = Math.max(MAX, num);
            MIN = Math.min(MIN, num);
            return;
        }
        
        for (int i=0; i<4; i++) {
            
            if (operator[i] > 0) {
                operator[i]--;
                
                switch (i) {
                    case 0: dfs(num + number[idx], idx + 1);
                        break;
                    case 1: dfs(num - number[idx], idx + 1);
                        break;
                    case 2: dfs(num * number[idx], idx + 1);
                        break;
                    case 3: dfs(num / number[idx], idx + 1);
                        break;
                }
                
                operator[i]++;
            }
        }
    }
}
/*
20992. 겹치는 건 싫어

two pointer
java array를 크기와 함께 initialize 하면 element의 기본 값이 0이다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    
    public static void main(String[] args) throws IOException {
        
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        
        int arr[] = new int[n];
        st = new StringTokenizer(in.readLine());
        for (int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        int ans = 0;
        int cnt[] = new int[100001];
        int start = 0;
        int end = 0;
        
        while(end < arr.length) {
            while(end < arr.length && cnt[arr[end]] + 1 <= k) {
                cnt[arr[end]]++;
                end++;
            }
            
            int len = end - start;
            ans = Math.max(ans, len);
            cnt[arr[end]]--;
            start++;
        }
        
        System.out.println(ans);
    }
}
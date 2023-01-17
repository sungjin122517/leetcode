import java.util.*;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        HashSet<String> hs = new HashSet<>();
        for (String word : wordDict) {
            hs.add(word);
        }

        boolean[] dp = new boolean[s.length()+1];
        dp[0] = true;

        for (int i=1; i<=s.length(); i++) {
            for (int j=i-1; j>=0; j--) {
                if (dp[j] && hs.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.length()+1];
    }
}
import java.util.*;
class Solution {
    public int longestConsecutive(int[] nums) {
        int l = 0;
       HashSet<Integer> hs = new HashSet<Integer>();
       for (int n: nums){
        hs.add(n);
       }
        for (int n :hs){
            if(!hs.contains(n-1)){
                int t = 0;
                while (hs.contains(n + t)) {
                    t++;
                }
                l = Math.max(t, l);
            }
        }
        return l;
    }
}
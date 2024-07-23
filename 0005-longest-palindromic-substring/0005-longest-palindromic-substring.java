import java.util.*;
class Solution {
    private String str;
    public String longestPalindrome(String s) {

        str = s;

        String result = "";
        String palindrome = "";

        StringBuffer sb = new StringBuffer(s); 

        if(s.length() < 2 || sb.reverse().equals(s)) return s;

        for(int i=0; i<s.length()-1; i++) {
            palindrome = expand(i,i+2).length() >= expand(i,i+1).length() ? expand(i,i+2) : expand(i, i+1);
            if(result.length() < palindrome.length()) result = palindrome; 
        }
        return result;
    }

    public String expand(int left, int right) {
        while((left >= 0 && right < str.length()) && str.charAt(left) == str.charAt(right)) {
            left--;
            right++;
        }
        return str.substring(left+1, right);
    }
}
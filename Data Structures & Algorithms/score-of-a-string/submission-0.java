class Solution {
    public int scoreOfString(String s) {
        int sum =0;
        for(int i =0;i<s.length()-1;i++){
            char a = s.charAt(i);
            char b = s.charAt(i+1);
            int n = a - b - 0;
            n = Math.abs(n);
            sum = n+ sum;
        }
        return sum;
    }
}
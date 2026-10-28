class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;

        // method 1
        
        // HashMap<Character,Integer> mapS = new HashMap<>();
        // HashMap<Character,Integer> mapT = new HashMap<>();
        // for(int i=0;i<s.length();i++){
        //     char a = s.charAt(i);
        //     char b = t.charAt(i);
        //     mapS.put(a,mapS.getOrDefault(a,0)+1);
        //     mapT.put(b,mapT.getOrDefault(b,0)+1);
        // }
        // return mapS.equals(mapT);

        // method2

        int arr[]= new int[26];
        for(int i=0;i<s.length();i++){
            arr[s.charAt(i) - 'a']++;
            arr[t.charAt(i) - 'a']--;
        }
        for(int num:arr){
            if(num!=0)return false;
        }
        return true;
    }
}

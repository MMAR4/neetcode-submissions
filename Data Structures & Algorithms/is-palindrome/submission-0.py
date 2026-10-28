class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and self.isalphanum(s[left]) == False:
                left +=1
            while left < right and self.isalphanum(s[right]) == False:
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1
        return True
    def isalphanum(self,s):
        return     (ord('a')<= ord(s)<= ord('z') 
                or ord('A')<= ord(s)<= ord('Z') 
                or ord('0') <= ord(s) <= ord('9'))

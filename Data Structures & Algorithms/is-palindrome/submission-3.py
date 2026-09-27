class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s = "".join([character.lower() for character in s if character.isalnum()])
        left, right = 0, len(s) - 1

        while left < right:
            print(f'{s[left]} = {s[right]} ?')
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return False
        
        return True
            
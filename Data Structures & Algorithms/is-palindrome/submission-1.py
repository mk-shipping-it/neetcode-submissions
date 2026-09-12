class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        left, right = 0, len(s) - 1

        print(f'Length of string {s}: {right} - {left}')

        while left < right:
                
            if s[right] != s[left]:
                return False
            else:
                right-=1
                left+=1
        
        return True
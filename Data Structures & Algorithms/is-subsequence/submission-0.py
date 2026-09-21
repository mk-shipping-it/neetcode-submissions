class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s = s + '1'
        t = t + '1'
        
        len_t, len_s = len(t), len(s)

        left, right = 0, 0


        print(s, t)

        while left < len_s and right < len_t:

            if s[left] == '1' and t[right] == '1':
                return True
            
            if s[left] == t[right]:
                print(f's[left]: {s[left]} and t[right]: {t[right]}')
                left+=1
                right+=1
                
            if s[left] != t[right]:
                right+=1

                # assuming the right pointer is in charge of covering the word

        return False
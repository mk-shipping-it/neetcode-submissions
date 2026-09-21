class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        


        # s = s + '1'
        # t = t + '1'
        
        len_t, len_s = len(t), len(s)

        left, right = 0, 0


        print(s, t)

        while left < len_s and right < len_t:

            # if s[left] == '1' and t[right] == '1':
            #     return True
            
            if s[left] == t[right]:
                print(f's[left]: {s[left]} and t[right]: {t[right]}')
                left+=1
                right+=1
            
            # the right pointer updates to point to a null array index, MUST BE STOPPED IN ITS TRACKS
            if right == len_t or left == len_s:
                break  

            if s[left] != t[right]:
                left+=1

                # assuming the right pointer is in charge of covering the word

        print(len(t[right:]))
        return len(t[right:])
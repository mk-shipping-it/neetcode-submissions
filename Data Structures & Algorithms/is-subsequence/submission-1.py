class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        left, right = 0, 0

        s = s + " "
        t = t + " "
        count = 0
        # since s is a subsequence it must be lesser than or equal to t
        
        while right < len(t):
            # condition to move both pointers

            if s[left] == t[right]:
                print(s[left], t[right])
                left+=1
                right+=1
                count+=1

            elif s[left] == " " and t[right] == " ":
                break
            else:
                #print(s[right])
                right+=1
        
        print(count)
        return count == len(s)

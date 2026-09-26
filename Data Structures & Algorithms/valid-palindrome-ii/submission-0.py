class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # pointer init at l and r
        # if value mismatch only allowing for 1, swap with the last position

        l, r = 0, len(s) - 1

        while l<r:

            if s[l]!=s[r]:
                # skipping either one to check if match
                # not bothering to join back since others started off with being pals anyway
                skip_l = s[l+1 : r+1]
                skip_r = s[l : r]


                if skip_l == skip_l[::-1] or skip_r == skip_r[::-1]:
                    return True
                else:
                    return False
            l+=1
            r-=1
        
        return True
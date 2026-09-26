class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        firstIdx = {}
        lastIdx = {}

        for i, c in enumerate(s):
            if c not in firstIdx:
                firstIdx[c] = i
            else:
                print(i - firstIdx[c] - 1, end = " ")
                res = max(res, i - firstIdx[c] - 1)
        
        print(firstIdx, res, end=" ")

        # for c in lastIdx:
        #     print(f'\n Difference b/w {lastIdx[c]} and {firstIdx[c]}: {lastIdx[c] - firstIdx[c] - 1}')
        #     res = max(res, lastIdx[c] - firstIdx[c] - 1)

        return res
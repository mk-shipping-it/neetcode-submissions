class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # max suffix from the right
        # except the rightmost element

        res = [0] * len(arr)
        res[-1] = -1

        print(res)
        for i in range(len(arr) - 1, 0, -1):
            print(f'max of res[i] = max({res[i]}, {arr[i]}) = {max(res[i], arr[i])}')
            res[i-1] = max(res[i], arr[i])
        
        print(res)
        return res
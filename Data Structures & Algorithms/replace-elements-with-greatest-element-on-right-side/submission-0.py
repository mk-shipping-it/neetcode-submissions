class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        len_arr = len(arr)
        suffix_array = [0] * (len_arr - 1)
        suffix_array.append(-1)

        for i in range(len_arr - 2, -1, -1):

            suffix_array[i] = max(suffix_array[i+1], arr[i+1])
        
        return suffix_array

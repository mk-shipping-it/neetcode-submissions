class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        first_index_substring = needle[0]
        change_dir = 0
        while first_index_substring in haystack[change_dir:]:
            haystack_window_beginning = haystack.index(first_index_substring, change_dir)
            print(f'The starting index of {first_index_substring} is {haystack_window_beginning}')
            # roll over
            # simple left and right pointers would also work
            left, right, count = 0, haystack_window_beginning, 0
            while left < len(needle) and right < len(haystack):
                if haystack[right] != needle[left]:
                    break
                else:
                    print(f'haystack and needle are the same {haystack[right]} and {needle[left]}', )
                    left+=1
                    right+=1
                    count+=1
            print(count)
            if count == len(needle):
                return haystack_window_beginning
            change_dir = haystack_window_beginning + 1
        return -1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # building the alien dictionary
        alien_dict = {}

        for index, alien_terms in enumerate(order):
            alien_dict[alien_terms] = index
            print(f'{alien_terms} mapped to {index}')

        # compare ith word to i+1th word

        for i in range(0, len(words) - 1):
            min_len = min(len(words[i]), len(words[i+1]))
            print(words[i], '-->', words[i+1])
            count = 0
            for chars in range(0, min_len):
                if alien_dict[words[i][chars]] > alien_dict[words[i+1][chars]]:
                    return False
                elif alien_dict[words[i][chars]] == alien_dict[words[i+1][chars]]:
                    count+=1
                    continue
                else:
                    print('True that', alien_dict[words[i][chars]], '<=', alien_dict[words[i+1][chars]], 'in terms of the alien dictionary')
                    break
            if count == min_len and (len(words[i]) > len(words[i+1])):
                return False
        return True


from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloons = defaultdict(int)
        balloons['b'] = 0
        balloons['a'] = 0
        balloons['l'] = 0
        balloons['o'] = 0
        balloons['n'] = 0
        
        for possiblities in text:
            balloons[possiblities]+=1
            #print(f'Frequency of {possiblities} in text is {balloons[possiblities]}')

        print(balloons)
        count = 0
        factor = True            
        while factor:
            factor = True if (balloons.get('b') >= 1 and balloons.get('a') >= 1 and balloons.get('l') >= 2 and balloons.get('o') >= 2 and balloons.get('n') >= 1) else False
            print('before subtraction')
            print(balloons)
            if factor:
                # subtract the exact number of character occurances of balloon
                balloons['b'] = balloons['b'] - 1
                balloons['a'] = balloons['a'] - 1
                balloons['l'] = balloons['l'] - 2
                balloons['o'] = balloons['o'] - 2
                balloons['n'] = balloons['n'] - 1
                count+=1
                print('after subtraction')
                print(balloons)
        return count
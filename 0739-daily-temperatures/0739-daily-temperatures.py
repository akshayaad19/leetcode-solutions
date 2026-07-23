class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmstack = []
        resultstack = [0] * len(temperatures)
        for i in range (0, len(temperatures)):
            while(warmstack and temperatures[i]> temperatures[warmstack[-1]]):
                resultstack[warmstack[-1]] = i-warmstack[-1]
                warmstack.pop()           
            warmstack.append(i)
        return resultstack


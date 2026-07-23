class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in range(0, len(tokens)):
            
            if tokens[i] not in "+/-*":
                result.append(int(tokens[i]))
            else:
                firstpop = result.pop()
                secondpop = result.pop()
                if tokens[i] == "+":
                    ans = secondpop + firstpop 
                elif tokens[i] == "-":
                    ans = secondpop - firstpop 
                elif tokens[i] == "*":
                    ans = secondpop * firstpop 
                else:
                    ans = secondpop / firstpop 
                result.append(int(ans))
        return result[0]



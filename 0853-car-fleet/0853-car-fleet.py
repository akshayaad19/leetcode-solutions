class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cardict = {}
        for i in range(0, len(position)):
            timetotarget = ((target-position[i])/speed[i])
            cardict[position[i]] = timetotarget
        sorted_cars = sorted(cardict.items(), reverse=True)
        stack = []
        for pos, time in sorted_cars:
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)

        return len(stack)        

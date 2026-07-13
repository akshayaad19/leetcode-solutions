class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        def backtrace():
            if len(nums)==len(path):
                result.append(path[:])
                return 
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrace()
                    path.pop()
        backtrace()
        return result
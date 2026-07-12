class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        result = nums[0]
        for num in range(1, len(nums)):
            temp = currMax 
            currMax = max(currMax*nums[num],currMin*nums[num],nums[num])
            currMin = min(temp*nums[num],currMin*nums[num],nums[num])
            if currMax > result:
                result =  currMax
        return result


        
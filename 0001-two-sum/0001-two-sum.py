class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumhash = {}
        for i in range(len(nums)):
            if target-nums[i] in sumhash:
                indexi = sumhash.get(target-nums[i])
                return(indexi, i)  
            else:
                sumhash[nums[i]]=i
                
      

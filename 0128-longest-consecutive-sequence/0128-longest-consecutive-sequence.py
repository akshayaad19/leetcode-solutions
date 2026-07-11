class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0
        for num in setnums:
            if num-1 not in setnums:
                length = 1
                while (num+1) in setnums:
                    num = num + 1
                    length += 1
                if length > longest:
                    longest = length
        return longest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        print(Counter(nums))
        kelements = (Counter(nums)).most_common()[:k]
        print(kelements)
        for i in kelements:
            l.append(i[0])
        return l
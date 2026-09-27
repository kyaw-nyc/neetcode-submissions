class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
            d[nums[i]] += 1
        
        pairs = sorted(d.items(), key=lambda x: x[1], reverse = True)

        lst = []
        for i in range(k):
            lst.append(pairs[i][0])

        return lst
        
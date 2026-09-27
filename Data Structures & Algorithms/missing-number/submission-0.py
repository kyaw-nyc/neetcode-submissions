class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sums = n * (n + 1) // 2
        actual_sums = sum(nums)
        return expected_sums - actual_sums

        

        
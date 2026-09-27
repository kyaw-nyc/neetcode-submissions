class Solution:
    def hammingWeight(self, n: int) -> int:
        return int((bin(n)), 2).bit_count()
            
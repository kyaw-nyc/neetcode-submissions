class Solution:

    def hammingweights(self, n: int) -> int:
        return n.bit_count()

    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n + 1):
            lst.append(self.hammingweights(i))

        return lst
        
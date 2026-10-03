class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        n = len(stones)


        while n > 1:
            stones.sort()
            x = stones[-1]
            y = stones[-2]

            if x == y:
                stones.pop(-1)
                stones.pop(-1)

            else:
                stones[-2] = x - y
                stones.pop(-1)
            
            
            n = len(stones)

            
        return stones[0] if len(stones) else 0

        
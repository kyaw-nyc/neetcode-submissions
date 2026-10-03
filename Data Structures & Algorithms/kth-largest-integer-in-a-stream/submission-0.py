class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        nums = self.nums
        nums.append(val)

        n = len(nums)

        nums.sort()
        return nums[-self.k]
            


        

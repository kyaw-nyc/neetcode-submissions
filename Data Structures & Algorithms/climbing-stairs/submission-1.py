class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2


        two_step_back = 1
        one_step_back = 2

        for i in range(3, n + 1):
            current_steps = two_step_back + one_step_back
            two_step_back = one_step_back
            one_step_back = current_steps
            
        return current_steps
            
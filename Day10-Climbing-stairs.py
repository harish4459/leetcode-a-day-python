You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

Solution -

class Solution:
    def climbStairs(self, n: int) -> int:
        self.ht = {}
        return self.f(0, n)
        
    def f(self, i, n):
        if (i > n):
            return 0
        elif (i == n ):
            return 1
        else:
            if (i in self.ht):
                return self.ht[i]
            else:
                self.ht[i] = self.f(i+1, n) + self.f(i + 2, n)
                return self.ht[i]



solution -
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        for i in range(n -1):
            temp = one
            one = one + two
            two = temp
        return one
            


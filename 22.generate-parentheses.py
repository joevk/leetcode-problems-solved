#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def backtrack(open,close):
            if open==close==n:
                res.append("".join(stack))
                return 
            
            if open<n:
                stack.append('(')
                backtrack(open+1,close)
                stack.pop()

            if close<open:
                stack.append(')')
                backtrack(open,close+1)
                stack.pop()

        backtrack(0,0)
        return res

sol=Solution()
op=sol.generateParenthesis(3)
print(op)
    


            


        
# @lc code=end


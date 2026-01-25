#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num=0
        originalX=x
        while x>0:
            last_digit=x%10
            reversed_num=reversed_num*10+last_digit
            x=x//10
        if reversed_num==originalX:
            return True 
        else: 
            return False


        
# @lc code=end

    #   s=str(x)
    #     if s==s[::-1]:
    #         return True
    #     else:
    #         return False
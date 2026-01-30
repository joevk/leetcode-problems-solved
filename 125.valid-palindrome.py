#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            if s[l].isalnum()==False:
                l+=1
            elif s[r].isalnum()==False:
                r-=1
            elif s[l].lower()!=s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True

print(Solution().isPalindrome("A MAN, A PLAN, A CANAL: panama "))        
# @lc code=end


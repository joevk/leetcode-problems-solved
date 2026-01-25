#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
                
        
                k=0
                for i in range(len(nums)):
                        if i==len(nums)-1 or nums[i]!=nums[i+1]:
                                nums[k]=nums[i]
     
                                k+=1
                    
                return k

sol=Solution()
print(sol.removeDuplicates([1,1,1,2,7,8,8]))

        
# @lc code=end


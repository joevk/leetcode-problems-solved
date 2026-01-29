#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        p1=m-1
        p2=n-1
        k=len(nums1)-1

        while p2>=0:
            if p1<0 or nums1[p1]<=nums2[p2]:
                nums1[k]=nums2[p2]
                k-=1
                p2-=1
    
            else:
                nums1[k]=nums1[p1]
                p1-=1
                k-=1


        #nums1[k]=nums1[p1]


nums1 = [2,0]
m = 1
nums2 = [1]        
n = 1
print(Solution().merge(nums1,m,nums2,n))
print(nums1)
# @lc code=end


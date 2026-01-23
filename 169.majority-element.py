#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate=1
        count=0

        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1

        return candidate

sol=Solution()
eg=[5,3,4,5,5,3,3,3]
print(sol.majorityElement(eg))

        
# @lc code=end
'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq_num={}
        for num in nums:
            freq_num[num]=freq_num.get(num,0)+1

        return max(freq_num,key=freq_num.get)



sol=Solution()
eg=[1,3,4,5,5,3,3,3]
print(sol.majorityElement(eg))
'''
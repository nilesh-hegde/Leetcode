'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threesum=[]
        nums.sort()
        i=0
        while i<=len(nums)-1:
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                i=i+1
                continue
            l=i+1
            h=len(nums)-1
            while l<h:
                if l>i+1 and nums[l]==nums[l-1]:
                    l=l+1
                    continue
                if h<len(nums)-1 and nums[h]==nums[h+1]:
                    h=h-1
                    continue
                if nums[i]+nums[l]+nums[h]<0:
                    l=l+1
                    continue
                if nums[i]+nums[l]+nums[h]>0:
                    h=h-1
                    continue
                threesum.append([nums[i],nums[l],nums[h]])
                l=l+1
                h=h-1
            i=i+1
        return threesum
        
                
                
                
        
        
        
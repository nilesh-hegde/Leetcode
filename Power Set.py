'''
JULY LEETCODING CHALLENGE Day 11

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums==[]:
            return [[]]
        else:
            x=self.subsets(nums[:-1])
            return x + [[nums[-1]]+a for a in x]

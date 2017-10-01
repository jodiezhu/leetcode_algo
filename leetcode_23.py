#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 14:14:45 2017

@author: jie
"""

class Solution(object):
    def firstMissingPositive(self,nums):
        if not nums:
            return 1
        
        for i in xrange(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                self.swap(nums,i)
                
        for i in xrange(len(nums)):
            if nums[i] != i+1:
                return i+1
        return nums[-1]+1
    
    def swap(self,nums,i):
        c = nums[i] - 1
        nums[i], nums[c] = nums[c], nums[i]
       
s=Solution()
print(s.firstMissingPositive([3,4,-1,1]))
        
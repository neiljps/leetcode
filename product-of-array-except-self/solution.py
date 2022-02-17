#!/bin/env python3
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        # Given an integer array nums, return an array answer 
        # such that answer[i] is equal to the product of 
        # all the elements of nums except nums[i].
        # You must write an algorithm that runs in O(n) time 
        # and without using the division operation.

        for i in range(0, len(nums)):
            toMultiply = []
            if i == 0:
                toMultiply = nums[1:]

            elif i == (len(nums) - 1):
                toMultiply = nums[:-1]
            else:
                numsCopy = nums.copy()
                numsCopy.pop(i)
                toMultiply = numsCopy
            
            product = 1
            for num in toMultiply:
                product *= num
            answer.append(product)

        return answer

s = Solution().productExceptSelf([1, 2, 3, 4])
print(s)

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

        hashTbl = {}
        # put the numbers to multiply in a hash table, keyed by i
        for i in range(0, len(nums)):
            if i == 0:
                hashTbl[i] = nums[1:]
            elif i == (len(nums) - 1):
                hashTbl[i] = nums[:-1]
            else:
                numsCopy = nums.copy()
                numsCopy.pop(i)
                hashTbl[i] = numsCopy

        # for each key, multiply the numbers and put in the answer
        for i in range(0, len(nums)):
            toMultiply = hashTbl[i]

            product = 1
            for num in toMultiply:
                product *= num
            answer.append(product)

        # hint: product = multiplication
        #for i in range(0, len(nums)):
        #    toMultiply = []
        #    for j in range(0, len(nums)):
        #        if i != j:
        #            toMultiply.append(nums[j])

        #    product = 1
        #    for num in toMultiply:
        #        product *= num
        #    answer.append(product)

        return answer

s = Solution().productExceptSelf([-1, 1, 0, -3, 3])
print(s)

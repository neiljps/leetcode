#!/usr/bin/python3
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answers = {}

        for i in range(0, len(nums)):
            difference = target - nums[i]

            # check if target - difference is already in answers
            if (target - difference) in answers.keys():
                # we have a match
                return [i, answers[target - difference]]
            else: # place in dictionary for later
                answers[difference] = i

        return []

def __main__():
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))

    return

if __name__ == "__main__":
    __main__()

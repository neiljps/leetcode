#!/usr/bin/python3

#Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

#Return k after placing the final result in the first k slots of nums.

#Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


def removeDuplicates(nums):
	for i in range(0, len(nums)):
		if (i + 1) < len(nums):
			# remove all subsequent duplicates of this number
			while ((i + 1) < len(nums)) and (nums[i] == nums[i + 1]):
				#print("i: " + str(i) + " " + str(nums[i]) + " " + str(nums[i + 1]))
				nums.pop(i) 
	return len(nums)

#nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#nums = [1, 1, 2]
nums = [1, 2, 2, 2, 2, 2, 3, 4]
expectedNums = [1, 2]

k = removeDuplicates(nums)
#k = f(nums)

print("k: " + str(k))
print(nums)



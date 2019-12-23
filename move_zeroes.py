'''
Source:
Problem: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example 1:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

'''

# Test Case
input_one = [0,1,0,3,12]
input_two = [0, 0, 1]

''' 
How to handle two 0's that are side by side while messing with the index values????

'''


def moveZeroes(nums):
    i = 0
    counter = 0
    while i < len(nums):
        if nums[i] == 0:
            counter += 1
            i += 1
        else:
            i += 1

    nums = [ el for el in nums if el != 0] 

    for i in range(counter):
        nums.append(0)

    print(nums)


print(moveZeroes(input_one))

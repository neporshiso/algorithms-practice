'''
Source: https://leetcode.com/problems/move-zeroes/
Problem: Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example 1:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

'''

# Test Case
input_one = [0,1,0,3,12]
input_two = [0, 0, 1]

def moveZeroes(nums):
    for i in reversed(nums):
        if i == 0:
            nums.remove(i)
            nums.append(i)

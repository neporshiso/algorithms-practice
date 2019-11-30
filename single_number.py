'''

Source: https://leetcode.com/problems/single-number/

Problem: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

'''


test_input_one = [2,2,1]
test_input_two = [4,1,2,1,2]

def single_number(arr):
    storage = {}
    for i in range(len(arr)):
        if arr[i] not in storage:
            storage[arr[i]] = 1
        else:
            storage[arr[i]] += 1

    for val,freq in storage.items():
        if freq == 1:
            return val
    

print(single_number(test_input_two))
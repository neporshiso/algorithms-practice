'''
Source: https://leetcode.com/problems/contains-duplicate/submissions/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''


input = [0, 1, 2, 3]


def duplicate_detection(list):
    tracker = {}
    for i in list:
        if i not in tracker:
            tracker[i] = 1
        else:
            return True

    return False

print(duplicate_detection(input))
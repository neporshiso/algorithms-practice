'''
Source: https://leetcode.com/problems/rotate-array/
Problem:  Given an array, rotate the array to the right by k steps, where k is non-negative.

'''

input = ['d', 'r', 'f', 'a', 't']
offset = 2

def rotate_array(list, k):
    shifted_elements = list[len(list)-k:]
    del list[len(list)-k:]
    for i in reversed(range(len(shifted_elements))):
        list.insert(0, shifted_elements[i])

rotate_array(input, offset)
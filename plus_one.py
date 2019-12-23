'''
Source: https://leetcode.com/problems/plus-one/
Problem: Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
# Test cases
input_one = [1, 2, 3]
input_two = [4, 3, 2, 1]
input_three = [1, 3, 9]
input_four = [9]
input_five = [9, 9]

def plusOne(digits):
    last = digits[-1]
    # handles an array with one element 9
    if len(digits) == 1:
        if last != 9:
            digits[-1] += 1
        else:
            digits.insert(0, 1)
            digits[-1] = 0

        return digits

    # handles vast majority of test cases
    if last != 9:
        digits[-1] += 1
        return digits

    # handles multiple 9's at the end of an array
    if last == 9:
        i = -1
        # want to keep checking for 9's starting at the end of the array
        while True:
            try:
                digits[i] = 0
                if digits[i-1] != 9:
                    digits[i-1] += 1
                    return digits
                else:
                    digits[i-1] += 1
                    i -= 1
            # once digits[i-1] triggers an IndexError, we've can stop the while loop, insert a 1, and break out
            except IndexError:
                digits.insert(i, 1)
                return digits

print(plusOne(input_four))

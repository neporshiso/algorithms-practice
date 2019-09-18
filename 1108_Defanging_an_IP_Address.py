'''
Leetcode - 
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

'''


class Solution:
    def defangIPaddr(self, address: str):
        d_str = ""

        for i in address:
            if i == ".":
                d_str += "[.]"
            else:
                d_str += i

        return d_str


answer = Solution()
print(answer.defangIPaddr("1.1.1.1"))

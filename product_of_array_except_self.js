/*
Source: https://leetcode.com/problems/product-of-array-except-self/
Problem: Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
*/


const input_one = [1,2,3,4]
const input_two = [0, 0]
const input_three = [1, 1]


var productExceptSelf = function(nums) {
    let output = []
    let numsCopy = [...nums]

    nums.forEach(element => {
        numsCopy.splice(numsCopy.indexOf(element), 1)
        let value = numsCopy.reduce((product, current) => product * current);
        output.push(value)
        numsCopy.push(element)
    });

    return output
};

console.log(productExceptSelf(input_two))
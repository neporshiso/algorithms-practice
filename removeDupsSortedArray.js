// Given a sorted array nums,
// 1. remove the duplicates in-place such that each element appear only once
// 2. return the new length

// Some commentary... I peeked at the solution for this challenge and noticed that although the instructions ask to "remove the duplicates in-place", the solution didn't really do that. 
// This code isn't as performant as I would like but it mutates the sorted array so that each element appears only once and returns the length of the array with no duplicate values

let input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
let input2 = [1, 1, 2];
let input3 = [];

const removeDuplicates = nums => {
  if (nums.length == 0) return 0;
  let i = nums.length - 1;
  
  for (let j = nums.length - 2; j >= 0; j--) {
    console.log(j);
    if (nums[j] == nums[i]) {
      nums.splice(i, 1);
    }
    i--;
  }
  return nums.length;
};

// removeDuplicates(input);
// removeDuplicates(input2)
// removeDuplicates(input3)

console.log('answer', removeDuplicates(input)); // 5
// console.log(removeDuplicates(input2)); // 2
// console.log(removeDuplicates(input3)); // 0

// Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

let input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
let input2 = [1, 1, 2];
let input3 = [];

const removeDuplicates = nums => {
  if (nums.length == 0) return 0;
  let i = 0;
  for (j = 1; j < nums.length; j++) {
    if (nums[j] != nums[i]) {
      i++;
      nums[i] = nums[j];
    }
  }
  console.log(nums)
  console.log(i + 1)
  return i + 1;
};

// removeDuplicates(input)
removeDuplicates(input2)
// removeDuplicates(input3)

// console.log(removeDuplicates(input)); // 5
// console.log(removeDuplicates(input2)); // 2
// console.log(removeDuplicates(input3)); // 0

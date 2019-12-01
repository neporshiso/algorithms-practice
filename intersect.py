'''
Source: 
Problem: Given two arrays, write a function to compute their intersection.

'''
# These are some test inputs I threw at the intersect function
nums1 = [1,2,2,1]
nums2 = [2,2]

nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

five = [1]
six = [1]

seven = [1]
eight = [1, 1]

nine = [3,1,2]
ten = [1,1]

def intersect(nums1, nums2):
    answer = []
    storage = {}
    len_1 = len(nums1)
    len_2 = len(nums2)

    def build_dict(arr):
        for i in arr:
            if i not in storage:
                storage[i] = 1
            else:
                storage[i] += 1

    def check_intersect(arr):
        for i in arr:
            if i in storage and storage[i] >= 1:
                answer.append(i)
                storage[i] -= 1
    # Want to keep the loop short so I want to make sure I loop over the smaller array and build a dictionary of the larger one            
    if len_1 > len_2:
        build_dict(nums1)
        check_intersect(nums2)
    else:
        build_dict(nums2)
        check_intersect(nums1)
                       
    return answer
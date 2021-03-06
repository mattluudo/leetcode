"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution(object):
    # Brute force solution with time O(n^2) and space O(1). Loop through twice and adding up numbers.
    def twoSum_brute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                two_sum = nums[x] + nums[y]
                if two_sum == target:
                    return [x,y]

    # Fast version solution with time O(n) and space O(n). Create dictionary, append each value in nums, and check if target-value exists.
    def twoSum_fast(self, nums, target):
        num_dict = {}
        for i, val in enumerate(nums):
            tar_comp = target - val
            if num_dict.get(tar_comp) != None:
                return [num_dict[tar_comp], i]            
            num_dict[val] = i

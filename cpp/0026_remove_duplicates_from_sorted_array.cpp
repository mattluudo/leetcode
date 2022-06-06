Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 2) {
            return nums.size();
        }
        int prev_val = nums[0];
        int cur_idx = 0;
        for (int ii=1; ii<nums.size(); ii++) {
            if (prev_val != nums[ii]) {
                nums[cur_idx] = prev_val;
                cur_idx++;
                prev_val = nums[ii];
            }
        }
        // Attach last unique value
        nums[cur_idx] = prev_val;
        cur_idx++;
        return cur_idx;
    }
};

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

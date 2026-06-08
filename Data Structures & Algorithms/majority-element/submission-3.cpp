class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end()); //sorting array
        int n = nums.size();
        return nums[n/2]; // returning major elements
    }
};
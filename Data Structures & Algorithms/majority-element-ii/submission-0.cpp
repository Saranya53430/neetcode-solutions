class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // sort the array

        vector<int> res; // store majority element
        int n = nums.size();
        int i = 0; //i points to the beginning of a group of equal numbers

        while(i < n){ //traverse the array
            int j = i+1;
            while(j < n && nums[i] == nums[j]){ //move j until value changes
                j++;
            }
            if(j-i > n/3){ // check majority
                res.push_back(nums[i]);
            }
            i = j;
        }
        return res;
    }
};
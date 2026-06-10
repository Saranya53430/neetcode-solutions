class Solution {
public:
    bool canJump(vector<int>& nums) {
        int mx = 0, n = nums.size(); // mx -> farthest position we can currently reach

        for(int i=0; i<n; i++){
            if(i > mx){
                return false;
            }
            mx = max(mx, i+nums[i]); // update farthest reach
            if(mx >= n-1){
                return true;
            }
        }
        return true;
    }
};

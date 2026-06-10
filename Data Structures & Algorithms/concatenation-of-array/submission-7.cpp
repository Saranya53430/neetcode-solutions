class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans; //store final concatenation array
        for(int i=0; i<2; ++i){ //for copying the entire array two times
            for(int num:nums){ //traverse all elements of nums {1,2,1}
                ans.push_back(num); //add each element to ans
            }
        }
        return ans; //return answer(concatenation)
    }
};

//TC : O[n]
//SC : O[n]
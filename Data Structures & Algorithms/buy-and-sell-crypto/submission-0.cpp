class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP = 0; // store maximum profit as 0
        int buy = prices[0]; // store first day's price in buy
        int n = prices.size();

        for(int i=0; i<n; i++){
            buy = min(buy, prices[i]);
            maxP = max(maxP, prices[i] - buy);
        }
        return maxP;
    }
};

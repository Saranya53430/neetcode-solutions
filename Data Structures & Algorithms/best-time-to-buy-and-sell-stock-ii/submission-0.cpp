class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int TotP = 0;
        int buy = prices[0];
        int n = prices.size();

        for(int i=0; i<n; i++){
            int sell = prices[i] - buy; // calculating change from previous day's price
            if(sell > 0){
                TotP += sell; // summing up total profits
            }
            buy = prices[i];
        }
        return TotP;
    }
};
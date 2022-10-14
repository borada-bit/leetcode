int maxProfit(int* prices, int pricesSize) {
    int low_i = 0;
    int profit = 0;

    for (int i = 1; i < pricesSize; ++i) {
        if (prices[i] < prices[low_i]) {
            low_i = i;
        } else if (prices[i] - prices[low_i] >= profit) {
            profit = prices[i] - prices[low_i];
        } 
    }

    return profit;
}

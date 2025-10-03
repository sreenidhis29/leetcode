class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price; // Update the minimum price if a lower price is found
            } else {
                maxProfit = Math.max(maxProfit, price - minPrice); // Calculate and update the max profit
            }
        }

        return maxProfit;
    }
}

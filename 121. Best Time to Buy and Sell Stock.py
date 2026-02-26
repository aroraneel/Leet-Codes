from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice

        return maxprofit


if __name__ == "__main__":
    sol = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    result = sol.maxProfit(prices)

    print("Prices:", prices)
    print("Maximum Profit:", result)

    # Summary:
    # This program finds the maximum profit from buying and selling a stock once.
    # It keeps track of the minimum price seen so far.
    # At each step, it calculates the possible profit.
    # The maximum profit found during traversal is returned.
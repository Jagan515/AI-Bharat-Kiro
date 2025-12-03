// 0/1 Knapsack Problem - Dynamic Programming
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int knapsack(int capacity, vector<int>& weights, vector<int>& values, int n) {
    // Create DP table
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    // Build table using dynamic programming approach
    for (int i = 1; i <= n; i++) {
        for (int w = 1; w <= capacity; w++) {
            if (weights[i-1] <= w) {
                // Max of including or excluding current item
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                );
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    
    return dp[n][capacity];
}

int main() {
    vector<int> values = {60, 100, 120};
    vector<int> weights = {10, 20, 30};
    int capacity = 50;
    int n = values.size();
    
    int maxValue = knapsack(capacity, weights, values, n);
    cout << "Maximum value in knapsack: " << maxValue << endl;
    
    return 0;
}

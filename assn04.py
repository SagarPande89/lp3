# Memoization approach for 0/1 Knapsack problem
def knapsack(wt, val, W, n):

    # Base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # Choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(wt, val, W-wt[n-1], n-1),
            knapsack(wt, val, W, n-1)
        )
        return t[n][W]
    else:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]

# Driver code
if __name__ == '__main__':
    # Taking user input for the number of items
    n = int(input("Enter the number of items: "))

    # Taking user input for the profits and weights
    profit = list(map(int, input("Enter the profits of the items separated by space: ").split()))
    weight = list(map(int, input("Enter the weights of the items separated by space: ").split()))

    # Taking user input for the maximum capacity of the knapsack
    W = int(input("Enter the maximum capacity of the knapsack: "))

    # We initialize the matrix with -1 at first
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    # Calling the knapsack function and printing the result
    result = knapsack(weight, profit, W, n)
    print(f"The maximum profit is: {result}")


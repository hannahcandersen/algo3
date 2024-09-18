"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/g9pcgr/problems/exactchange2
Find the minimum amount of coins to use to reach as close to the target price as possible.
Iterative bottom-up dynamic programming approach.
"""

t = int(input())

def solve(target, coins):
    solutions = {0: 0} # price: coins_needed

    for coin in coins:
        # Loop through all the prices we have calculated so far
        for price, coins_needed in list(solutions.items()):
            # If we make use of the current coin, we get a different solution
            new_price = price + coin
            new_amount = coins_needed + 1
            # This solution would not be interesting because it exceeds the maximum output size (very important as otherwise the dictionary becomes too big.)
            if new_price > target + max(coins):
                continue
            # Store solution if (a) we have not seen this price before, or (b) it's better than the currently best known solution.
            if new_price not in solutions or solutions[new_price] > new_amount:
                solutions[new_price] = new_amount

    # Search for the first entry that is at least target price in the solution
    for i in range(target, max(solutions) + 1):
        if i in solutions:
            return f"{i} {solutions[i]}"

for _ in range(t):
    price = int(input())
    n = int(input())

    coins = [int(input()) for _ in range(n)]

    print(solve(price, coins))
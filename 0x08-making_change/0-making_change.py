#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total
    """

    if total <= 0:
        return 0

    # Sorting coins in descending order
    coins.sort(reverse=True)

    remaining_total = total
    coins_count = 0
    coin_index = 0
    num_coins = len(coins)

    while remaining_total > 0:
        if coin_index >= num_coins:
            return -1

        if remaining_total - coins[coin_index] >= 0:
            remaining_total -= coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1

    return coins_count


# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))

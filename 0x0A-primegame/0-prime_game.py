#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(num):
    """
    Check if a number is prime.

    Parameters:
    num (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_game_winner(nums):
    """
    Determine the winner of a prime number game.

    Parameters:
    nums (list of int): A list of numbers representing
    the choices made by the players.

    Returns:
    str or None: The name of the winner ("Maria" or "Ben"),
    or None if it's a tie.
    """
    primes = [num for num in range(2, max(nums) + 1) if is_prime(num)]
    wins_maria = 0
    wins_ben = 0

    for n in nums:
        count = sum(1 for prime in primes if prime <= n)
        if count % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1

    if wins_maria > wins_ben:
        return "Maria"
    elif wins_ben > wins_maria:
        return "Ben"
    else:
        return None


def isWinner(x, nums):
    """
    Determine the winner of a prime number game.

    Returns:
    str or None: The name of the winner ("Maria" or "Ben"),
    or None if it's a tie.
    """
    return prime_game_winner(nums)

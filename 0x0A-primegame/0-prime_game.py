#!/usr/bin/python3
"""
isWinner function to solve the Prime Game problem.
"""


def primes(n):
    """Generate a list of prime numbers up to 'n'.

    Args:
        n (int): The upper limit of the range (inclusive).

    Returns:
        list: A list of prime numbers.
    """
    prime_numbers = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime_numbers.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime_numbers


def isWinner(x, nums):
    """Determine the winner of the prime_numbers Game.

    Args:
        x (int): The number of rounds of the game.
        nums (list): The upper limit of the range for each round.

    Returns:
        str or None: The name of the winner (Maria or Ben)
        or None if no winner can be determined.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_wins = Ben_wins = 0
    for i in range(x):
        prime_numbers = primes(nums[i])
        if len(prime_numbers) % 2 == 0:
            Ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > Ben_wins:
        return 'Maria'
    elif Ben_wins > maria_wins:
        return 'Ben'
    return None

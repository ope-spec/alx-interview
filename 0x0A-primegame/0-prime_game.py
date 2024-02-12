#!/usr/bin/python3

def is_prime(num):
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
    return prime_game_winner(nums)


if __name__ == "__main__":
    winner = isWinner(5, [2, 5, 1, 4, 3])
    if winner:
        print("Winner:", winner)
    else:
        print("Winner: None")

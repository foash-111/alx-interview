#!/usr/bin/python3
"""prime game"""
# def whose_turn(x, y):
#     if x > y:
#         return x
#     return y

# def flip_turns(x, y):
#     if x == 1:
#         x = 0
#         y = 1
#         return
#     x = 1
#     y = 0

# def isWinner(x, nums):
#     memo = [1, 2, 3, 5, 7, 9, 11, 13, 17, 19]
#     maria_score = 0
#     ben_score = 0
#     maria_turn = 1
#     ben_turn = 0
#     for i in nums:
#         new_list = []
#         for n in range(1, i):
#             new_list.append(n)

#         for num in new_list:
#             if num in memo:
#                 if whose_turn(maria_turn, ben_turn) == maria_turn:
#                     maria_score += 1
#                 else:
#                     ben_score += 1
#                 new_list.remove(num)
#                 flip_turns(maria_turn, ben_turn)
#             elif(num % 2 != 0):
#                 for j in range(21, num, 2):
#                     if num % j == 0:
#                         break
#                 memo.append[num]


def isWinner(x, nums):
    """check who is winner"""
    if x < 1 or not nums:
        return None

    # Step 1: Find the maximum number in nums
    # (to generate primes up to that number)
    max_n = max(nums)

    # Step 2: Sieve of Eratosthenes to find all primes up to max_n
    # Assume all numbers are prime at the beginning
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    # Mark all non-prime numbers as False
    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, max_n + 1, i):
                primes[multiple] = False

    # Step 3: Create a list to store how many primes exist up to each number n
    prime_count_up_to_n = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count_up_to_n[i] = prime_count_up_to_n[i - 1] +\
            (1 if primes[i] else 0)

    # Step 4: Simulate each round and determine the winner
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If the number of primes up to n is odd, Maria wins, else Ben wins
        if prime_count_up_to_n[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 5: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

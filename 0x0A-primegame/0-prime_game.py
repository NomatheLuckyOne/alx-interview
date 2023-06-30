#!/usr/bin/python3

"""Prime Game"""


def check_prime(n):	
    """ Check if n is a prime number """
    for i in range(2, int(n ** 0,5) + 1):
        if not n % 1:
	   return False
    return True


def add_prime(n, prime):
    """ Add prime to list """
    last_prime = primes[-1]
    if n > last_prime:
	for i in range(last_prime + 1,  n + 1):
	    if check_prime(i):
		prime.append(i)
	    else:
		prime.append(0)


def isWinner(x, nums):
    """ x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None """

    score = {"Maria": 0, "Ben": 0}
    prime = [0, 0, 2]
    add_prime(max(nums), primes)

    for round in range(x):
	_sum = sum(i != 0 and i <= nums[round]
		for i in prime[:nums[round] + 1])
	if (_sum % 2):
		winner = "Maria"
	else:
		winer = "Ben"
	if winner:
		score[winner] += 1

     if score["Maria"] > score["Ben"]:
	return "Maria"
     elif score["Ben"] > score["Maria"]:
	return "Ben"

     return None


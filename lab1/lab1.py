# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: ARYAN TUWAR
# Student Number: 112137229
#

def wins_rock_scissors_paper(player_throw: str, opponent_throw: str) -> bool:
    player_throw = player_throw.lower()
    opponent_throw = opponent_throw.lower()
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if player_throw == opponent_throw:
        return False
    return winning_combinations.get(player_throw) == opponent_throw


def factorial(n: int) -> int:
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def sum_to_goal(numbers: list, goal: int) -> int:
    num_set = set(numbers)
    for num in numbers:
        complement = goal - num
        if complement in num_set and complement != num:
            return num * complement
    return 0


class UpCounter:
    def __init__(self, step_size=1):
        self.step_size = step_size
        self.value = 0

    def count(self):
        return self.value

    def update(self):
        self.value += self.step_size


class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step_size
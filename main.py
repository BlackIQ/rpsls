from random import choice

actions = ["rock", "paper", "scissors", "lizard", "spock"]

user_input = str(input("What is your act (rock, paper, scissors, lizard, spock): "))

if (user_input in actions):
    user_action = user_input

computer_action = choice(actions)

computer_points = 0
user_points = 0

def check_actions(computer_act, user_act):
    return True
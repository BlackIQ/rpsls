from random import choice

computer_points, user_points = 0, 0

actions = ["rock", "paper", "scissors", "lizard", "spock"]

computer_action = choice(actions)
user_input = str(input("What is your act (rock, paper, scissors, lizard, spock): "))

if (user_input in actions):
    user_action = user_input

def check_actions(computer_act, user_act):
    return True
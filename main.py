from random import choice

actions = ["rock", "paper", "scissors", "lizard", "spock"]

computer_action = choice(actions)
user_input = str(input("What is your act (rock, paper, scissors, lizard, spock): "))

if (user_input in actions):
    user_action = user_input

def check_actions(computer_act, user_act):
    computer_points, user_points = 0, 0

    if user_act == actions[0]:
        if computer_act == actions[0]:
            print("Both same.")
        elif computer_act == actions[1]:
            print("Paper Covers Rock.")
            computer_points = computer_points + 1
        elif computer_act == actions[2]:
            print("Rock crushes Scissors.")
            user_points = user_points + 1
        elif computer_act == actions[3]:
            print("Rock crushes Lizard.")
            user_points = user_points + 1
        elif computer_act == actions[4]:
            print("Spock smashes Scissors.")
            computer_points = computer_points + 1
import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "please type either <enter> or amd integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()


# Main routine goes here

# set up valid options for user choice (including instruction and error message)
rps_list = ["rock", "paper", "scissors", "xxx"]
choose_instruction = "please choose rock (r), paper (p) or scissors (s)"
choose_error = "Please choose from rock rock / paper / scissors (or xxx to quit)"

# intialise rounds played, lost and drawn.
# Rounds won can then be calculated later
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f'Continuous Mode: round {rounds_played + 1}'

    else:
        heading = f' Round {rounds_played + 1} of {rounds}'

    print(heading)

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end="\t")

    # compare options
    if user_choice == comp_choice:
        result = "tie"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "win"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "win"
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "win"
    else:
        result = "lose"

    print("You chose {}, the computer chose {}"
          "\nResult: {}".format(user_choice, comp_choice, result))

    # end game if exit code is typed
    if user_choice == "xxx":
        break

    # rest of loop / game
    print(f'You chose {user_choice}')

    rounds_played += 1
print("Thank you for playing")

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# Ask user for # of rounds then loop...

# Ask user if they want to see their game history
# If yes show game history


# Show game statistics

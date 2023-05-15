import random


# Functions go here

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("Choose either a number of rounds or press <enter> for infinite mode")
    print()
    print("Then for each round, choose from rock / paper / scissors",
          "\n(or xxx to quit) You can type r / p / s if you dont want to",
          "\ntype the entire word.")

    print()
    print("The rules are...",
          "\n-Rock beats scissors",
          "\n-scissors beats paper",
          "\n-Paper beats rock.")
    print()
    print("*** Have fun ***")
    print()
    return ""


def check_rounds():
    while True:
        response = input("How many rounds, push <enter> for infinite: ")

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

game_summary = []

# initialise rounds played, lost and drawn.
# Rounds won can then be calculated later
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

mode = "regular"

played_before = yes_no("have you played this game before? ")

if played_before == "no":
    instructions()

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()
if rounds == "":
    rounds = 5
    mode = "infinite"

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if mode == "infinite":
        heading = f'Continuous Mode: round {rounds_played + 1}'
        rounds += 1

    else:
        heading = f' Round {rounds_played + 1} of {rounds}'

    print(heading)

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # end game if exit code is typed
    if user_choice == "xxx":
        break

    rounds_played += 1

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end="\t")

    # compare options
    if user_choice == comp_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "paper" and comp_choice == "rock":
        result = "win"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "win"
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "win"
    else:
        result = "lose"
        rounds_lost += 1

    feedback = "You chose {}, the computer chose {} " \
               "Result: {}".format(user_choice, comp_choice, result)

    outcome = f"Round {rounds_played}: {feedback}"
    game_summary.append(outcome)

    print(feedback)

    # rest of loop / game
    print(f'You chose {user_choice}')

    if rounds_played >= rounds:
        break

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
# quick calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

print()
print("***** Game History *****")
for game in game_summary:
    print(game)

# end game statements
print()
print("****** End Game Summary ******")
print("Won: {} \t|\t Lost: {} \t|\t Draw: "
      "{}".format(rounds_won, rounds_lost, rounds_drawn))

print()
print("Thanks for playing")

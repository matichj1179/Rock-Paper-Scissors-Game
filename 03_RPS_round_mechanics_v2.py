# Function used to check input is valid


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "please type either <enter> or amd integer that is more than 0"

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


# Main routine goes here...

rounds_played = 0
choose_instruction = "please choose rock (r), paper (p) or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f' continuous mode: Round{rounds_played}'
        print(heading)
        choose = input(f'{choose_instruction} or "xxx" to end: ')
        if choose == "xxx":
            break
        else:
            heading = f'Round {rounds_played + 1} of {rounds}'
            print(heading)
            choose = input(choose_instruction)
            if rounds_played == rounds - 1:
                end_game = "yes"

        # rest of loop / game
        print(f'You chose {choose}')

        rounds_played += 1
print("Thank you for playing")

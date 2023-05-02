# RPS Component 3 - Compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for thing in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

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

    comp_index += 1
    print()

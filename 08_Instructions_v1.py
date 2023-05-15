def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

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


# Main Routine goes here
played_before = yes_no("have you played this game before? ")

if played_before == "no":
    instructions()

print("program continues")

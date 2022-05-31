import random

computer_options = ["R", "P", "S"]
computer_choice = random.choice(computer_options)
choices_map = {
    "S": "Scissors",
    "P": "Paper",
    "R": "Rock"
}

while True:
    user_choice = input("""
Welcome to this fun Rock,Paper, Scissors game
Options: "R" for Rock, "P" for Paper
and "S" for Scissors \n
Enter a choice: """).upper()
    if user_choice == computer_choice:
        result = "Tie"
        print(f"{result}, \nPlayer({choices_map[user_choice]}) : CPU({choices_map[computer_choice]})")
    elif (user_choice == "P" and computer_choice == "R") or (user_choice == "S" and computer_choice == "P") or (
            "R" == user_choice and computer_choice == "S"):
        result = "You won!!!"
        print(f"{result}, \nPlayer({choices_map[user_choice]}) : CPU({choices_map[computer_choice]})")
        break
    else:
        result = "Oh no this mindless computer won, try again"
        print(f"{result}, \nCPU({choices_map[computer_choice]}) : Player({choices_map[user_choice]})")

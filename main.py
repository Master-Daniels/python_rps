import random

choices = ["R", "P", "S"]
computer_choice = random.choice(choices)
choices_map = {
    "S": "Scissors",
    "P": "Paper",
    "R": "Rock"
}
print("""
Welcome to this fun little Rock, Paper and Scissors
game, instructions on how to play are in the README file.
options are : 'R' for Rock, 'S' for Scissors and 'P' for Paper.
""")
while True:
    user_choice = input("Enter choice: ").upper()
    if user_choice not in choices:
        print("You have made a wrong choice, try again")
    elif user_choice == computer_choice:
        result = "Tied"
        print(f"{result}, \nPlayer({choices_map[user_choice]}) : CPU({choices_map[computer_choice]})")
    elif (user_choice == "P" and computer_choice == "R") or (user_choice == "S" and computer_choice == "P") or (
            "R" == user_choice and computer_choice == "S"):
        result = "You won!!!"
        print(f"{result}, \nPlayer({choices_map[user_choice]}) : CPU({choices_map[computer_choice]})")
        break
    else:
        result = "Oh no this mindless computer won, try again"
        print(f"{result}, \nCPU({choices_map[computer_choice]}) : Player({choices_map[user_choice]})")

from pyfiglet import figlet_format as figlet
from termcolor import cprint, colored
import random

cprint(figlet("Rock Paper Scissors"), "blue")
cprint("Pushkar Ps", "cyan")

com_points = 0
usr_points = 0

def menu():
    cprint("\n[1] Rock\n[2] Paper\n[3] Scissors\n[4] Menu\n[5] Exit", "yellow")

game_item = ['Rock', 'Paper', 'Scissors']

menu()

def print_score(user, com):
    cprint(f"🧠 AI: {game_item[com]}  👤 You: {game_item[user]}", "magenta")
    cprint(f"🏁 Score → You: {usr_points} | AI: {com_points}\n", "cyan")

while True:
    try:
        usr_choice = int(input(colored("Enter Your Choice: ", "magenta")))

        if usr_choice == 4:
            menu()
            continue
        elif usr_choice == 5:
            cprint(f"Your Final Score: {usr_points}", "green")
            cprint("👋 Thanks for playing!", "cyan")
            cprint("Creator: Pushkar Ps","red")
            break
        elif usr_choice not in [1, 2, 3]:
            cprint("❌ Invalid option. Please choose between 1-5.", "red")
            continue

        usr_index = usr_choice - 1
        com_choice = random.randint(0, 2)

        if usr_index == com_choice:
            cprint("🤝 It's a Draw!", "yellow")
        elif (usr_index == 0 and com_choice == 2) or \
             (usr_index == 1 and com_choice == 0) or \
             (usr_index == 2 and com_choice == 1):
            usr_points += 10
            cprint("🎉 You Won this round!", "green")
        else:
            com_points += 10
            cprint("💀 You Lost this round!", "red")

        print_score(usr_index, com_choice)

    except ValueError:
        cprint("❌ Please enter a valid number.", "red")

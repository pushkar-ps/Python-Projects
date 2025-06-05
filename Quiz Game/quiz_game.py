#!/usr/bin/env python3
from pyfiglet import figlet_format
from termcolor import cprint, colored
import json
import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "questions.txt")


cprint(figlet_format("Welcome To The Quiz Game"), "cyan")

try:
    with open(file_path, "r") as f:
        Questions = json.load(f)
except FileNotFoundError:
    cprint("❌ Questions file not found!", "red")
    exit()


random.shuffle(Questions)

points = 0
for qn in Questions:
    print(colored("Q. " + qn["question"], "magenta"))
    print()
    print("1.", qn["options"][0], "\t2.", qn["options"][1])
    print("3.", qn["options"][2], "\t4.", qn["options"][3])
    print()

    ans = input(colored("Enter Your Answer (1-4 or text, q to quit): ", "yellow")).strip()

    correct = False

    if ans.isdigit():
        if int(ans) - 1 == qn["ans"][0]:
            correct = True

    if(ans == qn["ans"][1] or ans == qn["ans"][1].lower()):
        correct = True

    if(ans == "q"):
        break

    if correct:
        cprint("✔ Correct!", "green")
        points += 1
    else:
        cprint(f"✖ Wrong! Correct answer is: {qn['options'][qn['ans'][0]]}", "red")

    print()

cprint(f"🏁 Game Over! Your Final Score: {points}/{len(Questions)}", "cyan")

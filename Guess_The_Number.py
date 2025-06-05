from pyfiglet import figlet_format as figlet
from termcolor import cprint, colored
import random

cprint(figlet("Guess The Number"),"blue")
cprint("Guess The Number Between 1 - 100","magenta")
cprint("Enter 'q' or 'exit' at any time to quit.\n","red",)

randomInt = random.randint(1, 100)

while True:
    usrInput = input(colored("Enter Your Number: ","yellow"))

    if(usrInput.lower() in ["q","exit"]):
        cprint(f"The Number Is {randomInt}",'cyan')
        break

    try:
        usrInput = int(usrInput)
        if(randomInt == usrInput):
            cprint(f"Congratulations You Guess The Right Number {randomInt}","green")
            break
        if(usrInput > randomInt):
            cprint(f"It's Higher Than The Number","red")
        else:
            cprint(f"It's Smaller Than The Number","red")
    except ValueError:
        cprint("❌ Please enter a valid number.","red")
        continue
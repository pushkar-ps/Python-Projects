from pyfiglet import figlet_format as figlet
from termcolor import cprint, colored

cprint(figlet("Calculator"),"red")

cprint("Enter 'q' or 'exit' at any time to quit.\n","red")



while True:
    num1 = input(colored(" Enter your 1st Number: ","blue"))
    if num1.lower() in ["q", "exit"]:
        break
    try:
        num1 = float(num1)
    except ValueError:
        cprint("❌ Please enter a valid number.", "red")
        continue

    optor = input(colored(" Enter  operator (+, -, *, /): ","yellow"))
    if optor.lower() in ["q", "exit"]:
        break

    num2 = input(colored(" Enter your 2nd Number: ","blue"))
    print()
    if num2.lower() in ["q","exit"]:
        break
    
    try:
        num2 = float(num2)
        if optor == '+':
            result = num1 + num2
        elif optor == '-':
            result = num1 - num2
        elif optor == '*':
            result = num1 * num2
        elif optor == '/':
            if num2 == 0:
                cprint("❌ Cannot divide by zero.","red")
                continue
            result = num1 / num2
        else:
            cprint("❌ Invalid operator.","red")
            continue

        cprint(f" Answer {num1} {optor} {num2} = {result}", "green")
        print()

    except ValueError:
        cprint("❌ Please enter a valid number.","red")
        continue
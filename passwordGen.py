from termcolor import cprint, colored
import random
import string

# Character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits    = string.digits
symbols   = string.punctuation

# Function to get a valid y/n input
def get_yes_no(prompt):
    while True:
        val = input(colored(prompt, "black")).strip().lower()
        if val in ['y', 'n']:
            return val
        else:
            cprint("❌ Invalid choice. Please select y (yes)/ n (no).", "red")

# Function to get a valid integer input
def get_valid_int(prompt):
    while True:
        try:
            val = int(input(colored(prompt, "cyan")))
            return val
        except ValueError:
            cprint("❌ Invalid input. Please enter a number.", "red")

# Header
def print_header():
    cprint("======================================", "blue")
    cprint("\tPASSWORD GENERATOR", "light_blue")
    cprint("======================================", "blue")
    print()
    cprint("1. Generate a new password", "yellow")
    cprint("2. How password is created (info)", "yellow")
    cprint("3. Exit", "yellow")
    cprint("--------------------------------------")

print_header()

# Start Program
while True:
    usrChoice = get_valid_int("Enter your choice (1-3): ")

    if usrChoice == 3:
        cprint("Goodbye! Stay safe online. 🔐", "green")
        break

    elif usrChoice == 1:
        passLen = get_valid_int("Enter desired password length (e.g., 12): ")

        if passLen < 4:
            cprint("❌ Password length too short. Try at least 4 characters.", "red")
            continue

        character_pool = ""

        # Collecting character type choices
        lowerCase = get_yes_no("Include lowercase letters? (y/n): ")
        upperCase = get_yes_no("Include uppercase letters? (y/n): ")
        isNumber  = get_yes_no("Include numbers? (y/n): ")
        isSymbols = get_yes_no("Include symbols (like @#$%)? (y/n): ")

        # Building character pool
        if lowerCase == "y":
            character_pool += lowercase
        if upperCase == "y":
            character_pool += uppercase
        if isNumber == "y":
            character_pool += digits
        if isSymbols == "y":
            character_pool += symbols

        # Check if user selected no character types
        if not character_pool:
            cprint("❌ No character types selected. Cannot generate password.", "red")
            continue

        # Generate password
        password = ''.join(random.choice(character_pool) for _ in range(passLen))
        print()
        cprint(f"🔐 Generated Password: {password}", "green")
        print()

    elif usrChoice == 2:
        cprint("""
Your password is created using a random mix of:
- Lowercase letters: a–z
- Uppercase letters: A–Z
- Numbers: 0–9
- Symbols: @#$%^&*...

We only include what YOU choose.
The more character types and the longer the password — the stronger it is!
        """, "light_magenta")
    else:
        cprint("❌ Invalid choice. Please select from 1, 2, or 3.", "red")

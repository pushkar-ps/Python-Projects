from pyfiglet import figlet_format as figlet
from termcolor import cprint, colored

cprint(figlet("ATM"), "blue")
cprint("🏦 Welcome to ATM Simulator", "cyan")
print("----------------------------------")

balance = 0

def menu():
    cprint("\n[1] Check Balance\n[2] Deposit Money\n[3] Withdraw Money\n[4] Exit", "yellow")

while True:
    menu()
    try:
        option = int(input(colored("Enter Your Choice: ", "magenta")))

        if option == 1:
            cprint(f"💰 Current Balance: ₹{balance}", "green")

        elif option == 2:
            deposited_money = int(input("Enter Amount to Deposit: ₹"))
            if deposited_money < 0:
                cprint("❌ Cannot deposit negative money.", "red")
                continue
            balance += deposited_money
            cprint(f"✅ ₹{deposited_money} Deposited. New Balance: ₹{balance}", "green")

        elif option == 3:
            withdraw_money = int(input("Enter Amount to Withdraw: ₹"))
            if withdraw_money > balance:
                cprint("❌ Insufficient Balance.", "red")
            elif withdraw_money < 0:
                cprint("❌ Cannot withdraw negative money.", "red")
            else:
                balance -= withdraw_money
                cprint(f"✅ ₹{withdraw_money} Withdrawn. Current Balance: ₹{balance}", "green")

        elif option == 4:
            cprint("👋 Thank you for using ATM Simulator. Goodbye!", "cyan")
            break

        else:
            cprint("❌ Invalid Option. Please choose between 1-4.", "red")

    except ValueError:
        cprint("❌ Please enter a valid number.", "red")

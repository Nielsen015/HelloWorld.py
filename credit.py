balance = 250
command = ""
menu = 20
while True:
    command = input(">").lower()
    if command == '*144#':
        print(f'Your balance is Ksh {balance}')
        break
    elif command == '*544#':
        print("""
1. sh250 (3GB for 24hrs)
2. sh300 (2.7GB for 48 hrs)
3. Data Deals
4. Data(No Expiry)
5. Calls and SMS(No Expiry)
6. Data(Expiry)
7. Post Pay & All in One
8. Lipa Mdogo
9. Quit
        """)
        if command == "1":
            print("You have successful Bought 3GB for 24hrs")
        elif command == "2":
            print("You have insufficient funds to purchase this offer, please recharge and try again!")
        elif command == "3":
            print("coming soon!")
        elif command == "4":
            print("coming soon!")
        elif command == "5":
            print("coming soon!")
        elif command == "6":
            print("coming soon!")
        elif command == "7":
            print("coming soon!")
        elif command == "8":
            print("coming soon!")
        elif command == "9":
            break
    elif command == "help":
        print("""
*144# - to check Balance
*544# - main menu
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("Invalid command, please type 'help' for assistance")

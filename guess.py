pin = 5050
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input("Enter your Pin: "))
    guess_count += 1
    if guess == pin:
        print("correct pin!")
        break
    else:
        print("Incorrect pin")

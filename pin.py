name = input('Enter your Name: ')
pin = 6878
limit = 3
count = 0
while count < limit:
    number = int(input('Enter your pin: '))
    count += 1
    if number == pin:
        print(f'welcome {name}')
        break
    else:
        print('Wrong Pin!!! Try again!')

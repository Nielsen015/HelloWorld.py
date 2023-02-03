weight = input('Enter your Weight: ')
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    value = float(weight) * 0.45
    print(f'Your are {value} Kgs')
else:
    value = float(weight)/0.45
    print(f'You are {value} pounds')





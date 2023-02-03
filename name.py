name = input("Enter Your name: ")
if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 10:
    print('Name must be a maximum of 10 characters')
else:
    print('Name is Okay')

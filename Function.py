def digit(number_one, number_two):
    output = number_one + 2
    output += number_two - 1
    return output


number = int(input('Enter your first number: '))
second = int(input('Enter your second number: '))
source = digit(number, second)
print(f'outcome is: {source}')

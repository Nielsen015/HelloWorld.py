numbers = [5, 2, 7, 15, 8]
numbers[0] = 20
max = numbers[0]
for large in numbers:
    if large > max:
        max = large
print(max)
print(numbers)

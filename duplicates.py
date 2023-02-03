numbers = (5, 2, 3, 2, 5, 7, 4, 7)
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

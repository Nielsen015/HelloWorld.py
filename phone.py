phone = input("Phone:")
digit_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)


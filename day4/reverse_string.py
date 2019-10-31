user_input = input("Enter string to be reversed: ")
index = len(user_input) - 1

while index >= 0:
    print(user_input[index], end = '')
    index -= 1
print()
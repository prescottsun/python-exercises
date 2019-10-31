user_input = input('String to translate to leetspeak: ').upper()

index = 0

while index < len(user_input):
    if user_input[index] == 'A':
        print('4', end='')
    elif user_input[index] == 'E':
        print('3', end='')
    elif user_input[index] == 'G':
        print('6', end='')
    elif user_input[index] == 'I':
        print('1', end='')
    elif user_input[index] == 'O':
        print('0', end='')
    elif user_input[index] == 'S':
        print('5', end='')
    elif user_input[index] == 'T':
        print('7', end='')
    else:
        print(user_input[index], end='')
    index += 1
print()
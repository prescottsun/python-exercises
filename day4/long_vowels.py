user_input = input('Input word for long-long vowel: ')

index = 0
long_vowel = ''
while index < len(user_input):
    
    if user_input[index] in ('a', 'e', 'i', 'o', 'u') and user_input[index] == user_input[index-1]:
        long_vowel += (user_input[index] * 4)
    else:
        long_vowel += (user_input[index])
    index += 1

print(long_vowel)

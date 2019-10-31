text = input("Please enter a phrase: ")
letters_to_convert = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
numbers = [4, 3, 6, 1, 0, 5, 7]
translation = ""
uppercased_text = text.upper()

index = 0
while index < len(uppercased_text):
    # print(uppercased_text[index])
    
    index_inner_loop = 0
    letter_to_add_to_translation = ""
    while index_inner_loop < len(letters_to_convert):
        # print(letters_to_convert[index_inner_loop])
        if uppercased_text[index] == letters_to_convert[index_inner_loop]:
            # print('We have a match!')
            # print(numbers[index_inner_loop])
            letter_to_add_to_translation = str(numbers[index_inner_loop])
            break
        else:
            # print('No matches!')
            letter_to_add_to_translation = uppercased_text[index]
        index_inner_loop += 1
    index += 1
    translation = translation + letter_to_add_to_translation

print(translation)
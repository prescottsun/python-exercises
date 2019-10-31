text = input('Enter letter summary text: ')
histogram = {}
for letter in text:
    histogram[letter] = text.count(letter)

print(histogram)
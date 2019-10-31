text = input('Enter word summary text: ')
split_text = text.split(' ')
histogram = {}
for word in split_text:
    histogram[word] = split_text.count(word)

print(histogram)
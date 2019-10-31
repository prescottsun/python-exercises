text = input('Please enter a sentence: ')

split_text = text.split(' ')
histogram = {}
for word in split_text:
    histogram[word] = text.count(word)

sorted_histogram = sorted(histogram.items(), key= lambda x: x[1], reverse=True)
print('The top three words are:')
try:
    index = 0
    while index < 3:
        print(sorted_histogram[index])
        index += 1
except IndexError:
    print('Not enough words')
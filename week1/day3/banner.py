text = input("Text? ")
width = len(text) + 4
i = 1

while i <= 3:
    if i == 2:
        print("*", text, "*")
    else:
        print("*" * width)
    i += 1

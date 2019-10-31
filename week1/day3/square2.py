side = int(input("How big is the square? "))
i = 0
while i < side:
    j = 0
    while j < side:
        print("*", end = "")
        j += 1
    i += 1
    print("")

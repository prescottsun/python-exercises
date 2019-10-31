coins = 0
a = "yes"
while a == "yes":
    print("You have " + str(coins) + " coins.")
    a = input("Do you want another? ")
    coins += 1

print("Bye")

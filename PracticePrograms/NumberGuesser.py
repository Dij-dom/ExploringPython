import random,math
def f1(name,lRange,uRange):
    num =  random.randint(lRange, uRange)
    guessMaX = round(math.log(uRange-lRange + 1, 2))
    print(name, ", you will be having", guessMaX, "guesses. Use your chance wisely")
    TheGame(num, guessMaX)

def TheGame(num, guessMaX):
    guesses = 0
    while (guesses <= guessMaX):
        guess = int(input("Enter your guess number \n"))
        guesses += 1
        if guess == num:
            print("Hurray you gueesed it right in",guesses, "guesses.")
            break
        elif guess > num:
            print("The value is high. Try again :)")
        elif guess < num:
            print("The value is less. Try again.")
        else:
            print("Better luck next time. The number was ", num)

name = input("Enter the name of the player ")
lRange = int(input("Enter the lower range: "))
uRange = int(input("Enter the upper range: "))
f1(name,lRange,uRange)



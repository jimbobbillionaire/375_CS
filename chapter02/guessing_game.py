import random
def main():
    magic_number=random.randrange (1,100)
    guess = 0
    attempts = 1
    while guess != magic_number:
        guess = eval(input("What's the magic number between 1 and 100?"))
        if guess > magic_number:
            print("You're too high")
            attempts = attempts + 1
        elif guess < magic_number:
            print("You're too low")
            attempts = attempts + 1
        elif guess > 100:
            print("The number is between 1 and 100")
            attempts = attempts + 1
        elif guess < 1:
            print("The number is between 1 and 100")
            attempts = attempts + 1
    if attempts > 1:
        print("That's the magic number, it took you", attempts,"Attempts")
    else:
        print("That's the magic number, it took you", attempts,"Attempt")
main()

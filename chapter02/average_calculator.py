#This Program Calculates Averages using the numbers the user inputs
import time
def main():
    print("This program will find an average of the numbers you input")
    time.sleep(2)
    score = input("What's the first number?")
    total = 0
    numbers = 0
    while score != "":
        total= total + eval(score)
        numbers= numbers + 1
        print(total)
        score = input("What's the next number?(Hit Enter with a blank space to stop)")
    print("Total:", total)
    average=total/numbers
    time.sleep(1)
    print("Average:", average)
main()

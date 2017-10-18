# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("enter a number if u real: "))
    qloop = eval(input("How many times are we looping g?: "))
    for i in range(qloop):
        x = 3.9 * x * (1 - x)
        print(x)
        print("we still going")
    print("gang gang we done")

main()

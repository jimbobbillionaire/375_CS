#this program will convert m/s to mph using a speed equation
def main():
    print("This equation will use an equation to convert meters per second to miles per hour")
    ms = eval(input("Enter the Meters per second"))
    if ms < 0:
        print("Invalid Input")
    else:
        print(((3600 * 100) / (5280 * 12 * 2.54)) * ms)
        print("mph")
main()

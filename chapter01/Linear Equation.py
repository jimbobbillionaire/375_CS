# This program calculates the Y-Intercept of a Linear Equation in Slope Intercept Form
import math
def main():
    print("This will solve a linear equation's Y Intercept")
    x = eval(input("Enter the X Value"))
    y = eval(input("Enter the Y Value"))
    m = eval(input("Enter the Slope"))
    print("Y Intercept:")
    print(m * x - y)

main()

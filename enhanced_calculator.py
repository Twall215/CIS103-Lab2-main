# --------------------------------------------------------
# Lab 2: Getting Started with Python
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Trey Wallace
# Date: 9/14/24
# Description:
# This script is an enhanced version of the original calculator.py
# --------------------------------------------------------

import math #need to import math from the get go
def add (num1,num2): 
    return num1 + num2
def subtract(num1,num2): 
    return num1 - num2
def multiply(num1,num2): 
    return num1 * num2
def divide (num1,num2):
    if num2 !=0:
        return num1/num2 
    else:
        return "Error ! Division by zero!"#need this to account for zero conundrum
def exponent(num1,num2):
    return num1 ** num2
def modulus(num1,num2):
    return num1 % num2
def sqaurert(num1):
    return math.sqrt(num1)

def super_calculator():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divison")
        print("5. Exponent")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Enter Choice ")
#These if statements call the functions
#Each choice needed to have the inputs within to account for each task
        if choice == '8':
            print("exiting, thank you!")
            break
        elif choice == "7":
            print("Only choose one number this time")
            num1 = float(input("Enter your first number: "))
            print(f"The square root of {num1} is {sqaurert(num1)}")
        elif choice == '1':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} to the {num2} power is {exponent(num1,num2)}")
        elif choice == '6':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} % {num2} leaves {modulus(num1,num2)} left")
        else:
            print("Invalid Input Please try again")#this should account for non options
        

if __name__ == "__main__":
    super_calculator()
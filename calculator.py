# --------------------------------------------------------
# Lab 2: Getting Started with Python
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Trey Wallace
# Date: 8/31/24
# Description:
# This script is a calulator
# --------------------------------------------------------


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
        return "Error ! Division by zero!"

def calulator():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divison")
        print("5. Exit")

        choice = input("Enter Choice ")

        if choice == '5':
            print("exiting, thank you!")
            break
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print("{num1}+{num2} = {add(num1,num2)}")


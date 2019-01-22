#import libary
from math import *

#simple print
print("Hello World!")
print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

#variable
name = "John"
age = 25
print("There once was a man name " + name + ", ")
print("he was " + str(age) + " years old.")
print("he really liked the name " + name + ", ")
print("but didn't like being " + str(age) + ".")

#new line, quote
print("first line \n second line")
print("quote\"")

#basic string function
print(name.lower())
print(name.upper())
print(name.isupper()) #return true or false if it uppercase or not
print(name.upper().isupper()) #more than one function
print(len(name)) #string lenght
print(name[0]) #return character by using index number
print(name.index("J")) #return character index number
print(name.replace("John", "Mike")) #replace word or letter (default, change)

#basic int
num1 = -5
print(abs(num1)) #return absulate number
print(pow(3, 2)) #power function
print(max(4, 6)) #return highest number between two
print(round(3.4)) #return rounded number
print(sqrt(9)) #return square root parameter number

#input
userName = input("Enter your name: ")
userAge = input("Enter your age: ")
print("Hello " + userName + "!!, your age is " + userAge)
num1 = input("Enter first number:")
num2 = input("Enter second number:")
result = float(num1) + float(num2) #convert string to int
print("Total = " + str(result))
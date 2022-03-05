import pyfiglet
import colorama
from colorama import Fore, Back, Style
from pyfiglet import figlet_format
Banner = figlet_format("             CLI Calculator")
print(Fore.RED+50*"_")
print(Fore.RED+50*"_")
print(Fore.GREEN+Banner)
print(Fore.RED+50*"_")
print(Fore.RED+50*"_")
print(3*"\n")

def add(x, y):
    return x+y
def Subtract(x, y):
    return x-y
def multiplication(x, y):
    return x*y
def division (x, y):
    return x/y
print(Fore.CYAN+8*"_")
print("\n")
print(Fore.RED+"1./    |")
print(Fore.GREEN+"2.*    |")
print(Fore.BLUE+"3.+    |")
print(Fore.YELLOW+"4.-    |")
print(            "       |")
print(Fore.CYAN+8*"_")
while True:
    num1 = float(input(Fore.BLUE+"{1}Enter First Number:- ")) 
    choice = input(Fore.RED+"{2}Enter Operation:- ")
    num2 = float(input(Fore.YELLOW+"{3}Enter Second Number:- "))
    if choice =='+':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice =='-':
        print(num1, "-", num2, "=", Subtract(num1, num2))
    elif choice =='*':
        print(num1, "*", num2,"=", multiplication(num1, num2))
    elif choice =='/':
        print(num1, "/", num2, "=", division(num1, num2))
    else:
        print(Fore.LIGHTGREEN_EX+"invalid syntax!!!!!",Fore.RED+"  [Please Enter Valid Syntax:]")
    calculation = input(Fore.LIGHTCYAN_EX+"Let's do next calculation? (yes/no): ")
    if calculation == "yes"or calculation=="y":
        print(Fore.LIGHTCYAN_EX+"      WELCOME BACK")
    elif calculation == "no"or calculation=="n":
        quit()
    
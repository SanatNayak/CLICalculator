import pyfiglet
import colorama
from colorama import Fore, Back, Style
from pyfiglet import figlet_format
Banner = figlet_format("                     CLI Calculator")
print(Fore.RED+80*"_")
print(Fore.RED+80*"_")
print(Fore.GREEN+Banner)
print(Fore.RED+80*"_")
print(Fore.RED+80*"_")
print("                                                                          \033[92mV.2")
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
    
    num1 = input(Fore.BLUE+"{1}Enter First Number:- ")
    choice = input(Fore.RED+"{2}Enter Operation:- ")
    num2 = input(Fore.YELLOW+"{3}Enter Second Number:- ")
    try:
        if choice =='+':
            print(num1, "+", num2, "=", add(float(num1), float(num2)))
        elif choice =='-':
            print(num1, "-", num2, "=", Subtract(float(num1), float(num2)))
        elif choice =='*':
            print(num1, "*", num2,"=", multiplication(float(num1), float(num2)))
        elif choice =='/':
            print(num1, "/", num2, "=", division(float(num1), float(num2)))
        else:
            print("\033[93m\ninvalid Symbol!!!!!",Fore.RED+"              [Please Enter Symbol:]    Example:-/,*,+,--\n")
    except :
        print("\033[93m\nInvalid Number!!!!!"     ,Fore.RED+        " [Please Enter Number]    Example:-1,2,3,4,5,6,7,8,9\n")
        
    calculation = input(Fore.LIGHTCYAN_EX+"Let's do next calculation? (yes/no): ")
    if calculation == "yes"or calculation=="y" or calculation == "Y" or calculation == "YES" or calculation == "Yes":
        print(Fore.LIGHTCYAN_EX+"       WELCOME BACK")
    elif calculation == "no"or calculation=="n" or calculation=="N" or calculation == "NO" or calculation == "No":
        Name = figlet_format(" Create By Sanat")
        print(Fore.GREEN+Name)
        quit()
    else :
        print(Fore.LIGHTWHITE_EX+"You Write Yes/No")    
        exit()
        
    

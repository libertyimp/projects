import sys
import os
import random
import math

def gameInfo():
    os.system('clear')
    print ("What info would you like to see?")
    print ("----------------------")
    print ("| 1.) Commands       |")
    print ("| 2.) Licensing      |")
    print ("| 3.) About          |")
    print ("----------------------")

    selection = input(">> ")

    if selection == 1:
        commands()
    elif selection == 2:
        licensing()
    elif selection == 3:
        about()
    else:
        os.system('clear')
        print ("Please input a valid option.")
        gameInfo()

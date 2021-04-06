import sys
import os
import random
import math

def main():
    os.system('clear')
    print ("Welcome to my game!\n")  #Input art of game title
    print ("----------------------")
    print ("| 1.) Start Game     |")
    print ("| 2.) Info           |")
    print ("| 3.) Exit           |")
    print ("----------------------")
    selection = input(">> ")

    if selection == 1:
       startGame() # MAKE startGame function
    elif selection == 2:
        gameInfo() # MAKE gameInfo function
    elif selection == 3:
        exit()
            
            
    

main()

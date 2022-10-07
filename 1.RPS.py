import random
from secrets import choice 
list = [1,2,3]
num = choice(list) 
option = input("Please enter r p or s")
if num == 1 :
    if option == "p" :
        print("You win")
    if option == "s" :
        print("You lose")
    if option == "r" :
        print("You draw")
if num == 2 :
    if option == "s" :
        print("You win")
    if option == "r" :
        print("You lose")
    if option == "p" :
        print("You draw")
if num == 3 :
    if option == "r" :
        print("You win")
    if option == "p" :
        print("You lose")
    if option == "s" :
        print("You draw")
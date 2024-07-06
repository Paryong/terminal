import sys
import random
import os
import datetime

now=datetime.datetime.now()
day_of_week = now.weekday()
if day_of_week==0:
    day="Monday"
elif day_of_week==1:
    day="Tuesday"
elif day_of_week==2:
    day="Wednesday"
elif day_of_week==3:
    day="Thursday"
elif day_of_week==4:
    day="Friday"
elif day_of_week==5:
    day="Saturday"
else:
    day="Sunday"

money=int("791")
print("$",money,)
print()
print("Welcome to the FORTUNE-9 OS \n          Courtesy of the Company")
print("Happy",day,".")
print()
print("Type 'help' for a list of commands.")



while True:
    type=input("")
    type=type.lower()
    if type=="help":
        os.system("cls")
        print(">MOONS\nTo see the list of moons the autopilot can route to.")
        print()
        print(">STORE\nTo see the company store's selection of useful items.")
        print()
        print(">BESTIARY\nTo see the list of wildlife on record.")
        print()
        print(">STORAGE\nTo access objects placed into storage.")
        print()
        print(">OTHER\nTo see the list of other commands")
        print()
    if type=="moons":
        print("hi")
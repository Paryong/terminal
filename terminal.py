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
        os.system("cls")
        buying_rate=('30','60','90')

        weather_number = int(random.randint(1, 100))
        if weather_number <= int(5):
            weather = "Eclipsed"
        elif weather_number <= int(15):
            weather = "Flooded"
        elif weather_number <= int(22):
            weather = "Foggy"
        elif weather_number <= int(32):
            weather = "Stormy"
        elif weather_number <= int(44):
            weather = "Rainy"
        else:
            weather = "Sunny"
        
        weather_number1 = int(random.randint(1, 100))
        if weather_number1 <= int(5):
            weather1 = "Eclipsed"
        elif weather_number1 <= int(15):
            weather1 = "Flooded"
        elif weather_number1 <= int(27):
            weather1 = "Stormy"
        elif weather_number1 <= int(38):
            weather1 = "Rainy"
        else:
            weather1 = "Sunny"

        weather_number2 = int(random.randint(1, 100))
        if weather_number2 <= int(5):
            weather2 = "Eclipsed"
        elif weather_number2 <= int(15):
            weather2 = "Flooded"
        elif weather_number2 <= int(22):
            weather2 = "Foggy"
        elif weather_number2 <= int(32):
            weather2 = "Stormy"
        else:
            weather2 = "Sunny"

        weather_number3 = int(random.randint(1, 100))
        if weather_number3 <= int(5):
            weather3 = "Eclipsed"
        elif weather_number3 <= int(15):
            weather3 = "Flooded"
        elif weather_number3 <= int(27):
            weather3 = "Stormy"
        elif weather_number3 <= int(38):
            weather3 = "Rainy"
        else:
            weather3 = "Sunny"
            
        weather_number4 = int(random.randint(1, 100))
        if weather_number4 <= int(5):
            weather4 = "Eclipsed"
        elif weather_number4 <= int(15):
            weather4 = "Flooded"
        elif weather_number4 <= int(22):
            weather4 = "Foggy"
        elif weather_number4 <= int(32):
            weather4 = "Stormy"
        else:
            weather4 = "Sunny"

        weather_number5 = int(random.randint(1, 100))
        if weather_number5 <= int(15):
            weather5 = "Eclipsed"
        elif weather_number5 <= int(42):
            weather5 = "Stormy"
        else:
            weather5 = "Sunny"

        weather_number6 = int(random.randint(1, 100))
        if weather_number6 <= int(15):
            weather6 = "Eclipsed"
        elif weather_number6 <= int(41):
            weather6 = "Flooded"
        else:
            weather6 = "Sunny"
        
        weather_number7 = int(random.randint(1, 100))
        if weather_number7 <= int(25):
            weather7 = "Eclipsed"
        elif weather_number7 <= int(42):
            weather7 = "Foggy"
        elif weather_number7 <= int(66):
            weather7 = "Stormy"
        else:
            weather7 = "Sunny"
        
        
        print("$",money,)
        print()
        print("Welcome to the exomoons catalogue.\nTo route the autopilot to a moon, use the word ROUTE.\nTo learn about any moon, use INFO.\n--------------------------------")
        print()
        print("The company building   //   Buying at ",random.choice(buying_rate),"%")
        print()
        print("* Experimentation (",weather,")")
        print("* Assurance (",weather1,")")
        print("* Vow (",weather2,")")
        print()
        print("* Offense (",weather3,")")
        print("* March (",weather4,")")
        print()
        print("Rend (",weather5,")")
        print("* Dine (",weather6,")")
        print("* Titan (",weather7,")")
        print()
    if type=="the company building" or type=="company building" or type=="route the company building":
        print("")
    elif type=="experimentation" or type=="exper" or type=="experi" or type=="route experimentation":
        os.system("cls")
        print("THe cost route 41-Experimentation is &0.\nIt is currently",weather,"weather on this moon.")
        print()
        print("Please CONFIRM or DENY.")
        print()
        moons_answer=input("")
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            print("Routing autopilot to 41-Experimentation.\nYour new balance is $",money,".")
            print()
            print("Please enjoy your flight.")
    elif type=="assurance" or type=="assu" or type=="route assurance":
        os.system("cls")
        print("The cost to route 220-Assurance is $0.\nIt is currently",weather1,"weather on this moon.")
        print()
        print("Please CONFIRM or DENY.")
        print()
        moons_answer=input("")
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            print("Routing autopilot to 220-Assurance.\nYour new balance is $",money,".")
            print()
            print("Please enjoy your flight.")
    elif type=="vow" or type=="route vow":
        os.system("cls")
        print("The cost to route 56-Vow is $0\nIt is currently",weather2,"weather on this moon.")
        print()
        print("Please CONFIRM or DENY.")
        print()
        moons_answer=input("")
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            print("Routing autopilot to 56-Vow.\nYour new balance is $",money,".")
    elif type=="offense" or type=="off" or type=="route offense":
        os.system("cls")
        print("The cost to route 21-Offense is &0.\nIt is currently",weather3,"weather on this moon.")
        print()
        print("Please CONFIRM or DENY")
        print()
        moons_answerinput("")
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            print("Routing autopilot to 21-Offense.\nYour new balance is",money,".")
            print()
            print("Please enjoy your flight.")
    elif type=="march" or type=="mar" or type=="route march":
        os.system("cls")
        print("The cost to route 61-March is $0.\nIt is currently",weather4,"weather on this moon.")
        print()
        moons_answer=input("")
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            print("Routing autopilot to 61-March.\nYour new balance is $",money,".")
            print()
            print("Please enjoy your flight.")
    elif type=="rend" or type=="route rend":
        os.system("cls")
        print("The cost to route 85-Rend is $550.\nIt is currently",weather5,"weather on this moon.")
        print()
        print("Please CONFIRM or DENY.")
        moons_answer=input("")
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            money_moons=int(money-550)
            print("Routing autopilot to 85-Rend.\nYour new balance is $",money_moons,".")
            print()
            print("Please enjoy your flight.")
    elif type=="dine" or type=="route dine":
        os.system("cls")
        print("The cost to route 7-Dine is $600.\nIt is currently",weather6,"weather on this moon.")
        print()
        print("Please CONFIRM or DENY.")
        moons_answer=input("")
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            money_moons=int(money-600)
            print("Routing to 7-Dine.\nYour new balance is $",money_moons,".")
            print()
            print("Please enjoy your flight.")
    elif type=="titan" or type=="route titan":
        os.system("cls")
        
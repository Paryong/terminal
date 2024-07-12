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
        
        rate=random.choice(buying_rate)

        print("$",money,)
        print()
        print("Welcome to the exomoons catalogue.\nTo route the autopilot to a moon, use the word ROUTE.\nTo learn about any moon, use INFO.\n--------------------------------")
        print()
        print("The company building   //   Buying at ",rate,"%")
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
                                                                                           
    if type=="the company building" or type=="company building" or type=="route the company building" or type=="company":
        os.system("cls")
        print("The cost to route 71-Gordion is $0.\nThe company building is buying at",rate,"%.")
        print()
        print("Please CONFIRM or DENY.")
        print()
        moons_answer=input()
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            print("Routing autopilot to 71-Gordion.\nYour new balance is $",money,".")
            print()
            print("Please enjoy your flight.")
    elif type=="experimentation" or type=="exper" or type=="experi" or type=="route experimentation":
        os.system("cls")
        print("The cost route 41-Experimentation is &0.\nIt is currently",weather,"weather on this moon.")
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
        moons_answer=input("")
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
        print("The cost to route 8-Titan is $700.\nIt is currently",weather7,"weather on this moon.")
        print()
        print("Please CONFIRM or DENY.")
        moons_answer=input("")
        moons_answer=moons_answer.lower()
        if moons_answer=="confirm" or moons_answer=="con" or moons_answer=="c":
            os.system("cls")
            money_moons=int(money-700)
            print("Routing autopilot to 8-Titan.\nYour new balance is $",money_moons,".")
            print()
            print("Please enjoy your flight.")
    elif type=="info experimentation" or type=="info experi":
        os.system("cls")
        print("41-Experimentation")
        print()
        print()
        print("Population: Abandoned.")
        print()
        print("Conditions: Dry. Low habitability, exacerbated by industrial artifacts.")
        print()
        print("History: Although undiscovered for a long time due to its close orbit around the gas giant 'Big Green',it appears to have been used in secret.")
        print()
        print("Fauna: Dominated by a few species.")
        print()
    elif type=="info assurance" or type=="info ass":
        os.system("cls")
        print("220-Assurance")
        print()
        print()
        print("Population: Abandoned.")
        print()
        print("Condition: Similar to its twin moon 41-Experience, but featuring a much more reugged and weathered terrain.")
        print()
        print("History: 220-Assurance was discovered long after 41-Experience.")
        print()
        print("Fauna: Territorial behavior is common due to the ecosystem.")
        print()
    elif type=="info vow":
        os.system("cls")
        print("56-Vow")
        print()
        print()
        print("Population: Abandoned.")
        print()
        print("Conditions: Humid.")
        print()
        print("History: Vow appears to have been home to several colonies across the continent, but today there are no signs of life and it has become a mystery.")
        print()
        print("Fauna: Diverse and rich in flora. Because of the competitive ecosystem, there are many aggressive life forms.")
        print()
    elif type=="info offense" or type=="info off":
        os.system("cls")
        print("21-Offense")
        print()
        print()
        print("Population: Abandoned.")
        print()
        print("Conditions: Seen as a spinoff from its cousin. Assurance, Offense has similar jagged, dry conditions but a different ecosystem.")
        print()
        print("Histroy: 21-Offense is classified as an asteroid moon and does not appear to have existed on its own for more believed to have been created long before the 21-Offense split, have been damaged.")
        print()
        print("Fauna: Due to the competitive and intensified ecosystem, aggressive life forms abound. Travelers visiting 21-Offense should be aware that it is not for the faint of heart.")
        print()
    elif type=="info march" or type=="info mar":
        os.system("cls")
        print("61-March")
        print()
        print()
        print("Population: Deserted. ")
        print()
        print("Conditions: Rain falls continuously. The terrain here is more expansive.")
        print()
        print("History: This moons is not noticeable because of its twin moon,Vow.")
        print()
        print("Fauna: Diverse.")
        print()
    elif type=="info rend":
        os.system("cls")
        print("85-Rend")
        print()
        print()
        print("Population: None.")
        print()
        print("Conditions: This planet orbits a white dwarf,creating a harsh and cold environment. Visibility is poor due to persistent blizzards.")
        print()
        print("History: Several famous travelers have gone missing here and gained fame, but the state of the planet means their bodies are unlikely to be found.")
        print()
        print("Fauna: Multicellular life is highly unlikely to exist here.")
        print()
    elif type=="info dine":
        os.system("cls")
        print("7-Dine")
        print()
        print()
        print("Population: None.")
        print()
        print("Conditions: This planet orbits a white dwarf,creating a harsh and cold environment. Visibility is poor due to persistent blizzards.")
        print()
        print("History: Several famous travelers have gone missing here and gained fame, but the state of the planet means their bodies are unlikely to be found")
        print()
        print("Fauna: Multicellular life is highly unlikely to exist here.")
        print()
    elif type=="info titan" or type=="info tit":
        os.system("cls")
        print("8-Titan")
        print()
        print()
        print("Population: None.")
        print()
        print("Conditions: Terrain is frozen and flat.")
        print()
        print("History: This satellite appears to have been mined for its resources. It's easy to get lost in a huge industrial complex. There are many enreances scattered through out.")
        print()
        print("Fauna: Dangerous beings are rumored to inhabit the vast network of tunnels.")
        print()
    elif type=="store":
        print("Welcome to the company store.\nUse words BUY and INFO on any item.\nOrder tools in bulk by typing a number.\n---------------------------")
        print()
        print()
        print("* Walkie-talkie  //  Price: $12\n* Flashlight  //  Price: $15\n* Shovel  //  Price: $30\n* Lockpicker  //  Price:$20\n* Pro-flashlight  //  Price: $25\n* Stun grenade  //  Price: $40\n* Boombox  //  Price: $60\n* TZP-Inhalant  //  Price: $120\n* Zap gun  //  Price: $400\n* Jetpack  //  Price: $700\n* Extension ladder  //  Price: $60\n* Rader-booster  //  Price: $50")
        print()
        print("SHIP UPGRADES: \n* Loud horn  //  Price: $150\n* Signal translator  //  Price: $255\n* Teleporter  //  Price: $375\n* Inverse Teleporter  //  Price: $425")
        print()
        print("The selection of ship decor rotates per-quota. Be sure to check back next week: \n---------------------------")
        print()
        print("Record player  //  $120\nTelevision  //  $130\nHazard suit  //  $90\nTable  //  $70")
        print()

    elif type=="walkie-talkie" or type=="walk" or type=="walkie":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(12*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order walkie-talkies.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"walkie-talkies. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shipping while on the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="flashlight" or type=="flash":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(15*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Flashlights.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Flashlights. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shipping while in the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="shovel" or type=="sho":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(30*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Shovels.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Shovels. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shipping while is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="lockpicker" or type=="lock":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(20*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Lockpickers.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Lockpickers. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shipping while is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")
            

    elif type=="pro-flashlight" or type=="pro":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(25*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Pro-flashlights.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Pro-flashlights. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="stun grenade" or type=="stun":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(40*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Stun grenades.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Stun grenades. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="boombox" or type=="boom":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(60*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Boomboxes.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Boomboxes. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="tzp-inhalant" or type=="tzp":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(120*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order TZP-Inhalant.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"TZP-Inhalant. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="tzp-inhalant" or type=="tzp":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(120*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order TZP-Inhalant.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"TZP-Inhalant. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="zap gun" or type=="zap":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(400*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Zap guns.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Zap guns. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="jetpack" or type=="jet":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(700*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Jetpacks.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Jetpacks. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="jetpack" or type=="jet":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(700*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Jetpacks.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Jetpacks. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="extension ladder" or type=="extension":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(60*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Extension ladders.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Extension ladders. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="rader-booster" or type=="rader":
        os.system("cls")
        print("How many items do you want to buy:")
        item_su=int(input())
        price=int(50*item_su)
        if price<money:
            os.system("cls")
            print("You have requested to order Rader-boosters.\nAmount:",item_su,".")
            print()
            print("Please CONFIRM or DENY.")
            type=input()
            if type=="confirm" or type=="con" or type=="c":
                os.system("cls")
                print("Ordered",item_su,"Rader-boosters. Your new balance is $",money-price,".")
                print()
                print("Our contractors enjoy fast, free shippng whle is the job! Any purchased items will arrive hourly at your approximate location.")
                print()
            elif type=="deny" or type=="d":
                print("Cancelled order.")
                print()
        else:
            print("You don't have enough money to buy this.")

    elif type=="loud horn" or type=="loud":
        os.system("cls")
        print("You have requested to order Loud Horn.")
        print()
        print("Please CONFIRM or DENY.")
        type=input()
        if type=="confirm" or type=="con" or type=="c":
            print("Order complete.\nYour new balance is $",int(money-100),".")

    elif type=="signal translator" or type=="signal":
        os.system("cls")
        print("You have requested to order Signal Translator")
        print()
        print("Please CONFIRM or DENY.")
        type=input()
        if type=="confirm" or type=="con" or type=="c":
            print("Order complete.\nYour new balance is $",int(money-255),".")

    elif type=="teleporter" or type=="tele":
        os.system("cls")
        print("You have requested to order Teleporter.")
        print()
        print("Please CONFIRM or DENY.")
        type=input()
        if type=="confirm" or type=="con" or type=="c":
            print("Order complete.\nYour new balance is $",int(money-375),".")

    elif type=="inverse teleporter" or type=="inverse":
        os.system("cls")
        print("You have requested to order Inverse Teleporter")
        print()
        print("Please CONFIRM or DENY.")
        type=input()
        if type=="confirm" or type=="con" or type=="c":
            print("Order complete.\nYour new balance is $",int(money-425),".")

    elif type=="record player" or type=="record":
        os.system("cls")
        print("You have requested to order Record Player.")
        print()
        print("Please CONFIRM or DENY.")
        type=input()
        if type=="confirm" or type=="con" or type=="c":
            print("Order complete.\nYour new balance is $",int(money-120),".")

    elif type=="television" or type=="tele":
        os.system("cls")
        print("You have requested to order Television.")
        print()
        print("Please CONFIRM or DENY.")
        type=input()
        if type=="confirm" or type=="con" or type=="c":
            print("Order complete.\nYour new balance is $",int(money-130),".")

    elif type=="hazard suit" or type=="hazard":
        os.system("cls")
        print("You have requested to order Hazard suit.")
        print()
        print("Please CONFIRM or DENY.")
        type=input()
        if type=="confirm" or type=="con" or type=="c":
            print("Order complete.\nYour new balance is $",int(money-90),".")
        
    
    elif type=="table":
        os.system("cls")
        print("You have requested to order Table.")
        print()
        print("Please CONFIRM or DENY.")
        type=input()
        if type=="confirm" or type=="con" or type=="c":
            print("Order complete.\nYour new balance is $",int(money-70),".")

    elif type=="info walk" or type=="info walkie" or type=="info walike-talkie":
        print("$",money)
        print()
        print("Useful for keeping in touch! Hear other players when the walkie talkie is in your inventory. Must be in your hand and pressed down to transmit voice.")
        print()

    elif type=="flash" or type=="flashlight":
        print("$",money)
        print()
        print("The most affordable light source. It's even waterproof!")
        print()

    elif type=="info sho" or type=="info shovel":
        print("$",money)
        print()
        print("For self-defense!")
        print()

    elif type=="info lock" or type=="info lockpicker":
        print("$",money)
        print()
        print("Lock-pickers will unlock your limitless potential for efficiency on the job. Powered by proprietary AI software, they will get you access through any locked door.")
        print()

    elif type=="info pro" or type=="info proflashlight":
        print("$",money)
        print()
        print("With an extra battery life and even brighter bulb, your colleagues can never leave you in the dark again!")
        print()

    elif type=="info stun" or type=="info stun grenade":
        print("$",money)
        print()
        print("[This action was not compatible with this object.]")
        print()

    elif type=="info boombox" or type=="info boom":
        print("$",money)
        print()
        print("These jamming tunes are great for a morale boost on your crew!")
        print()

    elif type=="info tzp" or type=="info tzp-inhalant":
        print("$",money)
        print()
        print("This safe and legal medicine can be administered to see great benefits to your performance on the job! Your ability to move LONG distances while carrying HEFTY objects will be second to none! Warning: TZP gas may impact the brain with extended exposure. Follow instructions manual privided with the canister.\nDon't forget to share!")
        print()

    elif type=="info zap" or type=="info zap gun":
        print("$",money)
        print()
        print("The most specialized self-protective equipment, capable of sending upwards of 80,000 volts!\n\nTo keep it targeted as long as possible, pull the gun side-to-side to counter the bend and fight against the pull of the electric beam. It can only stun for as long as you keep the current flowing.")
        print()

    elif type=="info jet" or type=="info jetpack":
        print("$",money)
        print()
        print("This device will get you around anywhere! Just use it responsibly!")
        print()
    
    elif type=="info extension" or type=="info extension ladder":
        print("$",money)
        print()
        print("The extension ladder can reach as high as nine meters! Use it to scale any cliff and reach for the stars! To save batteries the extension ladder automatically stores itself after 18 seconds.")
        print()

    elif type=="info rader" or type=="info rader booster":
        print("$",money)
        print()
        print("Use the 'SWITCH' command before the rader booster's name to view it on the main monitor. It must be activated\n\nUse the 'PING' command before the rader booster's name to play a special sound from the device.")
        print()
        
    elif type=="info spray":
        print("$",money)
        print()
        print("[This action wat now compatible with this object.]")
        print()
    
    elif type=="info weed" or type=="info weed killer":
        print("$",money)
        print()
        print("Deal with those pesky weeds! Repeated, firm presses on the trigger aimed at the root of the weed is all you need!")
        print()

    elif type=="info cruiser":
        print("$",money)
        print()
        print("The Company Cruiser is an entire delivery truck capable of carrying as many items as you could ever need, including your fellow coworkers! Your purchase of a Company Cruiser comes with one free, life-time warranty, because we are that confident in its durability and usefulness!\n\nIt comes with a manual, so make sure to read up on the best practices.")
        print()

    elif type=="info loud" or type=="info loud horn":
        print("$",money)
        print()
        print("Used to communicate with any crew member from any distance,no walki talkie required! The horn can be heard from anywhere. But what does it mean?\nThat's up to you!")
        print()

    elif type=="info signal" or type=="info signal translator":
        print("$",money)
        print()
        print("Use the 'transmit' command to broadcast a text message to all cremates. The message must be under 10 letters.")
        print()
        
    elif type=="info tele" or type=="info teleporter":
        print("$",money)
        print()
        print("Press the button to activate the teleporter. It will teleport whoever is currently being monitored on the ship's radar. They wil not able to keep any of their held items through the teleport. It takes about ten seconds to recharge.")
        print()

    elif type=="info inverse" or type=="info inverse teleporter":
        print("$",money)
        print()
        print("The inverse teleporter is a modified teleporter which will teleport you to a random position outside the ship. All your items will be dropped at the teleporter before transport. The inverse teleporter can be used by everyone at once and has a 3.5 minute cooldown.\n\nDISCLAIMER: The inverse teleporter can only transport you out, not in, and you may become trapped. The company is not responsible for injury or replacement of heads and limbs induced by quantum entanglement and bad luck.")
        print()

    elif type=="storage":
        print("$",money)
        print()
        print("While moving furniture with [B], you can press [X] to send it to storage. You can call it back from storage here.")
        print()
        print("These are the items in storage:\n\n[No items stored. While moving an object with B, Press X to store it.]")
        print()

    elif type=="best" or type=="bestiary":
        print("$",money)
        print()
        print("BESTIARY")
        print()
        print("To access a creature file, type 'INFO' after its name.\n--------------------------")
        print()
        print("No data collected on wildlife. Scans are required.")
        print()

    elif type=="other":
        print("$",money)
        print()
        print("Other commands:")
        print()
        print(">VIEW MONITOR\nTo toggle on AND off the main monitor's map cam")
        print()
        print(">SWITCH [Player name]\nTo switch view to a player on the main monitor")
        print()
        print(">PING [Rader booster name]\nTo make a rader booster play a noise.")
        print()
        print(">TRANSMIT [message]\nTo transmit a message with the signal translator.")
        print()
        print(">SCAN\nTo scan for the number of items left on the current planet.")
    
    elif type=="scan":
        print("$",money)
        print()
        print("There are 0 objects outside the ship, totalling at an approximate value of $0.")

    elif type=="sigurd":
        print("$",money)
        print()
        print("SIGURN'S LOG ENTRIES")
        print()
        print("To read a log, use keyword 'VIEW' before its name.\n---------------------")
        print()
        print()
        print("First Log - Aug 22")
        print()
        print()
        if type=="first log":
            print("Date: August 22, 1968\nHello. i am writing this log to keep myself sane. I couldnt find a way to do the most basic thing on this old janky butt computer so I had Desmond add it in, the log feature. till now ive just been adding my own notes to the bestiary whatever i know. My brother said i should keep a journal so im doing what i can! I am writing in a proffessional manner, as these logs could become a historical record, as they will probably be here for years, just as long as there isnt a clean wipe. that is what desmond saidfd.")
            print()
            print()
            print("If you are reading it in the future, you are probably from a nother crew. The turnover rate here is enormous, maybe cause this job sucks and every one turns over dead! Maybe I can give some help when I have some expirience. End log.\nOh, our names are: Sigurd (me), Richard, Desmond, Jess.")
            print()""
        


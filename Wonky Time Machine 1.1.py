#Wonky Time Machine, version 1.1
#copyright Marissa Skudlarek, 2018

import random
import time

def welcome():
    print("CHRONOMACHINA 2000-X")
    print("A STATE-OF-THE-ART SPATIOTEMPORAL RELOCATOR")
    print()

def get_destination_year():
    while True:
        year = input("What year shall we travel to? ")
        if year == "0":
            print("You can't fool me, there is no year 0!")
            print()
        elif year.lstrip("-").isdigit():
            if int(year) < -1000:
                print("Prehistory is too dangerous for modern humans. Please try again.")
                print()
            elif int(year) > 2486:
                print("Didn't your professors warn you about the Cataclysm of 2487? We're not going past then!")
                print()
            else:
                print()
                return year
        elif "BC" in year or "B.C." in year or "bc" in year or "b.c." in year:
            print("Please express B.C. years as negative numbers.")
            print()
        else:
            print("Not recognized. Please express year in digits according to the Gregorian calendar.")
            print()

def get_destination_place():
    outer_space = ["Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", 
    "Uranus", "Neptune", "Pluto", "Titan"]
    while True:
        place = input("And where are we going? ")
        if place.title() in outer_space:
            print("I'm a time machine, not a spaceship!")
            print()
        elif place.isdigit():
            print("Don't give coordinates, give a place name.")
            print()
        else:
            print()
            return place

def travel_process(year, place):
    print("Initializing systems to travel to {} in {}.".format(place, year))
    print()
    timer = 4
    while timer > 0:
        print("~ * ~ * ~ * ~")
        time.sleep(1)
        timer = timer - 1
        print("* ~ * ~ * ~ *")
        time.sleep(1)
        timer = timer - 1

def get_random_place():
    random_places = ["Egypt", "Paris", "Tokyo", "Mexico", "China", "London", 
    "Greece", "Moscow", "Manhattan", "Hawaii", "Australia"]
    random_place = random.choice(random_places)
    return random_place

def get_random_year():
    random_year = random.randint(-1000, 2486)
    if random_year == 0:
        random_year = random_year + random.randint(1, 2000)
        return random_year
    else:
        return random_year

def get_random_combo(place, year):
    print()
    print("Oh no! Something went wrong.")
    print()
    print("We ended up in {} in {}!".format(place, year))

def override_reminder(reminders):
    reminder_statements = ["The year H.G. Wells wrote The Time Machine", 
            "The year Oscar Wilde went to gaol", 
            "The year of the first Lumière Brothers films", 
            "Really, you need another hint? I give up. 1900 minus 5"]
    print()
    print("Do you need a reminder of the machine calibration code?")
    want_reminder = input("> ")
    want_reminder = want_reminder.upper()
    if want_reminder.startswith("Y"):
        print()
        reminders_index = (((reminders + 1) // 3)-1)
        print(reminder_statements[reminders_index])

def reboot():
    print()
    print ("Calibration code entered")
    print()
    print ("Time machine systems re-calibrating")
    timer = 4
    while timer > 0:
        print("*")
        time.sleep(1)
        timer = timer - 1
    print()
    print ("OK. Let's try to get you to your original destination.")
    print()

def fix_machine():
    print()
    print("You'd better fix this. Please enter the MACHINE CALIBRATION CODE.")
    override_code = "1895"
    guesses = 0
    while True:
        code_guess = input ("> ")
        if code_guess == override_code:
            reboot()
            break
        elif guesses < 13 and guesses % 3 == 2:
            override_reminder(guesses)
            guesses += 1
        else:
            guesses += 1
       
def retry_travel(destination_year, destination_place):
    fix_machine()
    travel_process(destination_year, destination_place)
    fail_chance = random.randint(0,2)
    if fail_chance == 2:
        get_random_combo(get_random_place(), get_random_year())
        retry_travel(destination_year, destination_place)

def travel_success(place, year):
    print()
    print("That worked! Welcome to {} in {}!".format(place, year))

def play_game():
    welcome()
    destination_year = get_destination_year()
    destination_place = get_destination_place()
    travel_process(destination_year, destination_place)
    get_random_combo(get_random_place(), get_random_year())
    retry_travel(destination_year, destination_place)
    travel_success(destination_place, destination_year)

play_game()

#special thanks to @jskud76 and @noahlt


#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

# pylint: disable=missing-module-
import datetime
import random
import json
import os
import pytz

def get_part_of_day(h):
    """Gets the current part of the day based on the hour. Used for `compliment()`"""
    return (
        "morning" if 5 <= h <= 11
        else "afternoon" if 12 <= h <= 17
        else "evening" if 18 <= h <= 22
        else "night"
    )

def compliment():
    """This gets a random phrase to say each time the main menu is reached from `phrases.json`"""
    time_part = get_part_of_day(datetime.datetime.now().hour)
    if random.randint(1, 5) == 5:
        time_part = "anytime"
        with open(os.getcwd() + '/phrases.json', encoding="utf-8") as phrases:
            data = json.load(phrases)
            c_list = data["morning"] if time_part == "morning" else data["afternoon"] if time_part == "afternoon" else data["evening"] if time_part == "evening" else data["night"]
            n = random.randint(0, len(c_list) - 1)
            compliment_1 = c_list[n]
            return compliment_1

def compliment_test(time_part):
    """A changeable version of compliment() that can have `part`, which refers to the part of day, can be manally input"""
    if random.randint(1, 5) == 5:
        time_part = "anytime"
        with open(os.getcwd() + '/phrases.json', encoding="utf-8") as phrases:
            data = json.load(phrases)
            c_list = data["morning"] if time_part == "morning" else data["afternoon"] if time_part == "afternoon" else data["evening"] if time_part == "evening" else data["night"]
            n = random.randint(0, 4)
            compliment_1 = c_list[n]
            print(compliment_1)
            return compliment_1



def main_menu():
    """Used to store the main menu for MFPython v2, to make the code cleaner anc easier to read"""
    
    header = "Welcome to MFPy - The MFPython Main Menu"
    options = [
        "Youtube Video Downloader",
        "Dice Roller"
    ]

    print("\033c") # clears the terminal
    print("=" * len(header))
    print(header)
    print("=" * len(header))
    compliment_p = compliment()
    if compliment_p is None:
        pass
    else:
        print(compliment_p)
    print("Please choose an option:")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    print("=" * len(header))
    if __name__ == "__main__":
        print()
    else:
        choice = int(input("> "))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        else:
            print("Invalid option. Please try again.")
            main_menu()
        return choice

def string_encode(string):
    """Encodes a string for searching/use in urls"""
    s = string.encode('utf-8')
    return s

def clear():
    """Just a simple function to let me import and be
    able to clear the screen without having to import other things."""
    os.system("clear")

def human_readable_number(number):
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return "{:.1f}K".format(number / 1000)
    elif number < 1000000000:
        return "{:.1f}M".format(number / 1000000)
    else:
        return "{:.1f}B".format(number / 1000000000)
# Function to format datetime into "Month Day, Year, Hour:Minute AM/PM" format
def format_datetime(dt):
    return dt.strftime("%b %d, %Y, %I:%M %p")
    
if __name__ == "__main__":
    print("Testing all functions in 'functions.py'")
    main_menu()
    clear()
    print(compliment())
    for hour in range(0, 24):
        print(datetime.datetime.now(pytz.timezone(tz)).hour)
        part = get_part_of_day(hour)
        print(f"hour {hour} is {part}")
        testing_compliments = compliment_test(part) if compliment_test(part) is not None else print("compliment.getcompliment.faliure.default")
        print(testing_compliments)

import datetime, random, json, pytz, os

def main_menu():
    header = "Welcome to MFPy - The MFPython Main Menu"
    options = [
        "Youtube Video Downloader",
        "Dice Roller"
    ]

    print("\033c") # clears the terminal
    print(header)
    print("=" * len(header))
    print("Please choose an option:")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    print("=" * len(header))
    if __name__ == "__main__":
        print()
    else:
        choice = int(input("> "))
        if choice == 1:
            print("You selected: Youtube Video Downloader")
        elif choice == 2:
            print("You selected: Dice Roller")
        else:
            print("Invalid option. Please try again.")
            main_menu()

def clear():
    os.system("clear")

def compliment():
    part = get_part_of_day(datetime.datetime.now().hour)
    if random.randint(1, 5) == 5:
        part = "anytime"
        with open(os.getcwd() + '/phrases.json') as phrases:
            data = json.load(phrases)
            c_list = data["morning"] if part == "morning" else data["afternoon"] if part == "afternoon" else data["evening"] if part == "evening" else data["night"]
            n = random.randint(0, len(c_list) - 1)
            compliment_2 = c_list[n]
            compliment_2 = "Hello there! It's always great to see you." if compliment == None else "Hello there! It's always great to see you." if compliment == "None" else compliment
            return compliment_2

def compliment_test(part):
    if random.randint(1, 5) == 5:
        part = "anytime"
        with open(os.getcwd() + '/phrases.json') as phrases:
            data = json.load(phrases)
            c_list = data["morning"] if part == "morning" else data["afternoon"] if part == "afternoon" else data["evening"] if part == "evening" else data["night"]
            n = random.randint(0, 4)
            compliment_1 = c_list[n]
            print(compliment_1)
            return compliment_1


def get_part_of_day(h):
    return (
        "morning" if 5 <= h <= 11
        else "afternoon" if 12 <= h <= 17
        else "evening" if 18 <= h <= 22
        else "night"
    )

if __name__ == "__main__":
    print("Testing all functions in 'functions.py'")
    main_menu()
    clear()
    print(compliment())
    for hour in range(0, 24):
        part = get_part_of_day(hour)
        print(f"hour {hour} is {part}")
        print(compliment_test(part)) if compliment_test(part) is not None else print("compliment.getcompliment.faliure.default")
    print()


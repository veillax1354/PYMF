
#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

# pylint: disable=missing-module-
import datetime
import random
import json
import os
import time

def t12_0(text, base_delay=0.02, ellipsis_delay=0.8):
    """Progressive text input, dubbed t12_type, or t12_0. Used to progressivley display characters in a string, using longer delays when an elipsis is encountered.

    Args:
        text (str): Input text that is then used to progressivley echo each char individually
        base_delay (float, optional): Base delay, used for normal chars. Measured in Seconds. Defaults to 0.03.
        ellipsis_delay (float, optional): Custom delay, used for elipsis (...). Measured in Seconds. Defaults to 0.8.
    """
    for char in text:
        if char == '.' and text[text.index(char):text.index(char)+3] == "...":
            print(".", end='', flush=True)
            time.sleep(ellipsis_delay)
        else:
            print(char, end='', flush=True)
            time.sleep(base_delay)
    print()

if __name__ == "__main__":
    text = "Connecting... Initiating connection... Connection secured..."
    t12_0(text)




def progressive_text_output(text, delay=0.03):
    """
        Litterally just me being lazy.
    """
    t12_0(text)

def choose_random_phrase():
    with open("phrases.json", "r") as f:
        phrases = json.load(f)
    
    anytime_phrases = phrases["anytime"]
    normal_phrases = phrases["phrases"]
    all_phrases = anytime_phrases + normal_phrases
    chosen_phrase = random.choice(all_phrases)
    f.close()
    return chosen_phrase

if __name__ == "__main__":
    random_phrase = choose_random_phrase()
    print(random_phrase)




def main_menu():
    """Used to store the main menu for MFPython v2, to make the code cleaner anc easier to read"""
    
    header = "                 Welcome                "
    options = [
        "Youtube Video Downloader",
        "Dice Roller"
    ]

    print("\033c") # clears the terminal
    progressive_text_output("=" * len(header))
    progressive_text_output(header)
    progressive_text_output("=" * len(header))
    progressive_text_output(choose_random_phrase())
    progressive_text_output("=" * len(header))
    progressive_text_output("Please choose an option:")
    for i, option in enumerate(options):
        progressive_text_output(f"{i + 1}. {option}")
    progressive_text_output("=" * len(header))
    if __name__ == "__main__":
        print()
    else:
        choice = int(input("> "))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        else:
            progressive_text_output("Invalid option. Please try again.")
            main_menu()
        return choice

def admin_menu():
    """Used to store the main menu for MFPython v2, to make the code cleaner anc easier to read"""
    
    header = "              Welcome, Veillax              "
    options = [  
        "Youtube Video Downloader",
        "Dice Roller"
    ]

    print("\033c") # clears the terminal
    progressive_text_output("=" * len(header))
    progressive_text_output(header)
    progressive_text_output("=" * len(header))
    progressive_text_output(choose_random_phrase())
    progressive_text_output("=" * len(header))
    progressive_text_output("Please choose an option:")
    for i, option in enumerate(options):
        progressive_text_output(f"{i + 1}. {option}")
    progressive_text_output("=" * len(header))
    if __name__ == "__main__":
        print()
    else:
        choice = int(input("> "))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        else:
            progressive_text_output("Invalid option. Please try again.")
            main_menu()
        return choice

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
    
def change_warning_value(change=False, new_value=None):
    with open("options.json", "r", encoding="UTF-8") as f:
        options = json.load(f)
    if new_value is not None and change == True:
        options["warning"] = new_value
    else:
        return options['warning']

    with open("options.json", "w", encoding="UTF-8") as f:
        json.dump(options, f, indent=4)

def admin_change_options(option, new_value=None):
    with open("options.json", "r", encoding="UTF-8") as f:
        options = json.load(f)
    if new_value is not None:
        options[option] = new_value
        return f"{option} has been changed to {new_value}"
    else:
        return options[option]

    with open("options.json", "w", encoding="UTF-8") as f:
        json.dump(options, f, indent=4)
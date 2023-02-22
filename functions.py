
#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

# pylint: disable=missing-module-docstring, dangerous-default-value, missing-function-docstring, invalid-name, line-too-long, redefined-outer-name
import random
import json
import os
import time
import html
import termios
import sys
import tty

def get_input():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        answer = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return answer

def get_key_press(expected_keys=[], should_print=False, print_string=None):
    """Gets the pressed key from the defined list and returns it

    Args:
        expected_keys (list, optional): Defined list of keys to check against. Defaults to [].
        should_print (bool, optional): Decides whether or not to pring which keys should pe pressed. Defaults to False.

    Returns:
        _type_: _description_
    """
    if should_print:
        if print_string is not None:
            keys = ""
            key = expected_keys
            keys = '"' + ', '.join(key) + '"'
            t12(f"{print_string} - {keys}: ")
        elif print_string is None:
            keys = ""
            key = expected_keys
            keys = '"' + ', '.join(key.upper()) + '"'
            t12(f"Press one of the following keys - {keys}: ")
    answer = get_input()
    if expected_keys != []:
        return answer
    elif expected_keys == []:
        return [answer, "Expected Not Specified"]
    
    


def on_key_press():
    check = get_key_press(["i", "s", "1"])
    print(f"Pressed {check}")

def unescape(text):
    return html.unescape(text)

def t12(inputtext, base_delay=0.02, ellipsis_delay=0.8):
    """Progressive text input, dubbed t12_type, or t12. Used to progressivley display characters in a string, using longer delays when an elipsis is encountered.

    Args:
        inputtext (str): Input text that is then used to progressivley echo each char individually using the given delay
        base_delay (float, optional): Base delay, used for normal chars. Measured in Seconds. Defaults to 0.03.
        ellipsis_delay (float, optional): Custom delay, used for elipsis (...). Measured in Seconds. Defaults to 0.8.
    """
    for char in inputtext:
        if char == '.' and inputtext[inputtext.index(char):inputtext.index(char)+3] == "...":
            print(".", end='', flush=True)
            time.sleep(ellipsis_delay)
        else:
            print(char, end='', flush=True)
            time.sleep(base_delay)
    print()

if __name__ == "__main__":
    text = "Connecting... Initiating connection... Connection secured..."
    #t12(text)
    # Sample text with encoded characters
    text = "This is an example of encoded text: &#39;Hello, World!&#39;"

    # Decode the encoded characters in the text
    decoded_text = html.unescape(text)

    # Print the original text and the decoded text
    print("Original text:", text)
    print("Decoded text:", decoded_text)

    on_key_press()



def choose_random_phrase():
    """Retrieves a random phrase from phrases.json

    Returns:
        str chosen_phrase: Returns the chosen phrase
    """
    with open("phrases.json", "r", encoding="UTF-8") as f:
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
    """Used to store the main menu for PYMF, to make the code cleaner anc easier to read"""
    
    header = "                 Welcome                "
    options = [
        "Youtube Video Downloader",
        "Temp Conversion",
        "Note Taking"
    ]

    os.system("clear") # clears the terminal
    t12("=" * len(header))
    t12(header)
    t12("=" * len(header))
    t12(choose_random_phrase())
    t12("=" * len(header))
    t12("Please choose an option:")
    for i, option in enumerate(options):
        t12(f"{i + 1}. {option}")
    t12("=" * len(header))
    if __name__ == "__main__":
        print()
    else:
        a = get_key_press(["1", "2", "3"])
        if a == "1":
            os.system("clear")
        elif a == "2":
            os.system("clear")
        elif a == "3":
            os.system("clear")
        else:
            t12("Invalid option. Please try again.")
            main_menu()
        return a

def admin_menu():
    """Used to store the main menu for PYMF, to make the code cleaner and easier to read"""
    
    header = "                Admin Console                "
    options = [  
        "Youtube Video Downloader",
        "Temp Conversion",
        "Notes"
    ]

    print("\033c") # clears the terminal
    t12("=" * len(header))
    t12(header)
    t12("=" * len(header))
    t12(choose_random_phrase())
    t12("=" * len(header))
    t12("Please choose an option:")
    for i, option in enumerate(options):
        t12(f"{i + 1}. {option}")
    t12("=" * len(header))
    if __name__ == "__main__":
        print()
    else:
        a = get_key_press(["1", "2", "3"])
        if a == "1":
            os.system("clear")
        elif a == "2":
            os.system("clear")
        elif a == "3":
            os.system("clear")
        else:
            t12("Invalid option. Please try again.")
            main_menu()
        return a

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
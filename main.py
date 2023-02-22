# pylint: disable=expression-not-assigned
from time import sleep
import getpass
import os
from os import system, path
from os.path import exists
import argparse
import functions
from functions import t12, get_key_press
import yt
import notes
import temperature


def main_menu(admin=False):
    if not admin:
        t12(">")
        a = functions.main_menu()
        if a == "1":
            sleep(1)
            yt.main()
        elif a == "2":
            while True:
                i_temp = input("Enter an input amount or \"e\" to exit: ")
                if i_temp.lower() == 'e':
                    break
                i_unit = get_key_press(["K", "F", "C"], True, "Choose an input temperature unit")
                o_unit = get_key_press(["K", "F", "C"], True, "Choose an output temperature unit")
                system(f"python3 temperature.py {i_temp} {i_unit} {o_unit}")
        elif a == "3":
            sleep(1)
            notes.main_menu()
        main_menu()
    elif admin:
        a = functions.admin_menu()
        if a == "1":
            sleep(1)
            yt.main()
        elif a == "2":
            while True:
                i_temp = input("Enter an input amount or \"e\" to exit: ")
                if i_temp.lower() == 'e':
                    break
                i_unit = get_key_press(["K", "F", "C"], True, "Choose an input temperature unit")
                o_unit = get_key_press(["K", "F", "C"], True, "Choose an output temperature unit")
                system(f"python3 temperature.py {i_temp} {i_unit} {o_unit}")
        elif a == "3":
            sleep(1)
            notes.main_menu()
        main_menu()

def login(type):
    username = "e18002"
    adminun = "e01-veillax"
    suid = "1217-42098"
    adminsuid = "1217-a12"
    password = "employee002048"
    adminpass = "a071129"
    quickskipadmin = 'qsa1'
    quickskip = 'qs01'
    os.system("clear")
    try:
        t12("\033[32m==========================================================================================================================================================", 0.01)
        print("\033[0m")
        t12("\033[33mEnter username: ") if type == 'SECURE' else t12("\033[32mEnter username: ")
        entered_username = input()
        if entered_username == quickskip or entered_username == quickskipadmin:
            if entered_username == quickskip:
                t12("Authorizing...")
                sleep(1)
                t12("Authorized! \033[32mAccess granted.")
                sleep(3)
                main_menu()
            elif entered_username == quickskipadmin:
                t12("Authorizing...")
                sleep(1)
                t12("Authorized! \033[32mAccess granted.")
                sleep(3)
                main_menu(True)
        if entered_username != quickskip or entered_username != quickskipadmin: 
            t12("Enter SUID: ") if type == 'SECURE' else t12("Enter SUID: ")
            entered_suid = input()
            if entered_suid == suid or adminsuid:
                t12("Enter password: ") if type == 'INSECURE'  else t12("Enter password: ")
                entered_password = getpass.getpass("") if type == 'SECURE' else input()
            else:
                t12("\033[1;31m\033[0;31mAccess denied")
                sleep(1)
                os.system("python3 main.py")

        else:
            t12("\033[1;31m\033[0;31mAccess denied")
            sleep(1)
            os.system("python3 main.py")
    except Exception as e:
        print(e)
    print("\033[32m")
    t12("==========================================================================================================================================================\033[0m", 0.01)

    if entered_username == username or quickskip and entered_suid == suid and entered_password == password:
        t12("Authorizing...")
        sleep(1)
        t12("Authorized! \033[32mAccess granted.")
        sleep(3)
        main_menu()
    elif entered_username == adminun or quickskipadmin and entered_suid == adminsuid and entered_password == adminpass:
        t12("Authorizing...")
        t12("Authorized! \033[1;92mAdmin access granted")
        t12("Welcome, Veillax.")
        sleep(3)
        main_menu(True)
    else:    
        t12("\033[1;31m\033[0;31mAccess denied")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional skipping to login.')
    parser.add_argument('--login', action='store_true', help='Skip to the login.')
    parser.add_argument('--skip', action='store_true', help='Skip the long login starting bit.')
    args = parser.parse_args()
    amnd2 = False
    if args.login:
        amnd2 = True
    if args.login and amnd2:
        os.system("clear")
        functions.t12("\033[0mConnecting...")
        sleep(1)
        functions.t12("Initiating connection...")
        sleep(1)
        functions.t12("Connection secured!\033[32m")
        sleep(1)
    if args.skip or (args.login and amnd2):
        t12("\033[32m==========================================================================================================================================================\033[0m", 0.01)
        if functions.change_warning_value(True):
            functions.t12("\033[0;91m\033[1;31mWARNING!\033[0m\033[31m It is highly recommended to avoid entering your password in plain text as it poses a security risk.\n\033[33mYour password may be visible to others and can be intercepted by malicious actors. Use caution when entering sensitive information\n\033[0m.")
        t12("Type \"s\" to use secure password input, otherwise, type \"i\".")
        check = input("\033[32m>>>\033[0m ")
        TYPE = 'SECURE' if check == 's' else 'INSECURE' if check == 'i' else 'n'
        if TYPE == 'n':
            t12("Please try again.") 
            system("clear")
            system("python3 main.py --skip")
        else:
            login(TYPE)
    else:
        main_menu()
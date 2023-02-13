# pylint: disable=expression-not-assigned
from time import sleep
import getpass
import os
import argparse
import mains
import functions
from functions import t12_0

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
    t12_0("\033[32m==========================================================================================================================================================", 0.01)
    print("\033[0m")
    t12_0("\033[33mEnter username: ") if type == 'SECURE' else t12_0("\033[32mEnter username: ")
    entered_username = input() if type == 'SECURE' else input()
    if entered_username == quickskip or quickskipadmin:
        if entered_username == quickskip:
            entered_suid = suid
            entered_password = password
        elif entered_username == quickskipadmin:
            entered_suid = adminsuid
            entered_password = adminpass
    elif entered_username == username or adminun:
        t12_0("Enter SUID: ") if type == 'SECURE' else t12_0("Enter SUID: ")
        entered_suid = input()
        if entered_suid == suid or adminsuid:
            t12_0("Enter password: ") if type == 'INSECURE'  else t12_0("Enter password: ")
            entered_password = getpass.getpass("__________\033[0m") if type == 'SECURE' else input("\033[0m")
        else:
            t12_0("\033[1;31m\033[0;31mAccess denied")
            sleep(1)
            os.system("python3 main.py")

    else:
        t12_0("\033[1;31m\033[0;31mAccess denied")
        sleep(1)
        os.system("python3 main.py")
    print("\033[32m")
    t12_0("==========================================================================================================================================================\033[0m", 0.01)

    if (entered_username == username or quickskip) and entered_suid == suid and entered_password == password:
        t12_0("Authorizing...")
        sleep(1)
        t12_0("Authorized! \033[32mAccess granted.")
        sleep(3)
        mains.main_menu()
    elif (entered_username == adminun or quickskipadmin) and entered_suid == adminsuid and entered_password == adminpass:
        t12_0("Authorizing...")
        t12_0("Authorized! \033[1;92mAdmin access granted")
        t12_0("Welcome, Veillax.")
        sleep(3)
        mains.main_menu(True)
    else:    
        t12_0("\033[1;31m\033[0;31mAccess denied")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional skipping to main eun or login.')
    parser.add_argument('--skip', action='store_true', help='Skip to the main menu.')
    parser.add_argument('--login', action='store_true', help='Skip to the login.')
    args = parser.parse_args()

    if not args.skip and not args.login:
        os.system("clear")
        functions.t12_0("\033[0mConnecting...")
        sleep(1)
        functions.t12_0("Initiating connection...")
        sleep(1)
        functions.t12_0("Connection secured!\033[32m")
        sleep(1)
        t12_0("==========================================================================================================================================================\033[0m", 0.01)
        if functions.change_warning_value(True):
            functions.t12_0("\033[0;91m\033[1;31mWARNING!\033[0m\033[31m It is highly recommended to avoid entering your password in plain text as it poses a security risk.\n\033[33mYour password may be visible to others and can be intercepted by malicious actors. Use caution when entering sensitive information\n\033[0m.")
        t12_0("Type \"s\" to use secure password input, otherwise, type \"i\".")
        check = input("\033[32m>>>\033[0m ")
        TYPE = 'SECURE' if check == 's' else 'INSECURE' if check == 'i' else 'n'
        if TYPE == 'n':
            t12_0("Please try again.\n\033[0;91m\033[1;31mTerminating Connection...") 
        else:
            login(TYPE)
    elif not args.skip and args.login:
        check = input("Type \"s\" to use secure password input, otherwise, type \"i\".")
        TYPE = 'SECURE' if check == 's' else 'INSECURE' if check == 'i' else 'n'
        login(TYPE)
    elif args.skip and not args.login:
        mains.main_menu()
    elif args.skip and args.login:
        ask = input("Skip straight to menu, or skip to login? Input either \"menu\" or \"login\"")
        if ask == 'menu':
            mains.main_menu() 
        else: 
            check = input("Type \"s\" to use secure password input, otherwise, type \"i\".")
            TYPE = 'SECURE' if check == 's' else 'INSECURE' if check == 'i' else 'n'
            login(TYPE)
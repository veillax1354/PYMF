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
    os.system("clear")
    t12_0("\033[33mEnter username: ") if type == 'SECURE' else t12_0("\033[32mEnter username: ")
    entered_username = input() if type == 'SECURE' else input()
    if entered_username == username or adminun:
        t12_0("Enter SUID: ") if type == 'SECURE' else t12_0("Enter SUID: ")
        entered_suid = input()
        if entered_suid == suid or adminsuid:
            t12_0("Enter password: ") if type == 'INSECURE'  else t12_0("Enter password: ")
            entered_password = getpass.getpass("**********") if type == 'SECURE' else input()
        else:
            print("\033[1;31m\033[0;31mAccess denied")
            sleep(1)
            os.system("python3 main.py")

    else:
        print("\033[1;31m\033[0;31mAccess denied")
        sleep(1)
        os.system("python3 main.py")

    if entered_username == username and entered_suid == suid and entered_password == password:
        print("Authorizing...")
        sleep(1)
        print("Authorized! \033[32mAccess granted.")
        sleep(3)
        mains.main_menu()
    elif entered_username == adminun and entered_suid == adminsuid and entered_password == adminpass:
        t12_0("Authorizing...")
        t12_0("Authorized! \033[1;92mAdmin access granted")
        t12_0("Welcome, Veillax.")
        mains.main_menu(True)
    else:    
        print("\033[1;31m\033[0;31mAccess denied")

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
        functions.t12_0("Connection secured...")
        sleep(1)
        if functions.change_warning_value(True):
            functions.t12_0("\033[0;91m\033[1;31mWARNING!\033[0m\033[31m It is highly recommended to avoid entering your password in plain text as it poses a security risk.\n\033[33mYour password may be visible to others and can be intercepted by malicious actors. Use caution when entering sensitive information\n\033[0mType \"s\" to use secure password input, otherwise, type \"i\".")
        check = input("\033[32m>>>\033[0m ")
        TYPE = 'SECURE' if check == 's' else 'INSECURE' if check == 'i' else 'n'
        if TYPE == 'n':
            print("Please try again.\n\033[0;91m\033[1;31mTerminating Connection...") 
        else:
            login(TYPE)
    elif not args.skip and args.login:
        login('SECURE')
    elif args.skip and not args.login:
        mains.main_menu()
    elif args.skip and args.login:
        ask = input("Skip straight to menu, or skip to login? Input either \"menu\" or \"login\"")
        mains.main_menu() if ask == 'menu' else login('SECURE')
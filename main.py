# pylint: disable=expression-not-assigned
from time import sleep
import getpass
import os
import argparse
import mains
import functions
from functions import t12

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
        if entered_username != quickskip or quickskipadmin:
            pass
        elif entered_username == quickskip or quickskipadmin:
            if entered_username == quickskip:
                entered_suid = suid
                entered_password = password
            elif entered_username == quickskipadmin:
                entered_suid = adminsuid
                entered_password = adminpass
        if entered_username == username or adminun and entered_username != quickskip or quickskipadmin:
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
        mains.main_menu()
    elif entered_username == adminun or quickskipadmin and entered_suid == adminsuid and entered_password == adminpass:
        t12("Authorizing...")
        t12("Authorized! \033[1;92mAdmin access granted")
        t12("Welcome, Veillax.")
        sleep(3)
        mains.main_menu(True)
    else:    
        t12("\033[1;31m\033[0;31mAccess denied")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Optional skipping to main eun or login.')
    parser.add_argument('--skip', action='store_true', help='Skip to the main menu.')
    parser.add_argument('--login', action='store_true', help='Skip to the login.')
    args = parser.parse_args()

    if not args.skip and not args.login:
        os.system("clear")
        functions.t12("\033[0mConnecting...")
        sleep(1)
        functions.t12("Initiating connection...")
        sleep(1)
        functions.t12("Connection secured!\033[32m")
        sleep(1)
        t12("==========================================================================================================================================================\033[0m", 0.01)
        if functions.change_warning_value(True):
            functions.t12("\033[0;91m\033[1;31mWARNING!\033[0m\033[31m It is highly recommended to avoid entering your password in plain text as it poses a security risk.\n\033[33mYour password may be visible to others and can be intercepted by malicious actors. Use caution when entering sensitive information\n\033[0m.")
        t12("Type \"s\" to use secure password input, otherwise, type \"i\".")
        check = input("\033[32m>>>\033[0m ")
        TYPE = 'SECURE' if check == 's' else 'INSECURE' if check == 'i' else 'n'
        if TYPE == 'n':
            t12("Please try again.\n\033[0;91m\033[1;31mTerminating Connection...") 
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
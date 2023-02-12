
#          Copyright Veillax 2023 - 2023 .
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import functions
import yt


def main_menu(admin=False):
    if not admin:
        choice = functions.main_menu()

        if choice == 1:
            yt.main()
        elif choice == 2:
            # Dice Roller Code, remove pass if implimented
            pass
    elif admin:
        choice = functions.admin_menu()

        if choice == 1:
            yt.main()
        elif choice == 2:
            # Dice Roller Code, remove pass if implimented
            pass

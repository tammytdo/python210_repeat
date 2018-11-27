"""

Donor Database Program

This mail room program stores donors, a history of donations, intakes
new donations, and generates thank you letters.

"""

import math
import re
import sys
import time


donor_db = [('Beyonce Knowles', [100.01, 201.02, 301.03]),
            ('Lucy Liu', [400.04, 500.05, 600.06]),
            ('Mandy Moore', [700.07, 800.08, 900.09]),
            ('Emma Watson', [1000.01, 2000.02, 3000.03])
            ]


def print_donors():
    print("Donors in the donor database:")
    for donor in donor_db:
        print("  -", donor[0])


def main_menu_selection():
    print("\nMain Menu")
    menu_selection = input("Please make a selection: "
                           "\n  -'T' to send a Thank You letter,"
                           "\n  -'R' to see a Report,"
                           "\n  -'Q' to Quit the mailroom"
                           "\n\nSelection: ")

    return menu_selection.strip().upper()


def gen_letter(donor_name):
    return "Thank you, {}. This much {}".format(donor_name[0], donor_name[1][-1])


def send_thank_you():
    while True:
        donor_name = input("\nEnter the donor's full name. (Enter 'L' for a list of donors or 'M' for main menu.): ").strip().title()
        if donor_name == 'L':
            print_donors()
        elif donor_name == 'M':
            return
        else:
            break

    while True:
        match_int = re.compile(r'^[0-9]+$')
        donation_amount = input("Enter donation amount (or 'M' for main menu): $ ").strip()
        if donation_amount in ['M', 'm']:
            return # how does this return all the way to main menu?


        amount_float = float(donation_amount)
        if math.isnan(amount_float) or math.isinf(amount_float) or round(amount_float, 2) == 0.00:
            print("Error. Enter a valid donation amount: ")
            return
        else:
            break

    donor = verify_donor(donor_name)
    for donor in donor_db:
        if donor == donor[0]:
            break

    else:
        print(f"\nCreating record for new donor: {donor_name}.")
        donor_name = [donor_name, []]
        donor_name[1].append(amount_float)
        donor_db.append(donor_name)

    print(gen_letter(donor_name))


def verify_donor(donor_name):
    # print("\n", donor_name, "\n")
    for donor in donor_db:
        if donor_name.lower() == donor[0].lower():
            return donor
    return None



def report():
    print("pass report")


def quit_database():
    print("\nExiting the donor database.")
    time.sleep(1)
    print("\nGoodbye.")
    sys.exit()

if __name__ == "__main__":
    print("Welcome to the donor database.")
    # running = True
    while True: # why not just say "while true"?
        selection = main_menu_selection()
        if selection == 'T':
            send_thank_you()
        elif selection == "R":
            report()
        elif selection == "Q":
            quit_database()
        else:
            print("\nInvalid selection.")
            time.sleep(1)

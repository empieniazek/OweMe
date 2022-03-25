from distlib.compat import raw_input

import person, product, bill

menu = {'HL': "to see list of your homies and their debt",
        'HA': "to add Homie to your list",
        'HR': "to remove Homie to your list",
        'HI': "to choose one of your homies",
        'EX': "to exit"
        }


def init_menu():
    welcome_message()
    menu_loop()


def menu_loop():
    # print_main_options()
    print("What do you wanna do?")
    options = menu.keys()
    for entry in sorted(options):
        print(entry, menu[entry])

    selection = raw_input("Please Select:")
    if selection == '1':
        print("add")
    elif selection == '2':
        print("delete")
    elif selection == '3':
        print("find")
    else:
        print("Unknown Option Selected!")


def print_main_options():
    print("Here are your options:")
    print("\tHL - to see list of your homies and their debt")
    print("\tHA - to add Homie to your list")
    print("\tHR - to remove Homie to your list")
    print("\tHI - to choose one of your homies")


def welcome_message():
    print("Hi Homie Welcome in OweMe")


init_menu()

from model.user_classes import *
from model.processing_img import *


def menu_options():
    print("1. Start")
    print("2. Register student")
    print("3. Exit")
    opt = int(input("Select option: "))
    return opt


def menu():
    while True:
        option = menu_options()
        if option == 1:
            fr = Frame()
            fr.set_resolution(1280, 720)
            fr.read()
            fr.close()
            print("No yet")
        elif option == 2:
            User.register()
        elif option == 3:
            print("Good bye!")
            break
        else:
            print("This option doesn't exists")


if __name__ == '__main__':
    menu()


while True:
    print("Welcome")
    check_option = int(input("Check in (1)\nCheck out (2)\nExit (0)\nYour option : "))

    if check_option == 0:
        break

    elif check_option == 1:
        print(f"You chose {check_option}")
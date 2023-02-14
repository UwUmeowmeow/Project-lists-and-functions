children = []
total_children = 0

# Check option
while True:

    print("Welcome")
    try:
        check_option = int(input("Exit (0)\nCheck in (1)"
                                 "\nCheck out (2)\nCalculate Costs (3)"
                                 "\nPrint roll (4)\nYour option: "))
    except ValueError:
        print("Error please type a number")

    if check_option == 0:
        break

    elif check_option == 1:
        child_in = input("Child name: ")
        children.append(child_in)

    elif check_option == 2:
        name = input("Enter your child name: ")
        if name in children:
            children.remove(name)
        else:
            print("Name not found!")
            break

    elif check_option == 3:
        print(f"Your charge is ${len(children) * 12}")

    elif check_option == 4:
        for thing in children:
            print(f"- {thing}")






def int_check(prompt):
    """Function to check if user input is an integer"""
    valid = False
    while not valid:
        try:
            number_check = int(input(prompt))
            if isinstance(number_check, int):
                valid = True
                return number_check
        except ValueError:
            print("Please enter a number")


def most_day():
    """Function to find the person who was absent for the most days"""
    absent_list = absent_staff
    highest_absent = 0
    for item in absent_list:
        if item[1] > highest_absent:
            highest_absent = item[1]
            highest_absent_name = item[0]
    return [highest_absent_name, highest_absent]


def none_absent(none):
    """Function to find the people who were not absent at all"""
    none_list = []
    for item in none:
        if item[1] == 0:
            none_list.append(item[0])
    return none_list


def above_absent(absent_staff_, average_):
    """Function to find the people who were absent for more days than the average"""
    above_list = []
    for item in absent_staff_:
        if item[1] > average_:
            above_list.append(item[0])
    return above_list


# Main routine
Total_absent = 0
total_data = 0
absent_staff = []
while True:
    # Ask user for name and number of absent days
    name = input("Enter your name: ")
    if name == "$":
        break
    days = int_check("Enter number of day your absent: ")
    total_data += 1
    absent_staff.append([name, days])
    Total_absent = Total_absent + days

# Find the person who was absent for the most days
Most_absent = most_day()
print(f"Most absent {Most_absent}")

# Print the list of absent staff
print(f"absent staff {absent_staff}")

# Find the people who were not absent at all
print(f"List of people not absent at all {none_absent(absent_staff)}")

# Find the average number of days staff were absent
average = Total_absent / total_data
print(f"Average number of days staff were absent {average:.2f}")

# Find the people who were absent for more days than the average
above_list_ = above_absent(absent_staff, average)
for name_ in above_list_:
    print(f"List of people absent above average: {name_}")

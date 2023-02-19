name = input("What is the driver's name: ")

trip_count = 0
total_time = 0
total_income = 0
Base_cost = 10

while True:
    try:
        trip = input("Do you want to start a new trip?\nYes (1)"
                     "\nNo (2)\nEnter Yes or No: ").lower()
    except ValueError:
        print("Error please type only Yes or No")

    if trip == "1" or trip == "yes":
        try:
            trip_time = float(input("How long will it take (IN MINUTES)? "))
            trip_count += 1
            total_time += trip_time
            trip_cost = (trip_time * 2) + Base_cost
            total_income += trip_cost
            print(f"This trp cost ${trip_cost:.2f}")

        except ValueError:
            print("Error please type only numbers")

    elif trip == "2" or trip == "no":

        print(f"Driver {name} had {trip_count} total trip time of "
              f"{round(total_time)}"
              f" Minutes\n"
              f"The average time of all trips was "
              f"{round(total_time / trip_count, 2)}\n"
              f"Minutes"
              f"Total income for the day was ${total_income:.2f}\n"
              f"The average cost for all trip was "
              f"${total_time / trip_count:.2f}")

    else:
        print("Please enter a valid choice")




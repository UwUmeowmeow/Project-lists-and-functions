reserve_price = 0
highest_bid = 0


auction = input("What is auction for?: ")
reserve = int(input("What is the reserve price?: "))
print(f"The auction for the {auction} has started!")

while True:

    print(f"The high bid so far is {highest_bid}")
    bid = int(input("What is your bid: "))

    if bid > highest_bid:
        highest_bid = bid

    elif bid < highest_bid:
        print(f"Please enter a bid that is higher than {highest_bid}")

    elif bid == -1:
        print("Auction had ended!")
        break








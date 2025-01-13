
try:
    with open("guest_list.txt", "r") as file:
        guests = [line.strip() for line in file.readlines()]
    print("Guest list loaded successfully.")
except FileNotFoundError:
    guests = [] 
    print("No guest list file found. Starting with an empty list.")

quit = False

while not quit:
    print(
        "\nWelcome to the guest manager!\n"
        "1. Add a guest\n"
        "2. Remove a guest\n"
        "3. List all guests\n"
        "4. Search for a guest\n"
        "5. Save and quit\n"
    )

    choice = input("What would you like to do? ")

    if choice == "1":
        name = input("What is the guest's full name? ").strip()
        guests.append(name)
        print(name + " has been added.")
    elif choice == "2":
        name = input("What is the guest's full name? ").strip()
        if name in guests:
            guests.remove(name)
            print(name + " has been removed.")
        else:
            print(name + " is not in the guest list.")
    elif choice == "3":
        if not guests:
            print("There are no guests yet, you need to add some.\n")
        else:
            print("Guest List:")
            for guest in guests:
                print(guest)
    elif choice == "4":
        name = input("What is the guest's first or last name? ").strip().lower()
        found = False
        for guest in guests:
            if name in guest.lower():
                print(guest)
                found = True
        if not found:
            print("No guests found with that name.")
    elif choice == "5":
        print("Saving guest list and exiting the guest manager...")
        with open("guest_list.txt", "w") as file:
            for guest in guests:
                file.write(guest + "\n")
        quit = True
    else:
        print("Invalid choice. Please try again.")

guests = []
quit = False
while quit != True:
    print(
        "Welcome to the guest manager!\n. "
        "1. Add a guest\n "
        "2. Remove a guest\n "
        "3. List all guests\n "
        "4. Search for a guest\n "
        "5. Quit"
    )
    

    choice = input("What would you like to do? ")

    if choice == "1":
        name = input("What is the guest's full  name? ")
        guests.append(name)
        print(name + " has been added.")
    elif choice == "2":
        name = input("What is the guest's full name? ")
        guests.remove(name)
        print(name + " has been removed.")
    elif choice == "3":
        if len(guests) == 0:
            print("There are no guests yet, you need to add some. \n")
        for guest in guests:
            print(guest)
    elif choice == "4":
        name = input ("What is the guest's first or last name? ")
        for guest in guests:
            if name in guest:
                print(guest)
    elif choice == "5":
        print("Exiting the guest manager...")
        quit = True
    else:
        print("Invalid choice. Please try again.")

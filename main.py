import parking


def main():
    while True:
        print("\t   ")
        print("Welcome to the car parking system!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice : ")
        if choice == "1":

            parking.register()

        elif choice == "2":
            parking.logIn()

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()

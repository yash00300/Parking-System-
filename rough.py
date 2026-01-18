# -----------------------------
# Global User Storage
# -----------------------------
userList = []

# -----------------------------
# Registration + Login
# -----------------------------
def register():
    print("\n--- User Registration (3 users) ---")
    for i in range(3):
        user = {
            'name': input("Enter username: "),
            'password': input("Enter password: ")
        }
        userList.append(user)

    print("\n--- Login ---")
    login_name = input("Enter your name to login: ")
    login_password = input("Enter your password to login: ")

    for user in userList:
        if user['name'] == login_name and user['password'] == login_password:
            print("Login successful!")
            return user   # return logged-in user

    print("Login failed. Incorrect name or password.")
    return None

# -----------------------------
# Parking Logic
# -----------------------------
def parking(logged_user):
    parkingList = [None] * 3

    while True:
        print("\n------- Parking Area -------")
        for index, val in enumerate(parkingList):
            if val is None:
                print(f"Slot {index}: Available")
            else:
                print(f"Slot {index}: {val['Car_Name']} | {val['Car_Number']} | Owner: {val['Owner_name']}")
        print("----------------------------")

        # ADMIN MENU
        if logged_user['name'] == 'admin':
            print("\n(Admin Access)")
            print("1. Park Car")
            print("2. Remove Car")
            print("3. Show Details")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                slot = int(input("Enter slot number: "))
                if 0 <= slot < len(parkingList) and parkingList[slot] is None:
                    car = {
                        'Car_Name': input("Car Name: "),
                        'Car_Number': input("Car Number: "),
                        'Owner_name': input("Owner Name: ")
                    }
                    parkingList[slot] = car
                    print("Car parked successfully!")
                else:
                    print("Invalid or occupied slot.")

            elif choice == '2':
                slot = int(input("Enter slot number to remove: "))
                if 0 <= slot < len(parkingList) and parkingList[slot] is not None:
                    parkingList[slot] = None
                    print("Car removed successfully!")
                else:
                    print("Invalid or empty slot.")

            elif choice == '3':
                continue

            elif choice == '4':
                print("Exiting parking system...")
                break

            else:
                print("Invalid choice!")

        # NORMAL USER MENU
        else:
            print("\n(User Access)")
            print("3. Show Details")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == '3':
                continue

            elif choice == '4':
                print("Exiting parking system...")
                break

            else:
                print("Invalid choice!")

# -----------------------------
# Main Program
# -----------------------------
def main():
    while True:
        print("\n==== Car Parking System ====")
        print("1. Register & Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            logged_user = register()
            if logged_user:
                parking(logged_user)

        elif choice == '2':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

# Run Program
main()

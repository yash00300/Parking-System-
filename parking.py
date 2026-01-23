# # Parking System
import pwinput
import validation
import remove_vehical
import car_park
import json


user_List = [
    {"id": 1, "user_name": "Yash", "email": "yash@gmail.com", "password": "Yash@123"}
]
login_List = []

def register():
    # 1. Load users from file
    try:
        with open('parkingData/user_List.json', 'r') as f:
            user_List = json.load(f)
    except FileNotFoundError:
        user_List = []

    user_name = input("Enter your user_name: ").strip()

    while True:
        email = input("Enter email: ")
        if email.endswith('@gmail.com') or email.endswith('@gmail.in'):
            print('valid email!')
            break
        else:
            print('Invalid email!')

    password = validation.validate_password()

    # 2. Check if user already exists
    for user in user_List:
        if user["user_name"] == user_name or user["email"] == email:
            print("User already exists!")
            return

    # 3. Add new user
    user_List.append({
        "id": len(user_List) + 1,
        "user_name": user_name,
        "email": email,
        "password": password
    })

    # 4. Save updated list
    with open('parkingData/user_List.json', 'w') as f:
        json.dump(user_List, f, indent=4)

    print("Registration successful!")
    return True



def logIn():

    with open('parkingData/user_List.json', 'r') as f:
        user_List = json.load(f)

    user_name = input("enter user_name:").strip()
    password = pwinput.pwinput(prompt="Enter your password to login: ",mask='*').strip()

    for user in user_List:
        if user["user_name"] == user_name and user["password"] == password:
            print("Login successful")

            parking()
            return
    print("\t   ")
    print(user["user_name"], user["password"])
    print("id and password is wrong")
    print("1. for forgot password")
    print("2. re-enter")
    choice = input("enter 1 or 2: ")
    if choice == "1":
        validation.forget_passowrd()
    elif choice == "2":
        logIn()
    else:
        print("please enter correct choice!!!")


# Parking Logic



def parking():
    parkingList = [None] * 3

    carDetail = {
        "Car_user_name": "",
        "Car_Number": "",
        "Owner_user_name": "",
    }

    while True:
        print("-------Parking Area---------")
        print("\t  ")

        for index, val in enumerate(parkingList):
            if val == None:
                print(f"Slot {index} is available.")
            else:
                print(
                    f"Slot {index}: {val['Car_user_name']} | {val['Car_Number']} | Owner: {val['Owner_user_name']}"
                )
        print("----------------------")
        print("\t   ")

        actionsList = {1: "Park", 2: "Remove", 3: "Details", 4: "exit", 5: 'Logout'}
        for num, action in actionsList.items():
            print(action, ":", num)
        print("----------------------")
        print("\t   ")

        task_Num = int(
            input(
                "Enter '1' to park a car, '2' to remove a car,'3' to show parking area details, or '4' to exit: "
            )
        )
        if task_Num == 1:
            parkNum = int(input("Enter slot:"))
            for index, val in enumerate(parkingList):
                if val == None and index == parkNum:
                    carDetail["Car_user_name"] = input("Enter Car user_name: ").strip()
                    carDetail["Car_Number"] = input("Enter Car Number: ").strip()
                    carDetail["Owner_user_name"] = input("Enter Owner user_name: ").strip()
                    parkingList[index] = carDetail.copy()
                    print(f"Car parked in slot {index}.")
                    print("------------------")
                    break
            else:
                print("No available slots or invalid slot number.")
            
            # car_park.carParking(parkingList)

        elif task_Num == 2:
            remove_vehical.remove_parking(parkingList)

        elif task_Num == 3:
            for detail in parkingList:
                if detail is not None:
                    print(
                        f"Car user_name: {detail['Car_user_name']}, Car Number: {detail['Car_Number']}, Owner user_name: {detail['Owner_user_name']}"
                    )
                else:
                    print("Empty Slot")
        elif task_Num == 4:
            break
        elif task_Num == 5:
            print("Logged out successfully!")
            return

        else:
            print("Invalid input. Please try again.")






# End of Parking Logic

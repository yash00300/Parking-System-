# # Parking System 
userList= []
loginList = []

def register():
    name = input("Enter your name: ").strip()
    password = input("Enter your password: ").strip()

    if len(password) == '':
      # validate password length
      print("Password must be exactly 2 characters long.")
      return
    

    

    # check if user already exists
    for user in userList:
        if user['name'] == name:
            print("User already exists!")
            return

    # add new user
    userList.append({
        'name': name,
        'password': password
    })
    print("Registration successful!")
    print('                                      ')


def logIn():
    # login
    userInput = {
        'name': input("Enter your name to login: ").strip(),
        'password':''
    }
    password = input("Enter your password to login: ").strip()
    if len(password)!='' :
      userInput['password']=password

    for user in userList:
        if userInput['name'] == user['name'] and userInput['password'] == user['password'] :
            if userInput not in loginList:
                loginList.append(userInput)
                print("Login successful!")
            print('                                        ')
            print()
            print('Current login user : ',loginList)
            print()

            return
    print("Login failed.")

# Parking Logic 

def parking():
  parkingList = [None]*3
  carDetail = {
    'Car_Name':'',
    'Car_Number':'',
    'Owner_name':'',
  }
  while True:
    print("-------Parking Area---------")

    for index , val in enumerate(parkingList):
      if val == None:
        print(f"Slot {index} is available.")
      else:
        print(f"Slot {index}: {val['Car_Name']} | {val['Car_Number']} | Owner: {val['Owner_name']}")
    print("----------------------")

    actionsList = {1:"Park", 2:"Remove", 3:"Details", 4:'exit' }
    for num, action in actionsList.items():
      print(action, ':', num)
    print("----------------------")


    taskNum = int(input("Enter '1' to park a car, '2' to remove a car,'3' to show parking area details, or '4' to exit: "))
    if taskNum == 1:
      parkNum = int(input('Enter slot:'))
      for index, val in enumerate(parkingList):
        if val == None and index == parkNum :
          carDetail['Car_Name'] = input("Enter Car Name: ").strip()
          carDetail['Car_Number'] = input("Enter Car Number: ").strip()
          carDetail['Owner_name'] = input("Enter Owner Name: ").strip()
          parkingList[index] = carDetail.copy()
          print(f"Car parked in slot {index}.")
          print('------------------')
          break
      else:
        print("No available slots or invalid slot number.")
    elif taskNum == 2:
      removeNum = int(input("Enter slot: "))
      if 0<= removeNum < len(parkingList) and parkingList[removeNum] is not None:
        parkingList[removeNum] = None
        print(f"Car removed from slot {removeNum}.")
      else:
        print("Invalid slot number or slot is already empty.")
    elif taskNum == 3:
      for detail in parkingList:
        if detail is not None:
          print(f"Car Name: {detail['Car_Name']}, Car Number: {detail['Car_Number']}, Owner Name: {detail['Owner_name']}")
        else:
          print("Empty Slot")
    elif taskNum == 4:
      break
    else:
      print("Invalid input. Please try again.")



# End of Parking Logic

def main():
  while True:
    print('Welcome to the car parking system!')
    print('1. Register')
    print('2. Exit')
    choice = input('Enter your choice : ')
    if choice == '1':
      
      register()
      logIn()
      for user in userList:
        for loginUser in loginList:
          if user == loginUser:
            parking()
      else:
        print('Please login to access the parking system.')
        logIn()
        for user in userList:
          for loginUser in loginList:
            if user == loginUser:
              parking()

    elif choice == '2':
      print('Exiting the system. Goodbye!')
      break
    else:
      print('Invalid choice. Please try again.')
main()







    
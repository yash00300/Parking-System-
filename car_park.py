import json

def carParking(parkingList):

    try:
        with open('parkingData/parkingList.json', 'r') as f:
            parkingList = json.load(f)
    except FileNotFoundError:
        parkingList = []

    carDetail = {
          "Car_user_name": "",
          "Car_Number": "",
          "Owner_user_name": "",
      }
  
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
    
    with open('parkingData/parkingList.json', 'w') as f:
        json.dump(parkingList, f, indent=4)



    


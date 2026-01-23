def remove_parking(parkingList):
    
    
    while True:
        remove_Num = int(input("Enter slot to remove: "))

        if 0 <= remove_Num < len(parkingList):

            # Check if slot is already empty
            if parkingList[remove_Num] is None:
                print("Slot is already empty!")
            else:
                parkingList[remove_Num] = None
                print("Car removed successfully!")

        else:
            print("Invalid Slot Number!")

        choice = input("Do you want to continue removing? (yes/no): ").lower()
        if choice != "yes":
            break

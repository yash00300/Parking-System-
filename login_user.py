import parking


def login_user():
    is_logged_in = False
    for user in parking.userList:
        for loginUser in parking.loginList:
            if user["name"] == loginUser["name"]:
                is_logged_in = True
                parking.parking()
                break
        if is_logged_in:
            break

    if not is_logged_in:
        print("Please login to access the parking system.")

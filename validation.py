import parking
import pwinput

# userList= [{'name': 'yash', 'password': 'yAsh123@'}]
def validate_password():
    while True:

        special = ["!", "@", "#", "$", "%", "^", "&", "*"]
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        password = pwinput.pwinput(prompt="Enter your password: ", mask="*").strip()

        has_special = False
        has_number = False
        has_len = False
        has_upper = False

        if len(password) >= 8:
            has_len = True

        for ch in password:
            if ch in special:
                has_special = True
            if ch in num:
                has_number = True
            if ch.isupper():
                has_upper = True

        if has_special and has_number and has_upper and has_len:
            print("Valid Password")
            return password
        else:
            print("Invalid Password")
            print(
                "Password must contain at least one special character, one number and one capital letter ."
            )
            print("Please try again.")


def forget_passowrd():

    for user in parking.userList:
        name = input("Enter your name: ").strip()
        if user["name"] == name:
            new_password = validate_password()
            user["password"] = new_password
            print("Password reset successful!")
            return

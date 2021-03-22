class InvalidPasswordException(Exception):
    def __init__(self):
        print("Invalid Password")

try:
    pd=input("Enter your password: ")
    if len(pd)>8:
        print("Password Accepted")
    else:
        raise InvalidPasswordException()
except InvalidPasswordException :
    print("Password must be 8 characters long")
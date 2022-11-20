import random
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

username = "samkillagane"
password = "123samyona"

inputuser = input('Enter username: ')
inputpass = input('Enter password: ')

if not (username == inputuser and password == inputpass):
    print('Invalid username or password')
    exit()


def containsnumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False


pass1 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '+',
    '"', '/'
]

passwordfor = input('Enter what is the password for: ')
passwordcreator = input('Enter the password creator: ')

password = ""
passwordRange = int(input("Enter the number of characters for the password:"))

while containsnumber(password) is False and len(password) < passwordRange:
    for x in range(passwordRange):
        password = password + random.choices(pass1)[0]

print("New password is : ", password, " and it is ", len(password), " characters ", dt_string)

try:
    file = open("C:\\Users\Samuel Killagane\OneDrive\password.txt", "a")
    toFile = "\nPassword for" + passwordfor + "New password is : " + password + " create at time " + dt_string
    file.write(toFile)
    file.close()
except:
    print("Error")

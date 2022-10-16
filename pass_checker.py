password = input("Enter password : ")

upper_status = False
lower_status = False
num_status = False

if 6 <= len(password) <= 20 :
    for char in password :
        if ord('A') <= ord(char) <= ord('Z'):
            upper_status = True
        elif ord('a') <= ord(char) <= ord('z'):
            lower_status = True
        elif ord('0') <= ord(char) <= ord('9'):
            num_status = True

if upper_status and lower_status and num_status :
    print("Password is valid")
else:
    print("Password is not valid")
            
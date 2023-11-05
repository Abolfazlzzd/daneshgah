#password_correct_incorrect

password1 = input("Enter current password : ")
password2 = input("Enter password you set : ")

while password1 != password2 :
    print("Passwords do not match.")
    break

password1 = input("Enter current password : ")
password2 = input("Enter password you set : ")

while password1 == password2:
    print("Passwords match!")
    break








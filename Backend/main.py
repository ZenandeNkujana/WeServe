# =================================
# Save user's information
# =================================
#Saving the user's information so we can know who we are dealing with
name = input("Enter your name: ").strip().lower()
surname = input("Enter your surname: ").strip().lower()
email = input("Enter your email adress: ").strip().lower()
password = input("Create a password containing at least 8 characters, including uppercase and lowercase letters, a number, and a special character (e.g. @, #, $): ").strip()
address =  input("Please enter ypur address: ").strip().lower()
gender = input("Enter your gender(Male or Female): ").strip().lower()

# Validate user's information
#name
if name == "":
    print("Enter your name: ")
elif not name.isalpha():
    print("Enter a valid name")
else:
    print(name)

#surname
if surname == "":
    print("Enter ayour name: ")#not final
elif not surname.isalpha():
    print("Please Enter a valid name")
else:
    print(surname)


#email
if email == "":
    print("Enter your email address")
elif "@" not in email:
    print("Enter a valid email address")#not final
else:
    print(email)
    
#password
if len(password) < 8:
    print("Enter a least 8 characters")
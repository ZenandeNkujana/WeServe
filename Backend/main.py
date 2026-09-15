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
def validate_password(password):

    # Keeping track of the required 
    has_lowercase = False
    has_uppercase = False
    has_number = False
    has_special = False

    # Check each character in the password
    for character in password:

        if character.islower():
            has_lowercase = True

        elif character.isupper():
            has_uppercase = True

        elif character.isdigit():
            has_number = True

        else:
            has_special = True

    # Validate the password
    if len(password) < 8:
        print("Enter at least 8 characters")

    elif not has_lowercase:
        print("Password must contain a lowercase letter")

    elif not has_uppercase:
        print("Password must contain an uppercase letter")

    elif not has_number:
        print("Password must contain a number")

    elif not has_special:
        print("Password must contain a special character")

    else:
        print("Password is valid")


validate_password(password)

#adress
if address == "":
    print("Please enter your address")
else:
    print(address)
    
#gender
if gender == "":
    print("Please enter your gender")
elif gender != "male" and gender != "female":
    print("Please enter Male or Female")
else:
    print(gender)
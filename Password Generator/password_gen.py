import random
import string

def gen_password(minimum_length, numbers=True, special_characters=True):
    letter = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letter
    if numbers:
        characters += digits
    if special_characters:
        characters += specials
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < minimum_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

minimum_length = int(input("Enter the minimum Length: "))
has_number = input("Do you want to have numbers (y/n) ? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n) ? ").lower() == "y"
pwd = gen_password(minimum_length, has_number, has_special)
print("The Generated Password is : ", pwd)
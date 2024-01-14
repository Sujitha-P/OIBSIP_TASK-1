import string
import random

def generate_password(len, upperc, lowerc, digs, spchars):
    character_set = ""
    
    while len <= 0:
        len = int(input("Enter password length: "))
        if len <= 0:
            print("Password length must be greater than 0.")
    
    upperc = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowerc = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digs = input("Include digits? (y/n): ").lower() == 'y'
    spchars = input("Include special characters? (y/n): ").lower() == 'y'
    
    if not (upperc or lowerc or digs or spchars):
        print("At least one character type must be selected.")
        return None
    
    character_set += string.ascii_uppercase if upperc else ""
    character_set += string.ascii_lowercase if lowerc else ""
    character_set += string.digits if digs else ""
    character_set += string.punctuation if spchars else ""
    
    if not character_set:
        print("At least one character type must be selected.")
        return None
    
    password = ''.join(random.choice(character_set) for _ in range(len))
    return password

if __name__ == "__main__":
    len, upperc, lowerc, digs, spchars = 0, False, False, False, False
    
    password = generate_password(len, upperc, lowerc, digs, spchars)
    
    if password:
        print(f"\nGenerated Password: {password}")

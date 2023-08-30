import random
import string

def generate_random_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if length < 4:
        print("Password length must be at least 4 characters.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter password length: "))
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    include_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_random_password(password_length, include_digits, include_special_chars)
    print("Generated Password:", password)

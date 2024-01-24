import random
import string

def generate_password(length):
    # Define characters for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password using specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# User input for password length
try:
    length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Check if the length is non-negative
if length <= 0:
    print("Password length should be a positive integer.")
else:
    # Generate and display the password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

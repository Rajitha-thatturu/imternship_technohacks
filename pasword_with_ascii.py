import string
import random

def generate_password(length):
    # Define the characters that will be used to generate the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using the random.choice function
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Test the function
length = int(input("Enter the length of the password: "))
print("Generated Password: ", generate_password(length))

import random
import string

# Function to generate password
def generate_password(length):

    # Combine all characters
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    # Generate random password
    password = ''.join(random.choice(characters) for i in range(length))

    return password


# User input
length = int(input("Enter password length: "))

# Generate and print password
password = generate_password(length)

print("\nGenerated Password:")
print(password)
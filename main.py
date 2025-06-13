import random
import string

def generate_password(length=16):
    # Define character pools
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure a strong password includes at least one of each character type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - 4)
    
    # Shuffle to avoid predictable sequences
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    new_password = generate_password()
    print("Generated Password:", new_password)

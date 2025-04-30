# password_manager.py
import json
import random
import string

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_password(service, password):
    """Save password to a JSON file."""
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[service] = password
    with open('passwords.json', 'w') as file:
        json.dump(data, file, indent=4)

def get_password(service):
    """Retrieve password for a service."""
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
            return data.get(service, "Service not found!")
    except FileNotFoundError:
        return "No passwords saved yet!"

def password_manager():
    """Main function for password manager."""
    print("Password Manager")
    print("1. Generate and save password")
    print("2. Retrieve password")

    while True:
        choice = input("Enter choice (1 or 2): ")
        if choice == '1':
            service = input("Enter service name (e.g., Gmail): ")
            length = int(input("Enter password length: "))
            password = generate_password(length)
            save_password(service, password)
            print(f"Generated password for {service}: {password}")
        elif choice == '2':
            service = input("Enter service name: ")
            print(f"Password: {get_password(service)}")
        else:
            print("Invalid choice! Please enter 1 or 2.")
            continue

        again = input("Continue? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    password_manager()

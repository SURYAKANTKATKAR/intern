import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

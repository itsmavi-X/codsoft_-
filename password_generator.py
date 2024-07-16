import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        raise ValueError("At least one character type must be selected")

    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if len(character_pool) == 0:
        raise ValueError("No characters available to generate password")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Advanced Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
            print(f"Generated password: {password}")
        
        except ValueError as e:
            print(e)

        play_again = input("Do you want to generate another password? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for using the Advanced Password Generator! Goodbye!")
            break

if __name__ == "__main__":
    main()

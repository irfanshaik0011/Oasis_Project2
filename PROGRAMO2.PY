import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be selected.")

    return ''.join(random.choice(character_set) for _ in range(length))

def main():
    try:
        length = int(input("Enter the password length: "))
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        if length <= 0:
            raise ValueError("Password length must be a positive integer.")

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if True:
    main()
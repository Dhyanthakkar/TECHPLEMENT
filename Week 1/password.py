import argparse
import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    if not (include_uppercase or include_lowercase or include_digits or include_special):
        raise ValueError("At least one character type must be selected")

    character_pool = ""
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    if len(character_pool) == 0:
        raise ValueError("Character pool is empty. Please select at least one character type.")

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main(args=None):
    parser = argparse.ArgumentParser(description='Generate a random password with specified criteria.')
    parser.add_argument('length', type=int, help='Length of the password')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-l', '--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--special', action='store_true', help='Include special characters')

    if args is None:
        # For testing purposes, define default arguments here
        args = ['12', '-u', '-l', '-d', '-s']  # Example arguments

    args = parser.parse_args(args)

    try:
        password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

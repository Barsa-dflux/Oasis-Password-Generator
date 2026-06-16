import random
import string

print("=" * 50)
print("      SIMPLE PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            continue

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure password contains all character types
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols)
        ]

        all_characters = lower + upper + digits + symbols

        for i in range(length - 4):
            password.append(random.choice(all_characters))

        random.shuffle(password)

        final_password = "".join(password)

        print("\nGenerated Password:", final_password)

        strength = ""
        if length <= 6:
            strength = "Weak"
        elif length <= 10:
            strength = "Medium"
        else:
            strength = "Strong"

        print("Password Strength:", strength)

        choice = input("\nGenerate another password? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")
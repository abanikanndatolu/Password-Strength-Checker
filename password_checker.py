import re

# Load common weak passwords
def load_common_passwords():
    with open("common_passwords.txt", "r") as file:
        return set(file.read().splitlines())

COMMON_PASSWORDS = load_common_passwords()

# Function to check password strength
def check_password_strength(password):
    strength_score = 0

    # Check password length
    if len(password) >= 12:
        strength_score += 2
    elif len(password) >= 8:
        strength_score += 1

    # Check character variety
    if re.search(r"[A-Z]", password):
        strength_score += 1
    if re.search(r"[a-z]", password):
        strength_score += 1
    if re.search(r"\d", password):
        strength_score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1

    # Check if password is common
    if password in COMMON_PASSWORDS:
        return "Weak: This password is commonly used and easily guessed."

    # Evaluate strength based on score
    if strength_score >= 6:
        return "Strong: Your password is well-secured!"
    elif strength_score >= 4:
        return "Moderate: Consider adding more complexity."
    else:
        return "Weak: Use a longer, more complex password."

# Example usage
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    print(check_password_strength(user_password))

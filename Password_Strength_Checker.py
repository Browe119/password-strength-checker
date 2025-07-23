def password_strength_checker(password):
    """
    Purpose: Check the strength of a password based on different variables.

    Parameter(s):
        password (str): The password to be checked.

    Return: A string indicating the strength of the password.
    """
    if len(password) < 8:
        return "Please enter a password with at least 8 characters."
    # Password strength score
    strength_score = 0
    # Password Length Checker
    if len(password) <= 8:
        strength_score += 0
    elif 8 < len(password) <= 12:
        strength_score += 1
    elif len(password) > 12:
        strength_score += 2
    # Password First Character Checker
    if password[0].islower():
        strength_score += 0
    elif password[0].isupper():
        strength_score += 1
    # Password Middle Character Checker
    middle_chars = password[1:-1]

    uppercase_count = sum(1 for char in middle_chars if char.isupper())

    if uppercase_count == 0:
        strength_score += 0
    elif uppercase_count <= 2:
        strength_score += 1
    elif uppercase_count >= 3:
        strength_score += 2

    # Password symbol Character Checker
    symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    symbol_count = sum(1 for char in password if char in symbols)
    if symbol_count == 0:
        strength_score += 0
    elif symbol_count <= 2:
        strength_score += 1
    elif symbol_count >= 3:
        strength_score += 2
    # Password Digit Character Checker
    digits = "0123456789"
    digit_count = sum(1 for char in password if char in digits)
    if digit_count == 0:
        strength_score += 0
    elif digit_count <= 2:
        strength_score += 1
    elif digit_count >= 3:
        strength_score += 2

    # Final Password Strength Evaluation
    if strength_score <= 3:
        return "Password needs work, consider adding more characters, uppercase letters, symbols, or digits."
    elif 4 <= strength_score <= 6:
        return "Moderate password"
    else:
        return "Excellent password"


if __name__ == "__main__":
    password = input("Enter a password to check: ")
    result = password_strength_checker(password)
    print("Password strength:", result)

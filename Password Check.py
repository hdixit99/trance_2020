import re

def is_valid_password(password):
    """
    Checks if the given password meets the minimum requirements.
    :param password: str, the password to check
    :return: bool, True if valid, False otherwise
    """
    if len(password) < 12:
        return False
    return True

def validate_password(password):
    """
    Validates the password for complexity requirements.
    :param password: str, the password to validate
    :return: bool, True if valid, False otherwise
    """
    if not re.search(r'[A-Z]', password):  # At least one uppercase letter
        return False
    if not re.search(r'[a-z]', password):  # At least one lowercase letter
        return False
    if not re.search(r'[0-9]', password):  # At least one digit
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # At least one special character
        return False
    return True

# Example usage
if __name__ == "__main__":
    test_password = input("Enter a password to check: ")
    if is_valid_password(test_password) and validate_password(test_password):
        print("Password is valid.")
    else:
        print("Password must be at least 12 characters long and include uppercase, lowercase, digits, and special characters.")123
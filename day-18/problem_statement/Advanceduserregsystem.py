import re

# Custom Exceptions
class InvalidUsernameException(Exception):
    pass

class InvalidPasswordException(Exception):
    pass

class InvalidEmailException(Exception):
    pass

class DuplicateUsernameException(Exception):
    pass

class SystemErrorException(Exception):
    pass

# Base User Class
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def validate_username(self):
        if not re.match(r'^[a-zA-Z0-9]{5,15}$', self.username):
            raise InvalidUsernameException("Username must be alphanumeric and between 5 to 15 characters.")

    def validate_password(self):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$', self.password):
            raise InvalidPasswordException("Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and be between 8 to 20 characters.")

    def validate_email(self):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
            raise InvalidEmailException("Email must follow standard email format (e.g., example@domain.com).")

# Registration System Class
class RegistrationSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, user):
        try:
            user.validate_username()
            user.validate_password()
            user.validate_email()

            if user.username in self.users:
                raise DuplicateUsernameException("Username already exists.")

            self.users[user.username] = user
            print(f"User {user.username} registered successfully.")

        except (InvalidUsernameException, InvalidPasswordException, InvalidEmailException) as e:
            print(f"Registration failed: {e}")
        except DuplicateUsernameException as e:
            print(f"Registration failed: {e}")
        except Exception as e:
            print(f"System error: {e}")

# Example Usage
try:
    user1 = User("user1668", "Password1!", "user1668@example.com")
    user2 = User("user16344", "Password1!", "user455@example.com")  # Duplicate username

    system = RegistrationSystem()
    system.register_user(user1)
    system.register_user(user2)
except SystemErrorException as e:
    print(f"System error: {e}")

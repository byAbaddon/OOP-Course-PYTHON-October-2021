class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, string):
        if 5 <= len(string) <= 15:
            self.__username = string
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_length):
        if len(password_length) < 8 or not len([x for x in password_length if x.isdigit()])\
                or not len([x for x in password_length if x.isupper()]):
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = password_length

    def __str__(self):
        return f'You have a profile with username: "{self.username}"' \
               f' and password: {"*" * len(self.password)}'




# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
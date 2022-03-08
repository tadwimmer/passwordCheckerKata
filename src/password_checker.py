

class PasswordChecker:

    def check_password(self, password):
        if len(password) < 8:
            return 'Password must be 8 characters long'
        else:
            return ''
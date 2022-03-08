

class PasswordChecker:

    @staticmethod
    def check_password(password):
        start = 'Password must'
        message = PasswordChecker.check_length(password)
        lower = PasswordChecker.check_lower_case(password)
        upper = PasswordChecker.check_uppercase(password)
        if len(message) > 0 and len(lower) > 0:
            message = message + ' and' + lower
        elif len(message) == 0:
            message = lower
        if len(message) == 0 and len(upper) > 0:
            return start + upper
        if len(message) > 0:
            return start + message

    @staticmethod
    def check_length(password):
        if len(password) < 8:
            return ' be 8 characters long'
        else:
            return ''

    @staticmethod
    def check_lower_case(password):
        message = ' contain at least one lowercase letter'
        for c in password:
            if c.islower():
                return ''
        return message

    @staticmethod
    def check_uppercase(password):
        message = ' contain at least one uppercase letter'
        for c in password:
            if c.isupper():
                return ''
        return message
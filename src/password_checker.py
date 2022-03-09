
class PasswordChecker:

    @staticmethod
    def check_password(password):
        message_list = list()
        length = PasswordChecker.check_length(password)
        lower = PasswordChecker.check_lower_case(password)
        upper = PasswordChecker.check_uppercase(password)
        numeral = PasswordChecker.check_numeral(password)
        symbol = PasswordChecker.check_symbol(password)
        if len(length) > 0:
            message_list.append(length)
        if len(lower) > 0:
            message_list.append(lower)
        if len(upper) > 0:
            message_list.append(upper)
        if len(numeral) > 0:
            message_list.append(numeral)
        if len(symbol) > 0:
            message_list.append(symbol)
        return PasswordChecker.build_message(message_list)

    @staticmethod
    def build_message(message_list):
        output = ''
        count = len(message_list)
        if count > 0:
            output = 'Password must'
            for i in range(0, count):
                output += message_list[i]
                if i < count - 2:
                    output += ', '
                elif i < count - 1:
                    output += ', and'
        return output if len(output) > 0 else None

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

    @staticmethod
    def check_numeral(password):
        for c in password:
            if c.isdigit():
                return ''
        return ' contain at least one numeral'

    @staticmethod
    def check_symbol(password):
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '?']
        for c in password:
            if c in symbols:
                return ''
        return " contain a symbol in '!@#$%^&*()+?'"

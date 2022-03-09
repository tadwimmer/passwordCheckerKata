from src.password_checker import PasswordChecker


class TestPasswordChecker:
    def test_check_password_8_characters_fail(self):
        pc = PasswordChecker
        assert pc.check_password('pA4$') == 'Password must be 8 characters long'

    def test_check_password_8_characters_pass(self):
        pc = PasswordChecker
        assert pc.check_password('asdf8hjk') != 'Password must be 8 characters long'

    def test_check_password_lower_case_fail(self):
        pc = PasswordChecker
        assert pc.check_password("ABCDEF7^") == \
               'Password must contain at least one lowercase letter'

    def test_check_password_all_pass(self):
        pc = PasswordChecker
        assert pc.check_password('Phyd3@ux') is None

    def test_check_password_short_upper(self):
        pc = PasswordChecker
        assert pc.check_password("ABC%E9G") == \
               'Password must be 8 characters long, and contain at least one lowercase letter'

    def test_check_password_uppercase_fail(self):
        pc = PasswordChecker
        assert pc.check_password('1dgjlhf!') == \
               'Password must contain at least one uppercase letter'

    def test_contains_number(self):
        pc = PasswordChecker
        assert pc.check_password('P@$$word') == \
               'Password must contain at least one numeral'

    def test_contains_symbol(self):
        pc = PasswordChecker
        assert pc.check_password('Passw0rd') == \
               "Password must contain a symbol in '!@#$%^&*()+?'"

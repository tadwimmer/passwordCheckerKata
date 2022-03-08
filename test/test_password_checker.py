from src.password_checker import PasswordChecker


class TestPasswordChecker:
    def test_check_password_8_characters_fail(self):
        pc = PasswordChecker
        assert pc.check_password('p') == 'Password must be 8 characters long'

    def test_check_password_8_characters_pass(self):
        pc = PasswordChecker
        assert pc.check_password('asdfghjk') != 'Password must be 8 characters long'

    def test_check_password_lower_case_fail(self):
        pc = PasswordChecker
        assert pc.check_password("ABCDEFGH") == 'Password must contain at least one lowercase letter'

    def test_check_password_all_pass(self):
        pc = PasswordChecker
        assert pc.check_password('Phyd3@ux') == None

    def test_check_password_short_upper(self):
        pc = PasswordChecker
        assert pc.check_password("ABCDEFG") == 'Password must be 8 characters long and contain at least one lowercase letter'

    def test_check_password_uppercase_fail(self):
        pc = PasswordChecker
        assert pc.check_password('adgjlhfs') == 'Password must contain at least one uppercase letter'
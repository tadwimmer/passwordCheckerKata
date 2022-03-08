from src.password_checker import PasswordChecker


class TestPasswordChecker:
    def test_check_password_8_characters_fail(self):
        pc = PasswordChecker
        assert pc.check_password(pc, 'P') == 'Password must be 8 characters long'

    def test_check_password_8_characters_pass(self):
        pc = PasswordChecker
        assert pc.check_password(pc, 'asdfghjk') != 'Password must be 8 characters long'
import unittest
import pytest
import string
from zad1.random_user import RandomUser


class TestGetRandomUserPassword(unittest.TestCase):

    def test_get_lower(self):
        try:
            result = self.user.get_random_user_password(['lower'])['results'][0]['login']['password']
            self.assertEqual(result.islower(), True)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_upper(self):
        try:
            result = self.user.get_random_user_password(['upper'])['results'][0]['login']['password']
            self.assertEqual(result.isupper(), True)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_special(self):
        try:
            special = string.punctuation + string.whitespace
            result = self.user.get_random_user_password(['special'])['results'][0]['login']['password']
            self.assertEqual(all(i in special for i in result), True)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_number(self):
        try:
            result = self.user.get_random_user_password(['number'])['results'][0]['login']['password']
            self.assertEqual(result.isdigit(), True)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_multiple_options(self):
        try:
            result = self.user.get_random_user_password(['special', 'lower', 'upper'])['results'][0]['login']['password']
            self.assertEqual(any(i.isnumeric() for i in result), False)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_default_length(self):
        try:
            result = self.user.get_random_user_password(['special', 'lower', 'upper', 'number'])['results'][0]['login']['password']
            self.assertEqual(8 <= len(result) <= 64, True)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_only_max_length(self):
        try:
            result = self.user.get_random_user_password(['special', 'lower', 'upper', 'number'], 15)['results'][0]['login']['password']
            self.assertEqual(8 <= len(result) <= 15, True)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_different_length(self):
        try:
            result = self.user.get_random_user_password(['special', 'lower', 'upper', 'number'], 35, 30)['results'][0]['login']['password']
            self.assertEqual(30 <= len(result) <= 35, True)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_wrong_length(self):
        with pytest.raises(ValueError, match=r'Length must be between 1 and 64!'):
            self.user.get_random_user_password(['special', 'lower', 'upper', 'number'], 85, 70)

    def test_get_no_options(self):
        with pytest.raises(ValueError, match=r'You must provide at least one option!'):
            self.user.get_random_user_password([])

    def test_get_option_doesnt_exists(self):
        with pytest.raises(ValueError, match=r'The specified option does not exist!'):
            self.user.get_random_user_password(['lowercase', 'uppercase'])

    def test_get_length_not_int(self):
        with pytest.raises(TypeError, match=r'Length must be of int type!'):
            self.user.get_random_user_password(['lower', 'upper'], '18', {'num': 15})

    def setUp(self):
        self.user = RandomUser()

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

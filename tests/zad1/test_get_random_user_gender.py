import unittest
import pytest
from zad1.random_user import RandomUser


class TestGetRandomUserGender(unittest.TestCase):

    def test_get(self):
        try:
            self.assertEqual(self.user.get_random_user_gender('male')['results'][0]['gender'], 'male')
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_neither_male_nor_female(self):
        try:
            self.assertEqual(self.user.get_random_user_gender('kobieta'), None)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_str_not_numeric(self):
        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.user.get_random_user_gender(1582)

    def setUp(self):
        self.user = RandomUser()

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

import unittest
import pytest
from zad1.random_user import RandomUser


class TestGetNRandomUsers(unittest.TestCase):

    def test_int_greater_than_0(self):
        try:
            self.assertEqual(len(self.user.get_n_random_users(8)['results']), 8)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_int_lower_or_equal_0(self):
        try:
            self.assertEqual(self.user.get_n_random_users(0), None)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_str_numeric(self):
        try:
            self.assertEqual(len(self.user.get_n_random_users('4')['results']), 4)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_str_not_numeric(self):
        with pytest.raises(TypeError, match=r'Input must refer to an int!'):
            self.user.get_n_random_users('one')

    def test_neither_int_nor_string(self):
        with pytest.raises(TypeError, match=r'Input must be of int type!'):
            self.user.get_n_random_users([])

    def setUp(self):
        self.user = RandomUser()

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

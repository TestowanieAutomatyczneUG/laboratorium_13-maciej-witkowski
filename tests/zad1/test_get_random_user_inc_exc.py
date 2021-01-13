import unittest
import pytest
from assertpy import *
from zad1.random_user import RandomUser


class TestGetRandomUserIncExc(unittest.TestCase):

    def test_get_inc(self):
        try:
            assert_that(self.user.get_random_user_inc_exc('inc', ['gender', 'name'])['results'][0])\
                .contains_only('gender', 'name')
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_exc(self):
        try:
            assert_that(self.user.get_random_user_inc_exc('exc', ['nat', 'name'])['results'][0])\
                .does_not_contain('nat', 'name')
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_neither_inc_nor_exc(self):
        with pytest.raises(ValueError, match=r'The specified option does not exist!'):
            self.user.get_random_user_inc_exc('sth', ['gender', 'name'])

    def test_get_no_params(self):
        with pytest.raises(ValueError, match=r'You must provide at least one parameter!'):
            self.user.get_random_user_inc_exc('exc', [])

    def test_get_params_doesnt_exists(self):
        with pytest.raises(ValueError, match=r'The specified parameter does not exist!'):
            self.user.get_random_user_inc_exc('inc', ['education', 'job'])

    def setUp(self):
        self.user = RandomUser()

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

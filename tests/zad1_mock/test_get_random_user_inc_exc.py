import unittest
import pytest
from unittest.mock import Mock
from assertpy import *
from zad1.random_user import RandomUser


class TestGetRandomUserIncExc(unittest.TestCase):

    def test_get_inc(self):
        self.user.get_random_user_inc_exc = Mock()
        self.user.get_random_user_inc_exc.return_value = {'results': [{
            'gender': 'female',
            'name': {'title': 'Mrs', 'first': 'Tonya', 'last': 'Ford'}
        }]}

        assert_that(self.user.get_random_user_inc_exc('inc', ['gender', 'name'])['results'][0])\
            .contains_only('gender', 'name')

    def test_get_exc(self):
        self.user.get_random_user_inc_exc = Mock()
        self.user.get_random_user_inc_exc.return_value = {'results': [{
            'gender': 'male',
            'name': {'title': 'Mr', 'first': 'Oliver', 'last': 'Chow'},
            'email': 'oliver.chow@example.com',
            'dob': {'date': '1967-12-25T14:19:06.010Z', 'age': 53},
            'registered': {'date': '2011-08-31T19:00:02.602Z', 'age': 9},
            'phone': '881-206-8689',
            'cell': '897-634-8230',
            'id': {'name': '', 'value': None},
            'nat': 'CA'
        }]}

        assert_that(self.user.get_random_user_inc_exc('exc', ['location', 'login', 'picture'])['results'][0])\
            .does_not_contain('location', 'login', 'picture')

    def test_get_neither_inc_nor_exc(self):
        self.user.get_random_user_inc_exc = Mock()
        self.user.get_random_user_inc_exc.side_effect = ValueError('The specified option does not exist!')

        with pytest.raises(ValueError, match=r'The specified option does not exist!'):
            self.user.get_random_user_inc_exc('sth', ['gender', 'name'])

    def test_get_no_params(self):
        self.user.get_random_user_inc_exc = Mock()
        self.user.get_random_user_inc_exc.side_effect = ValueError('You must provide at least one parameter!')

        with pytest.raises(ValueError, match=r'You must provide at least one parameter!'):
            self.user.get_random_user_inc_exc('exc', [])

    def test_get_params_doesnt_exists(self):
        self.user.get_random_user_inc_exc = Mock()
        self.user.get_random_user_inc_exc.side_effect = ValueError('The specified parameter does not exist!')

        with pytest.raises(ValueError, match=r'The specified parameter does not exist!'):
            self.user.get_random_user_inc_exc('inc', ['education', 'job'])

    def setUp(self):
        self.user = RandomUser()

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

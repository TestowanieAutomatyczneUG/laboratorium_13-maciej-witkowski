import unittest
import pytest
from unittest.mock import Mock
from zad1.random_user import RandomUser


class TestGetNRandomUsersMock(unittest.TestCase):

    def test_int_greater_than_0(self):
        self.user.get_n_random_users = Mock()
        self.user.get_n_random_users.return_value = self.result

        self.assertEqual(len(self.user.get_n_random_users(2)['results']), 2)

    def test_int_lower_or_equal_0(self):
        self.user.get_n_random_users = Mock()
        self.user.get_n_random_users.return_value = None

        self.assertEqual(self.user.get_n_random_users(0), None)

    def test_str_numeric(self):
        self.user.get_n_random_users = Mock()
        self.user.get_n_random_users.return_value = self.result

        self.assertEqual(len(self.user.get_n_random_users('2')['results']), 2)

    def test_str_not_numeric(self):
        self.user.get_n_random_users = Mock()
        self.user.get_n_random_users.side_effect = TypeError('Input must refer to an int!')

        with pytest.raises(TypeError, match=r'Input must refer to an int!'):
            self.user.get_n_random_users('one')

    def test_neither_int_nor_string(self):
        self.user.get_n_random_users = Mock()
        self.user.get_n_random_users.side_effect = TypeError('Input must be of int type!')

        with pytest.raises(TypeError, match=r'Input must be of int type!'):
            self.user.get_n_random_users([])

    def setUp(self):
        self.user = RandomUser()
        self.result = {'results': [
            {
                'gender': 'female',
                'name': {'title': 'Mrs', 'first': 'Inès', 'last': 'Simon'},
                'location': {
                    'street': {'number': 333, 'name': 'Rue du Dauphiné'},
                    'city': 'Nancy',
                    'state': 'Oise',
                    'country': 'France',
                    'postcode': 50461,
                    'coordinates': {'latitude': '-2.9443', 'longitude': '143.3300'},
                    'timezone': {'offset': '-8:00', 'description': 'Pacific Time (US & Canada)'}
                },
                'email': 'ines.simon@example.com',
                'login': {
                    'uuid': '7f820c9b-7d89-4a86-9565-2d4a010a79b5',
                    'username': 'goldencat854',
                    'password': 'harry',
                    'salt': '1IKPHygx',
                    'md5': '3642432819b709aa00c5aed190d81e86',
                    'sha1': 'a397a7cea0dc833f3f883ef4a4eb43b50f56a02d',
                    'sha256': '395bf9d879d5a6b1d8b74804e75138f8074b4a019f93af3528ebd7debeaa1a94'
                },
                'dob': {'date': '1958-11-06T04:40:53.387Z', 'age': 62},
                'registered': {'date': '2013-12-02T17:34:47.028Z', 'age': 7},
                'phone': '01-06-45-73-99',
                'cell': '06-71-24-00-15',
                'id': {'name': 'INSEE', 'value': '2NNaN46924107 15'},
                'picture': {
                    'large': 'https://randomuser.me/api/portraits/women/4.jpg',
                    'medium': 'https://randomuser.me/api/portraits/med/women/4.jpg',
                    'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/4.jpg'
                },
                'nat': 'FR'
            },
            {
                'gender': 'female',
                'name': {'title': 'Mrs', 'first': 'Rejanete', 'last': 'da Rocha'},
                'location': {
                    'street': {'number': 3201, 'name': 'Rua Santa Rita '},
                    'city': 'Umuarama',
                    'state': 'Ceará',
                    'country': 'Brazil',
                    'postcode': 84083,
                    'coordinates': {'latitude': '78.6078', 'longitude': '155.1672'},
                    'timezone': {'offset': '-9:00', 'description': 'Alaska'}
                },
                'email': 'rejanete.darocha@example.com',
                'login': {
                    'uuid': 'b2370019-6af4-4720-b2b1-ac5725af3dfb',
                    'username': 'blackdog971',
                    'password': 'kume',
                    'salt': '0ROcGYRd',
                    'md5': '66449014b41ee8dc2df03e7fd4e7fded',
                    'sha1': 'e38e27bd51bd9799c363b604f8370f142a7a3b74',
                    'sha256': 'f5c8a25b4f9f81984567a71cc9a48df24a9ac88eaa2157b0a603e6f9ac8722d8'
                },
                'dob': {'date': '1951-08-07T16:38:35.866Z', 'age': 69},
                'registered': {'date': '2014-08-01T08:49:46.602Z', 'age': 6},
                'phone': '(22) 5418-2501',
                'cell': '(05) 0597-9012',
                'id': {'name': '', 'value': None},
                'picture': {
                    'large': 'https://randomuser.me/api/portraits/women/73.jpg',
                    'medium': 'https://randomuser.me/api/portraits/med/women/73.jpg',
                    'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/73.jpg'
                },
                'nat': 'BR'
            }
        ]}

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

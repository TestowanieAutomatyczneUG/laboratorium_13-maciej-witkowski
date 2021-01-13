import unittest
import pytest
from unittest.mock import Mock
from zad1.random_user import RandomUser


class TestGetRandomUserGenderMock(unittest.TestCase):

    def test_get(self):
        self.user.get_random_user_gender = Mock()
        self.user.get_random_user_gender.return_value = self.result

        self.assertEqual(self.user.get_random_user_gender('male')['results'][0]['gender'], 'male')

    def test_neither_male_nor_female(self):
        self.user.get_random_user_gender = Mock()
        self.user.get_random_user_gender.return_value = None

        self.assertEqual(self.user.get_random_user_gender('kobieta'), None)

    def test_str_not_numeric(self):
        self.user.get_random_user_gender = Mock()
        self.user.get_random_user_gender.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.user.get_random_user_gender(1582)

    def setUp(self):
        self.user = RandomUser()
        self.result = {
            'results': [
                {
                    'gender': 'male',
                    'name': {'title': 'Mr', 'first': 'Torben', 'last': 'Baumgartner'},
                    'location': {
                        'street': {'number': 3307, 'name': 'Mittelweg'},
                        'city': 'Dillingen A.D. Donau',
                        'state': 'Niedersachsen',
                        'country': 'Germany',
                        'postcode': 12813,
                        'coordinates': {'latitude': '-46.5681', 'longitude': '-48.6634'},
                        'timezone': {'offset': '+11:00', 'description': 'Magadan, Solomon Islands, New Caledonia'}
                    },
                    'email': 'torben.baumgartner@example.com',
                    'login': {
                        'uuid': 'e0f5a380-aaad-4f15-90d8-125606993fd8',
                        'username': 'ticklishleopard157',
                        'password': '66666',
                        'salt': 'PNP20hwt',
                        'md5': 'd1a5dcc414062c91cc4016dd1ad50225',
                        'sha1': 'a05a81ca0866f80d2d8bb34f5ec029a8ea51eb8e',
                        'sha256': 'aabd2f1790061c6401fb62bd57b2ef6d6e49a27047fabd10dd55f8fe56e6ddba'
                    },
                    'dob': {'date': '1953-10-24T22:52:51.055Z', 'age': 67},
                    'registered': {'date': '2008-08-03T06:06:01.146Z', 'age': 12},
                    'phone': '0035-6298576',
                    'cell': '0171-0668425',
                    'id': {'name': '', 'value': None},
                    'picture': {
                        'large': 'https://randomuser.me/api/portraits/men/43.jpg',
                        'medium': 'https://randomuser.me/api/portraits/med/men/43.jpg',
                        'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/43.jpg'
                    },
                    'nat': 'DE'
                }
            ]
        }

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

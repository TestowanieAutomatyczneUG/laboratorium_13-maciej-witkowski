import unittest
import pytest
import string
from unittest.mock import Mock
from zad1.random_user import RandomUser


class TestGetRandomUserPasswordMock(unittest.TestCase):

    def test_get_lower(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.return_value = self.result
        self.result['results'][0]['login']['password'] = 'utbndwiogkpzataypfemhvonnz'

        result = self.user.get_random_user_password(['lower'])['results'][0]['login']['password']
        self.assertEqual(result.islower(), True)

    def test_get_upper(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.return_value = self.result
        self.result['results'][0]['login']['password'] = 'JSZPATUORTJMXUEZLYVFDXIQ'

        result = self.user.get_random_user_password(['upper'])['results'][0]['login']['password']
        self.assertEqual(result.isupper(), True)

    def test_get_special(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.return_value = self.result
        self.result['results'][0]['login']['password'] = "&_]':.!>'\\>+#*':)&_*,=(@=~$`&|;>[>:&,+/"

        special = string.punctuation + string.whitespace
        result = self.user.get_random_user_password(['special'])['results'][0]['login']['password']
        self.assertEqual(all(i in special for i in result), True)

    def test_get_number(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.return_value = self.result
        self.result['results'][0]['login']['password'] = '944860403'

        result = self.user.get_random_user_password(['number'])['results'][0]['login']['password']
        self.assertEqual(result.isdigit(), True)

    def test_get_multiple_options(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.return_value = self.result
        self.result['results'][0]['login']['password'] = 'dZfh:wcc=#'

        result = self.user.get_random_user_password(['special', 'lower', 'upper'])['results'][0]['login']['password']
        self.assertEqual(any(i.isnumeric() for i in result), False)

    def test_get_default_length(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.return_value = self.result
        self.result['results'][0]['login']['password'] = ";4`1(QlDVY(=RLz{W=('6>oXrS++QlF|vFLtr'4m"

        result = self.user.get_random_user_password(['special', 'lower', 'upper', 'number'])['results'][0]['login']['password']
        self.assertEqual(8 <= len(result) <= 64, True)

    def test_get_only_max_length(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.return_value = self.result
        self.result['results'][0]['login']['password'] = 'a^eP!Wz43.'

        result = self.user.get_random_user_password(['special', 'lower', 'upper', 'number'], 15)['results'][0]['login']['password']
        self.assertEqual(8 <= len(result) <= 15, True)

    def test_get_different_length(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.return_value = self.result
        self.result['results'][0]['login']['password'] = 'TU-Jy4M+w"WB}jX]]k,,#f-{oWnQ3J05 ~'

        result = self.user.get_random_user_password(['special', 'lower', 'upper', 'number'], 35, 30)['results'][0]['login']['password']
        self.assertEqual(30 <= len(result) <= 35, True)

    def test_get_wrong_length(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.side_effect = ValueError('Length must be between 1 and 64!')

        with pytest.raises(ValueError, match=r'Length must be between 1 and 64!'):
            self.user.get_random_user_password(['special', 'lower', 'upper', 'number'], 85, 70)

    def test_get_no_options(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.side_effect = ValueError('You must provide at least one option!')

        with pytest.raises(ValueError, match=r'You must provide at least one option!'):
            self.user.get_random_user_password([])

    def test_get_option_doesnt_exists(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.side_effect = ValueError('The specified option does not exist!')

        with pytest.raises(ValueError, match=r'The specified option does not exist!'):
            self.user.get_random_user_password(['lowercase', 'uppercase'])

    def test_get_length_not_int(self):
        self.user.get_random_user_password = Mock()
        self.user.get_random_user_password.side_effect = TypeError('Length must be of int type!')

        with pytest.raises(TypeError, match=r'Length must be of int type!'):
            self.user.get_random_user_password(['lower', 'upper'], '18', {'num': 15})

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

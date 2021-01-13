import requests


class RandomUser:

    def __init__(self):
        self.api = 'https://randomuser.me/api/?noinfo'

    def get_random_user(self):
        response = requests.get(self.api)
        if 'json' in response.headers.get('Content-Type'):
            return response.json()

    def get_n_random_users(self, n):
        response = requests.get(self.api + f'&results={n}')
        if isinstance(n, int):
            if n > 0:
                if 'json' in response.headers.get('Content-Type'):
                    return response.json()
            else:
                return None
        elif isinstance(n, str):
            if n.isnumeric():
                if 'json' in response.headers.get('Content-Type'):
                    return response.json()
            else:
                raise TypeError('Input must refer to an int!')
        else:
            raise TypeError('Input must be of int type!')

    def get_random_user_gender(self, gender):
        if not isinstance(gender, str):
            raise TypeError('Input must be of string type!')

        if not (gender == 'female' or gender == 'male'):
            return None

        response = requests.get(self.api + f'&gender={gender}')
        if 'json' in response.headers.get('Content-Type'):
            return response.json()

    def get_random_user_password(self, options, max_length=64, min_length=8):
        if len(options) < 1:
            raise ValueError('You must provide at least one option!')

        if not any(item in ['special', 'upper', 'lower', 'number'] for item in options):
            raise ValueError('The specified option does not exist!')

        if not(isinstance(max_length, int) or isinstance(min_length, int)):
            raise TypeError('Length must be of int type!')

        if not 1 <= min_length <= max_length <= 64:
            raise ValueError('Length must be between 1 and 64!')

        response = requests.get(self.api + f'&password={",".join(options)},{min_length}-{max_length}')
        if 'json' in response.headers.get('Content-Type'):
            return response.json()

    def get_random_user_nat(self, nationalities):
        if len(nationalities) < 1:
            raise ValueError('You must provide at least one nationality!')

        if not any(item in [
            'AU', 'BR', 'CA', 'CH', 'DE', 'DK', 'ES', 'FI',
            'FR', 'GB', 'IE', 'IR', 'NO', 'NL', 'NZ', 'TR', 'US'
        ] for item in [nat.upper() for nat in nationalities]):
            raise ValueError('The specified nationality does not exist!')

        response = requests.get(self.api + f'&nat={",".join(nationalities)}')
        if 'json' in response.headers.get('Content-Type'):
            return response.json()

    def get_random_user_inc_exc(self, option, params):
        if not (option == 'inc' or option == 'exc'):
            raise ValueError('The specified option does not exist!')

        if len(params) < 1:
            raise ValueError('You must provide at least one parameter!')

        if not any(item in [
            'gender', 'name', 'location', 'email', 'login', 'registered',
            'dob', 'phone', 'cell', 'id', 'picture', 'nat'
        ] for item in [param.lower() for param in params]):
            raise ValueError('The specified parameter does not exist!')

        response = requests.get(self.api + f'&{option}={",".join(params)}')
        if 'json' in response.headers.get('Content-Type'):
            return response.json()

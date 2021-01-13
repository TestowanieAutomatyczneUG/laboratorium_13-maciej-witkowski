import unittest
import pytest
from unittest.mock import Mock
from zad2.subscriber import Subscriber


class TestRemoveClient(unittest.TestCase):

    def test_remove_client(self):
        self.subscriber.remove_client = Mock()
        self.subscriber.remove_client.return_value = True

        self.assertEqual(self.subscriber.remove_client('5beead25-3978-4d7c-9033-a532c559f5e3'), True)

    def test_input_not_string(self):
        self.subscriber.remove_client = Mock()
        self.subscriber.remove_client.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.subscriber.remove_client(1582)

    def test_id_does_not_exists(self):
        self.subscriber.remove_client = Mock()
        self.subscriber.remove_client.side_effect = ValueError('Id does not exists!')

        with pytest.raises(ValueError, match=r'Id does not exists!'):
            self.subscriber.remove_client('ce4ffe04-bd7e-47fb-a65b-6e75bf11c932')

    def setUp(self):
        self.subscriber = Subscriber()
        self.subscriber.clients = [
            {
                'id': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                'mailbox': {
                    'received': [
                        {
                            'from': '5beead25-3978-4d7c-9033-a532c559f5e3',
                            'message': 'Lubisz placki!?',
                            'to': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d'
                        },
                        {
                            'from': '5beead25-3978-4d7c-9033-a532c559f5e3',
                            'message': 'Kiedy frytki?',
                            'to': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d'}
                    ],
                    'sent': [
                        {
                            'from': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                            'message': 'Spotkanie jest jutro o godzinie 15:00! Bądź na nogach!',
                            'to': '5beead25-3978-4d7c-9033-a532c559f5e3'
                        },
                        {
                            'from': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                            'message': 'Siema byku ;)',
                            'to': '0e74b7c4-7249-4fdf-89db-4bec8e6b390d'
                        }
                    ]
                },
                'name': {'first': 'Maciej', 'last': 'Witkowski'}
            },
            {
                'id': '5beead25-3978-4d7c-9033-a532c559f5e3',
                'mailbox': {
                    'received': [
                        {
                            'from': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                            'message': 'Spotkanie jest jutro o godzinie 15:00! Bądź na nogach!',
                            'to': '5beead25-3978-4d7c-9033-a532c559f5e3'
                        }
                    ],
                    'sent': [
                        {
                            'from': '5beead25-3978-4d7c-9033-a532c559f5e3',
                            'message': 'Lubisz placki!?',
                            'to': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d'
                        },
                        {
                            'from': '5beead25-3978-4d7c-9033-a532c559f5e3',
                            'message': 'Kiedy frytki?',
                            'to': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d'
                        }
                    ]
                },
                'name': {'first': 'Łukasz', 'last': 'Marczak'}
            },
            {
                'id': '0e74b7c4-7249-4fdf-89db-4bec8e6b390d',
                'mailbox': {
                    'received': [
                        {
                            'from': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                            'message': 'Siema byku ;)',
                            'to': '0e74b7c4-7249-4fdf-89db-4bec8e6b390d'
                        }
                    ],
                    'sent': []
                },
                'name': {'first': 'Mirosław', 'last': 'Kapczak'}
            }
        ]

    def tearDown(self):
        self.subscriber = None


if __name__ == '__main__':
    unittest.main()

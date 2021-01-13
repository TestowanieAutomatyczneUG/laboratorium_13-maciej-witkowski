import unittest
import pytest
from unittest.mock import Mock
from zad2.subscriber import Subscriber


class TestSendMessage(unittest.TestCase):

    def test_send_message(self):
        self.subscriber.send_message = Mock()
        self.subscriber.send_message.return_value = True

        self.assertEqual(self.subscriber.send_message(
            'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
            '5beead25-3978-4d7c-9033-a532c559f5e3',
            'Testowa wiadomość!'
        ), True)

    def test_from_id_not_string(self):
        self.subscriber.send_message = Mock()
        self.subscriber.send_message.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.subscriber.send_message(
                18295478524856471878474784874874841561,
                '5beead25-3978-4d7c-9033-a532c559f5e3',
                'Testowa wiadomość!'
            )

    def test_to_id_not_string(self):
        self.subscriber.send_message = Mock()
        self.subscriber.send_message.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.subscriber.send_message(
                'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                49525489528548954814844852152152891789,
                'Testowa wiadomość!'
            )

    def test_message_not_string(self):
        self.subscriber.send_message = Mock()
        self.subscriber.send_message.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.subscriber.send_message(
                'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                '5beead25-3978-4d7c-9033-a532c559f5e3',
                []
            )

    def test_empty_message(self):
        self.subscriber.send_message = Mock()
        self.subscriber.send_message.side_effect = ValueError('Message can not be empty!')

        with pytest.raises(ValueError, match=r'Message can not be empty!'):
            self.subscriber.send_message(
                'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                '5beead25-3978-4d7c-9033-a532c559f5e3',
                ''
            )

    def test_from_id_does_not_exists(self):
        self.subscriber.send_message = Mock()
        self.subscriber.send_message.side_effect = ValueError('Id does not exists!')

        with pytest.raises(ValueError, match=r'Id does not exists!'):
            self.subscriber.send_message(
                'qqqqqqqq-wwww-eeee-rrrr-tttttttttttt'
                'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                'Testowa wiadomość!'
            )

    def test_to_id_does_not_exists(self):
        self.subscriber.send_message = Mock()
        self.subscriber.send_message.side_effect = ValueError('Id does not exists!')

        with pytest.raises(ValueError, match=r'Id does not exists!'):
            self.subscriber.send_message(
                'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
                'qqqqqqqq-wwww-eeee-rrrr-tttttttttttt',
                'Testowa wiadomość!'
            )

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

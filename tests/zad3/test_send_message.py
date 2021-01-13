import unittest
import pytest
from unittest.mock import Mock
from zad3.messenger import Messenger
from uuid import uuid4


class TestSendMessage(unittest.TestCase):

    def test_send_message(self):
        self.messenger.template_engine.write = Mock()
        self.messenger.template_engine.write.return_value = {
            'from': self.messenger.client_id,
            'to': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
            'message': "Wiadomość testowa"
        }

        self.messenger.mail_server.send = Mock()
        self.messenger.mail_server.send.return_value = True

        self.assertEqual(self.messenger.send_message(
            'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
            "Wiadomość testowa"
        ), True)

    def test_send_message_error(self):
        self.messenger.template_engine.write = Mock()
        self.messenger.template_engine.write.return_value = {
            'from': self.messenger.client_id,
            'to': '5beead25-3978-4d7c-9033-a532c559f5e3',
            'message': "testowanko"
        }

        self.messenger.mail_server.send = Mock()
        self.messenger.mail_server.send.return_value = False

        self.assertEqual(self.messenger.send_message(
            '5beead25-3978-4d7c-9033-a532c559f5e3',
            "Wiadomość testowa"
        ), False)

    def test_to_id_not_string(self):
        self.messenger.template_engine.write = Mock()
        self.messenger.template_engine.write.return_value = {
            'from': self.messenger.client_id,
            'to': 185296481748184174174511,
            'message': 'Wiadomość testowa'
        }

        self.messenger.mail_server.send = Mock()
        self.messenger.mail_server.send.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.messenger.send_message(185296481748184174174511, 'Wiadomość testowa')

    def test_message_not_string(self):
        self.messenger.template_engine.write = Mock()
        self.messenger.template_engine.write.return_value = {
            'from': self.messenger.client_id,
            'to': 'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
            'message': {'message': "TESTUJE BYCZKU ;)"}
        }

        self.messenger.mail_server.send = Mock()
        self.messenger.mail_server.send.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.messenger.send_message('fbdb7e1c-8559-4dd1-9192-276213d6f63d', {'message': "TESTUJE BYCZKU ;)"})

    def setUp(self):
        self.messenger = Messenger(str(uuid4()))

    def tearDown(self):
        self.messenger = None


if __name__ == '__main__':
    unittest.main()

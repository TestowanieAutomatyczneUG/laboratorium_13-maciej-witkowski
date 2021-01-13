import unittest
import pytest
from unittest.mock import Mock
from zad3.messenger import Messenger
from uuid import uuid4


class TestReceiveMessage(unittest.TestCase):

    def test_receive_message(self):
        self.messenger.mail_server.receive = Mock()
        self.messenger.mail_server.receive.return_value = True

        self.assertEqual(self.messenger.receive_message(
            '5beead25-3978-4d7c-9033-a532c559f5e3',
        ), True)

    def test_receive_message_error(self):
        self.messenger.mail_server.receive = Mock()
        self.messenger.mail_server.receive.return_value = False

        self.assertEqual(self.messenger.receive_message(
            'fbdb7e1c-8559-4dd1-9192-276213d6f63d',
        ), False)

    def test_to_id_not_string(self):
        self.messenger.mail_server.receive = Mock()
        self.messenger.mail_server.receive.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Id must be of string type!'):
            self.messenger.receive_message(185296481748184174174511)

    def setUp(self):
        self.messenger = Messenger(str(uuid4()))

    def tearDown(self):
        self.messenger = None


if __name__ == '__main__':
    unittest.main()

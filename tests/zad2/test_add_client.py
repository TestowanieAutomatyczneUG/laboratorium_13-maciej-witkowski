import unittest
import pytest
from unittest.mock import Mock
from zad2.subscriber import Subscriber


class TestAddClient(unittest.TestCase):

    def test_add_client(self):
        self.subscriber.add_client = Mock()
        self.subscriber.add_client.return_value = True

        self.assertEqual(self.subscriber.add_client("Jan", "Kowalski"), True)

    def test_f_name_not_string(self):
        self.subscriber.add_client = Mock()
        self.subscriber.add_client.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.subscriber.add_client(1, "Kowalski")

    def test_l_name_not_string(self):
        self.subscriber.add_client = Mock()
        self.subscriber.add_client.side_effect = TypeError('Input must be of string type!')

        with pytest.raises(TypeError, match=r'Input must be of string type!'):
            self.subscriber.add_client("Jan", {})

    def setUp(self):
        self.subscriber = Subscriber()

    def tearDown(self):
        self.subscriber = None


if __name__ == '__main__':
    unittest.main()

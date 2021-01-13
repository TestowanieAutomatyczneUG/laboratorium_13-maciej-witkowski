import unittest
from unittest.mock import Mock
from zad2.subscriber import Subscriber
from uuid import uuid4


class TestGetIds(unittest.TestCase):

    def test_get_ids(self):
        ids = [str(uuid4()), str(uuid4())]
        self.subscriber.get_ids = Mock()
        self.subscriber.get_ids.return_value = ids

        self.assertEqual(self.subscriber.get_ids(), ids)

    def setUp(self):
        self.subscriber = Subscriber()

    def tearDown(self):
        self.subscriber = None


if __name__ == '__main__':
    unittest.main()

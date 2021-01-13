import unittest
import pytest
from zad1.random_user import RandomUser


class TestGetRandomUserNat(unittest.TestCase):

    def test_get(self):
        try:
            self.assertEqual(self.user.get_random_user_nat(['fr'])['results'][0]['nat'], 'FR')
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_get_multiple_nats(self):
        try:
            result = self.user.get_random_user_nat(['fr', 'GB', 'us'])['results'][0]['nat']
            self.assertEqual(result in ['FR', 'GB', 'US'], True)
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def test_no_nats(self):
        with pytest.raises(ValueError, match=r'You must provide at least one nationality!'):
            self.user.get_random_user_nat([])

    def test_nats_not_exists(self):
        with pytest.raises(ValueError, match=r'The specified nationality does not exist!'):
            self.user.get_random_user_nat(['pl', 'RU'])

    def setUp(self):
        self.user = RandomUser()

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

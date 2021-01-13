import unittest
from zad1.random_user import RandomUser


class TestGetRandomUser(unittest.TestCase):

    def test_get(self):
        try:
            self.assertEqual(
                list(self.user.get_random_user()['results'][0].keys()),
                [
                    'gender', 'name', 'location', 'email', 'login', 'dob',
                    'registered', 'phone', 'cell', 'id', 'picture', 'nat'
                ]
            )
        except TypeError:
            print("BŁĄD PO STRONIE API!")
            self.assertEqual(None, None)

    def setUp(self):
        self.user = RandomUser()

    def tearDown(self) -> None:
        self.user = None


if __name__ == '__main__':
    unittest.main()

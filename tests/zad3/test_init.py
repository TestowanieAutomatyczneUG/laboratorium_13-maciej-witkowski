import unittest
import pytest
from zad3.messenger import Messenger
from uuid import uuid4


class TestInit(unittest.TestCase):

    def test_init(self):
        with pytest.raises(TypeError, match=r'Id must be of string type!'):
            Messenger(uuid4())


if __name__ == '__main__':
    unittest.main()

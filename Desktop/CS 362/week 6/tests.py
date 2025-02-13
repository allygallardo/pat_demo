import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        str = ""
        self.assertFalse(check_pwd(str))


if __name__ == '__main__':
    unittest.main()

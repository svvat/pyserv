import unittest
from mod1 import getResponse

class TestMod1(unittest.TestCase):

    def test_response(self):
        self.assertEqual(getResponse(), b"Hello From Mod1")

if __name__ == '__main__':
    unittest.main()
import unittest
from demo import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Hell world!')

if __name__ == '__main__':
    unittest.main()
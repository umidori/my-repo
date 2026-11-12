import unittest
from calc import add

class TestCalc(unittest.TestCase):
  deff test_add(self):
    self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
  unittest.main()
  

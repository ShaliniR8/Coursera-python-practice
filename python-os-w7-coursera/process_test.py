import unittest
from process import USERNAME

class TestCompiler(unittest.TestCase):
     def test_username(self):
          testcase = '(abc@def)'
          expected = 'abc@def'
          self.assertEqual(USERNAME(testcase), expected)


unittest.main()
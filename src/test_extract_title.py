import unittest
from functions import extract_title

class TestTitleExtraction(unittest.TestCase):
    def test(self):
        markdown = '# This is the first heading!'
        expected_return = 'This is the first heading!'

        self.assertEqual(extract_title(markdown), expected_return)
        

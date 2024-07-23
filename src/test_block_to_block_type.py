import unittest
from functions import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("### This is a heading"), 'heading')

    def test_code(self):
        block = "```\ndef hello():\n    print('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), 'code')

    def test_quote(self):
        block = "> This is a quote.\n> Another quoted line."
        self.assertEqual(block_to_block_type(block), 'quote')

    def test_unordered_list(self):
        block = "* Item 1\n* Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), 'unordered list')

    def test_normal(self):
        block = "This is a normal block"
        self.assertEqual(block_to_block_type(block), 'paragraph')

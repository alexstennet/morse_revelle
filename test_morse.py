import unittest

from morse import parse, parse_word

class TestMorseMethods(unittest.TestCase):
    def test_parse_word_sos(self):
        result = parse_word('... --- ...')
        self.assertEqual(result, 'sos')

    def test_parse_hello_world(self):
        result = parse(['.... . .-.. .-.. ---', '.-- --- .-. .-.. -..'])
        self.assertEqual(result, 'hello world')

if __name__ == '__main__':
    unittest.main()

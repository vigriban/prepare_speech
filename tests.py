import unittest
import prepare_speech


class TransliterateTest(unittest.TestCase):


    def test_can_translit_text_symbolls(self):
        self.assertEqual('хелло', prepare_speech.transliterate_english_to_russian('hello'))

    def test_transform_number_to_letters(self):
        self.assertEqual('фиве ыеарс', prepare_speech.transliterate_english_to_russian('5 years'))

if __name__ == '__main__':
    unittest.main()

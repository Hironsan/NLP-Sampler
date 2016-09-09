# -*- coding: utf-8 -*-
import unittest

from ..ja.janome import JanomeTokenizer


class JanomeTokenizerTest(unittest.TestCase):

    def setUp(self):
        self.sent = '太郎は花子に花束をあげました。'
        self.tokenizer = JanomeTokenizer()

    def tearDown(self):
        pass

    def test_separated_words(self):
        separated_sent = self.tokenizer.separate_words(self.sent)
        self.assertTrue(all([isinstance(word, str) for word in separated_sent]))

    def test_tokenize(self):
        tokens = self.tokenizer.tokenize(self.sent)

    def test_filter_by_pos(self):
        tokens = self.tokenizer.filter_by_pos(self.sent)
        surfaces = [token.surface for token in tokens]
        self.assertEqual(surfaces, ['太郎', '花子', '花束'])
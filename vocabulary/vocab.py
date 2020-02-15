""" classes for the vocab, and for each word in it """

import openpyxl
import pykakasi


class Vocab():
    """ a class for a vocabulary of japanese words in kana and romaji, with English translation"""

    def __init__(self, load_screen):
        self.app = load_screen.app
        self.hiragana = []
        self.katakana = []
        self._load()

        # self.characters_hiragana = {
        #     "vowel": {"a": "あ", "i": "い","u": "う", "e": "え", "o": "お"},
        #     "k": {"a": "か", "i": "き","u": "く", "e": "け", "o": "こ"},
        #     "s": {"a": "さ", "i": "し", "u": "す", "e": "せ", "o": "そ"},
        #     "t": {"a": "た", "i": "ち","u": "つ", "e": "て", "o": "と"},
        #     "n": {"a": "な", "i": "に","u": "ぬ", "e": "ね", "o": "の"},
        #     "h": {"a": "は", "i": "ひ","u": "ふ", "e": "へ", "o": "ほ"},
        #     "m": {"a": "ま", "i": "み","u": "む", "e": "め", "o": "も"},
        #     "y": {"a": "や", "i": None, "u": "ゆ", "e": None, "o": "よ"},
        #     "r": {"a": "ら", "i": "り", "u": "る", "e": "れ", "o": "ろ"},
        #     "w": {"a": "わ", "i": None,"u": None, "e": None, "o": "を"},
        #     "n_consonant": {"a": None, "i": None, "u": "ん", "e": None, "o": None},
        # }

    def _load(self):
        self.vocab_xl = openpyxl.load_workbook("vocabulary/vocabulary.xlsx")

        self.hiragana_xlsh = self.vocab_xl["hiragana"]
        self._make_sheet(self.hiragana_xlsh, "hiragana", self.hiragana)

        self.katakana_xlsh = self.vocab_xl["katakana"]
        self._make_sheet(self.katakana_xlsh, "katakana", self.katakana)

    def _make_sheet(self, sheet, kana, word_list):
        """ function to make each sheet """
        kakasi = pykakasi.kakasi()
        if kana == "hiragana":
            kakasi.setMode("H", "a")
        elif kana == "katakana":
            kakasi.setMode("K", "a")

        for row in sheet.iter_rows(min_row=2, max_col=2):
            # each row in sheet has data for one word
            kana = row[0].value
            romaji = kakasi.getConverter().do(kana)
            if kana == romaji:
                continue
            english = row[1].value
            word = Word(kana, romaji, english)
            word_list.append(word)


class Word():
    def __init__(self, kana, romaji, english):
        self.romaji = romaji
        self.kana = kana
        self.english = english

    def __str__(self):
        str = "{kana}: {romaji} ({english})".format(
            kana = self.kana, romaji = self.romaji, english = self.english)
        return str
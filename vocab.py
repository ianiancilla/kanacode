import openpyxl
import pykakasi


import text

class Vocab():
    """ a class for a vocabulary of japanese words in kana and romaji, with English translation"""

    def __init__(self, load_screen):
        self.app = load_screen.app
        self.hiragana = {}
        self.katakana = {}
        self._load()

        # change app state to exit loading screem
        # self.app.state = main_menu
        # TODO test to remove!!!
        self.app.running = False


    def _load(self):
        self.vocab_xl = openpyxl.load_workbook("vocabulary.xlsx")

        self.hiragana_xlsh = self.vocab_xl["hiragana"]
        self._make_sheet(self.hiragana_xlsh, "hiragana", self.hiragana)

        self.katakana_xlsh = self.vocab_xl["katakana"]
        self._make_sheet(self.katakana_xlsh, "katakana", self.katakana)

    def _make_sheet(self, sheet, kana, dict):
        """ function to make each sheet """

        kakasi = pykakasi.kakasi()
        if kana == "hiragana":
            kakasi.setMode("H", "a")
        elif kana == "katakana":
            kakasi.setMode("K", "a")

        for row in sheet.iter_rows(min_row=2, max_col=2):    # each row in sheet has data for one word
            word = row[0].value
            romaji = kakasi.getConverter().do(word)
            if word == romaji:
                continue
            dict[romaji] = {}
            dict[romaji]["kana"] = word
            dict[romaji]["en"] = row[1].value

from PyQt6 import QtWidgets, uic
from wonderwords import RandomWord
import random

class FuckYouWindow(QtWidgets.QDialog):
    """
    This is a class to Fuck You
    """
    def __init__(self):
        super(FuckYouWindow, self).__init__()
        uic.loadUi('windows/scrooples.ui', self)
        self.show()

        # Find the Fuck You Button
        self.button_fuckyou = self.findChild(
            QtWidgets.QPushButton, 'button_fuckyou'
        )
        self.button_fuckyou.clicked.connect(self.fuckyou)

        self.text_fuckyou = self.findChild(
            QtWidgets.QPlainTextEdit, 'text_fuckyou'
        )
        self.fuck = 0
        self.fucking_profane_words = []

        with open('profanitylist.txt', 'r') as file:
            self.fucking_profane_words = file.readlines()

    def fuckyou(self):
        self.fuck += 1
        if self.fuck == 1:
            self.text_fuckyou.appendPlainText("NO, fuck YOU")
        elif self.fuck == 2:
            self.text_fuckyou.appendPlainText("Fuck you TWICE")
        elif self.fuck == 3:
            self.text_fuckyou.appendPlainText("Fuck you THRICE")
        elif self.fuck == 4:
            self.text_fuckyou.appendPlainText("Fuck you four times as much!")
        else:
            random_no = random.randint(0,3)
            rword = RandomWord()
            if random_no == 0:
                text_string = f"Why dont you {rword.word(include_categories=['verbs'])} a {rword.word(include_categories=['nouns'])}"
                self.text_fuckyou.appendPlainText(text_string)
            elif random_no == 1:
                text_string = f"You must be a {rword.word(include_categories=['adjectives'])} {rword.word(include_categories=['nouns'])}"
                self.text_fuckyou.appendPlainText(text_string)
            elif random_no == 2:
                text_string = f"You are an extraordiary example of a {rword.word(include_categories=['adjectives'])} {rword.word(include_categories=['nouns'])}"
                self.text_fuckyou.appendPlainText(text_string)
            elif random_no == 3:
                fucking_random_swear = self.fucking_profane_words[random.randint(0, len(self.fucking_profane_words))].strip()
                text_string = f"You {fucking_random_swear}" 
                self.text_fuckyou.appendPlainText(text_string)
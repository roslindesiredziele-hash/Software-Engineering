class Word:
    def __init__(self, text):
        self.text = text.lower()
        self.guessed = set()

    def guess(self, letter):
        pass

    def is_fully_guessed(self):
        pass

    def display(self):
        pass

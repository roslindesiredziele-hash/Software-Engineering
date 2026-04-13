class Word:
    def __init__(self, text):
        self.text = text.lower()
        self.guessed = set()

    def guess(self, letter):
        pass

    def is_fully_guessed(self):
        pass

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.text:
            self.guessed.add(letter)
            return True
        return False
    def display(self):
        return " ".join("_" for _ in self.text)



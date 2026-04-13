from Game.word import Word

def test_word_initial_state():
    w = Word("apple")
    assert w.text == "apple"
    assert w.guessed == set()

def test_guess_correct_letter():
    w = Word("apple")
    result = w.guess("a")
    assert result is True
    assert "a" in w.guessed

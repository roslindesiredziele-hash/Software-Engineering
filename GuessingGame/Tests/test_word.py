from Game.word import Word

def test_word_initial_state():
    w = Word("apple")
    assert w.text == "apple"
    assert w.guessed == set()

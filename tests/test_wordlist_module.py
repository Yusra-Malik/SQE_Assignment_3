import pytest
from textblob import WordList

class TestWordListClass:
    """Class-level unit tests for WordList collection."""

    @pytest.mark.run(order=2)
    @pytest.mark.wordlist_tests
    def test_wordlist_initialization(self):
        wl = WordList(["apple", "banana", "cherry"])
        assert len(wl) == 3

    @pytest.mark.wordlist_tests
    def test_wordlist_empty_bva(self):
        wl = WordList([])
        assert len(wl) == 0

    @pytest.mark.wordlist_tests
    def test_wordlist_slicing(self):
        wl = WordList(["a", "b", "c", "d"])
        assert wl[1:3] == WordList(["b", "c"])


class TestWordListFunctions:
    """Function-level unit tests for WordList methods."""

    @pytest.mark.wordlist_tests
    def test_func_wordlist_count(self):
        wl = WordList(["cat", "dog", "cat", "bird"])
        assert wl.count("cat") == 2
        assert wl.count("dog") == 1

    @pytest.mark.wordlist_tests
    def test_func_wordlist_upper(self):
        wl = WordList(["hello", "world"])
        assert wl.upper() == WordList(["HELLO", "WORLD"])

    @pytest.mark.wordlist_tests
    def test_func_wordlist_lemmatize(self):
        wl = WordList(["dogs", "cities"])
        assert wl.lemmatize() == WordList(["dog", "city"])

    @pytest.mark.wordlist_tests
    def test_func_wordlist_count_case_sensitivity(self):
        wl = WordList(["Cat", "cat"])
        assert wl.count("cat", case_sensitive=True) == 1

    @pytest.mark.wordlist_tests
    def test_func_wordlist_count_case_insensitive(self):
        wl = WordList(["Cat", "cat"])
        assert wl.count("cat", case_sensitive=False) == 2

    @pytest.mark.wordlist_tests
    def test_func_wordlist_lower(self):
        wl = WordList(["PYTHON", "CODE"])
        assert wl.lower() == WordList(["python", "code"])
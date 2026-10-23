import pytest
from textblob import Word

class TestWordClass:
    """Class-level unit tests for Word object."""

    @pytest.mark.run(order=1)
    @pytest.mark.word_tests
    def test_word_instance_type(self):
        w = Word("python")
        assert isinstance(w, str)
        assert isinstance(w, Word)

    @pytest.mark.word_tests
    def test_word_case_preservation(self):
        w = Word("CAT")
        assert w.pluralize() == "CATS"

    @pytest.mark.word_tests
    def test_word_string_methods(self):
        w = Word("hello")
        assert w.upper() == "HELLO"
        assert w.startswith("h")


class TestWordFunctions:
    """Function-level unit tests for Word methods."""

    @pytest.mark.word_tests
    def test_func_pluralize_standard(self):
        assert Word("cat").pluralize() == "cats"

    @pytest.mark.word_tests
    def test_func_pluralize_ending_y(self):
        assert Word("city").pluralize() == "cities"

    @pytest.mark.word_tests
    def test_func_pluralize_irregular(self):
        assert Word("goose").pluralize() == "geese"

    @pytest.mark.word_tests
    def test_func_singularize_standard(self):
        assert Word("dogs").singularize() == "dog"

    @pytest.mark.word_tests
    def test_func_singularize_ending_ies(self):
        assert Word("cities").singularize() == "city"

    @pytest.mark.word_tests
    def test_func_pluralize_bva_empty_string(self):
        assert Word("").pluralize() == ""

    @pytest.mark.word_tests
    def test_func_pluralize_bva_single_char(self):
        assert Word("a").pluralize() == "as"

    @pytest.mark.parametrize("singular, expected_plural", [
        ("bus", "busses"),
        ("box", "boxes"),
        ("child", "children")
    ])
    def test_func_pluralize_parameterized(self, singular, expected_plural):
        assert Word(singular).pluralize() == expected_plural
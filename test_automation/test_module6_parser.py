import pytest
from textblob.en.parsers import PatternParser



class TestPatternParserModuleClass:
    """Class/Module Level Tests for PatternParser"""

    @pytest.fixture
    def parser(self):
        return PatternParser()

    @pytest.mark.run(order=38)
    @pytest.mark.parser_tests
    def test_class_parser_initialization(self, parser):
        assert parser is not None
        assert isinstance(parser, PatternParser)

    @pytest.mark.run(order=39)
    @pytest.mark.parser_tests
    def test_class_parser_callable_interface(self, parser):
        assert hasattr(parser, "parse")
        assert callable(parser.parse)

    @pytest.mark.run(order=40)
    @pytest.mark.parser_tests
    def test_class_parser_simple_declarative_sentence(self, parser):
        out = parser.parse("The student writes unit tests.")
        assert isinstance(out, str)
        assert len(out) > 0

    @pytest.mark.run(order=41)
    @pytest.mark.parser_tests
    def test_class_parser_interrogative_sentence(self, parser):
        out = parser.parse("Did the automated suite pass?")
        assert isinstance(out, str)

    @pytest.mark.run(order=42)
    @pytest.mark.parser_tests
    def test_class_parser_bva_empty_string(self, parser):
        out = parser.parse("")
        assert out == ""

    @pytest.mark.run(order=43)
    @pytest.mark.parser_tests
    def test_class_parser_bva_single_word(self, parser):
        out = parser.parse("Execute")
        assert "Execute" in out


class TestPatternParserFunctions:
    """Function Level Tests for parse()"""

    @pytest.fixture
    def parser(self):
        return PatternParser()

    @pytest.mark.run(order=44)
    @pytest.mark.parser_tests
    def test_func_parse_returns_string_type(self, parser):
        result = parser.parse("Software engineering course.")
        assert isinstance(result, str)

    @pytest.mark.run(order=45)
    @pytest.mark.parser_tests
    def test_func_parse_noun_tagging(self, parser):
        result = parser.parse("Python")
        assert "/NN" in result or "/NNP" in result

    @pytest.mark.run(order=46)
    @pytest.mark.parser_tests
    def test_func_parse_verb_tagging(self, parser):
        result = parser.parse("running")
        assert "/VBG" in result or "/VB" in result

    @pytest.mark.run(order=47)
    @pytest.mark.parser_tests
    def test_func_parse_adjective_tagging(self, parser):
        result = parser.parse("fast execution")
        assert "/JJ" in result

    @pytest.mark.run(order=48)
    @pytest.mark.parser_tests
    def test_func_parse_multiple_words_preservation(self, parser):
        text = "Alpha Beta Gamma"
        result = parser.parse(text)
        assert "Alpha" in result and "Beta" in result and "Gamma" in result

    @pytest.mark.run(order=49)
    @pytest.mark.parser_tests
    def test_func_parse_bva_numerical_string(self, parser):
        result = parser.parse("2026")
        assert "2026" in result

    @pytest.mark.run(order=50)
    @pytest.mark.parser_tests
    def test_func_parse_bva_special_characters(self, parser):
        result = parser.parse("code @ test!")
        assert isinstance(result, str)

    @pytest.mark.run(order=51)
    @pytest.mark.parser_tests
    def test_func_parse_bva_multiline_string(self, parser):
        result = parser.parse("Line one.\nLine two.")
        assert isinstance(result, str)

    @pytest.mark.run(order=52)
    @pytest.mark.parser_tests
    @pytest.mark.parametrize("sentence,expected_token", [
        ("FAST University campus.", "FAST"),
        ("Unit testing in Python.", "Python"),
        ("Boundary value analysis.", "Boundary"),
        ("Equivalence class partitioning.", "Equivalence")
    ])
    def test_func_parse_parameterized_tokens(self, parser, sentence, expected_token):
        result = parser.parse(sentence)
        assert expected_token in result
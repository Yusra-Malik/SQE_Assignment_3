import pytest
from textblob import TextBlob, Sentence


class TestSentenceModuleClass:
    """Class/Module Level Tests for Sentence"""

    @pytest.mark.run(order=20)
    @pytest.mark.sentence_tests
    def test_class_sentence_inheritance(self):
        s = Sentence("This is a valid sentence.")
        assert isinstance(s, TextBlob)
        assert isinstance(s, Sentence)

    @pytest.mark.run(order=21)
    @pytest.mark.sentence_tests
    def test_class_sentence_string_equality(self):
        text = "Boundary testing sentence."
        s = Sentence(text)
        assert str(s) == text

    @pytest.mark.run(order=22)
    @pytest.mark.sentence_tests
    def test_class_sentence_words_property(self):
        s = Sentence("Automated software quality analysis.")
        assert list(s.words) == ["Automated", "software", "quality", "analysis"]

    @pytest.mark.run(order=23)
    @pytest.mark.sentence_tests
    def test_class_sentence_sentiment_inheritance(self):
        s = Sentence("This is an exceptional feature!")
        assert s.sentiment.polarity > 0.0

    @pytest.mark.run(order=24)
    @pytest.mark.sentence_tests
    def test_class_sentence_bva_single_character(self):
        s = Sentence("Z.")
        assert len(s.words) == 1

    @pytest.mark.run(order=25)
    @pytest.mark.sentence_tests
    def test_class_sentence_bva_question_mark_ending(self):
        s = Sentence("Is the test passing?")
        assert str(s).endswith("?")


class TestSentenceFunctions:
    """Function Level Tests for dict property and end property"""

    # --- Function 1: dict property ---
    @pytest.mark.run(order=26)
    @pytest.mark.sentence_tests
    def test_func_sentence_dict_structure(self):
        s = Sentence("Testing dictionary conversion.")
        d = s.dict
        assert isinstance(d, dict)
        assert "raw" in d
        assert "polarity" in d
        assert "subjectivity" in d

    @pytest.mark.run(order=27)
    @pytest.mark.sentence_tests
    def test_func_sentence_dict_raw_value(self):
        raw = "Exact raw text content."
        s = Sentence(raw)
        assert s.dict["raw"] == raw

    @pytest.mark.run(order=28)
    @pytest.mark.sentence_tests
    def test_func_sentence_dict_polarity_matching(self):
        s = Sentence("Great result!")
        assert s.dict["polarity"] == s.sentiment.polarity

    @pytest.mark.run(order=29)
    @pytest.mark.sentence_tests
    def test_func_sentence_dict_subjectivity_matching(self):
        s = Sentence("In my opinion this is good.")
        assert s.dict["subjectivity"] == s.sentiment.subjectivity

    @pytest.mark.run(order=30)
    @pytest.mark.sentence_tests
    def test_func_sentence_dict_bva_empty(self):
        s = Sentence("")
        assert s.dict["raw"] == ""

    @pytest.mark.run(order=31)
    @pytest.mark.sentence_tests
    def test_func_sentence_dict_start_end_keys(self):
        s = Sentence("Index sentence.", start_index=5, end_index=20)
        assert s.dict["start"] == 5
        assert s.dict["end"] == 20

    # --- Function 2: end property ---
    @pytest.mark.run(order=32)
    @pytest.mark.sentence_tests
    def test_func_sentence_end_position_specified(self):
        s = Sentence("Sample text", start_index=0, end_index=11)
        assert s.end == 11

    @pytest.mark.run(order=33)
    @pytest.mark.sentence_tests
    def test_func_sentence_end_position_default_none(self):
        s = Sentence("No position specified")
        assert s.end is None

    @pytest.mark.run(order=34)
    @pytest.mark.sentence_tests
    def test_func_sentence_end_position_zero_boundary(self):
        s = Sentence("", start_index=0, end_index=0)
        assert s.end == 0

    @pytest.mark.run(order=35)
    @pytest.mark.sentence_tests
    def test_func_sentence_end_position_large_boundary(self):
        s = Sentence("Long text", start_index=100, end_index=1000)
        assert s.end == 1000

    @pytest.mark.run(order=36)
    @pytest.mark.sentence_tests
    def test_func_sentence_start_position_matching(self):
        s = Sentence("Offset test", start_index=12, end_index=23)
        assert s.start == 12

    @pytest.mark.run(order=37)
    @pytest.mark.sentence_tests
    def test_func_sentence_start_position_default_none(self):
        s = Sentence("Default offset")
        assert s.start is None
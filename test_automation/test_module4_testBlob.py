import pytest
from textblob import TextBlob

class TestTextBlobModuleClass:

    @pytest.mark.run(order=1)
    @pytest.mark.blob_tests
    def test_class_blob_initialization_type(self):
        blob = TextBlob("Python software testing.")
        assert isinstance(blob, TextBlob)

    @pytest.mark.run(order=2)
    @pytest.mark.blob_tests
    def test_class_blob_word_count_property(self):
        blob = TextBlob("Software Quality Engineering")
        assert len(blob.words) == 3  # type: ignore

    @pytest.mark.run(order=3)
    @pytest.mark.blob_tests
    def test_class_blob_sentence_count_property(self):
        blob = TextBlob("First sentence. Second sentence! Third sentence?")
        assert len(blob.sentences) == 3  # type: ignore

    @pytest.mark.run(order=4)
    @pytest.mark.blob_tests
    def test_class_blob_string_representation(self):
        text = "Executing unit test automation suite."
        blob = TextBlob(text)
        assert str(blob) == text
        assert repr(blob) == f'TextBlob("{text}")'

    @pytest.mark.run(order=5)
    @pytest.mark.blob_tests
    def test_class_blob_empty_boundary(self):
        blob = TextBlob("")
        assert len(blob.words) == 0  # type: ignore
        assert len(blob.sentences) == 0  # type: ignore

    @pytest.mark.run(order=6)
    @pytest.mark.blob_tests
    def test_class_blob_whitespace_boundary(self):
        blob = TextBlob("   \n\t   ")
        assert len(blob.words) == 0  # type: ignore


class TestTextBlobFunctions:

    @pytest.mark.run(order=7)
    @pytest.mark.blob_tests
    def test_func_correct_single_spelling_error(self):
        blob = TextBlob("I havv a dream")
        assert str(blob.correct()) == "I have a dream"

    @pytest.mark.run(order=8)
    @pytest.mark.blob_tests
    def test_func_correct_multiple_spelling_errors(self):
        blob = TextBlob("goood speling is importent")
        assert str(blob.correct()) == "good spelling is important"

    @pytest.mark.run(order=9)
    @pytest.mark.blob_tests
    def test_func_correct_already_correct_sentence(self):
        blob = TextBlob("Python is clean and readable.")
        assert str(blob.correct()) == "Python is clean and readable."

    @pytest.mark.run(order=10)
    @pytest.mark.blob_tests
    def test_func_correct_uppercase_preservation(self):
        blob = TextBlob("WRONGG")
        assert str(blob.correct()) == "WRONGG"

    @pytest.mark.run(order=11)
    @pytest.mark.blob_tests
    def test_func_correct_bva_empty_string(self):
        blob = TextBlob("")
        assert str(blob.correct()) == ""

    @pytest.mark.run(order=12)
    @pytest.mark.blob_tests
    def test_func_correct_bva_single_char(self):
        blob = TextBlob("a")
        assert str(blob.correct()) == "a"

    @pytest.mark.run(order=13)
    @pytest.mark.blob_tests
    def test_func_ngrams_bigrams_default(self):
        blob = TextBlob("unit test automation pipeline")
        ngrams = blob.ngrams(n=2)
        assert len(ngrams) == 3
        assert list(ngrams[0]) == ["unit", "test"]

    @pytest.mark.run(order=14)
    @pytest.mark.blob_tests
    def test_func_ngrams_trigrams(self):
        blob = TextBlob("unit test automation pipeline")
        ngrams = blob.ngrams(n=3)
        assert len(ngrams) == 2
        assert list(ngrams[0]) == ["unit", "test", "automation"]

    @pytest.mark.run(order=15)
    @pytest.mark.blob_tests
    def test_func_ngrams_bva_n_equals_one(self):
        blob = TextBlob("hello world")
        ngrams = blob.ngrams(n=1)
        assert len(ngrams) == 2
        assert list(ngrams[0]) == ["hello"]

    @pytest.mark.run(order=16)
    @pytest.mark.blob_tests
    def test_func_ngrams_bva_n_equals_total_length(self):
        blob = TextBlob("one two three")
        ngrams = blob.ngrams(n=3)
        assert len(ngrams) == 1
        assert list(ngrams[0]) == ["one", "two", "three"]

    @pytest.mark.run(order=17)
    @pytest.mark.blob_tests
    def test_func_ngrams_bva_n_exceeds_length(self):
        blob = TextBlob("short text")
        ngrams = blob.ngrams(n=5)
        assert len(ngrams) == 0

    @pytest.mark.run(order=18)
    @pytest.mark.blob_tests
    def test_func_ngrams_bva_empty_blob(self):
        blob = TextBlob("")
        assert len(blob.ngrams(n=2)) == 0

    @pytest.mark.run(order=19)
    @pytest.mark.blob_tests
    def test_func_ngrams_punctuation_handling(self):
        blob = TextBlob("hello, world! testing...")
        ngrams = blob.ngrams(n=2)
        assert len(ngrams) == 2
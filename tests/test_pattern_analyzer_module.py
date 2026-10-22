import csv
import pytest
from textblob.en.sentiments import PatternAnalyzer

def load_sentiment_csv():
    test_data = []
    with open('data/sentiment_test_data.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_data.append((row['text'], row['expected_polarity_type']))
    return test_data

class TestPatternAnalyzerClass:
    """Class-level unit tests for PatternAnalyzer object."""

    @pytest.fixture
    def analyzer(self):
        return PatternAnalyzer()

    @pytest.mark.run(order=3)
    @pytest.mark.sentiment_tests
    def test_analyzer_return_type(self, analyzer):
        result = analyzer.analyze("Good day")
        assert isinstance(result, tuple)
        assert len(result) == 2


class TestPatternAnalyzerFunctions:
    """Function-level unit tests for PatternAnalyzer methods."""

    @pytest.fixture
    def analyzer(self):
        return PatternAnalyzer()

    @pytest.mark.sentiment_tests
    def test_func_analyze_positive(self, analyzer):
        polarity, _ = analyzer.analyze("This project is fantastic and awesome!")
        assert polarity > 0.0

    @pytest.mark.sentiment_tests
    def test_func_analyze_negative(self, analyzer):
        polarity, _ = analyzer.analyze("This software is terrible and completely broken.")
        assert polarity < 0.0

    @pytest.mark.sentiment_tests
    def test_func_analyze_neutral(self, analyzer):
        polarity, _ = analyzer.analyze("The file was saved to the directory.")
        assert polarity == 0.0

    @pytest.mark.sentiment_tests
    def test_func_analyze_bva_polarity_range(self, analyzer):
        polarity, subjectivity = analyzer.analyze("best best best")
        assert -1.0 <= polarity <= 1.0
        assert 0.0 <= subjectivity <= 1.0

    @pytest.mark.sentiment_tests
    def test_func_analyze_bva_empty_input(self, analyzer):
        polarity, subjectivity = analyzer.analyze("")
        assert polarity == 0.0
        assert subjectivity == 0.0

    
    @pytest.mark.sentiment_tests
    @pytest.mark.parametrize("text, expected_type", load_sentiment_csv())
    def test_func_analyze_from_csv_data(self, analyzer, text, expected_type):
        polarity, _ = analyzer.analyze(text)
        if expected_type == "positive":
            assert polarity > 0.0
        elif expected_type == "negative":
            assert polarity < 0.0
        else:
            assert polarity == 0.0
import os
import csv
import pytest
import pandas as pd
from textblob import TextBlob

def get_csv_file_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "test_data_member2.csv")

def load_member2_csv_data():
    test_cases = []
    csv_path = get_csv_file_path()
    
    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            test_cases.append((
                row["tc_id"],
                row["input_text"],
                int(row["expected_word_count"]),
                row["expected_has_spelling_error"].strip().lower() == "true"
            ))
    return test_cases

class TestDataDrivenCSVAndExcel:

    def test_case_001_from_csv(self):
        data = load_member2_csv_data()[0]
        tc_id, input_text, expected_count, expected_error = data
        blob = TextBlob(input_text)
        assert len(list(blob.words)) == expected_count  # type: ignore
        actual_error = (str(blob.correct()) != input_text)
        assert actual_error == expected_error

    def test_case_002_from_csv(self):
        data = load_member2_csv_data()[1]
        tc_id, input_text, expected_count, expected_error = data
        blob = TextBlob(input_text)
        assert len(list(blob.words)) == expected_count  # type: ignore
        actual_error = (str(blob.correct()) != input_text)
        assert actual_error == expected_error

    def test_case_003_from_csv(self):
        data = load_member2_csv_data()[2]
        tc_id, input_text, expected_count, expected_error = data
        blob = TextBlob(input_text)
        assert len(list(blob.words)) == expected_count  # type: ignore
        actual_error = (str(blob.correct()) != input_text)
        assert actual_error == expected_error

    def test_case_004_from_csv(self):
        data = load_member2_csv_data()[3]
        tc_id, input_text, expected_count, expected_error = data
        blob = TextBlob(input_text)
        assert len(list(blob.words)) == expected_count  # type: ignore
        actual_error = (str(blob.correct()) != input_text)
        assert actual_error == expected_error

    @pytest.mark.parametrize("tc_id,input_text,expected_word_count,expected_has_spelling_error", load_member2_csv_data())
    def test_consume_csv_data_and_assert(self, tc_id, input_text, expected_word_count, expected_has_spelling_error):
        blob = TextBlob(input_text)
        assert len(list(blob.words)) == expected_word_count  # type: ignore
        corrected_text = str(blob.correct())
        actual_has_error = (corrected_text != input_text)
        assert actual_has_error == expected_has_spelling_error

    def test_export_task3_excel_sheet(self):
        csv_data = load_member2_csv_data()
        results = []

        for tc_id, text, exp_count, exp_error in csv_data:
            blob = TextBlob(text)
            actual_count = len(list(blob.words))  # type: ignore
            corrected_text = str(blob.correct())
            actual_error = (corrected_text != text)

            passed = (actual_count == exp_count) and (actual_error == exp_error)
            status = "PASS" if passed else "FAIL"

            results.append({
                "Test Case ID": tc_id,
                "Input Text": text,
                "Expected Word Count": exp_count,
                "Actual Word Count": actual_count,
                "Expected Spelling Error": exp_error,
                "Actual Spelling Error": actual_error,
                "Execution Status": status
            })

        df = pd.DataFrame(results)
        output_dir = os.path.dirname(os.path.abspath(__file__))
        excel_path = os.path.join(output_dir, "Member2_Test_Execution_Results.xlsx")
        
        df.to_excel(excel_path, index=False)
        assert len(df) >= 4
        assert os.path.exists(excel_path)
# Unit Test Design Notes (ECP & BVA)

## Module 1: Word
* **Equivalence Class Partitioning (ECP):**
  * Valid inputs: Standard nouns ("cat"), words ending in 'y' ("city"), irregular plurals ("goose").
  * Case handling: Preserving uppercase strings ("CAT").
* **Boundary Value Analysis (BVA):**
  * Minimum string length: Empty string `""` (0 chars).
  * Single character input: `"a"`.

## Module 2: WordList
* **Equivalence Class Partitioning (ECP):**
  * Normal list of strings vs empty collection.
  * Case sensitivity flag: `case_sensitive=True` vs `case_sensitive=False`.
* **Boundary Value Analysis (BVA):**
  * Collection boundaries: Empty list `[]` (0 elements), single element `["apple"]`, multiple elements.

## Module 3: PatternAnalyzer
* **Equivalence Class Partitioning (ECP):**
  * Positive sentiments (polarity > 0.0).
  * Negative sentiments (polarity < 0.0).
  * Neutral text (polarity == 0.0).
* **Boundary Value Analysis (BVA):**
  * Text length boundaries: Empty string `""`.
  * Output range validation: Polarity within `[-1.0, 1.0]`, Subjectivity within `[0.0, 1.0]`.
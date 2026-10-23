Unit Testing Strategy and Partitioning Notes (Yusra Malik)

Module 4: textblob.blob.TextBlob

Focus: correct() and ngrams() methods.

ECP (Equivalence Partitioning):

Valid inputs: Standard correctly spelled sentences, sentences with single or multiple typos, and mixed case strings.

Inputs containing numbers, special symbols, and punctuation.

BVA (Boundary Value Analysis):

Empty string "" (zero length).

Whitespace-only strings like "   \n\t " to verify no crash and an empty list is returned.

N-gram boundaries: n=1 (unigrams), n equal to word count, and n greater than word count (should return an empty list).

Module 5: textblob.blob.Sentence

Focus: dict property and end index property.

ECP (Equivalence Partitioning):

Declarative, interrogative (ending with ?), and exclamatory (ending with !) sentences.

Sentences created with explicit start and end character offsets versus default unindexed sentences.

BVA (Boundary Value Analysis):

Single-character sentence "A.".

Index boundaries: start=0, large offsets like start=100 and end=1000, and missing indices (None).

Empty sentence string boundary.

Module 6: textblob.en.parsers.PatternParser

Focus: parse() method (Part-of-Speech tagging).

ECP (Equivalence Partitioning):

Simple declarative statements, questions, and multi-word sentences.

Inputs with mixed word types including nouns, verbs, adjectives, and numbers.

BVA (Boundary Value Analysis):

Empty string "" input (returns empty string output).

Single word input "Execute".

Non-alphabetic inputs: purely numerical strings like "2026" and punctuation-only strings like "...!!!".
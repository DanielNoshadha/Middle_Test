import pytest
import re

# фікстура для зчитування вхідних даних з файлу
@pytest.fixture()
def file_text():
    filename = "test_file.txt"
    with open(filename, 'r') as file:
        text = file.read()
    return text

# параметризований тест для функції word_counter
@pytest.mark.parametrize("text, expected", [
    ("Hello, world!", 2),
    ("This is a test.", 4),
    ("   ", 0)
])
def test_word_counter(text, expected):
    def word_counter(text):
        words = re.findall(r'\b\w+\b', text)
        num_words = len(words)
        return num_words
    assert word_counter(text) == expected

# параметризований тест для функції sentences_counter
@pytest.mark.parametrize("text, expected", [
    ("Hello, world!", 1),
    ("This is a test.", 1),
    ("This is a test. This is only a test.", 2),
    ("   ", 0)
])
def test_sentences_counter(text, expected):
    def sentences_counter(text):
        sentences = re.findall(r'[\w\s]*[\.\?!]', text)
        num_sentences = len(sentences)
        return num_sentences
    assert sentences_counter(text) == expected



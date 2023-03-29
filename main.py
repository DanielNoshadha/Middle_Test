import re

def file_text():
    filename = "text.txt"
    with open(filename, 'r') as file:
        text = file.read()
    return text

# визначаємо кількість слів
def word_counter(text):
    words = re.findall(r'\b\w+\b', text)
    num_words = len(words)
    return print("Кількість слів у файлі:", num_words)

# визначаємо кількість речень

def sentences_counter(text):
    sentences = re.findall(r'[\w\s]*[\.\?!]+|[\w\s]*\.{3}', text)
    num_sentences = len(sentences)
    return print("Кількість речень у файлі:", num_sentences)

word_counter(file_text())
sentences_counter(file_text())
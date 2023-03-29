import re

filename = input("Введіть назву файлу: ")

with open(filename, 'r') as file:
    text = file.read()

# визначаємо кількість слів
def word_counter():
    words = re.findall(r'\b\w+\b', text)
    num_words = len(words)
    print("Кількість слів у файлі:", num_words)


word_counter()

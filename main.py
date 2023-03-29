import re

filename = input("Введіть назву файлу: ")

with open(filename, 'r') as file:
    text = file.read()


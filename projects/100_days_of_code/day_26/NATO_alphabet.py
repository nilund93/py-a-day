
import pandas
student_data_frame = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
NATO_alphabet = {row.letter: row.code for (_, row) in student_data_frame.iterrows()}
print(NATO_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What is your name? ").upper()
nato_name = [NATO_alphabet[letter] for letter in name]
print(nato_name)

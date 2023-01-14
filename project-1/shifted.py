#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrick Kariuki
Date: 01/03/2023

Bootcamp Python
Johns Hopkins University
Intersession 2023

Project 1
Problem B: Decrypting encrypted message using shifted approach.
"""
# Normal list of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#alphabet ="abcdefghijklmnopqrstuvwxyz"

# Collect the encrypted message from the user
encrypted_message = input("Enter the encrypted message: ")

# Empty list that will contain the 25 possible values
# of the decrypted messages.
possibilities = []

# Decrypt all 25 values from the encrypted message
for shifted_by in range(1, 26):
    # String representing the decrypted message
    decrypted = ""
    for letter in encrypted_message:
        if letter in alphabet:
            new_index = alphabet.index(letter) + shifted_by
            if new_index >= 25:
                new_index -= 26
                decrypted += alphabet[new_index]
            else:
                decrypted += alphabet[new_index]
        else:
            decrypted += letter
    # Append individual decrypted messages in possibilities
    possibilities.append(decrypted)


# Read the frequencies of the letters in sample, and store them in dictionary
count = {}
with open("pride_prejudice.txt", "r") as file:
    contents = file.read()
    # Count the number of occurrences of every letter in the alphabet
    for letter in contents.lower():
        if letter.isalpha(): 
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

# Total number of characters in sample
total_chars = sum(count.values())

# Calculate the Chi score for each decrypted possibility
chi_scores = []
for possibility in possibilities:
    # Chi score for each character in each possibility
    score = 0
    # Loop though each letter in each decrypted possibility
    for character in possibility:
        if character.isalpha():
            # Get the number of times character occurs in possibility
            char_count = possibility.count(character)
            # Variable holding likelihood values multiplied by
            # length of the decrypted message
            var_holder = count[character] / total_chars * len(possibility)
            # Calculate chi score for character
            score += (char_count - var_holder) ** 2 / var_holder 
    # Append individual scores to chi_scores
    chi_scores.append(score)

# Find the index of the possibility with the lowest score
lowest_score_index = chi_scores.index(min(chi_scores))

# Print the decrypted message with the lowest Chi score
print("The plaintext message is:", possibilities[lowest_score_index])

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrick Kariuki
@JHED: pkariuk1
Date: 01/03/2023

Bootcamp Python
Johns Hopkins University
Intersession 2023

Project 1
Problem A: Decrypting encrypted message using reverse alphabet.
"""
# Normal list of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# List of the alphabet in reverse order
reverse_alphabet = alphabet.copy()
reverse_alphabet.reverse()

# Collect input from user
encrypted_message = input("Enter the encrypted message: ")
# String representing the decrypted message
decrypted_message = ""

# Iterate through each letter in the user's input
for letter in encrypted_message:
    if letter in alphabet:
        # Get the index of current letter in the alphabet and get
        # the corresponding letter in the reverse alphabet list
        index = alphabet.index(letter)
        decrypted_message += reverse_alphabet[index]
    else:
        # Caters for punctuation and whitespace in encrypted message
        decrypted_message += letter

# Output to console
print("The plaintext message is:", decrypted_message)

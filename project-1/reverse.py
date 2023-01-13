#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrick Kariuki
@JHED: pkariuk1
Date: 01/03/2023

Bootcamp Python
Johns Hopkins University
Intersession 2023

Project 1A: Decrypting encrypted message using reverse alphabet.
"""
# Normal list of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# List of the alphabet in reverse order
reverse_alphabet = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p',
                    'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
                    'd', 'c', 'b', 'a']

encrypted_message = input("Enter the encrypted message: ")
# String representing the decrypted message
decrypted_message = ""

for letter in encrypted_message:
    if letter in alphabet:
        index = alphabet.index(letter)
        decrypted_message += reverse_alphabet[index]
    else:
        # Caters for punctuation and whitespace in encrypted message
        decrypted_message += letter

print("The plaintext message is:", decrypted_message)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 18:39:48 2023

@author: Patrick Kariuki
@JHED: pkariuk1
Date: 01/03/2023
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse_alphabet = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

encrypted_message = input("Enter the encrypted message: ")

decrypted_message = ""

for letter in encrypted_message:
    if letter in alphabet:
        index = alphabet.index(letter)
        decrypted_message += reverse_alphabet[index]
    else:
        decrypted_message += letter

print("The plaintext message is:", decrypted_message)

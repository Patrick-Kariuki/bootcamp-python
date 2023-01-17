#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrick Kariuki
@JHED: pkariuk1
Date: 01/09/2023

Bootcamp Python
Johns Hopkins University
Intersession 2023

Project 2
"""
# Global variables
# Dictionary to hold the binary pair - DNA base scheme
dna_encoding = {"00": "A", "01": "T", "10": "C", "11": "G"}

# Dictionary to hold DNA base - binary pair scheme
dna_decoding = {"A": "00", "T": "01", "C": "10", "G": "11"}


def encode_sequence(input_string):
    """
    Function: encode_sequence: Converts a string to an encoded DNA sequence
        that contains the same information as the string
        
    Parameters:
    ----------
    input_string : String to be encoded to a DNA sequence

    Returns:
    -------
    dna_sequence : String containing encoded DNA sequence from the input

    """
    
    # Initialize empty string to store encrypted message
    # This string will be returned by the function
    dna_sequence = ""
    
    # Iterate through each character in the input string
    for character in input_string:
        # Convert character to ascii value and then to 8 bits
        bit_form = format(ord(character), "08b")
        #Iterate though the bit pairs of the character binary form
        for i in range(0, len(bit_form), 2):
            # Get the current binary pair
            bit_pair = bit_form[i: i + 2]
            # Map the binary pair in dna_encoding to get DNA base
            # Add the encoded DNA base to the DNA sequence
            dna_sequence += dna_encoding[bit_pair]
            
    # Return the encoded dna_sequence
    return dna_sequence


def decode_sequence(dna_input):
    """
    Function: decode_sequence: Decodes a string of encoded information in DNA
        bases to a string in English text

    Parameters:
    ----------
    dna_input : DNA string to be decoded to English text
        
    Returns: 
    -------
    decoded_string : English text string decoded from dna_input
        
    """
    
    # Initialize empty string to store decoded English text message
    # This string will be returned by the function
    decoded_string = ""
    # Initialize empty string to hold binary representation of dna_input
    binary_form = ""
    
    # Iterate through bases in dna_input and get its decoded binary form
    for base in dna_input:
        binary_form += dna_decoding[base]
    # Iterate through the binary form of dna_input in steps of 8
    # Because 8 bits are used to represent ascii value of a character
    for i in range(0, len(binary_form), 8):
        # Gets the current 8 bits, convert to ascii and then character
        char_bit = binary_form[i: i + 8]
        ascii_value = int(char_bit, 2)
        # English text character added to decoded string
        decoded_string += chr(ascii_value)
    
    # Return the decoded English text
    return decoded_string


def encrypt_decrypt(string, key = "CAT"):
    """

    Parameters:
    ----------
    string : TYPE
        DESCRIPTION.
    key : TYPE, optional
        DESCRIPTION. The default is "CAT".

    Returns:
    -------
    encrypted_string : TYPE
        DESCRIPTION.

    """
    # Initialize empty string
    encrypted_string = ""
    key_index = 0
    # Iterate through the input string
    for i in range(len(string)):
        # Get the current letter and key letter
        letter = string[i]
        key_letter = key[key_index]
        # XOR the current letter with the key letter
        xor = chr(ord(letter) ^ ord(key_letter))
        # Append the resulting letter to the output string
        encrypted_string += xor
        key_index += 1
        # If key_index reaches the end of the key, start again from the beginning
        if key_index == len(key):
            key_index = 0
    return encrypted_string


def synthesizer(dna_sequence):
    return


def error_count(input_string1, input_string2):
    """
    Function: error_count: counts the number of mismatches in 2 strings

    Parameters: 
    ----------
    input_string1 : First string to be compared
    input_string2 : Second string to be compared

    Returns
    -------
    num_mismatches : Integer that gives the number of mismatches found

    """
    
    # Initialize variable to hold number of mismatches
    num_mismatches = 0
    # Iterate through the first string
    # Compare current letter with letter in same index in second string
    # If they do not match, add 1 to num_mismatches
    for index, letter in enumerate(input_string1):
        if letter != input_string2[index]:
            num_mismatches += 1
    
    # Return the number of mismatches found
    return num_mismatches


if __name__ == "__main__":
    print(encode_sequence("Frieza"))
    print(decode_sequence("TATCTGACTCCTTCTTTGCCTCAT"))
    #print(encrypt_decrypt("TAAT"))
    print(error_count("Patrick", "Kariuki"))

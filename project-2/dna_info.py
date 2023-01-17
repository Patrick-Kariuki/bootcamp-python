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
    # Dictionary to hold the binary pair - DNA base scheme
    dna_encoding = {"00": "A", "01": "T", "10": "C", "11": "G"}
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
    # Dictionary to hold DNA base - binary pair scheme
    dna_decoding = {"A": "00", "T": "01", "C": "10", "G": "11"}
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


def encrypt_decrypt(input_string, key = "CAT"):
    return


if __name__ == "__main__":
    print(encode_sequence("Frieza"))
    print(decode_sequence("TATCTGACTCCTTCTTTGCCTCAT"))
    #print(encrypt_decrypt("TAAT"))

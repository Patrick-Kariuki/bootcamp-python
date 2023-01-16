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
            
    # Return the decoded dna_sequence
    return dna_sequence

def decode_sequence(dna_input):
    """
    Function: de

    Parameters
    ----------
    dna_input : TYPE
        DESCRIPTION.

    Returns
    -------
    decoded_string : TYPE
        DESCRIPTION.

    """
    
    
    # Dictionary to hold the DNA base - binary pair scheme
    #dna_decoding = {"A": "00", "T": "01", "C": "10", "G": "11"}
    # Initialize empty string to store decoded string to be returned
    decoded_string = ""
    
    # Iterate though each base in the dna input in steps of 4
    # Because each Englist text character was converted to 8 bit to yield
    # 4 DNA bases for its encoded message
    for i in range(0, len(dna_input), 4):
        # DNA bases representing a character in English text
        char_dna_bases = dna_input[i: i + 4]
        
        # Iterate through each base in the character DNA bases
        for base in char_dna_bases:
            # Empty string to hold the binary form of the bases
            binary_form = ""
            # Map the base to binary and add to binary_form string
            if base == "A":
                binary_form += "00"
            elif base == "T":
                binary_form += "01"
            elif base == "C":
                binary_form += "10"
            else:
                binary_form += "11"
        print(binary_form)
        
        # Convert the base to binary pair form and then to ascii value
        ascii_value = int(binary_form, 2)
        # Convert ascii value to English text and add to decoded string
        decoded_string += chr(ascii_value)
        
    # Return decoded sequence
    return decoded_string


if __name__ == "__main__":
    print(encode_sequence("Frieza"))
    print(decode_sequence("TATCTGACTCCTTCTTTGCCTCAT"))

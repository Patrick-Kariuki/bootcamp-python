#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrick Kariuki
Date: 01/09/2023

Bootcamp Python
Johns Hopkins University
Intersession 2023

Project 2
"""
# Import Random module
import random

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


def encrypt_decrypt(input_string, key = "CAT"):
    """
    Function: encrypt_decrypt: Encrypt the input DNA sequence with the key
        using the XOR operation
    
    Parameters:
    ----------
    input_string : String to be encoded
        
    Optional Parameters:
    key : String to encrypt DNA sequence using XOR operation
         The default is "CAT"

    Returns:
    -------
    encrypted_string : String representing the encrypted sequence

    """
    
    # Initialize the encrypted message to return with the input string
    encrypted = input_string
    # Iterate through the bases in the key
    for i in range(len(key)):
        # Get the current base in the key
        current_key_base = key[i]
        # Initialize an empty string to hold the resulting encrypted message
        # after each iteration
        new_encrypted = ""
        # Iterate through each base in the input string and XOR it with
        # the current key base
        for j in range(len(encrypted)):
            # Since we can only XOR the binary pairs in dna decoding scheme,
            # we need to retrieve them and store the result in a retrieval
            # value. This value will then get the corresponding base from the
            # dna encoding scheme
            
            # Get the current base in encrypted
            current = encrypted[j]
            retriever = str(int(dna_decoding[current_key_base]) \
                            ^ int(dna_decoding[current]))
            
            # we need to replace the retriever value if it's 0 or 1 since 
            # the dna encoding scheme used "00" and "01"
            if retriever == "0":
                retriever = "00"
                # Get the corresponding value and add to new encrypted
                new_encrypted += dna_encoding[retriever]
            elif retriever == "1":
                retriever = "01"
                # Get the corresponding value and add to new encrypted
                new_encrypted += dna_encoding[retriever]
            # The rest match the scheme, so we add them
            else:
                new_encrypted += dna_encoding[retriever]
        # The encrypted message is passed for the next iteration
        encrypted = new_encrypted
        
    # Return the encrypted message
    return encrypted


def synthesizer(dna_sequence):
    """
    Function: synthesizer: Simulates DNA manufacturing process by a robot

    Parameters
    ----------
    dna_sequence : DNA sequence string to be turned to DNA synthesized by
        a robot

    Returns
    -------
    synthesized_dna : String of DNA synthesized by a robot

    """
    # Initialize empty string to store generated sequence
    synthesized_dna = ""
    
    # Iterate through the bases in the input dna_sequence
    for dna_base in dna_sequence:
        # Generate a random float between 0 and 1 for the synthesis
        # output possiblity
        output_possibility = random.random()
        
        # Check which base will be added based on the current base
        # and output possibility
        if dna_base == "A":
            # Base A produced 100% of the time
            synthesized_dna += "A"
        # For the rest, we will have to also account for output possibility
        # I arranged output possibility in decreasing order
        elif dna_base == "T":
            if output_possibility <= 0.90:
                synthesized_dna += "T"
            elif output_possibility <= 0.95:
                synthesized_dna += "A"
            elif output_possibility <= 0.98:
                synthesized_dna += "C"
            else:
                synthesized_dna += "G"
        
        elif dna_base == "C":
            if output_possibility <= 0.97:
                synthesized_dna += "C"
            elif output_possibility <= 0.98:
                synthesized_dna += "A"
            elif output_possibility <= 0.99:
                synthesized_dna += "T"
            else:
                synthesized_dna += "G"
        
        else:
                if output_possibility <= 0.95:
                    synthesized_dna += "G"
                elif output_possibility <= 0.97:
                    synthesized_dna += "C"
                elif output_possibility <= 0.99:
                    synthesized_dna += "T"
                else:
                    synthesized_dna += "A"
    
    # Return the Robot synthesized dna
    return synthesized_dna


def error_count(input_string1, input_string2):
    """
    Function: error_count: Counts the number of mismatches in 2 strings

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


def redundancy(n, input_string):
    """
    Function: redundancy: Obtains n copies of the synthesized DNA from
        synthesizer function, compares all n copies, to find the correct
            letter in each position

    Parameters
    ----------
    n : Integer, number of times to repeat synthesis on input
    input_string : TString to synthesize

    Returns
    -------
    error_corrected : TError corrected string with the most frequent base
        at every index in the synthesized dna sequences

    """
    # Initialize an empty list to store values returned from
    # the synthesizer function
    synthesized_dna_list = []
    
    # Use synthesizer function to obtain n copies of dna
    for i in range(n):
        synthesized_dna = synthesizer(input_string)
        synthesized_dna_list.append(synthesized_dna)
    
    # Initialize an empyt string to store the error-corrected sequence
    error_corrected = ""
    # Iterate through each dna base in the input string
    for i in range(len(input_string)):
        # Initialize a dictionary to store current dna base counts
        base_counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        # Iterate through each synthesized dna sequence
        for synthesized_dna in synthesized_dna_list:
            # Increment the count for the base at the current position
            base_counts[synthesized_dna[i]] += 1
        # Find the base that occurred most frequently
        most_frequent = max(base_counts, key=base_counts.get)
        error_corrected += most_frequent
    
    # Return error corrected string
    return error_corrected


if __name__ == "__main__":
    # For testing
    print(encode_sequence("Frieza"))
    print(decode_sequence("TATCTGACTCCTTCTTTGCCTCAT"))
    print(encrypt_decrypt("TAAT"))
    print(encrypt_decrypt("CGGC"))
    print(synthesizer("TAATCGGATCAGTACGGATCAGTACGGATCAGTACGGATCAGTACGGATCAG"))
    print(error_count("Patrick", "Kariuki"))
    print(redundancy(5, "AATCGGATCAGTACGGATCAGTAC"))

    #Sample input string of length 50
    sample_string = "TAATCGGATCAGTACGGATCAGTACGGATCAGTACGGATCAGTACGGATCAG"

    # Write name file
    with open("error_count.txt", "w", encoding="utf-8-sig") as file:
        file.write("Name: Patrick Kariuki\n")

    # Test the redundancy scheme for different values of n
    for n in [1, 2, 5, 10, 20, 50, 75, 80, 90, 100]:
        corrected_string = redundancy(n, sample_string)
        errors = error_count(sample_string, corrected_string)
        with open("error_count.txt", "a", encoding="utf-8-sig") as file:
            file.write("n = {}, errors = {} \n".format(n, errors))
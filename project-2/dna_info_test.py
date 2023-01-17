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
from dna_info import redundancy, error_count

# Sample input string of length 50
sample_string = "TAATCGGATCAGTACGGATCAGTACGGATCAGTACGGATCAGTACGGATCAG"

# Test the redundancy scheme for different values of n
for n in [1, 2, 5, 10, 20]:
    corrected_string = redundancy(n, sample_string)
    errors = error_count(sample_string, corrected_string)
    print(f"n = {n}, errors = {errors}")


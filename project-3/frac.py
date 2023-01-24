#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrick Kariuki
Date: 01/11/2023

Bootcamp Python
Johns Hopkins University
Intersession 2023

Project 3
"""
# Import math module
import math

class Frac:
    
    """ Class representing a fraction with basic operations of addition
    subtraction, multiplication and division"""
    
    def __init__(self, num, den):
        """
        Function: __init__: Initialize an instance of Frac class

        Parameters
        ----------
        num : Integer representing the fraction's numerator
        den : Integer representing the fraction's denominator

        Returns
        -------
        None.

        """
        self.num = num
        self.den = den

    def __add__(self, other):
        # Compute the numerator
        sum_num = self.num * other.den + self.den * other.num
        # Compute the denominator
        sum_den = self.den * other.den
        
        # Return sum as a simplified fraction
        return (Frac(sum_num, sum_den)).simplify()

    def __sub__(self, other):
        # Compute the numerator
        sub_num = self.num * other.den - self.den * other.num
        # Compute the denominator
        sub_den = self.den * other.den
        
        # Return difference as a simplified fraction
        return (Frac(sub_num, sub_den)).simplify()

    def __mul__(self, other):
        # Compute the numerator
        mul_num = self.num * other.num
        # Compute the denominator
        mul_den = self.den * other.den
        
        # Return product as a simplified fraction
        return (Frac(mul_num, mul_den)).simplify()

    def __truediv__(self, other):
        # Compute the numerator
        div_num = self.num * other.den
        # Compute the denominator
        div_den = self.den * other.num
        
        # Return division as a simplified fraction
        return (Frac(div_num, div_den)).simplify()

    def simplify(self):
        """
        Function: simplify: Represents a fraction in its simplified form

        Returns
        -------
        A fraction in its simplified form

        """
        # Get the greatest common divisor of numerator and denominator
        gcd = math.gcd(self.num, self.den)
        # Divide numerator and denominator with GCD to reduce fraction
        self.num //= gcd
        self.den //= gcd
        
        # Return simplified fraction
        return Frac(self.num, self.den)

    def __str__(self):
        """
        Function: __str__: Create a string that "textually represents" Frac
            object

        Returns
        -------
        A string representation of the card object

        """
        return "{}/{}".format(self.num, self.den)

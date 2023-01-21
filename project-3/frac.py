#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrick Kariuki
@JHED: pkariuk1
Date: 01/11/2023

Bootcamp Python
Johns Hopkins University
Intersession 2023

Project 3
"""
import math

class Frac:
    
    """ Class representing a fraction with basic operations of addition
    subtraction, multiplication and division"""
    
    def __init__(self, num, den):
        """
        

        Parameters
        ----------
        num : TYPE
            DESCRIPTION.
        den : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.num = num
        self.den = den

    
    def __add__(self, other):
        sum_fracs = Frac(self.num * other.den + self.den * other.num, 
                         self.den * other.den)
        return sum_fracs.simplify()
    
    def __sub__(self, other):
        difference = Frac(self.num * other.den - self.den * other.num, 
                          self.den * other.den)
        return difference.simplify()
    
    def __mul__(self, other):
        product = Frac(self.num * other.num, self.den * other.den)
        return product.simplify()
    
    def __truediv__(self, other):
        division = Frac(self.num * other.den, self.den * other.num)
        return division.simplify()
    
    def simplify(self):
        """
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        gcd_fracs = math.gcd(self.num, self.den)
        self.num //= gcd_fracs
        self.den //= gcd_fracs
        return Frac(self.num, self.den).simplify()
    
    def __str__(self):
        """
        

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return "{}/{}".format(self.num, self.den)
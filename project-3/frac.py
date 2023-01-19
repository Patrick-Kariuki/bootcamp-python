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
        self.num = num
        self.den = den

    
    def __add__(self, other):
        sum_fracs = Frac(self.num * other.den + self.den * other.num, self.den * other.den)
        return sum_fracs
    
    def __sub__(self, other):
        difference = Frac(self.num * other.den - self.den * other.num, self.den * other.den)
        return difference
    
    def __mul__(self, other):
        product = Frac(self.num * other.num, self.den * other.den)
        return product
    
    def __truediv__(self, other):
        division = Frac(self.num * other.den, self.den * other.num)
        return division
    
    def simplify(self):
        gcd_fracs = math.gcd(self.num, self.den)
        self.num /= gcd_fracs
        self.den /= gcd_fracs
        return Frac(self.num, self.den)
    
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
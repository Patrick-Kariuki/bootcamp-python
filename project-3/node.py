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

class Node:
    
    """ Node class corresponding to each of the buildings in mall """
    
    def __init__(self, ID, connected_nodes, minimum_price, fractional_price):
        """
        Function: __init__: Initialize an instance of Node class

        Parameters
        ----------
        ID : String to uniquely identify each building
        connected_nodes : List of Node IDs to which this Node has outgoing 
            edges
        minimum_price : Fraction representing the minimum accepted price 
            to make a purchase
        fractional_price : Fraction representing the fraction of buyer's 
            budget to use to buy if they can make the purchase

        Returns
        -------
        None.

        """
        self.id = ID
        self.connected_nodes = connected_nodes
        self.minimum_price = minimum_price
        self.fractional_price = fractional_price
        # The amount collected in each building after a purchase
        self.revenue = 0
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
        self.id = ID
        self.connected_nodes = connected_nodes
        self.minimum_price = minimum_price
        self.fractional_price = fractional_price
        self.revenue = 0
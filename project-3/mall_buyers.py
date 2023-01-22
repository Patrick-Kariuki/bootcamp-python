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
# Import the frac class
import frac

class Buyer:
    
    """ Buyer class corresponding to each buyer at the mall """
    
    def __init__(self, current_node_id, remaining_budget):
        """
        Function: __init__: Initialize Buyer instance

        Parameters
        ----------
        current_node_id : String representing the ID of the current Node
            the buyer is located
        remaining_budget : Frac object representing the buyer's remaining
            budget

        Returns
        -------
        None.

        """
        self.ID = current_node_id
        self.remaining_budget = remaining_budget
        
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
import frac

class Buyer:
    
    """ Buyer class corresponding to each buyer at the mall"""
    def __init__(self, current_node_id, remaining_budget):
        self.ID = str(current_node_id)
        self.remaining_budget = frac(remaining_budget)
        
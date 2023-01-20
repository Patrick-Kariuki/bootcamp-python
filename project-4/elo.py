#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Patrick Kariuki
@JHED: pkariuk1
Date: 01/15/2023

Bootcamp Python
Johns Hopkins University
Intersession 2023

Project 4
"""
# Import pandas module
import pandas as pd
import math

def calculate_ratings(past_matches):
    """
    Function: calculate_ratings: Estimates each player's skill level based
        on their past matches

    Parameters
    ----------
    past_matches : CSV file with data on the players based on past matches 

    Returns
    -------
    player_ratings : Dictionary with estimated player ratings

    """
    # Initialize each player's ratings at 1500
    player_ratings = {player: 1500 for player in range(8)}
    
    # Use a try...except block to open file
    try:
        # Extract past matches data from csv file
        df = pd.read_csv(past_matches, index_col=0)
        
        # Iterate through each row in the file to obtain the names of
        # player_A, player_B and the winner
        for index, row in df.iterrows():
            player_A = row['player_A']
            player_B = row['player_B']
            winner = row['winner']
            
            # Calculate the difference in skill levels for the 2 players
            delta_skills = (player_ratings[player_A] - \
                            player_ratings[player_B]) / 100
            
            # Calculate the probablity of both players winning the game
            prob_A_wins = math.exp(delta_skills) / 1 + math.exp(delta_skills)
            prob_B_wins = 1 - prob_A_wins
            
            # Update player ratings if player_A wins the current game
            if winner is player_A:
                player_ratings[player_A] += 5 * (1.0 - prob_A_wins)
                player_ratings[player_B] += 5 * (0.0 - prob_B_wins)
            # Update player ratings if player_A loses the current game
            else:
                player_ratings[player_A] += 5 * (0.0 - prob_A_wins)
                player_ratings[player_B] += 5 * (1.0 - prob_B_wins)
        
        # Return the player ratings dictionary
        return player_ratings
    
    # Output message if an error occurs in reading the input file
    except FileNotFoundError:
        print("File", past_matches, "cannot be found")
        
    
print(calculate_ratings("past_matches.csv"))

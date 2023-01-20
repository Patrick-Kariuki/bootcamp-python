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
# Import matplotlib module
import matplotlib.pyplot as plt
# import math module
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


def display_ratings(ratings_dict):
    """
    Function: display_ratings: Generates to the console and saves to a file 
        named projections.pdf a bar graph displaying each player's ratings

    Parameters
    ----------
    ratings_dict : Dictionary containing players and their ratings

    Returns
    -------
    None.

    """
    # Set fonts on graph
    plt.rc('font', family='serif')
    
    # Create an empty plot of size 8 inches by 8 inches
    fig = plt.figure(figsize=(8, 8))
    # Initialize a list of players from keys in ratings_dict
    players = [player for player in ratings_dict.keys()]
    # Initialize a list of player ratings from values in ratings_dict
    ratings = [rating for rating in ratings_dict.values()]
    
    # Edit range of y-axis and label displayed
    plt.ylabel('Rating', fontsize=24)
    plt.ylim(0, 1600)
    
    # Edit label ox x-axis
    plt.xlabel('Player', fontsize=24)
    
    # Adjust the tick sizes and the corresponding labels in the plot
    plt.xticks(fontsize=24)
    plt.yticks([i * 100 for i in range(16)], fontsize=24)
    
    # Draws a bar graph in the empty plot
    plt.bar(players, ratings)
    
    # Adjust axes locations and labels within the plot area
    plt.tight_layout()
    # Save the visualization
    plt.savefig('projections.pdf')
    # Display the plot
    plt.show()


def display_probs(probs_dict):
    """
    Fuction: display_probs: Generates to the console and saves to a file 
        named projections_pie.pdf a pie-chart displaying each player's 
        probability of winning a match, saves to a file named probs.csv each 
        player and their probability of winning a match

    Parameters
    ----------
    probs_dict : Dictionary containing players and their probablity of
        winning a match

    Returns
    -------
    None.

    """
    # Initialize empty dictionary to be turned to CSV
    my_dict = {}
    
    # Sort the values in dict and reverse them to get highest to lowest
    sorted_prob_values = sorted(probs_dict.values())
    sorted_prob_values.reverse()
    # Initialize an empty list to hold sorted values of players
    # from the one with highest prob value to one with lowest
    sorted_prob_players = []
    
    # Iterate through probs_dict to get the players sorted in order
    # of decreasing prob values
    for prob_value in sorted_prob_values:
        for key, value in probs_dict.items():
            if prob_value == value:
                sorted_prob_players.append(key)
    
    # Add sorted players and values to dictionary as series
    my_dict['Player'] = sorted_prob_players
    my_dict['Probability'] = sorted_prob_values
    
    # Convert to CSV and store to file
    dfr = pd.DataFrame(my_dict, index = range(8))
    dfr.to_csv("probs.csv")
    
    # Pie-chart operations
    # Labels for the pie-chart from the sorted prob list
    labels = sorted_prob_players
    # Pie-chart slice sizes from sorted values list
    slice_sizes = sorted_prob_values
    
    # Output to console and save file
    fig1, ax1 = plt.subplots()
    ax1.pie(slice_sizes, labels=labels)
    ax1.axis('equal')
    plt.savefig("projections_pie.pdf")
    plt.show()

    
ratings = calculate_ratings("past_matches.csv")
print(ratings)
display_ratings(ratings)
test_dict = {0: 0.8985, 1: 0.1437, 2: 0.2890, 3: 0.4515, 4: 0.6742, 5: 0.3096, 
             7: 0.5673, 6: 0.76892}
display_probs(test_dict)

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
# Import numpy
import numpy as np
# import math module
import math
# Import random module
import random


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
            prob_A_wins = math.exp(delta_skills) / (1 + math.exp(delta_skills))
            prob_B_wins = 1 - prob_A_wins
            
            # Update player ratings if player_A wins the current game
            if winner == player_A:
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
    plt.ylim(0, 1800)
    
    # Edit label ox x-axis
    plt.xlabel('Player', fontsize=24)
    
    # Adjust the tick sizes and the corresponding labels in the plot
    plt.xticks(fontsize=24)
    plt.yticks([i * 100 for i in range(18)], fontsize=24)
    
    # Draws a bar graph in the empty plot
    plt.bar(players, ratings)
    
    # Adjust axes locations and labels within the plot area
    plt.tight_layout()
    # Save the visualization
    plt.savefig('projections.pdf')
    # Display the plot
    plt.show()
    

def project_win_probs(ratings_dict):
    """
    Function: project_win_probs: Repeatedly simulates a completed tournament
        100 times and calculates the probability of each player winning
        the tournament

    Parameters
    ----------
    ratings_dict : Dictionary containing players and their ratings
    Returns
    -------
    possibility_win : Dictionary containing players and their probability 
        of winning the tournament
    """
    # Initialize an empty dictionary with each player's possibility of winning
    possibility_win = {player: 0 for player in range(8)}
    
    # Simulate the game 100 times
    for n in range(100):
        # These players proceed to the next round
        current_winners = []
        # List of tuples simulating the initial game plays (Figure 1)
        game_plays = [(0, 7), (1, 6), (2, 5), (3, 4)]
        # Iterate through the initial game plays
        for match in game_plays:
            # Simulate a single match between 2 players and get the winners
            winner = play_game(ratings_dict, match)
            # Add winners to current winners list
            current_winners.append(winner)
        
        # At this point, the game has 4 players who proceed to the next round
        # Update game plays for next round
        game_plays.clear()
        game_plays.append(tuple(current_winners[0:2]))
        game_plays.append(tuple(current_winners[2:4]))
        # Clear the current_winners list for new round
        current_winners.clear()
        
        # Iterate through the 2nd round game plays
        for match in game_plays:
            # Simulate a single match between 2 players and get the winners
            winner = play_game(ratings_dict, match)
            # Add winners to current winners list
            current_winners.append(winner)
        
        # At this point, the game has 2 players who proceed to the next round
        # Update game plays for next round
        game_plays.clear()
        game_plays.append(tuple(current_winners[0:2]))
        # Clear the current_winners list for new round
        current_winners.clear()
    
        # Get the final winner
        for match in game_plays:
            final_winner = play_game(ratings_dict, match)
        
        # Add a win to the final winner
        possibility_win[final_winner] += 1
    
    # Calculate the probability of each player to win as percentage
    for key, value in possibility_win.items():
        possibility_win[key] = value / 100
            
    # Return the players and their probability of winning
    return possibility_win


def play_game(ratings_dict, players):
    """
    Function: play_game: Simulates a single match between 2 players

    Parameters
    ----------
    ratings_dict : Dictionary containing players and their ratings
    players : Tuple with players playing the current match

    Returns
    -------
    The winner of the current match

    """
    # Get each player by name
    player_A = players[0]
    player_B = players[1]
    
    # Generate a random number between 0 and 1
    rand_num = random.random()
    
    # Compute the expected win probability of player_A
    delta_skills = (ratings_dict[player_A] - ratings_dict[player_B]) / 100
    prob_A_wins = math.exp(delta_skills) / (1 + math.exp(delta_skills))
    
    # Get the winner in the match
    # If rand_num is less than probability of player A winning, player A wins
    if rand_num < prob_A_wins:
        return player_A
    # Otherwise player B wins
    else:
        return player_B


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
    # Sort the keys in dict and reverse them to get highest to lowest
    sorted_prob_players = [player for player, prob in \
                           sorted(probs_dict.items(), key=lambda x: x[1])]
    sorted_prob_players.reverse()
    
    # Add sorted players and values to dictionary as series
    my_dict['Player'] = sorted_prob_players
    my_dict['Probability'] = sorted_prob_values
    
    # Convert to CSV and store to file
    dfr = pd.DataFrame(my_dict)
    dfr.to_csv("probs.csv")

    # Labels for the pie-chart from the sorted prob list
    labels = [i for i in probs_dict.keys()]
    # Pie-chart slice sizes from probs_dict
    drawing_values = np.array([i for i in probs_dict.values()])
    # Pie-chart operations
    plt.pie(drawing_values, labels = labels)
    plt.savefig("projections_pie.pdf")
    plt.show()


if __name__ == "__main__":
    # For testing
    ratings = calculate_ratings("past_matches.csv")
    print(ratings)
    display_ratings(ratings)
    probs = project_win_probs(ratings)
    print(probs)
    display_probs(probs)

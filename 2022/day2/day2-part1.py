import csv
import os
import re

path = (os.path.dirname(os.path.realpath(__file__)) + r"\input.txt")

# Opponent: A for Rock, B for Paper, and C for Scissors
# Player: X for Rock, Y for Paper, and Z for Scissors

# The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

with open(path, newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=' ')

    o_rock = 'A'
    o_paper = 'B'
    o_scissors = 'C'

    p_rock = 'X'
    p_paper = 'Y'
    p_scissors = 'Z'

    rock_point = 1
    paper_point = 2
    scissor_point = 3

    lost = 0
    draw = 3
    won = 6

    count = 0

    games = []

    for row in rowreader:

        player_wins = 0

        #row[0] == opponent
        #row[1] == player

        #Rock
        if row[0] == o_rock and row[1] == p_rock:
            player_result = draw + rock_point
        
        if row[0] == o_rock and row[1] == p_paper:
            player_result = won + paper_point

        if row[0] == o_rock and row[1] == p_scissors:
            player_result = lost + scissor_point

        #Paper
        if row[0] == o_paper and row[1] == p_rock:
            player_result = lost + rock_point
        
        if row[0] == o_paper and row[1] == p_paper:
            player_result = draw + paper_point

        if row[0] == o_paper and row[1] == p_scissors:
            player_result = won + scissor_point

        #Scissors
        if row[0] == o_scissors and row[1] == p_rock:
            player_result = won + rock_point
        
        if row[0] == o_scissors and row[1] == p_paper:
            player_result = lost + paper_point

        if row[0] == o_scissors and row[1] == p_scissors:
            player_result = draw + scissor_point

        count = count + 1

        round = {
            "match": count,
            "opponent": row[0],
            "player": row[1],
            "result": player_result
        }

        games.append(round)

    total_score = sum(round['result'] for round in games)

    print(total_score)



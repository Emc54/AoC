with open("input","r") as f:
    data = f.read().split("\n")

# import re

# # Initialize an empty dictionary to store the parsed data
# games_data = {}

# # Split the input data by lines
# games = data

# # Iterate over each game
# for game in games:
#     # Split the game data into game number and rounds
#     game_info, rounds_data = game.split(':')
    
#     # Initialize a dictionary to store rounds for each game
#     game_rounds = {}
    
#     # Split the rounds and iterate over them
#     for round_data in rounds_data.split(';'):
#         # Initialize a dictionary to store color and number pairs for each round
#         round_colors = {}
        
#         # Split the color/number pairs and iterate over them
#         for color_data in round_data.strip().split(','):
#             # Split each pair into color and number
#             number, color = color_data.strip().split()
            
#             # Add the color and number to the round_colors dictionary
#             round_colors[color] = int(number)
        
#         # Add the round_colors dictionary to the game_rounds dictionary
#         game_rounds[len(game_rounds) + 1] = round_colors
    
#     # Add the game number and its corresponding game_rounds dictionary to the games_data dictionary
#     games_data[game_info] = game_rounds

# # Print the resulting nested dictionary
# print(games_data)

# impossibles = []
# # red 12, green 13, blue 14
# for game, rounds in games_data.items():
#     for round in rounds.values():
#         for color, val in round.items():
#             if color == "red" and val > 12:
#                 break
#             if color == "green" and val > 13:
#                 break
#             if color == "blue" and val > 14:
#                 break
#             else:
#                 continue
#         break    
#     impossibles.append(game)
    
# print(impossibles)


possible = {'red': 12, 'green': 13, 'blue': 14}
possible_games = 0
for id, game in enumerate(data, start=1):
    game = game.split(': ')[1]
    for hand in game.split('; '):
        is_impossible = False
        for subset in hand.split(', '):
            n, color = subset.split()
            if int(n) > possible[color]:
                is_impossible = True
                break
        if is_impossible:
            break
    else:
        possible_games += id
print(possible_games)
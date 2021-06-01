"""
Model to simulate a tournament of 7 games, with probability of a 'BlueJays' win in a game uniformly distributed between upper and lower bounds.
"""

import numpy as np

win_prob = {'Game1':np.random.uniform(0.6, 0.7),
            'Game2':np.random.uniform(0.57, 0.72),
            'Game3':np.random.uniform(0.43, 0.53),
            'Game4':np.random.uniform(0.35, 0.50),
            'Game5':np.random.uniform(0.4, 0.6),
            'Game6':np.random.uniform(0.5, 0.6),
            'Game7':np.random.uniform(0.5, 0.65)}

def Game(prob):
    r = np.random.uniform(0,1)
    winner = 'BlueJays' if r<prob else 'Opponent'
    return winner

def Series(win_prob):
    score = {'BlueJays':0,
             'Opponent':0}
    num_games=0
    for game, prob in win_prob.items():
        num_games+=1
        winner = Game(prob)
        score[winner] = score[winner]+1
        for index, val in score.items():
            if val==4:
                return num_games, score['BlueJays']

simulations = 1000
num_games=[]
tbj_wins=[]
for i in range(simulations):
    win_prob = {'Game1': np.random.uniform(0.6, 0.7),
                'Game2': np.random.uniform(0.57, 0.72),
                'Game3': np.random.uniform(0.43, 0.53),
                'Game4': np.random.uniform(0.35, 0.50),
                'Game5': np.random.uniform(0.4, 0.6),
                'Game6': np.random.uniform(0.5, 0.6),
                'Game7': np.random.uniform(0.5, 0.65)}
    games, wins = Series(win_prob)
    num_games.append(games)
    tbj_wins.append(wins)

games, count = np.unique(num_games, return_counts=True)

print("Probability of 7 games:",count[games==7]/count.sum())

print("Probability of T. BlueJays win:",tbj_wins.count(4)/len(tbj_wins))
import csv

import pandas as pd
import matplotlib.pyplot as plt
from codons import EMOTION_CODES
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
bins = [0, 20, 40, 50, 70, 80]
df = pd.read_csv(f'{dir_path}/ras.csv', sep=',')

with open(f'{dir_path}/ras.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    plt.ion()
    plt.yticks(list(EMOTION_CODES.values()), list(EMOTION_CODES.keys()))
    plt.axis([0, 1195840, 0, 100])
    plt.legend(EMOTION_CODES)
    for row in plots:
        value=int(row[1])
        color = 'black'
        if value > 70:
            color = 'red'
        elif value > 50:
            color = 'pink'
        elif value > 40:
            color = 'gray'
        elif value > 30:
            color = 'lightblue'
        elif value > 20:
            color = 'blue'
        elif value > 10:
            color = 'green'
        plt.bar(int(row[0]),int(row[1]), color=color, width=35)
    plt.show()
    input("Press Enter to continue...")

colors = {'Happy': 'red',
          'Surprise': 'orange',
          'Neutral': 'gray',
          'Sad': 'lightblue',
          'Fear': 'blue',
          'Great': 'green',
          'Disgust': 'black'}

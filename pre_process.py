import pandas as pd
import numpy as np

df = pd.read_csv('./data/2017_plays.csv')
sf_plays = df[df['TeamWithPossession'] == 'San Francisco 49ers']
print(sf_plays.head())
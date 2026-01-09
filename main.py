import pandas as pd
import numpy as np

df = [pd.read_csv(f'./data/{year}_plays.csv') for year in range(2017, 2025)]
df = pd.concat(df)
sf_plays = df[df['TeamWithPossession'] == 'San Francisco 49ers']
sf_plays.drop(columns=['Day', 'Date', 'DriveNumber', 'TeamWithPossession', 'IsScoringDrive', 'PlayNumberInDrive'], inplace=True)
print(sf_plays)
import numpy as np
import pandas as pd

df = pd.read_csv('imdb_top_1000.csv')
print(df)
result = df.head()
result2 = df.head(10)
result3 = df.tail()
result4 = df.tail(10)
'''
result5 = df.columns
for column in df.columns:
    print(column)
'''
# Meta_score, IMDB_Rating, Released_Year, No_of_Votes
result5 = df['Series_Title']
result6 = df['Series_Title'].head()
result7 = df[['Series_Title', 'Meta_score']].head()
result8 = df[['Series_Title', 'Meta_score']].tail(7)
result9 = df[5:10][['Series_Title', 'Meta_score']].head()
result10 = df[['Series_Title', 'Meta_score', 'IMDB_Rating']][df['IMDB_Rating'] > 8.0].head(50)
result11 = df['Released_Year'][(df['Released_Year'] >= '2014') & (df['Released_Year'] <= '2015')]

result12 = df[['No_of_Votes', 'IMDB_Rating']][(df['No_of_Votes'] > 100000) | ((df['IMDB_Rating'] >= 8) & (df['IMDB_Rating'] <= 9))]
print(result12)
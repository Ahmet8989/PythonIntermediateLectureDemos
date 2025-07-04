import numpy as np
import pandas as pd

'''
with open("sample.csv", "x", encoding="utf-8") as file:
    file.write("")
with open("sample.json", "x", encoding="utf-8") as file:
    file.write("")
with open("sample.xlsx", "x", encoding="utf-8") as file:
    file.write("")

'''
'''
df = pd.read_csv('sample.csv')
print(df)
df = pd.read_csv('sample.json')
print(df)
# For reading excel file, we need extra library
# pip install xlrd
'''

df = pd.read_excel('sample.xlsx')
print(df)
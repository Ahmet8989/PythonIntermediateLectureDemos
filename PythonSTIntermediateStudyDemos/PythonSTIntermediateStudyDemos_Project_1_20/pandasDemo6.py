import numpy as np
import pandas as pd

employeeFile = {
    'Employee' : ["Jessica Black", "Jason North", "James Iron", "Norman Prince", "Robin Love", "Samantha Steel", "Jonathan Long"],
    'Department' : ["Human Resources", "IT", "Accounting", "Human Resources", "IT", "Accounting", "IT"],
    'Age' : [30, 25, 45, 50, 23, 34, 42],
    'City' : ["London", "New York", "Madrid", "New York", "Madrid", "New York", "London"],
    'Salary' : [5000, 3000, 4000, 3500, 2750, 6500, 4500]   
}

df = pd.DataFrame(employeeFile)

result = df['Salary'].sum()
result2 = df.groupby('Department').groups
result3 = df.groupby(['Department','City']).groups

cities = df.groupby('City')
for name, group in cities:
    print(name)
    print(group)
    print("===")
print("==========")
departments = df.groupby('Department')
for name,group in departments:
    print(name)
    print(group)
    print("===")
print("==========")
result4 = df.groupby('City').get_group('London')
result5 = df.groupby('Department').get_group('IT')
result6 = df.groupby('Department')[['Age', 'Salary']].sum()
result7 = df.groupby('Department')[['Age', 'Salary']].mean()
result8 = df.groupby('City')['Age'].mean()
result9 = df.groupby('City')['Employee'].count()
result10 = df.groupby('Department')['Age'].max()
result11 = df.groupby('Department')['Salary'].min()
result12 = df.groupby('Department')['Salary'].max()['Accounting']
result13 = df.groupby('Department')[['Salary', 'Age']].sum()

print(result13)

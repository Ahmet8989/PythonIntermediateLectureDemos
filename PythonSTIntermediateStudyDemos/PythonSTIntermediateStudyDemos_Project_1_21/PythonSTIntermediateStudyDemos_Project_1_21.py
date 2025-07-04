import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
'''
'''
plt.plot(x)
plt.show()
'''

# plt.plot(x, y, color="red", linewidth="5")
# plt.plot(x, y, "-g") # It draws green solid line
# plt.plot(x, y, "--g") # It draws green dashed line
'''
plt.plot(x, y, "o--r") # It draws red dashed line with round marker format -> marker, line, color
plt.axis([0, 6, 0, 20])
plt.title("EXAMPLE GRAPH")
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
'''
'''
x = np.linspace(0, 4, 100)
plt.plot(x, x, label="Linear", color="red")
plt.plot(x, x ** 2, label="Quadratic", color="yellow")
plt.plot(x, x** 3, label="Cubic", color="green")
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")

plt.legend()
plt.title("Simple Plot")

plt.show()
'''
'''
x = np.linspace(0, 4, 100)

figure,axess = plt.subplots(4)

axess[0].plot(x, x, color="red")
axess[0].set_title("Graph1")
axess[1].plot(x, x ** 2, color="yellow")
axess[1].set_title("Graph2")
axess[2].plot(x, x ** 3, color="green")
axess[2].set_title("Graph3")
axess[3].plot(x, x ** 4, color="blue")
axess[3].set_title("Graph4")
'''
'''
x = np.linspace(0, 4, 100)

figure,axess = plt.subplots(2, 2)
figure.suptitle("EXAMPLE GRAPH")

axess[0, 0].plot(x, x, color="red")
axess[0, 0].set_title("Graph1")
axess[0, 1].plot(x, x ** 2, color="yellow")
axess[0, 1].set_title("Graph2")
axess[1, 0].plot(x, x ** 3, color="green")
axess[1, 0].set_title("Graph3")
axess[1, 1].plot(x, x ** 4, color="blue")
axess[1, 1].set_title("Graph4")
plt.tight_layout()

figure.savefig('example.png')
figure.savefig('example.pdf')
'''
'''
years = [2011, 2012, 2013, 2014, 2015]
player1 = [10, 12, 13, 15, 17]
player2 = [4, 5, 6, 7, 8]
player3 = [5, 6, 7, 8, 9]

# STACK PLOT

plt.plot([], [], color="y", label = "player1")
plt.plot([], [], color="r", label = "player2")
plt.plot([], [], color="b", label = "player3")
plt.stackplot(years, player1, player2, player3, colors=['y', 'r', 'b'])
plt.title("Scores")
plt.xlabel("Years")
plt.ylabel("Number of Scores")
'''

# PIE GRAPH

'''
goalTypes = ["Right Foot", "Left Foot", "Head"]
goals = [10, 12, 13]
colors = ['y', 'r', 'b']
plt.pie(goals, labels = goalTypes, colors = colors, shadow = True, explode = (0.05, 0.05, 0.05), autopct = "%1.1f%%")
'''

# BAR GRAPH

'''
plt.bar([0.35, 1.35, 2.35, 3.35, 4.35], [40, 20, 30, 50, 70], label="BMW", width=0.4)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [70, 20, 30, 50, 60], label="Audi", width=0.4)

plt.xlabel("DAY")
plt.ylabel("Distance (km)")
plt.title("CAR DATA")
'''

# HISTOGRAM GRAPH

ages = [22, 55, 62, 45, 23, 22, 34, 43, 43, 103, 95, 85, 55, 110, 120, 130, 70, 65, 55]
ageGroups = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 

plt.hist(ages, ageGroups, histtype = "bar", rwidth = 0.6)
plt.xlabel("AGE GROUPS")
plt.ylabel("NUMBER OF PEOPLE")
plt.title("HISTOGRAM EXAMPLE")

plt.show()
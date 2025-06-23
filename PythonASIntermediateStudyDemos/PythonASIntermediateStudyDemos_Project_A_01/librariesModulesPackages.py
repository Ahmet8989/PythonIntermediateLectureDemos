import numpy as np
import matplotlib.pyplot as mayplot

salaryList = np.random.normal(4000, 500, 1000) # average : 4000, data number : 1000

result = np.mean(salaryList)

matplot.hist(salaryList, 50)
matplot.show()

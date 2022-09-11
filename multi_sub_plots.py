import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

flight_data=sns.load_dataset('flights')
iris_data=sns.load_dataset('iris')

sns.set_style("darkgrid")
fig, ax = plt.subplots(nrows=2, ncols=2)
ax1, ax2, ax3, ax4 = ax.flatten()

sns.lineplot(x="month",y="passengers", data=flight_data)
sns.lineplot(x="month",y="passengers", data=flight_data)
sns.lineplot(x="month",y="passengers", data=flight_data)
sns.lineplot(x="species",y="sepal_length", data=iris_data)
sns.lineplot(x="species",y="sepal_length", data=iris_data)
sns.lineplot(x="species",y="sepal_length", data=iris_data)

plt.show()
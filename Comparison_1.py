from Assignment8 import dataframe
import seaborn as sns
import matplotlib.pyplot as plt

dataframe_1 = dataframe()

sns.scatterplot(data=dataframe_1, x="Edible Status", y="Odor")
plt.title("Edible Status vs Odor")
plt.show()
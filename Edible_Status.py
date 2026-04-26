from Assignment8 import dataframe
import seaborn as sns
import matplotlib.pyplot as plt

dataframe_1 = dataframe()

sns.histplot(data=dataframe_1, x='Edible Status', bins=2)
plt.title("Edible Distribution")
plt.ylabel("Count")
plt.show()
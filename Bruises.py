from Assignment8 import dataframe
import seaborn as sns
import matplotlib.pyplot as plt

dataframe_1 = dataframe()

sns.histplot(data=dataframe_1, x='Bruises', bins=2)
plt.title("Bruise Distribution")
plt.ylabel("Count")
plt.show()
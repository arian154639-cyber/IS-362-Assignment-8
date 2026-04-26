from Assignment8 import dataframe
import seaborn as sns
import matplotlib.pyplot as plt

dataframe_1 = dataframe()

sns.histplot(data=dataframe_1, x='Odor', bins=9)
plt.title("Odor Distribution")
plt.ylabel("Count")
plt.show()

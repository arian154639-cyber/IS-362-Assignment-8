from Assignment8 import dataframe
import seaborn as sns
import matplotlib.pyplot as plt

dataframe_1 = dataframe()

sns.scatterplot(data=dataframe_1, x="Bruises", y="Edible Status")
plt.title("Bruises vs Edible Status")
plt.show()

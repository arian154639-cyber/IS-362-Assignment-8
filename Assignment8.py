import pandas as pd

def dataframe():
    dataframe_1 = pd.read_csv("agaricus-lepiota.data", header=None)
    dataframe_1 = dataframe_1[[0, 5, 4]]
    dataframe_1.columns = ["Edible Status", "Odor", "Bruises"]

    dataframe_1["Edible Status"] = dataframe_1["Edible Status"].map({
        "e": 0,
        "p": 1
    })

    dataframe_1["Odor"] = dataframe_1["Odor"].map({
        "a": 0,
        "l": 1, 
        "c": 2,
        "y": 3,
        "f": 4,
        "m": 5,
        "n": 6,
        "p": 7,
        "s": 8
    })

    dataframe_1["Bruises"] = dataframe_1["Bruises"].map({
        "f": 0,
        "t": 1
    })
    return dataframe_1

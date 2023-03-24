import pandas as pd
import numpy as np
import seaborn as sns


file = pd.read_csv('medicine_dataset.csv')
df = pd.DataFrame(file)


print(df.head())
print(df.columns.to_list())
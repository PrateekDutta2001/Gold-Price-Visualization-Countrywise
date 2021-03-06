# -*- coding: utf-8 -*-
"""simple-visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17teU39HEbmg96P3rY3KK4huEUV7rJUON
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive/')
# %cd /gdrive

ls

cd/gdrive/My Drive/Gold Rate/

ls

import pandas as pd
import numpy as np
import seaborn as sns
import os

df = pd.read_csv("annual_gold_rate.csv")
data = df.copy()

data.head()

data.describe().T

data.isnull().sum()

data["INR"].fillna(data.INR.mean(), inplace = True)
data["AED"].fillna(data.AED.mean(), inplace = True)
data["CNY"].fillna(data.CNY.mean(), inplace = True)

data["USD"].describe().T

"""## USD"""

sns.lineplot(x = "Date", y = "USD", data = data);

sns.kdeplot(data.USD, shade = True);

sns.scatterplot(x = "Date", y = "USD", data = df);

sns.lmplot(x = "USD", y = "Date", data = data);

"""## Euro"""

sns.lineplot(x = "Date", y = "EUR", data = data);

sns.kdeplot(data.EUR, shade = True);

sns.scatterplot(x = "Date", y = "EUR", data = df);

sns.lmplot(x = "EUR", y = "Date", data = data);

"""## GBP"""

sns.lineplot(x = "Date", y = "GBP", data = data);

sns.kdeplot(data.GBP, shade = True);

sns.scatterplot(x = "Date", y = "GBP", data = df);

sns.lmplot(x = "GBP", y = "Date", data = data);

"""## INY"""

sns.lineplot(x = "Date", y = "INR", data = data);

sns.kdeplot(data.INR, shade = True);

sns.scatterplot(x = "Date", y = "INR", data = df);

sns.lmplot(x = "INR", y = "Date", data = data);

"""## AED"""

sns.lineplot(x = "Date", y = "AED", data = data);

sns.kdeplot(data.AED, shade = True);

sns.scatterplot(x = "Date", y = "AED", data = df);

sns.lmplot(x = "AED", y = "Date", data = data);

"""## CNY"""

sns.lineplot(x = "Date", y = "CNY", data = data);

sns.kdeplot(data.CNY, shade = True);

sns.scatterplot(x = "Date", y = "CNY", data = df);

sns.lmplot(x = "CNY", y = "Date", data = data);
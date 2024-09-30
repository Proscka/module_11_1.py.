import requests
import numpy as np
import pandas as pd

r = requests.get("https://api.github.com", auth = ("user","pass"))
print(r.status_code)
print(r.json())
print(requests)

a = np.array([10,11,12,13,14])
b = np.array([2,4,6,8])
print(a)
print(b)
print(a[:3])
print(b[0])

a = pd.Series([1,4,6,np.nan,7,8])
dates = pd.date_range("19730101", periods = 4)
print(a,dates, a.value_counts())



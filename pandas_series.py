# -*- coding: utf-8 -*-

import pandas as pd


serie = pd.Series([30, 40, 32, 5, 1001])

print(serie) # prints list serie
print(serie.sum()) # sum all list values

# to update

serie.put(indices=2, values=60)
print(serie)

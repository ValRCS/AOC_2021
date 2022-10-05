import pandas as pd
# create random 2d array of 100 rows and 4 columns
import numpy as np
np.random.seed(42)
df = pd.DataFrame(np.random.randint(0,10000,size=(100, 3)), columns=list('ABC'))
# save to csv
df.to_csv('2d.csv', index=False)
print(df.describe())
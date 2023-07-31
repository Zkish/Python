import pandas as pd
dfpath = "/FilesAndPictures/google-stock.csv"
df = pd.read_csv(dfpath)
print(df.shape)
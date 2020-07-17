import pandas as pd


data = pd.DataFrame.from_dict({'a':[1,2,3],'b':[1,2,3]})

for index,rows in data.iterrows():
    print(index)


print(len(data))
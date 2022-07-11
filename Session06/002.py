import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('D:\\Personal\\Courses\\DCBootCamp\\dosyalar\\projects.csv')
print(df)

df=df.reset_index().drop('index', axis=1)
df.info()
# find the number of residential project vs Industerial Projects
tmpdf=df.type.value_counts()
tmpdf
print(plt.pie(tmpdf.values, labels= tmpdf.index))
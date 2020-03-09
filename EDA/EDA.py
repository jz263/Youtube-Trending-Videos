import pandas as pd
import numpy as np
import os
from plotnine import *
os.chdir('C:/Users/Jiajie Zhang/mbds-cee-690/Project/00_source_data')
os.getcwd()
category =pd.read_json('youtube-new/CA_category_id.json')['items']
df = pd.read_csv('youtube-new/CAvideos.csv')
df['video_id'].value_counts()
test = df.loc[df['video_id']== 'VYOjWnS4cMY']
df.dtypes
(ggplot()+
geom_point(test,aes(x = 'trending_date',y = 'views'))
)

df.groupby('category_names')['views'].describe()

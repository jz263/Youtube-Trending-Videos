
import pandas as pd
import numpy as np
import os


os.chdir('./20_intermediate_files')
os.getcwd()


df = pd.read_csv('data_w_cate_mean.csv')
# %% codecell
df.dtypes


#df.columns
cols = ['trending_days','likes', 'dislikes', 'comment_count','like_dislike_ratio','mean_views',
       'mean_likes', 'mean_dislikes', 'mean_comment_count',
       'mean_trending_days','views']
df[cols] = (df[cols] - df[cols].mean())/df[cols].std()


df_cate_dummy =  pd.get_dummies(df['category_id'],drop_first=True)
df_cate_dummy.head()


df_new = df.merge(df_cate_dummy,left_index=True,right_index=True)


df_new.to_csv('data_std_dummy.csv')

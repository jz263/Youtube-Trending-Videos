import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
import pymc3 as pm
os.environ['THEANO_FLAGS'] = 'device=cpu'

os.chdir('C:/Users/Jiajie Zhang/mbds-cee-690/Project/20_intermediate_files')
os.getcwd()
df = pd.read_csv('data_w_cate_mean.csv')
predictors = ['trending_days','likes', 'dislikes', 'comment_count','like_dislike_ratio','mean_views',
       'mean_likes', 'mean_dislikes', 'mean_comment_count',
       'mean_trending_days']
df_X_raw = df[predictors]
df_y_raw = df['views']
#standardize
df_X = (df_X_raw - df_X_raw.mean())/df_X_raw.std()
df_y = (df_y_raw- df_y_raw.mean())/df_y_raw.std()

### create a multi-linear regression model
multi_model = pm.Model()
with multi_model:
    intercept = pm.Normal('intercept',mu = 0,sd = 100)
    beta =  pm.Normal('beta',sd = 100,shape = len(predictors))
    variance = pm.InverseGamma('variance',alpha = 0.1,beta = 0.1)
    sd = pm.Deterministic('sd',variance**0.5)
    yhat = pm.Deterministic('yhat',intercept +pm.math.dot(df_X,beta))
    y = pm.Normal('y',mu = yhat,sd=sd, observed = df_y)

with multi_model:
    trace = pm.sample(draws = 200,tune = 1000,cores = 1)

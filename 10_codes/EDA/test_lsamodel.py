import os
os.chdir('C:/Users/Jiajie Zhang/mbds-cee-690/Project/10_codes/EDA')
os.getcwd()

from LSA_model import *

#read in dataset
df = pd.read_csv('../../20_intermediate_files/data_std_dummy.csv')
df_tags = df['tags']
#run lsa model
number_of_topics=9
words=10
LSA = Bayesian_Lsi()
clean_text = LSA.preprocess_data(df_tags)

model=LSA.create_gensim_lsa_model(clean_text)

new_df = LSA.concat_lsa(model)
start,stop,step=2,17,1
#plot_graph(clean_text,start,stop,step)

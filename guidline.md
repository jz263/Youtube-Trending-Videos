===All empirical models
1. Model Criticism
  Comparison:
    AIC/WAIC
    CV accuracy
    'reasonableness' /parsinmony

2. Performance ' in the wild ':

===Bayesian
Posterior checks ()
Prior checks (before check)

Compare ML model to Bayesian Model:
  Usually use CV accuracy
  AIC/WAIC or Parsimony is not applicable here

Bayesian autoregression:
  $AR1: Xt = rho *Xt-1 +Er_t$
  -CAR

Multiple regresson vs. Multivariate regression:
  Multivariate regression: predicitng multiple output at same time

Categorical:
  # of categories
  Text => 100 binary cols or =>5 cols by grouping

Text
  1. cols = binary variables (len(sntence))
  2. Stemming: walking -walk (NLP stemming lib)
  3. LSI: feature selection
    try use lower dimension vectors
  4. words with low frequency but highly informative:
    a. upweight them by showing them more frequently
    b. get rid of as many as the less informative words

Events/Seasons:
  

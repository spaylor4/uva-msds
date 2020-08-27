# Supervised Learning

Readings: ISL 1, 2.1; ESL 1, 2.1-2.4

- Statistical learning involves estimating the systematic information ($f(X)$) that some set of predictors/features ($X$) provide about a response ($Y$). 
- Estimating $f$ can be used for prediction (in which case the actual form of $f$ is not important) and for inference (in which the form of $f$ is used to answer questions about the relationship between the response and various predictors).
  - Linear models are usually more easily interpretable for inference, but may or may not provide the most accurate predictions. Generally, as models get more flexible, they also get less interpretable. Highly flexible models are also more susceptible to overfitting.
- *Parametric* statistical learning methods involve estimating parameters for an assumed form (e.g. linear) of a model $f$. *Non-parametric* methods do not make explicit assumptions about the form of $f$.
  - A downside of parametric methods is that if the chosen form of $f$ differs significantly from the true $f$, the model will not fit the data well.
  - A downside of non-parametric methods is that they require a much larger number of observations $n$ to accurately estimate $f$.
- *Supervised* learning problems have a response variable associated with the data, while *unsupervised* ones do not.
  - Clustering is one example of unsupervised learning.
- Generally, problems with a quantitative response variable are called *regression* problems, while those with a qualitative response are called *classification* problems.
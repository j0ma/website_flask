---
title: Statistical tests == linear models
author: Jonne Saleva
---

![](https://upload.wikimedia.org/wikipedia/commons/d/d4/Thomas_Bayes.gif)

Yesterday, I came across [this wonderful post](https://eigenfoo.xyz/tests-as-linear/) about how *common statistical tests are essentially linear models*.

This is super exciting, for the following reasons:

- Statistical hypothesis testing is often taught in a way that is very confusing, and prone to misinterpretation. For example, consider how often confidence intervals get interpreted as their Bayesian counterparts.

- In addition to tests, people who take "statistical methods" courses are often also taught about ANOVA, fixed/random/mixed effect models etc. Learning about any of these usually comes with a long laundry list 

- On the other hand, in ML and NLP, people rarely learn about the aforementioned conceptes, but they **do** learn linear regression! Using this fundamental linear models -- tests connection, ML practicioners can now use and apply all statistical tests only using linear regression.

- Since linear models are very easily extended to be Bayesian, we can suddenly start to perform *Bayesian hypothesis testing* in addition to all other potential questions we may be interested in asking.

- Bayes also lets us ask these questions in an intuitive way!

$$
\boxed{\text{So, to summarize: this connection + Bayes = interpretable inferences from experiments!}}
$$

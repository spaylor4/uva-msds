# Density Estimation

Readings: IPSUR ch. 9.1 MLE Intro, [Maximum Likelihood Estimation](https://www.math.arizona.edu/~jwatkins/O_mle.pdf), IPSUR ch. 5-7 Random Variable review; [Silverman](https://books.google.com/books?id=e-xsrjsL7WkC&lpg=PP1&pg=PA20#v=onepage&q&f=false) ch. 2.1-2.6

- Histograms provide a simple density estimator.
- The naive estimator counts the number of observations falling within a range centered on each $x$ divided by the total number of observations times the width of the range.
  - Not a continuous function; more like a histogram with each observation having a bin.
- Kernel estimators sum probability distribution functions (often Gaussian) centered at each observation.
  - As with naive estimator, depends on smoothing parameter $h$, the window width.
  - Gives a smooth/continuous pdf.
  - Can show spurious noise in long-tailed distributions.
- K-nearest neighbor estimators adapt the amount of smoothing to the local density of the data.
  - Related to naive estimator and likewise is not smooth.
- Variable kernel estimator marries classical kernel and k-nearest neighbor approaches to produce a smooth curve but have flatter kernels where observations are sparse.

### Point Estimation

- For a family of PDFs $f(x | \theta)$ with parameter $\theta$ and $n$ i.i.d. random samples, the likelihood function of the observed data $x_1, x_2, ... x_n$ is $L(\theta) = \prod_{i=1}^n f(x_i | \theta)$.  The maximum likelihood estimator (MLE) $\hat\theta$ is the value of $\theta$ that maximizes the likelihood function.
  - The maximum log likelihood and maximum likelihood occur at the same value of $\theta$.
  - Method of moments (MOM) estimators are one alternative to MLEs.
- If $E(\hat\theta) = \theta$, then $\hat\theta$ is an unbiased estimator.

## Class Notes

*October 1, 2020*

- Transitioning to unsupervised learning; will return to supervised later with trees and boosting, among others.
- Parametric distributions can be fully characterized by a set of parameters, $\theta$. 
  - E.g. for Gaussian distribution, parameters are mean $\mu$ and standard deviation $\sigma$ and for Poisson distribution, parameter is rate $\lambda$.
- Non-parametric methods estimate distributions without enforcing a parametric family.
  - Non-parametric methods will perform better than parametric (with enough data) when true distribution differs from chosen parametric distribution.
- Density estimation can be useful in association analysis.
  - E.g. market basket analysis: what items shoppers tend to buy together.
- Also useful for anomaly detection (e.g. covid water treatment analysis project that Prof. Porter is working on).
  - Is there a distribution controlling the outliers?
- Fitting Poisson disease outbreak example:
  - Previously minimized loss for fitting, now maximizing likelihood (or log-likelihood).

*October 6, 2020*

- Density histogram most appropriate for unequal binwidths.
- Histograms are local estimates of density: only observations within a bin contribute to bin height. Unlike parametric density estimation, where all observations impact the parameters.
  - Local estimates are good if you have enough data.
- Histogram bin width analagous to kernel density estimate bandwidth parameter.
  - Can think of bin width and bin anchor points/shifts as tuning parameters.
- Bin anchor points: how to estimate density for point on a bin border?
  - Frequency polygon connects midpoint of each bin with a line. Can implement in ggplot.
  - Average shifted histogram takes average density for several different bin anchor points.
  - Kernel density estimates avoid issue of bin anchor points entirely (although they still have bandwidth). KDEs are basically continuous moving window estimates.
- KDE larger bandwidth gives smoother estimate. See shiny [app](https://pasda.shinyapps.io/Old_Faithful/) for exploring effects.
- Kernel is the shape used at each point - Gaussian kernel commonly used.
  - Gaussian kernel gives better and smoother estimates than rectangular kernel.
  - If you have big data or need to predict over a wide range, may want to consider different kernels (e.g. biweight) with compact support, since Gaussian will almost never have values outside 3-4 standard deviations of the mean.
  - Bandwidth corresponds to standard deviation of  kernel distribution used (e.g. Gaussian).
- Density estimation can be used for clustering, anomaly detection, and classification (among others). Optimal bandwidth depends on the problem you have.
- Plug-in method of choosing bandwidth parameter uses sample standard deviation to choose optimal bandwidth. Cross-validation is other common method for selecting best bandwidth.
  - Professor Porter recommends any of the cross-validation methods in the `kde` function.
- Multivariate Gaussians have mean vector and variance-covariance matrix.
  - Variance-covariance matrix controls orientation, shape, and volume of density contours.
  - Five model parameters in bivariate Gaussian: two means, two variances, and covariance.
- Three methods for multivariate KDE:
  - Multivariate kernels
    - Most complex
  - Product kernels method assumes kernels are independent in different dimensions (one less model param to estimate).
    - Forces off-diagonal elements of variance-covariance matrix to be 0.
    - Kernel must align with axes.
  - Independence assumption method estimates density in each dimension independently.
    - Least complex
    - Wouldn't work well for Old Faithful example since variables are clearly related (not independent).
- Bandwidth parameter is matrix of same shape as variance-covariance matrix.
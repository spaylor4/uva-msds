# Resampling

### Bootstrap

Readings: ISL 5.2, ESL 7.11, [Bootstrapping Regression Models](https://socialsciences.mcmaster.ca/jfox/Books/Companion-1E/appendix-bootstrapping.pdf)

- The bootstrap can be used to quantify the uncertainty of an estimate or statistical learning method, and can be applied to a wide range of methods, even some for which measuring variability is otherwise difficult.
- Boostrapping involves repeatedly sampling observations from the original dataset (with replacement), estimating the parameter of interest, and calculating the standard error of those bootstrap estimates.
  - For a parameter $\alpha$ and $B$ bootstrap samples, the standard error is calculated as $SE_B(\hat\alpha) = \sqrt{\frac{1}{B-1}\sum_{r=1}^{B}(\hat\alpha^{*r} - \frac{1}{B}\sum_{r'=1}^{B}\hat\alpha^{*r'})^2}$, where $\hat\alpha^{*r}$ is the $r^{th}$ bootstrap estimate of $\alpha$.

### Cross-Validation

## Class Notes


# Model-Free Prediction

Reading: *Reinforcement Learning* Ch. 5, 6, 7.1, 12.1, 12.2

### Monte Carlo Methods

- MC methods do not require complete knowledge of the environment, only experience of sample sequences of states, actions, and rewards.
- MC methods solve RL problems by averaging sample returns. Only applied to episodic tasks in this book. Value estimates and policies are only updated after completion of an episode.
  - Estimate expected return by averaging observed returns after visits to that state. Average should converge to true expected value after enough observations (as number of observations goes to infinity).
- *First-visit MC method* estimates $v_\pi(s)$ by averaging the returns following all first visits to $s$, while *every-visit MC method* averages the returns following all visits to $s$ (since $s$ can be visited multiple times in a single episode).
- Even with complete knowledge of the environment, dynamic programming (DP) requires computation of all probabilities before DP can be applied. MC is much easier because it doesn't require computing these probabilities.
- The backup diagram for a MC problem shows only the states/transitions in a single episode, and not all possible states.
- Estimates for each state are independent: helps reduce computation and makes MC methods especially attractive when we want to ignore some states. 
- When a model is not available, it can be particularly useful to estimate *action* values (state-action pairs) rather than *state* values.
  - Same process to estimate $q_\pi(s, a)$ as $v_\pi$. One complication is that many state-action pairs may not be visited. Assumption of *exploring starts* addresses this by randomly starting in a state-action pair, so that each state-action pair is eventually selected many times as the start point, even if it would not be visited under the policy.
    - Exploring starts is impractical because it requires infinite simulations.
- Monte Carlo policy iteration alternates between evaluation and improvement on an episode-by-episode basis.
- *On-policy* methods attempt to evaluate or improve the policy that is used to make decisions, while *off-policy* methods evaluate/improve a policy different from that used to generate data.
  - Off-policy methods are more powerful and general, but are also generally slower to converge and have greater variance.
  - On-policy methods can be thought of as a special case of off-policy method on-policy methods in which the target and behavior policies are the same.
- *$\epsilon$-greedy policies* choose greedy choice most of the time, but choose an action with less than maximum estimated action value with probability $\epsilon$.
  - A *soft* policy is one in which $\pi(a|s)>0$ for all $a$ and all $s$. An *$\epsilon$-soft* policy is one in which $\pi(a|s) \ge \frac{\epsilon}{|A(s)|}$ for all states and actions.
  - $\epsilon$-greedy policies are examples of $\epsilon$-soft policies and are better than or equal to them.
- In an off-policy prediction problem, we wish to estimate $v_\pi$ or $q_\pi$, but have episodes generated from policy $b$ (the behavior policy, which is not equal to the optimal policy).
  - *Coverage* assumption: $\pi(a|s)>0$ implies $b(a|s) >0$ (every action taken under $\pi$ must at least occasionally be taken under $b$).
- *Importance sampling* is used in most off-policy methods to estimate expected values under one distribution given samples from another.
  - The *importance sampling ratio* measures the relative probability of returns under the target ($\pi$) and behavior policies. This ratio is defined as $\rho_{t:T-1} = \prod_{k = t}^{T-1} \frac{\pi(A_k|S_k)}{b(A_k|S_k)}$.
  - *Ordinary importance sampling* estimates $v_\pi(s)$ as $V(s) = \frac{\sum_{t\in T(s)}\rho_{t:T(t)-1}G_t}{|T(s)|}$, where $T(s)$ is the set of all time steps in which $s$ is visited (or the first steps for first-visit instead of every-visit method).
  - *Weighted importance sampling* instead uses a weighted average $V(s) = \frac{\sum_{t\in T(s)}\rho_{t:T(t)-1}G_t}{\sum_{t\in T(s)}\rho_{t:T(t)-1}}$.
  - Weighted importance sampling is biased (ordinary is unbiased) but has drastically lower variance than ordinary and is usually preferred.
- *Off-policy Monte Carlo control* methods follow a behavior policy while learning about and improving a target policy. Allows evaluation of a deterministic target policy.
- Advantages of MC over DP:
  - Can learn optimal behavior directly from environment, with no model of environment's dynamics.
  - Can be used with simulation or sample models.
  - Easy to focus on a small subset of states of interest, and in that case is more efficient.
  - Do not bootstrap (use successor states in updating value estimates), and therefore are less harmed by violations of the Markov property.

### Temporal-Difference Learning



### Class Notes

*March 2, 2021*

- Backup method (dynamic programming) doesn't work as state space gets extremely large. Instead need model-free learning, of which the simplest is Monte Carlo RL.
- Monte Carlo RL learns from complete episodes (can't be infinite).
  - Can't use bootstrapping to estimate future rewards, have to experience them.
  - Uses simplest possible idea of value: mean return (empirical, rather than expected return).
    - Return is total discounted reward.
    - Value function = expected return.
- Temporal-Difference learning is an alternative to Monte Carlo (still model-free). TD learns from incomplete episodes by bootstrapping, but does not give unbiased estimator.
  - Updates value towards estimate return, rather than toward acual return (like in Monte Carlo).
  - Updates value with each new state, don't have to wait until end of episode.
  - TD can be used for continuous (non-terminating) environments, but MC cannot.
  - TD can learn before knowing the final outcome or from incomplete/infinite sequences.
- Bias of an estimator is how far it is from expected value.
  - Return $G_t$ is an unbiased estimator of $v_\pi(S_t)$.
  - True TD target $R_{t+1} + \gamma v_\pi(S_{t+1})$ is an unbiased estimator of $v_\pi (S_t)$. However, we don't know $v_\pi(S_{t+1})$, so use $R_{t+1} + \gamma v(S_{t+1})$ instead, which is a biased estimate.
    - If we start with bad estimates of value function $v(S_{t+1})$, we will get bad estimates of the optimal value.
  - MC has high variance, no bias; TD has low variance, some bias.
    - MC has good convergence properties, but TD usually more efficient. TD more sensitive to initial value.
- TD exploits Markov property, and is usually more efficient in Markov environments, while MC is more effective in non-Markov environments.
  - Don't always know what type of environment you have.
- TD bootstraps (update an estimate from an estimate). TD & DP bootstrap, MC doesn't.
- MC samples (update samples an expectation). MC and TD sample, DP does not.
  - DP combines sampling and bootstrapping.

*March 11, 2021*

- Continuum exists between TD and MC: if we think about TD target looking $n$ steps into the future instead of just one step.
- The $\lambda$-return (TD-lambda) combines all $n$-step returns in an average with weighting param $\lambda$.
  - Generally want to use around $\lambda = 0.9$ to look pretty far out in the future.
  - If $\lambda = 0$, all weight will be on one-step return (basic TD discussed before); if $\lambda = 1$, all weight will be on T-step (final step) return  (equivalent to MC).
    - TD(1) is roughly equivalent to every-visit Monte-Carlo.
- Forward-view TD is offline (updates after episode); backward-view is online (updates from incomplete sequences).
  - The sum of offline updates is equal for forward and backward-view.
- Eligibility traces combine frequency and recency heuristics.
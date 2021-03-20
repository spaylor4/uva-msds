# Model-Free Control



### Class Notes

*March 11, 2021*

- Model free control *optimizes*, whereas model free prediction *estimates*.
- On-policy "learns on the job" (learn about policy $\pi$ from experience sampled from $\pi$); off-policy learns by "looking over someone's shoulder" (learn about policy $\pi$ from experience sampled from $b$).

*March 16, 2021*

- Greedy policy improvement over $V(s)$ requires model of MDP, but over $Q(s, a)$ is model-free.
  - $v$'s are intuitive but not as useful. $q$'s are more computationally rigorous.
  - $v$ only needs to be estimated for each state; $q$ needs to be estimated for each state-action pair.
- Greedy policies can cause you to get "stuck" and not explore enough and miss optimal actions. $\epsilon$-greedy exploration addresses this by choosing the greedy action most of the time, but picks an action at random $\epsilon$ of the time.
- GLIE = greedy in the limit with infinite exploration.
- SARSA algorithm: in state S, take action A, get reward R, go to state S', sample from policy to choose next action A'
  - Q-learning will be similar to SARSA.
  - SARSA is on-policy control (rather than off-policy).

*March 18, 2021*

- SARSA converges to the optimal action-value function.
- SARSA($\lambda$) is like TD-$\lambda$. There's some optimal $\lambda$ between 1 and infinity, but we don't know what it is when solving. Instead can use weights to blend returns from all $\lambda$ values to generate $q^\lambda$.
- As in TD, we use eligibility traces in an online algorithm.
  - SARSA has one trace for each state-action pair (TD just had one for each state).

- Off-policy learning allows agents to learn from observing humans or other agents. Also can learn about optimal policy while following an exploratory policy, or learn about multiple policies while following one policy.
- Monte Carlo importance sampling works in theory, but in practice leads to dramatically increased variance.
  - Instead do importance sampling on one-step TD-return. Lower variance because policies only have to be similar over one time step, not all.
- Greedy policy with respect to Q is optimal, but doesn't allow for enough exploration.
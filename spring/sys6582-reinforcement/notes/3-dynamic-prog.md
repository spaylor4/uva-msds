# Dynamic Programming

Reading: Reinforcement Learning Ch. 4

- Dynamic programming is used to solve for optimal policies when we have a perfect model of the environment as a Markov decision process.
  - Usually assume the environment is a finite MDP (sets of possible states, actions, and rewards are finite).
- Policy evaluation or prediction involves computing the state-value function $v_\pi$ for an arbitrary policy $\pi$.
  - $v_\pi (s) = E_\pi [R_{t+1} + \gamma v_\pi(S_{t+1})]$ $= \sum_a \pi(a|s)\sum_{s', r}p(s', r|s, a)[r + \gamma v_pi(s')]$, where $\pi(a|s)$ is the probability of taking action $a$ in state $s$ under policy $\pi$.
  - Iterative policy evaluation involves computing successive approximations $v_{k+1}$from $v_k$ until convergence to $v_\pi$. Each step is an *expected update*.
- The policy improvement theorem says that for any pair of policies $\pi$ and $\pi'$, if $q_\pi(s, \pi '(s))\ge v_\pi (s)$ for all $s$, then $\pi'$ must be as good or better than $\pi$, i.e. $v_{\pi'}(s)\ge v_\pi(s)$.
  - Policy improvement involves improving an existing policy by making it greedy with respect to the value function of the existing policy.
- Policy iteration rotates evaluation and improvement steps until convergence to the optimal policy and value functions.
  - Policy evaluation makes the value function consistent with the current policy, while policy improvement makes the policy greedy with respect to the current value function.
- Value iteration truncates policy iteration after one sweep of policy evaluation (one update at each state), rather than having a policy evaluation loop nested within the algorithm.
- Asynchronous dynamic programming doesn't require a systematic sweep over all states (which is a problem when there are many states, such as backgammon, which has $10^{20}$).

### Class Notes

*February 18, 2021*

- Oil well problem: don't know future price of oil, but need to figure out what to charge for lease on oil well.
  - Actions: idle/pump normally/pump enhanced, $A = \{I, PN, PE\}$
  - States: amount of oil in the ground, oil price, and year, $S = \{(OR, M, Y)\}$
  - Rewards: positive price of oil, negative cost of pumping
  - Transition probability: 50% (equally likely to be \$20 or ​\$30/barrel)

*February 23, 2021*

- [Open AI Gym](https://gym.openai.com) contains environments already coded.
  - Python package `gym` allows you to create these environments easily in Python.
- Dynamic programming uses subproblems to solve complex problems with large potential solution spaces.
  - Solutions to subproblems can be cached and reused due to overlap. Bellman equations involve overlap with recursive decomposition.

*February 25, 2021*

- Car rental example: as policy iterates, it becomes assymetrical due to the differences between the two locations (higher demand at location two).
- Value iteration: start with final rewards and work backward (as in oil well problem). Works for deterministic or stochastic MDPs.
  - No explicit policy, but converges to $v*$.
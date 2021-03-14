# Introduction to Reinforcement Learning

Reading: Reinforcement Learning Ch. 1

- Reinforcement learning involves mapping situations to actions in order to maximize a reward signal.
- In reinforcement learning, agents learn from their own experience, rather than from some external supervisor. 
- An *agent* must balance *exploiting* what it has experienced and knows will lead to reward and *exploring* things it hasn't experienced in order to make better actions in the future.
- Reinforcement learning agents have explicit goals, can senseaspects of their environments, and can choose actions to influence their environments.
- A *policy* defines the learning agent’s way of behaving at a given time based on the current environment. It is a function mapping states to actions.
- A *reward signal* indicates to the agent value at the current time. A *value function* defines the expected reward that will be accumulated over future states from a particular state. Estimating value is the most important component of RL algorithms.
- Some algorithms include a *model* of the environment to help predict future behavior of the environment. These are *model-based* as opposed to *model-free* methods.

### Class Notes

*February 2, 2021*

- Reinforcement learning involves making decisions sequentially.
- Reinforcement learning is closely related to psychology and neuroscience, along with other areas like operations research.
- Reinforcement learning is another type of ML in addition to supervised/unsupervised.
  - No supervisor, only a reward signal (though feedback is delayed, not instantaneous).
  - Data is not iid, but dependent on time and previous actions by the agent.
- Example applications: backgammon, investment management, making a robot walk,  [hide and seek](https://openai.com/blog/emergent-tool-use/) game, etc.
- "The question of whether machines can think ... is about as relevant as the question of whether submarines can swim." - Edsgar Dijkstra

*February 4, 2021*

- Rewards are the basis of reinforcement learning.
  - Reward is a scalar feedback signal at each time step. Agent's goal is to maximize cumulative reward through sequential decisions.
  - Rewards may be delayed and may require short-term sacrifice.
- **Reward hypothesis**: all goals can be described by the maximization of expected cumulative reward.
- Rewards can be positive and negative. For example, in controlling a power station, could have positive reward for producting power and negative reward for exceeding safety thresholds.
- Rewards and observations come from the environment.
- Rewards can be stochastic (random variables).
- The **history** is the sequence of observations, actions, and rewards (all observed variables up to time $t$). 
- **State** is the information used to determine what happens next, and is a function of the history ($S_t = f(H_t)$).
  - Entire history may not be relevant and will become unmanageable as history gets very long, so the state is used for decision making. A **Markov state** contains all useful information from the history.
    - Once the Markov state is known, the history is no longer needed.
  - The environment state is the environment's private representation and is not usually visible to the agent, or may be visible but include irrelevant info.
  - The agent state is the agent's internal representation of its position. This state is what RL algorithms use to pick the next action.
    - Different agent states can give different decisions.
  - In partially observable environments, the agent state $\not=$ environment state.
- Policy $\pi$ (map from state to action) can be deterministic ($\pi(s)$) or stochastic ($\pi(a | s)$).
- Value function $v_\pi$ predicts future reward using a policy. Often discounts reward further in the future (e.g. time value of money).

*February 9, 2021*

- A model predicts what the environment will do next. $P$ predicts the next state, $R$ predicts the next (immediate) reward.
  - A model is not required for RL. Agents can be model free or model-based.
- RL agents can be value-based (have only an implicit policy), policy-based (no value function), or actor critic (have both policy and value function).
- RL is trial and error learning: tension between trying new things to find more reward (exploring) and sticking with known high-reward actions (exploiting).
- Prediction vs. control: prediction involves evaluating the future given a policy; control is optimizing the future by finding the best policy.
- Gridworld example: policy in squares A and B doesn't matter, since you will move to A' and B' regardless.
- Inverse RL: agent observes an expert's actions, but rewards are unknown.
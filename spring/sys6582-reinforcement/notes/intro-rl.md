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
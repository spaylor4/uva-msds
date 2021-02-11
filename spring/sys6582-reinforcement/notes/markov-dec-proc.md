# Markov Decision Processes

Reading: Reinforcement Learning Ch. 3

- In a finite MDP, there are a finite number of choices of states, actions, and rewards. 
- The next reward and state $R_t$ and $S_t$ depend on the previous state and action $S_{t-1}$ and $A_{t-1}$. This can be written as a probability distribution function $p(s', r |s, a)$, where $p$ defines the **dynamics** of the MDP.
  - In order to satisfy the Markov property, the state must contain any relevant information about previous interactions between the agent and the environment.
- Anything that cannot be changed arbitrarily by the agent is considered part of its environment. For example, the motors and mechanical linkages of a robot are part of the environment rather than the agent, even though they are part of the robot, since the robot can't change them.
- Reward signals must be defined to reflect what you want achieved, and shouldn't include anything about how it should be achieved, else the agent may learn to achieve subgoals without achieving the true goal.

- In the simplest case, the agent-environment interaction can be broken into subsequences called **episodes** that begin independently of previous episodes and end in a **terminal state**. Games and mazes are examples. 
  - In this case the expected return is the sum of rewards for each state up to the terminal state, $G_t = R_{t+1} + R_{t+2} + ... + R_T$.
- In many cases, RL involves **continuing tasks** with no well-defined endpoint. Process-control or robots are examples.
  - To deal with potentially infinite time values, we use **discounting** to calculate the expected reward, $G_t + R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3}+ ... = \sum_{k=0}^\infty \gamma^k R_{t+k+1}$, where $\gamma$ is the **discount rate** between 0 and 1. This calculates the present value of future rewards.
- To consolidate notation and consider both episodic and continuing tasks together, we can consider the terminal state of episodic tasks as an **absorbing state** where subsequent steps stay in that state with probability 1 and reward 0.
- A **policy** maps states to probabilities of selecting each possible action when in a certain state. RL methods specify how the agent’s policy is changed as a result ofits experience.
- The Bellman equation specifies the relationship between the value of a state and the value of its successor states.
  - Explicitly solving the Bellman optimality equation requires that (1) the dynamics of the environment are accurately known, (2) computational resources are sufficient to complete the calculation, and (3) the states have the Markov property. These three conditions are rarely true in practice, and approximate solutions are required.
- An **optimal policy** is better than or equal to all other policies, which means its expected return is greater than or equal to each other policy's for all states.
  - If the optimal value function $v_*$ is known, then a policy that is greedy with respect to $v_*$ is an optimal policy.
  - An optimal action-value function $q_*$ gives the expected return for taking action $a$ in state $s$ and thereafter following optimal policy. This function effectively caches the results of all one-step-ahead searches, allowing the agent to simply select the action that maximizes $q_*$.
- RL allows approximation of optimal policies to focus more effort on making good decisions for frequently encountered states and less effort on infrequent ones.

### Class Notes

*February 9, 2021*

- In MDPs the environment is fully observable, and the current state fully characterizes the process.
- Markov property: the future is independent of the past given the present.
- For a Markov state $s$ and successor state $s'$, the state transition probability is $P_{ss'} = P[S_{t+1} = s' | S_{t} = s]$.


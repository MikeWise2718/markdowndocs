---
title: "Reinformcement Learning - Sutton and Barto - Notes and Problems"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
This is apparently *the* RL book.

Example image:
![Red Fish](SmallerFish.png)

Example equation: $c^2 = \sqrt{a^2 + b^2}$

#  1 - Introduction
## 1.1	Reinforcement Learning <br>
## 1.2	Examples <br>
## 1.3	Elements of Reinforcement Learning <br>
## 1.4	Limitations and Scope <br>
## 1.5	An Extended Example: Tic-Tac-Toe <br>
- Interesting early (in book) discussion of "Temporal Differencing"
### Exercise 1.1: Self Play
Suppose, instead of playing against a random opponent, the reinforcement
learning algorithm described above played against itself, with both sides learning. What do you think would happen in this case? 
- It would fairly quickly reach a state where it would never win

Would it learn a different policy for selecting moves?
- Probably not

### Exercise 1.2: Symmetries 
Many tic-tac-toe positions appear different but are really the same because
of symmetries. How might we amend the learning process described above to take advantage of this?
- To Do

In what ways would this change improve the learning process? 
- To Do

Now think again. Suppose the opponent did not take advantage of symmetries. In that case, should we? 
- To Do

Is it true, then, that symmetrically equivalent positions should necessarily have the same value?
- To Do
### Exercise 1.3: Greedy Play 

Suppose the reinforcement learning player was greedy, that is, it always
played the move that brought it to the position that it rated the best. Might it learn to play better, or worse, than a nongreedy player? What problems might occur? 

- To Do


### Exercise 1.4: Learning from Exploration 

Suppose learning updates occurred after all moves, including exploratory moves. If the step-size parameter is appropriately reduced over time (but not the tendency
to explore), then the state values would converge to a set of probabilities. What are the two sets of probabilities computed when we do, and when we do not, learn from exploratory moves? 

- To Do

Assuming that we do continue to make exploratory moves, which set of probabilities might be better to learn?

- To Do

Which would result in more wins? 
- To Do

### Exercise 1.5: Other Improvements 

Can you think of other ways to improve the reinforcement learning
player? 
- To Do

Can you think of any better way to solve the tic-tac-toe problem as posed?

- To Do


## 1.6	Summary <br>
## 1.7	Early History of Reinforcement Learning <br>

#  2  - Multi-armed Bandits
## 2.1 A k-armed Bandit Problem
## 2.2	Action-value Methods 
## 2.3	The 10-armed Testbed 
## 2.4	Incremental Implementation 
## 2.5	Tracking a Nonstationary Problem 
## 2.6	Optimistic Initial Values 
## 2.7	Upper-Confidence-Bound Action Selection 
## 2.8	Gradient Bandit Algorithms 
## 2.9	Associative Search (Contextual Bandits) 
## 2.10	Summary 


# Outline

1	Introduction <br>
1.1	Reinforcement Learning <br>
1.2	Examples <br>
1.3	Elements of Reinforcement Learning <br>
1.4	Limitations and Scope <br>
1.5	An Extended Example: Tic-Tac-Toe <br>
1.6	Summary <br>
1.7	Early History of Reinforcement Learning <br>
<br>
I         Tabular Solution Methods <br>
2	Multi-armed Bandits <br>
2.1	A k-armed Bandit Problem <br>
2.2	Action-value Methods <br>
2.3	The 10-armed Testbed <br>
2.4	Incremental Implementation <br>
2.5	Tracking a Nonstationary Problem <br>
2.6	Optimistic Initial Values <br>
2.7	Upper-Confidence-Bound Action Selection <br>
2.8	Gradient Bandit Algorithms <br>
2.9	Associative Search (Contextual Bandits) <br>
2.10	Summary <br>
3	Finite Markov Decision Processes <br>
3.1	The Agent– Environment Interface <br>
3.2	Goals and Rewards <br>
3.3	Returns and Episodes <br>
3.4	Unified Notation for Episodic and Continuing Tasks <br>
3.5	Policies and Value Functions <br>
3.6	Optimal Policies and Optimal Value Functions <br>
3.7	Optimality and Approximation <br>
3.8	Summary<br>
4	Dynamic Programming <br>
4.1	Policy Evaluation (Prediction)<br>
4.2	Policy Improvement <br>
4.3	Policy Iteration <br>
4.4	Value Iteration <br>
4.5	Asynchronous Dynamic Programming <br>
4.6	Generalized Policy Iteration <br>
4.7	Efficiency of Dynamic Programming <br>
4.8	Summary <br>
<br>
5	Monte Carlo Methods <br>
5.1	Monte Carlo Prediction <br>
5.2	Monte Carlo Estimation of Action Values <br>
5.3	Monte Carlo Control <br>
5.4	Monte Carlo Control without Exploring Starts <br>
5.5	Off-policy Prediction via Importance Sampling <br>
5.6	Incremental Implementation <br>
5.7	Off-policy Monte Carlo Control <br>
5.8	* Discounting-aware Importance Sampling <br>
5.9	* Per-decision Importance Sampling <br>
5.10	Summary <br>
6	Temporal-Difference Learning <br>
6.1	TD Prediction <br>
6.2	Advantages of TD Prediction Methods <br>
6.3	Optimality of TD( 0) <br>
6.4	Sarsa: On-policy TD Control <br>
6.5	Q-learning: Off-policy TD Control <br>
6.6	Expected Sarsa <br>
6.7	Maximization Bias and Double Learning <br>
6.8	Games, Afterstates, and Other Special Cases <br>
6.9	Summary <br>
7	n-step Bootstrapping <br>
7.1	n-step TD Prediction <br>
7.2	n-step Sarsa <br>
7.3	n-step Off-policy Learning <br>
7.4	* Per-decision Methods with Control Variates <br>
7.5	Off-policy Learning Without Importance Sampling: The n-step Tree Backup Algorithm <br>
7.6	* A Unifying Algorithm: n-step Q( s) <br>
7.7	Summary <br>
8	Planning and Learning with Tabular Methods <br>
8.1	Models and Planning <br>
8.2	Dyna: Integrated Planning, Acting, and Learning <br>
8.3	When the Model Is Wrong <br>
8.4	Prioritized Sweeping <br>
8.5	Expected vs. Sample Updates <br>
8.6	Trajectory Sampling <br>
8.7	Real-time Dynamic Programming<br>
 <br>
II         Approximate Solution Methods <br>
9	On-policy Prediction with Approximation <br>
9.1	Value-function Approximation <br>
9.2	The Prediction Objective (VE) <br>
9.3	Stochastic-gradient and Semi-gradient Methods <br>
9.4	Linear Methods <br>
9.5	Feature Construction for Linear Methods <br>
9.5.1	Polynomials <br>
9.5.2	Fourier Basis <br>
9.5.3	Coarse Coding <br>
9.5.4	Tile Coding <br>
9.5.5	Radial Basis Functions <br>
9.6	Selecting Step-Size Parameters Manually <br>
9.7	Nonlinear Function Approximation: Artificial Neural Networks <br>
9.8	Least-Squares TD <br>
9.9	Memory-based Function Approximation <br>
9.10	Kernel-based Function Approximation <br>
9.11	Looking Deeper at On-policy Learning: Interest and Emphasis <br>
9.12	Summary <br>
10	On-policy Control with Approximation <br>
10.1	Episodic Semi-gradient Control <br>
10.2	Semi-gradient n-step Sarsa <br>
10.3	Average Reward: A New Problem Setting for Continuing Tasks <br>
10.4	Deprecating the Discounted Setting <br>
10.5	Differential Semi-gradient n-step Sarsa <br>
10.6	Summary <br>
11	* Off-policy Methods with Approximation <br>
11.1	Semi-gradient Methods <br>
11.2	Examples of Off-policy Divergence <br>
11.3	The Deadly Triad <br>
11.4	Linear Value-function Geometry <br>
11.5	Gradient Descent in the Bellman Error <br>
11.6	The Bellman Error is Not Learnable <br>
11.7	Gradient-TD Methods <br>
11.8	Emphatic-TD Methods <br>
11.9	Reducing Variance<br>
<br>
<br>
<br>
<br>
<br>
12	Eligibility Traces <br>
12.1	The ?-return <br>
12.2	TD( ?) <br>
12.3	n-step Truncated ?-return Methods <br>
12.4	Redoing Updates: Online ?-return Algorithm <br>
12.5	True Online TD( ?) <br>
12.6	* Dutch Traces in Monte Carlo Learning <br>
12.7	Sarsa( ?) <br>
12.8	Variable ? and ? <br>
12.9	Off-policy Traces with Control Variates <br>
12.10	Watkins’s Q( ?) to Tree-Backup( ?) <br>
12.11	Stable Off-policy Methods with Traces <br>
12.12	Implementation Issues <br>
12.13	Conclusions <br>
13	Policy Gradient Methods <br>
13.1	Policy Approximation and its Advantages <br>
13.2	The Policy Gradient Theorem <br>
13.3	REINFORCE: Monte Carlo Policy Gradient <br>
13.4	REINFORCE with Baseline <br>
13.5	Actor– Critic Methods <br>
13.6	Policy Gradient for Continuing Problems <br>
13.7	Policy Parameterization for Continuous Actions <br>
13.8	Summary <br>
<br>


---
title: "Reinformcement Learning - Sutton and Barto - Notes and Problems"
output: html_document
---
[up](https://mikewise2718.github.io/markdowndocs/)

# Intro
This is apparently *the* RL book.

Example image:
![Red Fish](SmallerFish.png)

Example equation: $c = \sqrt{a^2 + b^2}$

#  1 - Introduction
## 1.1	Reinforcement Learning <br>
## 1.2	Examples <br>
## 1.3	Elements of Reinforcement Learning <br>
## 1.4	Limitations and Scope <br>
## 1.5	An Extended Example: Tic-Tac-Toe <br>
- They talk of "evolutionary methods" and how they only make use of the state at the end. I suppose they mean the Monte-carlo methods of Chapter 5.
- Interesting early (in book) discussion of "Temporal Differencing"
### Exercise 1.1: Self Play
Suppose, instead of playing against a random opponent, the reinforcement
learning algorithm described above played against itself, with both sides learning. What do you think would happen in this case? 
- It would fairly quickly reach a state where it would never win

Would it learn a different policy for selecting moves?
- If the opponent was not perfect them (as per assumtion), then it would learn a different policy...

### Exercise 1.2: Symmetries 
Many tic-tac-toe positions appear different but are really the same because
of symmetries. How might we amend the learning process described above to take advantage of this?
- We could wire the values of the states together, and update all wired symetric values together.

In what ways would this change improve the learning process? 
- It would cover the space of possible moves quicker, so in the case of playing a very good player it would probably learn faster.

Now think again. Suppose the opponent did not take advantage of symmetries. In that case, should we? 
- No, because then we could not identify opponent weakeness that result from symmetry differences.

Is it true, then, that symmetrically equivalent positions should necessarily have the same value?
- No


### Exercise 1.3: Greedy Play 

Suppose the reinforcement learning player was greedy, that is, it always
played the move that brought it to the position that it rated the best. Might it learn to play better, or worse, than a nongreedy player? What problems might occur? 

- No, because it will not be able to disciver when its ratings are wrong.


### Exercise 1.4: Learning from Exploration 

Suppose learning updates occurred after all moves, including exploratory moves. If the step-size parameter is appropriately reduced over time (but not the tendency to explore), then the state values would converge to a set of probabilities. What are the two sets of probabilities computed when we do, and when we do not, learn from exploratory moves? 

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

### Exercise 2.1 
In epsilon-greedy action selection, for the case of two actions and $\epsilon$ = 0.5, what is the probability that the greedy action is selected?
- ToDo

### Exercise 2.2: Bandit example 

Consider a k-armed bandit problem with k = 4 actions, denoted 1, 2, 3, and 4. Consider applying to this problem a bandit algorithm using $\epsilon$-greedy action selection,
sample-average action-value estimates, and initial estimates of Q1(a) = 0, for all a. Suppose the initial sequence of actions and rewards is:

 $A_1$ = 1, $R_1$ = 1, $A_2$ = 2, $R_2$ = 1, $A_3$ = 2, $R_3$ = 2, $A_4$ = 2, $R_4$ = 2, $A_5$ = 3, $R_5$ = 0

 On some of these time steps the $\epsilon$ case may have occurred, causing an action to be selected at random. On which time steps did this definitely occur? 

- ToDo

On which time steps could this possibly have occurred? 

## 2.3	The 10-armed Testbed 

### Exercise 2.3 
In the comparison shown in Figure 2.2, which method will perform best in the long run
in terms of cumulative reward and probability of selecting the best action? 
- ToDo

How much better will it be? Express your answer quantitatively.

- ToDo

## 2.4	Incremental Implementation 
## 2.5	Tracking a Nonstationary Problem 

### Exercise 2.4 

If the step-size parameters, $\alpha_n$, are not constant, then the estimate $Q_n$ is a weighted
average of previously received rewards with a weighting different from that given by (2.6). What is the weighting on each prior reward for the general case, analogous to (2.6), in terms of the sequence of step-size parameters? 


### Exercise 2.5 (programming) 

Design and conduct an experiment to demonstrate the difficulties that sample-average methods have for nonstationary problems. Use a modified version of the 10-armed
testbed in which all the $q_∗(a)$ start out equal and then take independent random walks (say by adding a normally distributed increment with mean zero and standard deviation 0.01 to all the $q_∗(a)$ on each step). 

Prepare plots like Figure 2.2 for an action-value method using sample averages, incrementally computed, and another action-value method using a constant step-size parameter, $\alpha$ = 0.1. Use $\epsilon$ = 0.1
and longer runs, say of 10,000 steps. 

## 2.6	Optimistic Initial Values 

### Exercise 2.6: Mysterious Spikes 

The results shown in Figure 2.3 should be quite reliable because they are averages over 2000 individual, randomly chosen 10-armed bandit tasks. Why, then, are there oscillations and spikes in the early part of the curve for the optimistic method? 

In other words, what might make this method perform particularly better or worse, on average, on particular early steps?

- Todo

## 2.7	Upper-Confidence-Bound Action Selection 

### Exercise 2.7 

Show that in the case of two actions, the **soft-max** distribution is the same as that given by the **logistic**, or **sigmoid**, function often used in statistics and artificial neural networks. 

## 2.8	Gradient Bandit Algorithms 


## 2.9	Associative Search (Contextual Bandits) 

### Exercise 2.8 

Suppose you face a 2-armed bandit task whose true action values change randomly from
time step to time step. Specifically, suppose that, for any time step, the true values of actions 1 and 2 are respectively 0.1 and 0.2 with probability 0.5 (case A), and 0.9 and 0.8 with probability 0.5 (case B). 

If you are not able to tell which case you face at any step, what is the best expectation of success you can achieve and how should you behave to achieve it? 
- Todo

Now suppose that on each step you are told whether you are facing case A or case B (although you still don’t know the true action values). This is an associative search task. What is the best expectation of success you can achieve in this task, and
how should you behave to achieve it?

- Todo

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


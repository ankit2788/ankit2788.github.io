---
layout: post
title: "Policy Gradient - REINFORCE"
date: 2021-04-15
tags: Mathematics ReinforcementLearing MachineLearning
comments: true
categories: [MachineLearning]
---

Flow -->
- 1st para about Policy gradient (with minor mathematical formulation) 
- 2nd para --> What is reinforce with proper algo


Policy Gradient algorithms have gained quite some popularity these days. With usage across continuous space-continuous actions, these algorithms cater to wide variety of problems ranging from [systematic trading](https://arxiv.org/abs/1911.10107) algorithms to [self-driving cars](https://link.springer.com/chapter/10.1007/978-981-15-1081-6_5). So, what are these policy gradient algorithms and why are they gaining such popularity. This series of articles is dedicated to wide variety of Policy Gradient algorithms. 

#### A quick recap on Value based agents
As we have read that [Value based learnings](https://en.wikipedia.org/wiki/Reinforcement_learning#Value_function) (such as _Q-learning_, _DQN_, _DDQN_ etc.) algos aim to maximize the state-value (or action-value).
$$ V^\pi(s) = \mathbb{E}[R|s, \pi] $$.
$$ V^*(s) = max_\pi V^\pi(s) $$.

In DQN (or any other value based learning agent), the objective is to maximize value functions.

<p class="aligncenter"> 
<img src="/data/pics/2021/04/DQN.png" alt="DQN network" width="800" height="500" />
</p>


But such agents come with certain challenges of their own:
* Limited to Discrete Action space problems. 
* Slower convergence
* Exploration Exploitation dilemma
* Experience Memory maintenance


#### So, what are Policy Gradient Algorithms
We have been using $$ /pi(a/s, \theta) $$ as our policy. But, we never thought of directly optimizing the policy. 
Objective:
$$ max {J}(\theta) $$, where $$\theta$$ refers to policy parameters

We can use [stochastic gradient ascent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) methods to solve this optimization problem. I will not go into mathematical details as there is a lot of literature available on that. In short, here is what comes out as policy gradient algorithm:

$$ \nabla_\theta{J}(\theta) \propto  {G}.\nabla_\theta{log}\pi_\theta(s/a) $$
$$ \theta_{t+1} = \theta_{t} + \alpha.G_t.\nabla_\theta{log}\pi_\theta(s/a) $$

Key takeaway from above equation:
1. $$ \nabla_\theta{J} $$ is independent of states distribution
2. $$ \theta $$ is updated in proportion to return. If higher return is achieved by taking a particular action, then the probability of taking that action rises in proportion


#### Why would I chose Policy Gradient over Value Learning Agent?
PG methods provide quite a few valid reasons why I should choose them. Mind that the list is not exhaustive. I will add more as I stumble upon more advanatges:
1. Faster convergence, Well, who doesnt like it? 
2. Can cater to high dimensions and __continuous__ state-action space environments. Becomes handy with real-life situations. I cant always take a 90 degree left turn (an action) while driving my car. 
3. Can learn __Stochastic Policies__. In simple words, you choose action from a distribution.

<p class="aligncenter"> 
<img src="/data/pics/2021/04/PG.png" alt="Simple PG network" width="800" height="500" />
</p>








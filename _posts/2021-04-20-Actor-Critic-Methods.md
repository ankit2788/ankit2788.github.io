---
layout: post
title: Actor Critic Methods
date: 2021-04-20
tags: Mathematics Reinforcement MachineLearning
comments: true
categories: [Reinforcement]
---

Policy Gradient are "cool" algorithms to make the agent learn. We saw how REINFORCE, as simple as it is, can help learn the agent. With few tricks, such as _baseline methods_, learning variances can be reduced further. 
Next in line of the Policy Gradient techniques is Actor Critic (AC) Methods. First introduced in 2013 through the paper [Natural Actor-Critic Algorithms](https://hal.inria.fr/hal-00840470/document), they now set a foundation to a series of advanced AC methods (A2C, A3C), which we will dig further in later articles. 

So, lets begin with the need of AC methods in the first place before we jump onto the mathematical technicalities.

## A case for Actor Critic methods?
<p class="aligncenter"> 
<img src="/data/pics/2021/04/reinforce_episode.png" alt="Reinforce" width="840" height="300" />
</p>

1. __Dont need Full episode__ -- 
A fully Monte Carlo method, REINFORCE needed a complete knowledge of entire episode before the policy could learn. In above episode, $$a_1$$ taken at $$s_0$$ turns out to generate negative reward. So, why run entire episode to discredit action $$a_1$$?
<br>
Actor Critic methods comes handy in this case, as they use [__Temporal Difference (TD)__](https://en.wikipedia.org/wiki/Temporal_difference_learning) learnings.

2. __Critic to judge the performance__ -- 
Imagine you (_actor_) are learning to ride a bike. You paddle hard! But your mom (_critic_) tells you to paddle harder!
That's what Actor Critic is. Another agent to evaluate the performance under current policy.
Simple, isnt it? 


## Actor Critic
The policy network acts as an _actor_, whereas a value network acts as a _critic_ which evaluates how good or bad the updated policy is. <br>
Here is a graphical representation of the architecture used in AC method. A lot to digest here. So, sit back and relax while I try to brew the math here :)

<p class="aligncenter"> 
<img src="/data/pics/2021/04/ac_arch.png" alt="AC Architecture" width="350" height="350" />
</p>

Now, since there are 2 agents required which are working in conjuction to each other, lets try to understand the how part of their implementation.




----------------

# Appendix

### References

> 1. Reinforcement Learning, An Introduction (Second Edition). [Sutton and Barto ](http://incompleteideas.net/book/first/ebook/node66.html) <br>
> 2. [University of California, Berkeley - Youtube Lecture](https://www.youtube.com/watch?v=EKqxumCuAAY&list=PLkFD6_40KJIwhWJpGazJ9VSj9CFMkb79A&index=8) <br>
> 3. [Lilianweng Github Page](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html)





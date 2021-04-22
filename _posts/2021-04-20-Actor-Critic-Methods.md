---
layout: post
title: Actor Critic Methods
date: 2021-04-20
tags: Mathematics Reinforcement MachineLearning
comments: true
categories: [Reinforcement]
---

Policy Gradient are "cool" algorithms to make the agent learn. We saw how REINFORCE, as simple as it is, can help learn the agent. With few tricks, such as _baseline methods_, learning variances can be reduced further. 
Next in line of the Policy Gradient techniques is Actor Critic (AC) Methods. First introduced in 2013 through the paper [Natural Actor-Critic Algorithms](https://hal.inria.fr/hal-00840470/document){:target="_blank"}, they now set a foundation to a series of advanced AC methods (A2C, A3C), which we will dig further in later articles. 

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

[Quick recap](/2021-04-16-Policy-Gradient-REINFORCE.md){:target="_blank"} of the Policy gradient (REINFORCE) equation:<br>
$$ \nabla_\theta{J}(\theta) \propto  \mathbb{E_\pi}[{G_t}.\nabla_\theta{log}\pi_\theta(s/a)] $$ , 
where $$G$$ is defined as expected rewards if started from state $$s$$

Adding a baseline leaves us at:

$$ \nabla_\theta{J}(\theta) \propto  \mathbb{E_\pi}[({G_t - b_t(s))}.\nabla_\theta{log}\pi_\theta(s/a)] $$ , <br>

But here is the catch. Both the formulations require a full episodic knowledge! Actor Critic Methods are one step ahead in a way that they utilize TD methods to perform _online learning_ .<br>
The policy network acts as an _actor_, whereas a value network acts as a _critic_ which evaluates how good or bad the updated policy is at every step. <br>
Here is a [visualization](http://incompleteideas.net/book/first/ebook/node66.html){:target="_blank"} of the architecture used in AC method. A lot to digest here. So, sit back and relax while I try to brew the math here :)

<p class="aligncenter"> 
<img src="/data/pics/2021/04/ac_arch.png" alt="AC Architecture" width="350" height="350" />
</p>

* ### Value Function:<br>

<p class="center"> 
<img src="/data/pics/2021/04/value.png" alt="Value Function" width="300" height="120" />
</p>

Given a state under a policy $$\pi$$, this function approximator returns the value of that state, i.e. $$V_\phi^\pi(s)$$. <br>
How do we create this function approximator? This, in essence, is similar to [Q-learning methods](https://en.wikipedia.org/wiki/Q-learning){:target="_blank"}. Here is a quick summary:
> Training data: $$ { (s_{i, t}, y_{i, t} = r(s_{i, t}, a_{i, t}) + \gamma.V_\phi^\pi(s_{t+1}))} $$ <br>
> Loss function (_supervised regression_): $$ L(\phi) = 1/2(\sum_i ( V_\phi^\pi(s_{t}) - y_i)^2) $$ <br>
 
In the above training data, we just need only next step value, instead of entire episode. Loss function is simply defined as the __Mean squared TD(1) error__. <br>
Using a simple NN can help achieve the above function.




* ### Policy Network:<br>

<p class="center"> 
<img src="/data/pics/2021/04/policy.png" alt="Policy" width="300" height="120" />
</p>

The policy network works as usual (similar to [REINFORCE](/2021-04-16-Policy-Gradient-REINFORCE.md){:target="_blank"}), with a slight change. Instead of using the entire episodic discounted reward to update $$\theta$$, we will use the below update methodology, wherein we have the TD error (or Advantage ): <br>
$$ \theta_{t+1} = \theta_{t} + \alpha.A_t^\pi.\nabla_\theta{log}\pi_\theta(s/a) $$, where <br>
$$A_t^\pi$$ is the  _TD error_, mathematically formulated as: $$r(s_{i, t}, a_{i, t}) + \gamma.V_\phi^\pi(s_{t+1}) - V_\phi^\pi(s_{t}) $$

> Training data: $${ (s_i, y_i = \pi_\theta(s_t/ a_t) + \beta.A_t.\nabla_\theta{log}\pi_\theta(s/a))}$$. <br>
> Loss function (_cross entropy_): $$ L(\theta) = \sum_i(-y_i.{log(\pi_\theta)}) $$ <br>


## Sneak peak into the Algorithm
<p class="center"> 
<img src="/data/pics/2021/04/ac_algo.png" alt="A/C Algorithm" width="600" height="200" />
</p>
[Source](http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_5_actor_critic_pdf){:target="_blank"}


## Implementation

### 1. Network Design (2 vs 1)
Since, there are 2 separate learnings happening in AC methods, at first glance, it makes sense to use 2 separate networks to learn the policy and value functions separately. But, there is another school of thought which lets us use a dual network design as below:
<p class="center"> 
<img src="/data/pics/2021/04/networks.png" alt="A/C Algorithm" width="700" height="320" />
</p>

### 2. Batch vs Online Learning
Online learning will require the parameter update at every step. Although technically feasible, but an update after every step makes the network unstable. Hence, all the updates wil happen after the end of each episode, i.e. batch learning in this case. 

### 3. Actor & Critic learning
Since, we have a dual shared network, we can combine the losses as below: <br>
$$ L = L_{actor} + L_{critic} $$

* Actor Loss <br>
    $$ L(\theta) = \sum_i(-y_i.{log(\pi_\theta)}) $$  <br>
* Critic Loss <br>
    $$ L(\phi) = 1/2(\sum_i ( V_\phi^\pi(s_{t}) - y_i)^2) $$  <br>
    or, we can replace it with [huber loss](https://en.wikipedia.org/wiki/Huber_loss){:target="_blank"} to make it differential everywhere. 

    ~~~python
    with tf.GradientTape() as tape:

        # sample --> tuple of current state, actions, rewards, next states, value (given current state)
        # get log prob
        state   = tf.Variable([sample[0]], trainable = True,   dtype=tf.float32)
        nextState   = tf.Variable([sample[3]], trainable = True,   dtype=tf.float32)
        action, reward, dead  = sample[1], sample[2], sample[4]
        
        # run shared network to get action prob distro and value associated with that state
        actionProbDistro, _currStateValue = self.SharedNetwork(state, training = True)
        _actionProbDistro, _nextStateValue = self.SharedNetwork(nextState, training = True)

        # compute TD error
        # delta = r + gamma*V_(t+1) - V_t
        delta = reward + self.discountfactor* tf.squeeze(_nextStateValue) * (1 - int(dead)) - tf.squeeze(_currStateValue)

        # compute critic loss
        loss_sample_critic = delta**2

        # compute actor loss
        actionProb      = actionProbDistro.numpy()[0, action]
        loss_sample_actor =  tf.math.log(actionProb) * delta

        networkLoss = loss_sample_critic + loss_sample_actor

        # performing Backpropagation to update the network
        grads = tape.gradient(networkLoss, self.SharedNetwork.trainable_variables)
        self.SharedNetwork.optimizer.apply_gradients(\
            (grad, var) for (grad, var) in zip(grads, self.SharedNetwork.trainable_variables) \
                if grad is not None)

    ~~~
> **_NOTE:_**  Please reach out to me directly for detailed code


## Conclusion
While REINFORCE was just an actor based method, we see that if we add a critique to criticise the policy learning, we can achieve a stable performance over time. Next in the article series are A2C and A3C, which are further developments in the actor-critic worlds.


## Supplementary Read (for enthusiast learners)
So far, we only talked about TD based critic. But, you can ask whether that's the only way to criticise the policy? The answer, ofcourse, is NO. Listed below are some other known critics that are available in literature. 

* Q Actor-Critic
* Advantage Actor-Critic
* TD Actor-Critic
* TD(λ) Actor-Critic
* Natural Actor-Critic




----------------

# Appendix

### References

> 1. Reinforcement Learning, An Introduction (Second Edition). [Sutton and Barto ](http://incompleteideas.net/book/first/ebook/node66.html){:target="_blank"} <br>
> 2. [University of California, Berkeley - Youtube Lecture](https://www.youtube.com/watch?v=EKqxumCuAAY&list=PLkFD6_40KJIwhWJpGazJ9VSj9CFMkb79A&index=8){:target="_blank"} <br>
> 3. [University of California, Berkeley - Lecture slides](http://rail.eecs.berkeley.edu/deeprlcourse-fa17/f17docs/lecture_5_actor_critic_pdf){:target="_blank"} <br>
> 4. [Lilianweng Github Page](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html){:target="_blank"}
> 5. [Phil Tabor's Youtube Page](https://www.youtube.com/watch?v=LawaN3BdI00){:target="_blank"}




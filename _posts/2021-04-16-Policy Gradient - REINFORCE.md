---
layout: post
title: "Policy Gradient - REINFORCE"
date: 2021-04-16
tags: Mathematics Reinforcement MachineLearning
comments: true
categories: [Reinforcement]
---

In this article, we will talk about the foundation Policy Gradient algorithm: __REINFORCE__.

The underlying idea here is to reinforce actions which result in higher cumulative rewards. In simple words, the algorithm increases the probability of action if it results in more rewards.

As in below figure, 
* $$a_0$$ with probability($$p_0$$): 0.5 results in cumulative reward of 100. 
* $$a_1$$ with probability($$p_1$$): 0.5 results in cumulative reward of 50. <br>


Hence, increasing $$p_0$$ will result in higher rewards on average.


<p class="aligncenter"> 
<img src="/data/pics/2021/04/REINFORCE.png" alt="Reinforce" width="615" height="350" />
</p>

REINFORCE works on this simple idea. Ofcourse, the internal mathematics and technicalities are more complex than above diagram.




## Digging Deeper - Mathematically
We would like to learn a policy that can take best actions without consulting the value functions. It becomes a conventional optimization problem as below:

__Objective__:
$$ {max} {J}(\theta) $$, where $${J} {, } \theta$$ refer to performance measure and policy parameters respectively.

Using [stochastic gradient ascent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent), we update $$\theta$$ in the direction of $$\nabla_\theta{J(\theta)}$$. <br>
$$ \theta_{t+1} = \theta_{t} + \alpha.\mathbb{E}[\nabla_\theta{J(\theta)}] $$

It turns out that computing gradient of performance is further simplified to:

$$ \nabla_\theta{J}(\theta) \propto  {G}.\nabla_\theta{log}\pi_\theta(s/a) $$ <br>

and $$\theta$$ udpate is re-written as :
$$ \theta_{t+1} = \theta_{t} + \alpha.G_t.\nabla_\theta{log}\pi_\theta(s/a) $$

Key takeaways from above equation:
1. $$ \nabla_\theta{J} $$ is independent of states distribution.
2. $$ \theta $$ is updated in proportion to return. If higher return is achieved by taking a particular action, then the probability of taking that action rises in proportion.


## Quick peek into the Algo 
Before we delve into the detailed algorithm, here are few tacts related to REINFORCE:
* A [_Monte Carlo_ based method](https://www.analyticsvidhya.com/blog/2018/11/reinforcement-learning-introduction-monte-carlo-learning-openai-gym/), i.e. it needs knowledge of full episode before learning.
* An [_On Policy_ algorithm](https://analyticsindiamag.com/reinforcement-learning-policy/), i.e. only learns the policy which decides the actions.
<p></p>

Here is a snippet of psuedo code taken from [Sutton and Barto's RL Book](http://incompleteideas.net/book/the-book-2nd.html)

<p class="aligncenter"> 
<img src="/data/pics/2021/04/reinforce_algo.png" alt="Reinforce Algo" width="650" height="250" />
</p>


<p></p>
A rough REINFORCE flow looks like:
<p class="aligncenter"> 
<img src="/data/pics/2021/04/reinforce_flow.png" alt="Reinforce Algo" width="735" height="350" />
</p>


## Implementation
There are many implementations available on the web, and I will not write another one here. The idea wanted to highlight is certain nuances while implementing this algorithm. So, sip your coffee slowly now!

* __Policy Network__:
    * Input: state vector 
    * Output: log probability per action,; determined using softmax
    * Loss function: Cross entropy. 
        * [Cross Entropy Loss](https://en.wikipedia.org/wiki/Cross_entropy) : $$L = \sum(y_i.{log p_i})$$
        * Our Policy Gradient also seeks for log of probability
    * Target value: Now, this is quite tricky. 
        * We use NNs under the realm of supervised learning. 
        * However, in RL, we are trying to better our target itself. 
        * Hence, we use a proxy for target variable as below:

        ~~~python
        # p_i --> action probability
        # y_i --> 1 for chosen action and 0 for not chosen action
        # alpha --> learning rate for policy network
        # G --> discounted Rewards

        gradient = -(p_i - y_i)           # this is the gradient of cross entropy loss

        # update the target value by gradient
        y_target = p_i +  alpha * G * gradient        
        ~~~ 

* __Training the agent__:
    * Since this is Monte carlo method, agent can only learn once the entire episode has ended

> **_NOTE:_**  Please reach out to me directly for detailed code


## Challenges & Potential Solutions
Being a basic algorithm, REINFORCE is bound to have certain challenges of its own.

#### __High Variance and slow learning__
> __Problem__
>>    * With cumulative rewards varying a lot every episode, the overall lerning becomes a bit noisy with high variance. 
>>    * A better way to reduce the noise is to normalize the rewards used. This is what we have now <br>
        $$ \theta_{t+1} = \theta_{t} + \alpha.G_t.\nabla_\theta{log}\pi_\theta(s/a) $$

> __Solution__
>>    * __Reinforce with Baseline__ -- > If we amend the reward by a function which is _independent_ of action taken, the overall learning becomes faster. <br>
        $$ \theta_{t+1} = \theta_{t} + \alpha.(G_t - b(s_t)).\nabla_\theta{log}\pi_\theta(s/a) $$
>>    * How do we choose baseline:
        1. Normalize Cumulative rewards: 
            $$G_t - b(s_t) = (G_t - \mu(G_t))/\sigma(G_t)) $$
        2. Use Value function as baseline.
            $$G_t - b(s_t) = G_t - V(s_t) $$



<p class="aligncenter"> 
<img src="/data/pics/2021/04/baseline.png" alt="Baseline comparison" width="500" height="240" />
</p>


#### __Episodic Learning__
> __Problem__
>>    * Being a Monte carlo method, knowledge of entire episode is required. 
>>    * Becomes impractical in more real-life scenarios when you dont know what may happen in the environment

> __Solution__
>>    * We need to move towards Temporal Difference (TD) methods; which we will learn more about in next articles


## Conclusion
Here, we learnt about the most basic Policy Gradient alogrithm. Ofcourse, this is just to do some warm up while we work out further deep into PG techniques. 







----------------






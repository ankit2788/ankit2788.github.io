---
layout: quantBook
title: "Introduction to Partial Differential Equations"
date: 2024-12-15
tags: [FinancialEngineering]
comments: true
categories: [Projectquant]
usemathjax: true
---

Math and Finance go hand in hand. Or should I say complex math and Finance always hold hands together. But, sometimes the whole math gets overwhelming we tend to skip the core concepts. In this series of articles, I will debunk some of the complexities around Mathematics in Derivatives, and go from simpler concepts to more evolved in today's world.

The 1st in this series is an introduction to Diffusion-Convection PDE, a form of [_Partial Differential Equation (PDE)_](https://en.wikipedia.org/wiki/Parabolic_partial_differential_equation), heavily used in the Financial Mathematics. So, hold your coffee and sip slowly. _A bit of caution here, as we simplify math, we cant avoid it._

## 1. Partial Differential Equation?

### a. What is it?

It is a type of differential equation that describes processes which evolve over time and space, such as heat diffusion, _option pricing_, etc. But what is it? Let's understand it through an example commonly available in natural world:

{% include admonition.html type="example" title="Example" body="Imagine we have a metal rod with a uniform initial temperature, and we heat one end of the rod. Over time, heat will spread through the rod, gradually evening out the temperature across its length. This process is governed by the heat equation, which mathematically is a <b> parabolic PDE</b>." %}


Later, we will extend the analogy to Financial Markets. 

The "parabolic" refers to the fact that the equation’s solution behaves like the shape of a parabola. This means that the equation models processes where the behavior smooths out over time and space, without abrupt jumps or oscillations in the space dimension.

In its simple 1 dimensionsal _space - time_ form, a parabolic PDE can be framed as below. This is an example of **Diffusion-Convection Process**

$$
% \begin{aligned}
\frac{\partial V}{\partial t} = \alpha \frac{\partial^2 V}{\partial x^2} + \beta \frac{\partial V}{\partial x} + \gamma V 
% \end{aligned}
$$

Or

$$
% \begin{aligned}
V_{t} = \alpha V_{xx} + \beta  V_{x} + \gamma V 
% \end{aligned}
$$

where 
$$V_{xx}$$ represents the second derivative of $$V$$ with respect to $$x$$

Now, lets break the equation down. 

### b. Diffusion Component

$$ \alpha \frac{\partial^2 V}{\partial x^2} $$ highlights the diffusion in the process. This process looks something like the below (_in a 2D space_). 
{% include admonition.html type="example" title="Example" body="Imagine opening a perfume bottle in a room. At first, the scent is concentrated near the bottle. Over time, the scent spreads throughout the room. This spreading of the perfume molecules is <b>diffusion</b>." %}

<p align="center"> 
<img src="/data/pics/finengg/numerical/DiffusionAnim.gif" alt="Diffusion Process"  width="200" height="200" text-align="center"/>
</p>


### c. Convection Component

$$ \beta \frac{\partial V}{\partial x} $$ determines the convection part in the above PDE. 
{% include admonition.html type="example" title="Example" body="Imagine a pot of water heating up. The water at the bottom gets hot, rises, and then cooler water moves down to take its place. This circular movement is <b>convection</b>." %}





## 2. Black Scholes Equation - The Core in Financial Mathematics


Black Scholes Equation is the fundamental force in Derivative pricing. If you havent heard of it, then may be this article is not relevant for you! In its basic form with all assumptions, the equation takes the below form. The equation is a type of Parabolic PDE, and may look a bit scary to begin with. 

$$
% \begin{aligned}
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} r S \frac{\partial V}{\partial S} - r V = 0
% \end{aligned}
$$

Where:
- $$V = V(S, t)$$ is the price of the option as a function of the stock price $$S$$ and time $$t$$.
- $$S$$ is the current price of the underlying asset (e.g., stock). 
- $$t$$ is the time.
- $$r$$ is the risk-free interest rate, and can be a function of $$S$$ and $$t$$
- $$\sigma$$ is the volatility of the asset’s returns, and can be a function of $$S$$ and $$t$$
- $$ \frac{\partial C}{\partial t} $$ is the partial derivative of the option price with respect to time.
- $$ \frac{\partial^2 C}{\partial S^2} $$ is the second partial derivative of the option price with respect to the stock price.
- $$ \frac{\partial C}{\partial S} $$ is the first partial derivative of the option price with respect to the stock price.

<br>
{% include admonition.html type="tip" title="TIP" body="Here, we aim to solve to V(S, t), i.e. the value of the derivative. The above equation is called a Forward Black Scholes equation. Forward is in time, i.e., sitting today, we aim to value the option expiring 1 month in the future." %}



### a. From forward Black Scholes to backward equation
Above is a forward equation, in which time refers to current time, and V (price of the derivative) evolves through time. For example, sitting today, and valuing a 1 month maturity derivative, $$T$$ = 1 month. 

However, under initial conditions, we only know the payoff at maturity, i.e., only on maturity, we can explicitly compute the derivative's payoff.

> **Note**: Hence, we need to convert the forward equation into a backward equation where $$t$$ will refer to time to maturity.

$$

t' = T - t \\
\frac{\partial v}{\partial t} = -\frac{\partial v}{\partial t'} 

$$

Now, replace this in the Black-Scholes equation to make it backward in time:

$$
% \begin{aligned}
-\frac{\partial V}{\partial t'} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0 
% \end{aligned}
$$

Where:
- $$ V(S, t') $$ is the option price as a function of the asset price $$ S $$ and time $$ t' $$,
- $$ t' $$ is the time to expiry.

{% include admonition.html type="tip" title="Backward Black Scholes" body="We will now use this equation as our base equation to solve, where $$t'$$ will be interchangeably replaced by t, but reflecting time to expiry." %}


### b. Initial Conditions

Initial values are extremely important in order to approximate a PDE. These refer to the value of the unknown, i.e. the derivative $$V(S, t)$$, at $$t = 0$$. Based on the derivative involved, the initial value is observable. 

**Examples**: 
- For a **European call option**:
  $$ V(S, 0) = \max(S_T - K, 0) $$
- For a **European put option**:
  $$ P(S, 0) = \max(K - S_T, 0) $$

where $$ S_T $$ is the stock price at maturity and $$ K $$ is the strike price.

This is usually known as [Initial Value problem](https://en.wikipedia.org/wiki/Initial_value_problem) in calculus..


### c. Boundary Value conditions
These are sort of constraints defined on the original differential equation at the extremes (or boundaries). In the context of Black Scholes (or a derived equation), these can be formed as 

$$
% \begin{aligned}
V(S_{min}, t) = \alpha(t) \\
V(S_{max}, t) = \beta(t) 
% \end{aligned}
$$

where 
- $$\alpha$$ and $$\beta$$ are independent of $$S$$ and only dependent on $$t$$
- $$V(S_{min})$$ and $$V(S_{max})$$ are boundary conditions at $$S_{min}$$ and $$S_{max}$$ respectively



This case of boundary condition is known as [Dirichlet Boundary Conditions](https://en.wikipedia.org/wiki/Dirichlet_boundary_condition), where the value of unknown function $$V$$ is known at boundary points. <br>

There could be other case of boundary conditions where the 1st derivative of unknown function is known at $$S_{min}$$, i.e. $$ \frac{\partial C}{\partial t}  = \alpha $$. It is called [Neumann Boundary Conditions](https://en.wikipedia.org/wiki/Neumann_boundary_condition)


---

This equation forms the basis for the **Black-Scholes model** to calculate the theoretical price of European call and put options. In the simplest form, Black Scholes takes on multiple assumptions. In subsequent articles, we will start with the case when $$\sigma$$ is considered to be a constant, but will gradually shift to a more realistic case when $$\sigma$$ takes on more practical stochastic nature. 
The next few articles will focus on explaining the different Numerical methods, i.e. Finite Difference techniques and other variations.

Till then, stay tuned for the next article. 

---

## Math Concepts
Listing down some of the mathematical concepts referred in this article
1. Partial Differential Equations (PDE) - Diffusion/ Convection Processes
2. Parabolic PDE
3. Initial Value Problem
4. Boundary Value Conditions (Dirichlet, Neumann, Robin etc)



# Appendix

> 1. Research Details & Source: **Project Quant**, by _Ankit Gupta_







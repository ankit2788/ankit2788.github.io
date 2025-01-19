---
layout: quantBook
title: "Numerical Methods - Explicit Euler Methods"
date: 2024-12-17
tags: [FinancialEngineering]
comments: true
categories: [Projectquant, FinancialEngineering]
usemathjax: true
---

In the [last article](/projectquant/financialengineering/2024-12-15-Intro-to-PDE/){:target="_blank"}, we introduced the concept of Partial Differential equations, and how Black Scholes is a wonderful such example 

Starting this article, we will uncover some of the techniques to solve for the Black Scholes equation, i.e. approximating the option values. Note that, for a vanilla call and put option, there is a closed form equation [already available](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model){:target="_blank"} which is used in real-world. But the idea of this article to identify techniques which can solve a complex Partial Differential equation. 

This article is the 1st of **Numerical Methods** for solving Partial Differential Equation, with the focus here on **Explicit Euler Scheme**. 

Let's start with the summary of the Black Scholes PDE.

---


**Summary of Black Scholes PDE**

<details>
<summary><b>Backward Black Scholes PDE</b></summary>
$$
% \begin{aligned}
-\frac{\partial V}{\partial t'} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0 
% \end{aligned}
$$
</details>

<details>
<summary><b>Initial Value problem</b></summary>

For a European call option: 
$$ 
% \begin{aligned}
V(S, 0) = \max(S_T - K, 0) 
% \end{aligned}
$$

{% include admonition.html type="note" title="Note" body="In later articles, we will try to value a more complex derivative product, such as Barrier option or a Equity-Credit Hybrid product with a more complex initial value." %}

</details>


<details>
<summary><b>Boundary Conditions</b></summary>
In the case of boundary conditions, we tend to find option values at extreme ends of stock price.

$$
% \begin{aligned}
V(0, t) = 0 \\
V(S_{max}, t) = S_{max} - K e^{(-rt)}
% \end{aligned}
$$

</details>

---



## Explicit Euler Method - The Theory
Under the Numerical methods, the process is discretized with steps in both space and time. In a simple case of single option pricing, we can have a 2D discretized grid as below, where the y-axis represents possibilities of the stock price movement


<p align="center"> 
<img src="/data/pics/finengg/numerical/explicit.png" alt="Explicit Euler Scheme"  width="471" height="285" text-align="center"/>
</p>

A Vanilla call option pricing can be iteratively done through this grid, given that 
- we have the Initial values available at t = 0, i.e. at maturity, and
- boundary conditions are known, i.e, option value when underlying stock is at the extreme.

{% include admonition.html 
  type="note" 
  title="Note" 
  body="V(i,n+1) depends on 3 points. 
  <ul>
    <li><i>V(i-1, n): option value at \( S = S_{i-1} \) and previous time</i></li>
    <li><i>V(i, n): option value at \( S = S_{i} \) and previous time</i></li>
    <li><i>V(i+1, n): option value at \( S = S_{i+1} \) and previous time</i></li>
  </ul>" 
%}

---


## Discretized Black Scholes - Application in Finance

### a. Time derivative

Here, $$ n+1 $$ refers to forward in time, using _forward difference method_ --->   $$ \frac{\partial v}{\partial t'} \approx \frac{v_i^{n+1} - v_i^n}{\Delta t'} $$

### b. Spatial derivative (2nd order)
For the second spatial derivative $$ \frac{\partial^2 v}{\partial S^2} $$, we use the _central difference_ ---> $$ \frac{\partial^2 v}{\partial S^2} \approx \frac{v_{i+1}^{n} - 2v_i^{n} + v_{i-1}^{n}}{(\Delta S)^2} $$

### c. Spatial derivative (1st order)
For the first spatial derivative $$ \frac{\partial v}{\partial S} $$, we use the _central difference_ as well ---> $$ \frac{\partial v}{\partial S} \approx \frac{v_{i+1}^{n} - v_{i-1}^{n}}{2 \Delta S} $$

### d. Black Scholes discretization
Hence, under the **Explicit Euler Scheme**, the Backward Black Scholes can be approximated as:

$$
% \begin{aligned}
-(\frac{v_i^{n+1} - v_i^n}{\Delta t}) + \frac{1}{2} \sigma^2 S_i^2 \frac{v_{i+1}^{n} - 2v_i^{n} + v_{i-1}^{n}}{(\Delta S)^2} + r S_i \frac{v_{i+1}^{n} - v_{i-1}^{n}}{2 \Delta S} - r v_i^{n} = 0
% \end{aligned}
$$

This can be re-written as: $$ -{\theta}_i + \frac{1}{2} \sigma^2 S_i^2 {\gamma}_i + r S_i {\delta}_i - r v_i^{n} = 0 $$

where 
- $$ {\theta}_i = \frac{v_i^{n+1} - v_i^n}{\Delta t} $$ represents how the price changes per unit of time
- $$ {\delta}_i = \frac{v_{i+1}^{n} - v_{i-1}^{n}}{2 \Delta S} $$ represents how price changes per unit of underlying price
- $$ {\gamma}_i = \frac{v_{i+1}^{n} - 2v_i^{n} + v_{i-1}^{n}}{(\Delta S)^2} $$ represesnts how delta changes per unit of price


Hence, $$ v_i^{n+1} = v_i^n + \Delta t.\theta $$


### Codify Explicit Euler - Black Scholes

Above discretization steps help compute the value of $$ v_i^{n+1} $$ at time step $$ n+1 $$. The entire process needs to execute iteratively across values of time ranging till t = $$ T $$. Within each time step, we need to iterate through each space step as well. 

{::options parse_block_html="true" /}  
<details><summary markdown="span">Here is a sample python code depicting Explicit Euler Scheme:</summary>


```python

  SMax  = 200
  SMin  = 0
  timetoMaturity = 1
  vol   = 0.2
  rate  = 0.05
  nbSpaceSteps = 100
  nbTimeSteps = 100
  K = 100     # strike
  S0 = 100
  
  # initializing the space and time vectors for the grid
  S = np.linspace(SMin, SMax, nbSpaceSteps + 1)
  dS = (SMax - SMin)/nbSpaceSteps

  t = np.linspace(0, timetoMaturity, nbTimeSteps + 1)
  dt = (timetoMaturity - 0)/nbTimeSteps

  # setting the storage grid for derivative price
  V = np.zeros((nbSpaceSteps+1, nbTimeSteps+1))
  
  # initial condition 
  if optiontype.upper()[0] == "C":
      V[:,0] = np.maximum(S - strike, 0)
  else:
      # for put option
      V[:,0] = np.maximum(strike - K, 0)

  # boundary condition
  if optiontype.upper()[0] == "C":
      V[0, :] = 0
      V[-1, :] = (SMax - strike)*np.exp(-rate*t)
  else:
      V[-1, :] = 0
      V[0, :] = (strike- SMin)*np.exp(-rate*t) 

  # apply Explicit Euler discretization
  for n in range(0, nbTimeSteps):
      # time refers to time to maturity

      for i in range(1, nbSpaceSteps):

          # compute intermediaries
          _delta = (V[i+1, n] - V[i-1, n])/(2*dS)
          _gamma = (V[i+1, n] - 2*V[i, n] + V[i-1, n])/(dS*dS)
          _theta = -0.5*vol**2*S[i]**2*_gamma - rate*S[i]*_delta + rate*V[i,n]

          V[i, n+1] = V[i, n] - dt*_theta


```

</details>
{::options parse_block_html="false" /}   

---

## Results


### a. Option Valuation

A vanilla call option is, as the name suggests, "Vanilla". Similar valuation can be obtained through the closed form equation for Call option. However, in the later articles we will extend the techniques to price more complex derivatives. 

<p align="center"> 
<img src="/data/pics/finengg/numerical/explicit_call.png" alt="3D Call price"  width="594" height="500" text-align="center"/>
</p>

### b. Stability Challenges


Well, Explicit Euler Scheme behaves erratically for certain cases. 

<details>
<summary><b> b.1. Less number of timesteps for computation </b></summary>

<p align="center"> 
<img src="/data/pics/finengg/numerical/explicit_stability.png" alt="Stability"  width="1300" height="240" text-align="center"/>
</p>


As step size, _dt_,  increases (or timesteps decrease), stability concerns start arising. Computation of the option price becomes extremely unstable. Figure (i) displays how the option price significantly fluctuates before getting more stable once timesteps increase. Similarly, Figure (iv) tells the story about gamma. Gamma (second order derivative) compuation fluctuates at the boundary values of underlying price. 

</details>


<details>
<summary><b> b.2. Low Volatility </b></summary>

As volatiliy decreases (or diffusion component decreases), Explicit Euler scheme tends to render itself as useless. In the case of FX derivatives, where volatility tends to be usually in single digits, this scheme may not be the best. 

At a volatility level of 0.1% (extremely low vol), the unstability is clearly evident near the strike
<p align="center"> 
<img src="/data/pics/finengg/numerical/explicit_vol1.png" alt=""  width="1300" height="280" text-align="center"/>
</p>



As volatility goes up, we tend to obtain a more stabile profile of price and risk profiles.

<p align="center"> 
<img src="/data/pics/finengg/numerical/explicit_vol2.png" alt=""  width="1300" height="280" text-align="center"/>
</p>



<p align="center"> 
<img src="/data/pics/finengg/numerical/explicit_vol3.png" alt=""  width="1300" height="280" text-align="center"/>
</p>

</details>

---


## Summary

Explicit Euler Scheme is the most basic of Numerical Methods of solving Partial Differential Equations. Although simplistic, both in understanding and python implementation, this scheme comes with quite a few limitations, and hence a lower practical usage. In the next article, I will focus on another version of Euler methods. 

---

## Math Concepts
Listing down some of the mathematical concepts referred in this article
1. Explicit Euler Schemes
2. Central Difference Technique, Forward Difference techniques
3. Trinomial Pricing (lattice models)


# Appendix

> 1. Research Details & Source: **Project Quant**, by _Ankit Gupta_
> 2. Finite Difference Methods in financial engineering, A Partial Differentiation Equation Approach, by Daniel J Duffy







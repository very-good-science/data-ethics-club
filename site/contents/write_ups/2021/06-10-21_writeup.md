# Data Ethics Club: [Structural Injustice and Individual Responsibility](https://www.abc.net.au/radionational/programs/philosopherszone/structural-injustice-and-individual-responsibility/13486680) (6th October 2021)
<!--Please don't edit the info panel below-->

```{admonition} What's this? 
This is summary of Wednesday 6th October's Data Ethics Club discussion, where we spoke about the podcast episode [Structural Injustice and Individual Responsibility](https://www.abc.net.au/radionational/programs/philosopherszone/structural-injustice-and-individual-responsibility/13486680), an episode of the podcast The Philosopher's Zone
with David Rutledge, with guest Robin Zheng, Assistant Professor in Philosophy, Yale-NUS College Singapore..

The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with a final edit.
```
## Introduction

This week's discussion was on [Structural Injustice and Individual Responsibility](https://www.abc.net.au/radionational/programs/philosopherszone/structural-injustice-and-individual-responsibility/13486680), an episode of the podcast The Philosopher's Zone
with David Rutledge, with guest Robin Zheng, Assistant Professor in Philosophy, Yale-NUS College Singapore.

The episode asks who is responsible for structural injustice? Whilst some might say the answer is “practically everybody”, others might suggest that is just another way of saying “effectively nobody”. In a few of our previous talks, we've discussed what responsibility individuals bear for structural injustice and how can this responsibility be acted upon. 

## What do you see as the structural injustices in data science, compared to the injustices that are largely out of data scientists control? 

Structural injustics seem like the things that data scientists often struggle to control. Historically we may always have modelled things in a certain way and we can't quickly change the ways that things are measured. A great example of this is the English language bias in programming. Languages like Python functions are designed with English as a default. 

Structural injustices seen in data science are often seen in the data itself. The big thing we often call for is greater mutlidisciplinairy approaches to design and evaluation of systems.

Tools we use depend on higher level scripting languages which are less energy efficient, especially in the age of *big data* (e.g.[ “The ecological impact of high-performance computing in astrophysics” (Zwart, 2020)](https://arxiv.org/abs/2009.11295v1)). The effects of global warming disproportionately affects developing countries.


Inherent bias in NLP & sentiment analysis. 

Ableims in graphs - blind-ness and graphs. The way that we communicate data is inherently biased. 

‘‘‘Fair’ is the stupidest word humans ever invented, except for ‘staycation’.’’
https://www.cell.com/patterns/fulltext/S2666-3899(20)30089-1#%20

We love to know what we're doing and get excited about how to do it. But lots of people are happy to forget about the "why". Academics and scientists are trained to big up our results - a focus on the success of this (tech) approach.

How comfortable are we data scientists using the work/products of underpaid workers (this links abck to when we talked about the [Nevada Lake](https://very-good-science.github.io/data-ethics-club/contents/write_ups/2021/11-08-21_writeup.html) in a previous discussion).

Both are due to incentives for funding and career progression.
- Example: gender recognition from names (text)
- Example: GitHub - I cannot work without it, but it's a bit evil for sure (ICE contracts).
- Buying/selling data - commercial interests (e.g crypto companies getting custom by **not** selling data)
- Ecological footprint of services like GH
- "If you don't think you can make a difference, spend a night in a room with a mosquito"
- E.g. we could make figures that have alternative text . 

From summary - the scale of data science tools is part of what makes them so concerning. 

## Who is attributable for harmful deployments of data science? (E.g. The original researchers? The company who sold it? The government who bought and deployed it?) And who is accountable?

Broadly speaking, those with a STEM background think in a reductionist way to problems: here's a problem, here are the tools we have to fix them, how are we going to make this happen. Liberal arts backgrounds might have a different viewpoint where they see some problems not having solutions and that we should sometimes avoid trying to solve some, as we might make those problems worse.

Introducing greater multidisciplinary design is a great way to bring together the pragmatic utility typically associated with a STEM background and the more considerate thoughtfullness of those with alternative backgrounds.

We tend to select projects based on this reductionist problem/solution approach
big data, build what they think as needed, but data is biased - who defines what is biasaed or unbiased?

When arguing about attribution for harmful uses of data science, one could make a strong analogy on insurance; there are plenty of other things we don't blame people for, but we have to decide as a group how we share the responsibility to sort stuff out.

But the insurance analogy still puts culpability in the hands of those who can manage the risk. Car manufacturers are responsible for adhering to certain safety standards, even if at times it might limit the capabilities of your technological developments. The difficulty is agreeing on what those standards are in, particuarly in a context of a quickly evolving technological capabilities that we are all struggling to keep up with.

If we're part of the system, are we automatically complicit? As a data scientist is it your duty to correct things? There should be a responsibility to think critically about methods used and findings - ignorance is not an excuse. 

Figuring out where blame or attribution lies is very difficult because there is a big chain of input and responsibility. 

Data scientists is frequently not as life and death as the automotive industry, but they tackle a lot of questions that are related to structural injustice. Data scientists still have a responsibility to consider how they use the tools at their disposal. 

There is a burden of responsibility which could prove to be heavy and overwhelming. Indeed, some  It's difficult to feel the whole weight of the heaviness and responsibility. 

## How could individuals in the role of data scientist, publisher, funder, company, or government use their role to push boundaries?

Facebook going down a few days before this discussion was had was a noteworthy example of the monopoly they had affected a lot of people - the fact that they have been able to get this monopoly is problematic. It provides an interesting case study when considering what individuals can do to make a difference.

What's realistic about what we could change?  Will Facebook cease to exist overnight? Probably not. Will it help if everyone who is ethical leaves Facebook? Or if more ethical people join Facebook, does that just let Facebook get away with the bad things that they do? 

What if everyone left, and created a competitor? It would require a lot of coordination, will, and resources and would be a large uphill battle. Even if it was successful, what would stop this competitor becoming just like Facebook.

Do we perpetuate the system in the short-term in order to make things better in the long-term? Who decides what is "better"?

It's important to pull together and convene different disciplines. Recognising bias in data is super important. It's not the data scientists job to fix the data. How should we define biased or unbiased? Whose job is that?

We should push to involve more people in the conversation, even this likely will slow down the process of development.

Taking the time to sit and think about things as a developer is important but not universally done. There's not inscentives for developers to behave ethically, just to get the job done. Not only are developers not comfortable admitting potential culpability, there's in fact strong pushback from developers over ethics "getting in the way". This is particularly true with large developments into AI/machine learning.

Data scientists are not the only people accountable for developing tools used for bad things - marketing folks are culpable too!

"Why don't you focus on hitting your target and worry about the fluffy stuff later?"

Sharing the burden of responsibility with others is helpful! It maybe makes it easier to remind ourselves of our purpose and 

One practical example of how a company could use their role to push boundaries would be to stop offering unpaid internships.

It's not untypical to see ethical considerations ignored until release manager blocks deployment, showing there is a slow evolution into introducing regulation. Ironically, some developers literally see ethical considerations as something restricting to them.

---

## Attendees

__Name, Role, Affiliation, Where to find you, Emoji to describe your day__
- Natalie Thurlby, Data Scientist, University of Bristol, [NatalieThurlby](https://github.com/NatalieThurlby/), [@StatalieT](https://twitter.com/StatalieT) 
- Nina Di Cara, PhD Student, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Aaron MacSween, applied cryptographer/project lead, XWiki SAS/CryptPad, [ansuz](https://github.com/ansuz), 🐶
- Euan Bennet, Senior Research Associate, University of Bristol, [@DrEuanBennet] (https://twitter.com/DrEuanBennet)
- Kamilla ['Milli'](https://www.linkedin.com/in/kamilla-wells/) Wells, Citizen Developer
- Mia Mace, [mace-space](https://github.com/mace-space)


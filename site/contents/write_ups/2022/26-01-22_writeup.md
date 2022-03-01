# Data Ethics Club: [Which Programming Languages Use the Least Electricity?](https://thenewstack.io/which-programming-languages-use-the-least-electricity/)
<!--Please don't edit the info panel below-->

```{admonition} What's this? 
This is summary of Wednesday 26th January's Data Ethics Club discussion, where we spoke about the article [Which Programming Languages Use the Least Electricity?](https://thenewstack.io/which-programming-languages-use-the-least-electricity/) by David Cassel.

The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with a final edit.
```

## Introduction

The article investigates the question "Can energy usage data tell us anything about the quality of our programming languages?", commenting on the research paper [Energy Efficiency Across Programming Languages](https://greenlab.di.uminho.pt/wp-content/uploads/2017/10/sleFinal.pdf). In this paper, the researchers ran the solutions to 10 programming problems written in 27 different programming languages, while carefully monitoring how much electricity each one used — as well as its speed and memory usage. We discussed the methodology of the paper, the results and how it affected our view on coding in a more green way.

## Are you surprised by any of the results?

One of our members, Ben, pointed out some technical problems with the methodology of the paper, specfically, that the cache effects excluded.

The cache keeps frequently used data nearby for quick access. This reduces the number of times you have to access your main memory. This has a large effect on energy consumption. This is one of the things that would have the most important impact on the output. The problems which the authors chose to analyse were comparatively small.

In summary, the problem is measured wrong, based on flawed assumptions.

The paper asks a question that is almost too specific. Another interesting question might be, which languages do people make the most mistakes in? This would mean having to consider recompiling the same problem over and over.

Some of us were suprised about the detail in the discussion, but not the results, generally that high level languages tend to use more energy. There is a lot of things missing on general sustainability.

Others were not really sure what we expected, but our main expectations were C will be quite efficient and Python will not be. Python is more familiar to a lot of us so we do not want to go back to C. We will go back to C once billionaires stop launching themselves into space. 

Perhaps the reduction in environmental impact by using C is cancelled out by everyone having multiple tabs open with "how do I do anything in C?" Many people are self-taught in coding and their teacher wasn't very good. Is it fair for the purposes of this study to assume that everyone is a good coder?

Many of us use Python, but often it is actually using C under the hood. We would have liked to see comparisons to numpy/pandas. For example, NumPy is available in Python and uses C but they didn't include this.

There were also some of us who used R or C as well. Other languages such as Fortran are efficient, archaic but very old school. The closer a language is to how a computer "thinks" the more energy effecient they tend to be at the cost of being harder for people to learn and implement efficiently. For the average coder, this means that there will be a tradeoff when using more effecient but harder to work with languages. 

One member shared an example of an individual program used repeatedly being optimised from [University of Bristol's Advanced Computing Research Centre](https://bristol.ac.uk/acrc/research-software-engineering/case-studies/minimalmarkers/#d.en.578273):
"The Research Software Engineering (RSE) Group worked with Dr Gary Barker, a Senior Lecturer in the School of Biological Sciences, to speed up a Perl script that he developed to find the minimal set of genetic markers needed to differentiate all samples in a genotyping dataset. After 10 days of work, the software was accelerated by over 25,000 times (figure 1). This reduced the runtime for identifying the minimal set of markers to distinguish different varieties of wheat from about 10 days to just 34 seconds!"

## Is changing our programming practices an effective way to reduce our environmental footprint?

Regardless of any technical issues of the study, many of us came to the conclusion that nothing from this paper at all should affect how we go about coding. 

Should we be thinking more carefully about which programming problems we even attempt to tackle and perhaps focussing on important and useful problem instead of training more and more useless models? Should energy metrics be reported alongside accuracy metrics? If all computational number theorists stopped computing or even if they just switched from Python to C, would that be better?

There is great value to fundamental research even if it is not immediately apparent and so we should be cautious at cutting corners in research.

Not everyone has access to run expensive time consuming models. At a management level, people are deciding which cloud services to use have a lot of power to change the environmental cost. 

This paper feels quite out of context from that. What papers like this seem to encourage is 15-20 of us is to ditch Python and go to C and doesn't really address bigger organisations doing an enormous amounts of power usage.

Realistically, how would this paper be applied? Maybe this sort of study (perhaps with some technical adjustments) could be done within a large institution to consider the energy cost/loss. 

There are no limits on hardware/software that stop you running out your battery immediately/using loads of energy. User experience can be a competing requirement. There is a risk of premature optimisation. 

Are there better things to optimise? Not everything needs to be smart, e.g. kettles, lamps, BBQs. Reusable code will be able to be better optimised - reinventing the wheel.

Policy is very focused on the energy source of heat and transport, but not on digital technologies and how they use the energy.

Any discussion about energy efficiency needs to include big companies. There exists a dichotomy between prioritising research (for the benefit of society as opposed to personal profit) vs being energy effecient. Potentially we want to have a different discussion about whether colonising other planets is energy efficient.

Could we offer companies an audit on energy usage and/or do they need to use machine learning? Because more often than not, they don't.

High vs low level languages: how much of what is actually being run by the computer is being hidden from you. A key example is memory management: you don't need to delete arrays that you're finished using to make sure that you're not keeping those arrays in memory any more.

## Are some jobs just not worth doing?

We also thought about the coding infastructure and the amount of electricity involved. Do these need to be considered? Is this a "useful" component in this economy? Is it time to admit that some jobs are just not worth doing? What if it is more efficient to just not do them?

This kind of research has a place within that and is a relevant consideration but has to be put into context. In Scotland there was a consideration to extend working from home (not just for pandemic reasons) and some media outlets tried to undermine the pollution factor at play.

How much has this problem been thought of before?
Coding and coding infastructure is probaly not top of the list when we think of climate change. This paper does highlight that computational resources is fairly worth thinking about. Urgent to tackle but easiest solution (switch to renewable energy). Fewer steps to solving this. But we should also be mindful about resources used to make computers, as we discussed in a [previous talk](https://dataethicsclub.com/contents/write_ups/2021/11-08-21_writeup.html).

Speed is a good proxy for energy consumption. But if we make things faster then people might just run them more ofter. For example, creating more energy efficient fuel sources created more fuel consumption. This is an example of [Jevons' paradox](https://en.wikipedia.org/wiki/Jevons_paradox#:~:text=In%20economics%2C%20the%20Jevons%20paradox,rises%20due%20to%20increasing%20demand.).

## What change would you like to see on the basis of this piece? Who has the power to make that change?

What is the point of us being more effecient with coding when we're flying internationally for our jobs? Every little helps but it is difficult to make a significant impact on a larger scale.

We are incentivised to drive cars, which is part of the reason it continues to happen. Is it the programming language or the context (architecture? libraries? CI? RStudio/Jupyter notebook?) Maybe we should be optimising libraries rather than the people using them. Why not get a GitHub button that gives an energy rating for code? At graphcore it tells you how much CO2 a job will take. People are either horrified or desensitised. 

Ultimately this piece gave us an opportunity to reflect on our own individual energy usage but bought us back to the idea of corporate responsibility.

["There is a greater honor is deleting code than in writing more"](https://twitter.com/EduanBekker/status/1233241991598788608?s=20)

--- 

## Attendees
__Name, Role, Affiliation, Where to find you__
- Natalie Thurlby, Data Scientist, University of Bristol, [NatalieThurlby](https://github.com/NatalieThurlby/), [@StatalieT](https://twitter.com/StatalieT) 
- Nina Di Cara, PhD Student, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
-  Euan Bennet, Senior Research Associate, University of Bristol, [@DrEuanBennet](https://twitter.com/DrEuanBennet)
- Emma Tonkin, Research Fellow, University of Bristol (https://twitter.com/emmatonkin)

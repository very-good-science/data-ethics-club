# Data Ethics Club: [Hacking the cis-tem](https://www.marhicks.com/writing/hicks-hackingthecistempreprint.pdf)
<!--Please don't edit the info panel below-->

```{admonition} What's this? 
This is summary of Wednesday 21st September's Data Ethics Club discussion, where we spoke [Hacking the cis-tem](https://www.marhicks.com/writing/hicks-hackingthecistempreprint.pdf), a paper by Mar Hicks from the Illinois Institute of Technology. 
The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with the final edit.
```

```{image} ../../images/Phrenology.jpg
:width: 200px
:align: center
:alt: Drake me. Saying no to "Measurements of bumps on the skull to predict mental traits" but yes to "Training an ML model to do it for you" Meme made by Huw Day.
```

## Introduction

In this meeting, we discussed the paper [Hacking the cis-tem](https://www.marhicks.com/writing/hicks-hackingthecistempreprint.pdf), written by Mar Hicks. As outlined in the abstract:

"This paper looks at the case of transgender Britons who tried to correct the
gender listed on their government-issued ID cards, but ran up against the British
government’s increasingly computerized methods for tracking, identifying, and defining
citizens."

We used the paper to launch our own discussions about how data science practitioners are often guilty of forcing people/subjects into discrete categories at the expense of their identity. This can take the form of being too restrictive with initial inputs of data (e.g. sex or gender) or making it difficult to change these categories (e.g. if someone transitions or if someone's name changes due to marriage or other circumstances). Often this isn't done maliciously, but it remains the responsibility of the data wranglers in question to be well informed of potential pitfalls.

We shared times we had ourselves been guilty of these practises, discussed how this can lead to discrimination, issues with machine learning systems trying to "identify" or arbitrarily place people in these categories and the responsibilities of those constructing these systems.

## Can you think of a time you’ve been guilty of this practice?

Euan's background is astrophysics but he started working with data working with horses. One of his earliest encounters with identity categories was of "horse sex". It transpires that there are more than 2 categories of horse sex.

One of our members has seen that the NHS is guilty of reinforcing some of these issues. They claim to collect "gender" but it's actually sex. There is an "undisclosed" option. Depending on the service, this category can be interpreted as sex or gender. This feels like the data is being used against people rather than to help them and that it is probably causing harm somewhere.

Some of our members admitted they likely had been guilty of these practises, but unaware of it. Now they choose not to collect it because it's not relevant to what they're doing. These practises came up when doing "AI" categorisation of gender (looking at names for example), to see what averages of people are discussing/believe different things. It is difficult to include non binary people but an uphill battle to make this issue a priority for private companies.
On the other hand, we've discussed previously how not collected data about marginalised groups prevents us from testing whether models are biased against them. 

The patent office did something similar where they aiming to find out whether some groups of people (e.g. women) were underrepresented in patents, but the methodology is quite flawed (which they admit). They could identify male and female names but there are a number of names that fall into both categories depending on region and when the person was born/named.  

Just because something does not harm many people, that doesn't necessarily mean it is less harmful overall - a lot of harm could be caused to a small number of people. This subtlety is complicated because we also don't always have reliable numbers for either of these things.

A common one was making decisions about how to record gender in forms. Open text? Drop down?
Difficult when you're having to satisfy someone else's requirements for reporting or accounting reasons if working within wider systems. There's often an inherent assumption of women being associated with non-binaryness. 

In Australia the [census this year was an online tool](https://www.sbs.com.au/news/article/faafafine-the-boys-raised-to-be-girls/5tmlnxjaj), so questions appeared based on what answer you selected.

## How can the construction and manipulation of identity categories by computerised systems lead to discrimination? 

The problems we discussed highlight that biological essentialism was baked into the welfare state and the assumptions that came with that. However, a lot of the design choices are probably convenience based for the people designing the system rather than maliciousness (but not always, and this does not excuse these design choices). Sometimes it can be a case of "protecting" the protected variables. If its a category someone might be discriminated against, it might be worth protecting/obscuring this to the general public.

Dataset size is an issue when you use a larger number of categories. For example, if you've got 100 people identifying as male and then 10 as non-binary then it might be hard to do meaningful analysis on  the smaller dataset.

The difficulty with putting people into categories is that things like gender are being regarded as more of a spectrum and so classifying many different pronouns, you start to lose anonyminity when you identify them. Being in a minority group puts you at higher risk of discrimination and so we need to strike the balance between minorities being seen but not at a higher risk.

How do you handle the fact that these variables might change over time? Be it gender, sexuality or even surname. Euan worked with a database which had no identifying numbers, only had names. One database did update surnames if population members got married, one didn't. This lead to difficulty when comparing between datasets. But anytime identifiers are needed, the requirement of anonymity needs to be considered.

Are changes to datasets going forward going to include updating retrospective data? Could this lead to misunderstandings of how society is changing? Is co-design a solution? Should we be having more conversations about when collecting certain data is even necessary? We're told that digitising things is improving them, but often that's not always true.

The problem is often bureaucracy, not necessarily technology. For example, not being able to get a bank account without an address. There's an assumption there that everyone has a house. 

It is vital to consider edge cases. A system that works 99% of the time sounds good, but the consequence of being in the 1% is very hard. Although as Ruth Ng points out: ["In tech, there are "edge cases". But there are no such thing as edge case people."](https://www.ruth-ng.co.uk/how-to-ask-about-gender-in-forms-respectfully).

## What are the risks of AI systems artificial intelligence systems that are designed to “discern” or algorithmically “identify” aspects like gender or sexuality from facial data or other categories?

Humans jump to conclusions is because it helps us make very quick decisions. One thing we do is look at someone's face and make judgement calls. These judgements can include gender identity, sexuality or race. You can't get an algorithm to do that quick thinking and justify it like a human can. Without explainability, you don't have a leg to stand on. Even as people, that's kind of what we do.

Datasets trained on straight cis white men will be better at identifying straight cis white men than other groups. We have to be careful about algorithimic decision pipelines which don't have humans involved. We have online data but also natural data from our world. People present themselves online in a different way to how they actually are (e.g. instagram vs reality).

Is it somehow better if you're aggregating a group vs targetting individuals? We got into this in a previous discussion [“Participant” Perceptions of Twitter Research Ethics (25th Aug 21)](https://dataethicsclub.com/write_ups/2021/25-08-21_writeup.html). It could be used to not market to a particular group (bad) or try to be more accessible to a particular group (good). 

In general we felt that such systems opens a whole can of worms and was basically tech based [phrenology](https://en.wikipedia.org/wiki/Phrenology) - a pseudoscience which involves the measurement of bumps on the skull to predict mental traits.

## What responsibility do government and/or technological platforms have when constructing such computerised systems?

All of the responsibility. The government need to do better. Some countries have systems where [self identity is the default](https://en.wikipedia.org/wiki/Gender_self-identification). The government has a responsibility to treat all citizens equally...right? This should follow on for tech companies too, in theory.

There appears to be an issue with diffusion of responsibility. If you're making a system, many of us feel you should be responsible for every step of the way in how its used. It's sad how a business case often needs to be made for a company to perform ethically. See our previous talk on [Economies of Virtue: The Circulation of ‘Ethics’ in Big Tech](https://dataethicsclub.com/write_ups/2022/04-05-22_writeup.html).

From the perspective of government/healthcare, some trans people are getting health invites for things that are not relevant to them. For medical reasons, the types of data gathered might need to be different. This even applies to cis people as their personal circumstances change with regards to their health.

An imperfect and time consuming solution for this would be to have individuals tick a box/answer a question about every possible health condition and treatment they might have to undergo and whether it is relevant to them personally. This creates an apparent dichotomy between categorising and efficiency. We believe that in the era of big data, data scientists should be able to do better.

Should employees in tech firms have to take a hippocratic oath in order to use AI in healthcare? This is a concern of clinicians. Meaningfully categorising any group is a challenge, and a political descision. Political descisions become design decisions and sometimes the designers are not qualified enough to make these decisions without outside input.

## Closing thoughts

Many of us reading this didn't realise there were difficulties with people confirming their gender as far back as the 1950s. We didn't like how the paper described transwoman as "glamourous" and a transman as "stoic" - is this reinforcing the gender binary or pointing out how trans people felt that they had to conform to stereotypes? 

What data do we need to know and what don't we need to know: by not collecting data about people some categories, you don't cater to them. By leaving people out, will we miss finding important things about them? Drugs for cystic fibrosis can't be tested on pregnant people, but it could also harm the unborn child to come off the medication. This affected people's attitudes to taking the covid vaccine when pregnant. 

In the ONS Census last year children under age 16 could not have the option of answering the question related to identifying the same as at birth. This question had been tested by ONS but was deemed publicly acceptable for this age group. How does this affect trans teenagers and how they feel about their gender/sexuality?

This has the implicit implication that it's not worth thinking about your gender identity until you're at least 16. One of our members summed up their thoughts on this with the line: 

"The unexamined cis-life is not worth living."

---

## Attendees

__Name, Role, Affiliation, Where to find you, Emoji to describe your day__
- Natalie Zelenka, Data Scientist, University of Bristol, [NatalieZelenka](https://github.com/NatalieZelenka/), [@NatZelenka](https://twitter.com/NatZelenka) 
- Nina Di Cara, Research Associate, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Euan Bennet, Lecturer, University of Glasgow, [@DrEuanBennet](https://twitter.com/DrEuanBennet)
- Laura, Software engineer working in data collection
- Lucy Bowles, Junior Data Scientist @ Brandwatch
- Roman Shkunov, about to start (!) as a Graduate Data Scientist @ Lloyds Banking Group
- Zoë Turner, Data Scientist, Nottinghamshire Healthcare NHS Foundation Trust [@Letxuga007](https://twitter.com/Letxuga007)
- Marissa Ellis, Founder www.diversily.com, https://twitter.com/diversily
- [Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/), Citizen Developer, Australian Public Service, Brisbane

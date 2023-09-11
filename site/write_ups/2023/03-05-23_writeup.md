# Data Ethics Club: [Queer In AI: A Case Study in Community-Led Participatory AI](https://arxiv.org/pdf/2303.16972.pdf)

<!--

```{admonition} What's this? 
This is summary of Wednesday 05th May’s Data Ethics Club discussion, where we spoke and wrote about the article [Queer in AI: A Case Study in Community-Led Participatory AI](https://arxiv.org/pdf/2303.16972.pdf) by the organisers of Queer in AI.
The summary was written by Jessica Woodgate, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Huw Day, Nina Di Cara and Natalie Thurlby helped with the final edit.
```

-->

## Do you have any examples/experiences of data collection or use that may have contributed to the marginalisation of queer people. If you were involved, could you have done something differently, and what were the barriers to this?

### Data collection and the categorisation of gender

For many of us, there was absolutely no doubt that data collection we may have participated in contributed to the marginalisation of queer people. Whenever gender has been involved in the data, then this was probably an issue. However, the question of queer marginalisation was rarely, if ever, brought up. There should be clear procedures in place so that events concerning gender fluidity in data collection, such as a mismatch of suffix and gender identity, can be handled easily and sensitively. When similar issues have been previously raised in our workplaces, there has been no response.

An example of this is in younger persons’ services, where data models are rigid with only a binary categorisation of gender. This fails to account for gender fluidity; name choices can change, as well as pronouns and suffixes. Identifiers can change over different timescales, for example just once, or on a daily basis. It can be extremely emotionally challenging for individuals when organisations insist on keeping previous identifiers. A deliberate change in identity can in fact be important and useful data, but in some systems is treated as an error.

Storing data about gender identity in such a rigid and fixed way does not fit the information it is attempting to capture. Identities can change, as well as the meanings of the categories we attempt to use to define them. We don’t seem to be aggregating and counting properly. Yet, when attempts are made to better define categories there is an often raised complaint that the data is too small, or put into too small buckets. How do we represent people in small samples? Why are we collecting data when the numbers are deemed too small to run statistical analysis? Perhaps gender should not only be thought as discrete data types, but on some continuous metric, reframing the structure of the data. The philosophical sands of categories are always shifting! 

Issues with categorising gender need to be raised repeatedly. It reflects deeper problems with bureaucracy and data collection, as categories have existed long before the advent of computers. Thus, the marginalisation of queer people has been going on as long as there has been data collection. It is almost an inherent fact of data collection that edges are ‘rounded off’, which almost always results in missing complexity. It is a fundamental problem, which you can read more about in the book [Sorting Things Out](https://mitpress.mit.edu/9780262522953/sorting-things-out/). 
Barriers around data collection exist, such as expense and participant unwillingness, which impact the ability to have more extensive information about identity. There are practical issues with dataset size, and ethical problems such as anonymisation. In addition, creating labels can provide structure for a community to form around, however labels can also become a means for gate-keeping.

### Safety and anonymity

When we come across mismatched identifiers, e.g. suffix and pronoun, we should consider our approach with care. There is often an assumption that this is a data quality issue, however it carries a risk of inadvertently outing someone, or highlighting information that people aren’t ready to have shared. Privacy implications carry over to issues with ‘overcategorising’, which runs the risk of data being too identifying. It is important to retain a degree of anonymity.

We should think about the effects of context on safety and anonymity. Circumstance may alter how someone identifies themselves, and some circumstances may be safer than others. This impacts how we go about collecting and using data. For example, the importance of context is highlighted in the problem of violence against trans people in prison, and not recording individuals as trans until there is some incident. We need to think about when peoples’ identities should be entered into a system, and why. 

In addition, we should think about the kinds of questions we are asking, and how to make sure people feel safe in answering. The way you ask a question really matters. Systemic oppression can impact mental health; the very act of sharing data can be problematic. When multiple choice answers are presented, people are positioned in relation to others. What is the context you are asking the questions in, and what questions are relevant or appropriate?

### What kinds of data should we be collecting?

We wondered why HR (or another data collecting entity) needs to know your gender at all? We argued that our data is valuable, and we need to be given good reasons to share it. One instance of problematic data collection is censuses, which often have limited options for identity; the UK census had unclear guidance for how trans people should answer questions. Just because a model has used information from a census, doesn’t mean it’s perfect. However, people tend to adopt questions from the census, and it is often used as a model for other surveys. For example, the NHS uses wording from the census. When working in digital health in the NHS, the options we saw were either male or female. Is this sufficient for a medical context? Is that the only threshold we should consider?

Perhaps information on people’s biological sex is not fundamental, and often we can default to using gender instead. Language choices can be neutral, and a medical history podcast - [Sawbones](https://maximumfun.org/podcasts/sawbones/) – refers to ‘people who have a uterus’ and ‘people who do not’. People may self-identify differently to how others might expect them to, and we haven’t really established the basics of the language we should use.

An interesting example of how our language insufficiently captures the nuances of gender identity is how robots and bots are being gendered. From some of our work in automation, robot user accounts in the payroll system were given MX titles. However, the bots were given binary titles. Pronouns may affect how we perceive robots!

Applications of AI by the government (e.g. immigration, benefit allocation) use historical data which can keep the system stagnant and subject to feedback loops based on the past. We need to address the fact that as our data collection changes, the data will also change. If identities are rooted in the freedom of being, screw the census. However, does this mean policy makers will struggle to be data driven?

There was a lot of discussion around [the New Zealand 2023 census](https://www.census.govt.nz/about-the-census/). Australia and the UK asked questions in their census about sex/sexual identity in 2021, followed by New Zealand introducing gender diverse questions in 2023. ‘Australia has a crack of it and then inevitably New Zealand does it better’. Is there a [Data Hazard](https://datahazards.com/index.html) here? You aren’t given a lot of information about how the data will be used; anytime there’s a marginalised group, there’s a dichotomy between collecting data to make better decisions for them, but also a risk that the very same data will be used against them.

### What can we do?

Advocacy is needed to bang the drum loudly and keep drumming. We need to niggle away until such issues become a normal consideration. There is too much hesitation around rocking the boat, but the way things have been operating hasn’t been working. Perhaps we can influence how data is gathered if we’re a bit ‘downstream’ and have more involvement between data collection and analysis areas. On the analysis side, we can point out holes in the data such as the difference between sex and gender. We can also use [The Inclusive Innovation Playbook](https://diversily.thinkific.com/courses/the-inclusive-innovation-playbook), developed to help inform more people about how to intentionally embed diversity and inclusion considerations when creating digital products and services.

## Decentralised organising is core to the Queer in AI approach. Is this a style of organising you are familiar with? If you are inclined to think it is a useful/not useful approach, why is that?

### Examples of decentralised organising

Some examples were given of different forms of decentralised organising. We spoke about experiences of decentralised organising through the [NHS-R community](https://nhsrcommunity.com/), which is distinctly different to the usual NHS/social care hierarchical management and leadership. They have a code of conduct which may hold behaviour to a higher standard than organisational procedures. The example of [Web3](https://web3.com/) was given, which is a decentralised autonomous organisation run on blockchain through the use of smart contracts. However, bad actors still appear. There is also the [w3c organisation](https://www.w3.org/), which is famous for being quite decentralised. Interest groups develop standards such as these, and in some ways they are more democratic. [Mastodon](https://joinmastodon.org/) is an example of decentralised social media, however people just copied and pasted the general guidelines, which wasn’t effective. Guidelines should be authentic and meaningful.

We also talked about organisations which are typically very hierarchical, however allow for responsibility in certain areas such as the military. One example of this is retired US Navy Captain [David Marquet](https://www.youtube.com/watch?v=psAXMqxwol8), who redistributed responsibility amongst his crew so that he held control only over critical decisions, e.g. those that could involve someone dying.

Another type of organisational structure is ‘flat hierarchies’, which has few or no levels of middle management between staff and executives. Flat hierarchies are seen in [Extinction Rebellion](https://rebellion.global/), and the [Swedish Pirate Party](https://en.wikipedia.org/wiki/Pirate_Party_%28Sweden%29). They seem to have developed more democratic ways of making decisions, and – whether you love them or hate them – have been quite effective. However, some of us found it hard to claim that a hierarchy is flat.

### What are the benefits of decentralised organisation?

We understood that decentralised organisation is what allows Queer in AI to eb, flow, and adapt. In terms of getting new initiatives off the ground, this could be very productive. Team empowerment and moving towards agile working changes the structure and requires a level of trust to empower everybody to make decisions. Some of us were optimistic; when people really care, there is a lot of power in teaming up in different ways. In the context of Queer in AI, the contributions that people can bring through lived experience are hugely valuable. This could be fostered through decentralised organisations, rather than the traditional routes of organisational structure, in which those voices often get lost.

### The tyranny of structurelessness

A pitfall of decentralised organisations is that they can fall into the trap of the tyranny of structurelessness, which [we have discussed before](https://dataethicsclub.com/write_ups/2022/23-03-22_writeup.html) at Data Ethics Club. Some of us thought that maybe a power structure would just emerge; even amongst your own friendship group, this often happens. They found it hard to even get 7 friends to go to the movies at the same time, let alone coordinate a whole organisation…

There can be disagreement within the queer community, for example the [pride parade in Canada coming up against BLM protests due to the inclusion of the police]( https://www.cbc.ca/news/canada/toronto/pride-parade-toronto-1.3662823). Decentralisation can allow for more disagreement – but maybe this disagreement can be better or healthier in some ways? There should be protocols in place, and facilitators to ensure everyone is heard. The paper gave the example of Queer in AI’s use of Slack, where some people are louder, and write more. This aligns with coaches used in agile development, who smooth paths and help teams with any impediment. Facilitators need to acknowledge that people contribute in different ways, and we should notice when they are quiet. In traditional structures, very few organisations have product inclusion managers, but they will have product managers. A lot can be told from the evolution of job titles.

## What would it look like to prioritise intersectionality in our personal work contexts - what types of initiatives might we see?

Our systems don’t support the richness of data on people in regard to intersectionality. With the way things are inputted, communication and sharing resources aren’t easily understood from what we currently collect in data. There is a lot that can’t be evidenced. For example, in social services, preferred language is often asked, but not dialect or requirement for a translator. This needs to be considered and built into systems, which might actually be a [Data Hazard](https://datahazards.com/index.html): ‘lacks community involvement’. What you learn from one community can inform how you conduct research. See [Queer Data: Using Gender, Sex and Sexuality Data for Action](https://www.bloomsbury.com/uk/queer-data-9781350230729/) by Kevin Guyan for more information.

If systems were better equipped for intersectionality, people would get more personalised support for their unique situation. In the translation example, if people don’t understand, how can they report that back to us? We need to make sure we are hearing people’s difficulties. Context comes into consideration again; different contexts may involve different intersections.

Including better diversity and intersectionality in academic staff/data collectors can help, as it affects what people think to record in their data. Can this be used to make academia/education in general more attractive?

We would have liked the paper to talk more specifically about intersectionality and how it relates to queerness.

## Attendees
__Name, Role, Affiliation, Where to find you, Emoji to describe your day__
- Natalie Zelenka, Data Scientist, University of Bristol, [NatalieZelenka](https://github.com/NatalieZelenka/), [@NatZelenka](https://twitter.com/NatZelenka) 
- Nina Di Cara, Research Associate, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Vanessa Hanschke, PhD, University of Bristol
- Paul Matthews, Lecturer, UWE Bristol [@paulusm@scholar.social](https://scholar.social/@paulusm)
- Jessica Woodgate, PhD, University of Bristol
- Amy Joint, Commissioning Manager, F1000, [@AmyJointSci] (https://twitter.com/AmyJointSci) 
- Noshin Mohamed, Quality Assurance in children's services
- Marissa Ellis, Founder of Diversily 
- Zoë Turner, Senior Data Scientist, Midland and Lancashire Commissioning Support Unit, [https://github.com/Lextuga007]
- [Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/), Citizen Developer, Australian Public Service, Brisbane

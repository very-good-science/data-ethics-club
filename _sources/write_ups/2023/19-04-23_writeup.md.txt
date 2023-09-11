# Data Ethics Club: [Social Biases in NLP Models as Barriers for Persons with Disabilities](https://arxiv.org/pdf/2005.00813.pdf)

```{admonition} What's this? 
This is summary of Wednesday 19th April's Data Ethics Club discussion, where we spoke and wrote about [Social Biases in NLP Models as Barriers for Persons with Disabilities](https://arxiv.org/pdf/2005.00813.pdf), a paper written by Ben Hutchinson, Vinodkumar Prabhakaran, Emily Denton, Kellie Webster, Yu Zhong, Stephen Denuyl.
The summary was written by Huw Day and Jessica Woodgate, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with the final edit.
```

## Discussion

### Opening thoughts

A lot of us did not enjoy this paper and were skeptical about aspects of it, particuarly those on sentiment analysis. We did however enjoy the discussion after the fact. 

We wondered how do you define disability? How do you define conversations around different physical disabilities? Who makes these 

The databases that the model in the paper is trained on are guidelines published by three US-based organizations: [Anti-Defamation League](https://www.adl.org/), [SIGACCESS](https://www.sigaccess.org/welcome-to-sigaccess/resources/) and the [ADA National Network](https://adata.org/).

How up to date are these guidelines? What bias is encoded there? What's the half life of this kind of dataset? Would you need to update this every couple of years as language evolves?

We also didn't like that there were no mention of mitigation methods.

In a meeting on the famous [Stochastic parrots paper](https://dl.acm.org/doi/10.1145/3442188.3445922), a worker from Kenya talked about their experience assisting training for [ChatGPT](https://dataethicsclub.com/write_ups/2023/07-02-23_writeup.html). Workers aimed to make ChatGPT  less toxic by getting moderators to score sentences on toxicity - the rationale was that if ChatGPT gets an insight into what constitutes as toxic, it can aim to produce less content of that nature. Low wages and the workers being exposed to a lot of troubling content means this could end up being a not very data ethicsy way of doing data ethics.

### What are the consequences of “innocuous sentences discussing disability being supressed” in online moderation contexts?

#### Context and Nuance

Marginalised communities may choose to 'reclaim' certain langugage - automatic moderation may prevent them from doing so. There could be discourse in groups where words are reclaimed (e.g. the word ["queer"](https://en.wikipedia.org/wiki/Queer) has had derogatory connotations in colloquial use but has been reclaimed as neutral/positive identifier). It doesn't feel right to say you can't use that.

Making places safe is very important, but if we try to automate it we solidify it. There is a removal of flexiblity in human judgement as at its base it's a rule following system.

Communication broadens and complicates based on context. Who do we speak to? Children, adults, classes? How does the machine make a judgement? There a lot of human factors to consider.

We are opting out in the path of least resistance because there is so much content to moderate. Who gets to decide? It's always going to be the people with the power not the people who are harmed.

There is some debate on person centered language versus other language. "Deaf person" versus "person who is deaf". This is not necessarily agreed within communities. Wider group discussions have been used for "patients", "service users", "clients". We may not be aware of the intention, maybe trying to do the right thing but not necessarily examine those intentions and motivations.

Language that is seemingly negative, like swearing, may not be perceived by the person as such but could have useful context. It might be typical language for some people in some groups/contexts and can also express heightened emotion.

Ismael was involved in a Genomics England’s Participant Panel who created a [guide on how
to talk about the people whose data
is curated at Genomics England](https://files.genomicsengland.co.uk/documents/Genomics-England-Language-Guide.pdf).

Rachael noted: Language evolves over time - meanings of certain words change with time. How can we ensure that language is not out of date?
This reflects the importance of having diverse teams. Diversity could mean a lot of different things - it might also mean knowledge of internet sub-cultures and what is or is not offensive. This isn't always obvious. Paul's student did work investigating online communities for disabled artists. They called themselves "crips". Who says the word and in what context is really important to evaluating if its usage is appropriate.

#### Accessibility Issues for Marginalised Groups

Already marginalised people could be prevented from commenting/tweeting/making videos. People will get around some of these checks to some extent with workarounds, e.g. unalive, le$$bean. How fast can sentiment analysis adapt? Is it faster than human moderators?

Is there an access issue? The time you need to make an input in any system can be more precious for disabled people. Disabled people are already at a disadvantage on these systems such as Twitter/Reddit/TikTok. Disabled people are less likely to report things as toxic because of this time pressure. People have a limited number of ["spoons" or "spell slots"](www.medium.com/collected-blog-posts-of-a-bipolar-author/spell-slots-and-spoon-theory-f9481abaacd6). 

Getting feedback is difficult here by virtue of it being extra effort for those affected to self advocated For example in the case of "long covid" (3 months or longer). After 12 months, x% of people are recovered - or have they just stopped engaging with healthcare? 

Deborah Lupton examines ‘the digital patient experience economy’ in [The Commodification of Patient Opinion](www.onlinelibrary.wiley.com/doi/full/10.1111/1467-9566.12109) which is relevant to this discussion.

The concept of sexual harrassment in the workplace is an example of [hermeneutic injustice](https://en.wikipedia.org/wiki/Epistemic_injustice) when someone's experiences are not well understood — by themselves or by others. It can also be that you've internalised mistreatment so you can't see it. Hermeneutics is the science of interpretation. A good book on this topic is: :sparkles: [Epistemic Injustice by Miranda Fricker](https://academic.oup.com/book/32817)

Silencing already marginalised voices by stopping people having a space to talk to speak to each other and stopping other people from hearing from them. It reinforces the medical model of disability versus the social model, creating a feedback loop.

Capitalism devalues disabled people because they are often less able to make money. If only there was something we could do about that...

#### NLPs vs Human Moderators

What would be the ideal content moderation? At what stage do we have human input? Volunteer moderators vs paid moderators aided by automation.

When do we decide to use NLP versus a person? In which situations is it actually better to use a person? This becomes a conversation on who is allowed to say what and when. At the very least, the paper shows that this type of bias is likely to come up when training NLP models. It is very difficult to see how this could be managed well without humans. A good example is moderators on sub-reddits who decide on a set of rules about what is okay versus what is not okay. 

Explainability does come into this too - how do we know what is being moderated and make this explicit. It's important for there to be accountability. Systems become more and more complex, but this shouldn't be confused with more sophistication. It makes it harder to explain what is or is not allowed. 

Usage in a live context might be more useful rather than outsourcing decision making in different contexts? You end up with a language model that has learnt some kind of weird combination of rules that don't actually apply globally and apply to lots of different contexts/rules.

### What are the consequences of these findings given the growing use of LLMs?

Not a question of safe/unsafe, just the scale is too great to moderate. People are using ChatGPT for everyday tasks. Should they be?

As we've already noted, language generally is full of values that change over time and not everyone agrees, so can we rely upon machines to resolve that for us?

One of us recalled an example of GPT 3.5 identifying women as nurse and men as doctor even when it doesn't make grammatical sense. 

People don't know that these are problems that exist with LLMs. When you point them out, they're obvious, but at the initial outset of LLMs, this is not something that comes up very often and that is a worry. Because it is proliferating so much, no one can be on top of what people are doing. [Does “AI” stand for augmenting inequality in the era of covid-19 healthcare](https://www.bmj.com/content/372/bmj.n304)

ChatGPT is retrainable so they're using feedback from people to retrain the model but is this enough? There could be an arms race of people trying to train it to be toxic and another trying to train it to be wholesome. 

The understanding that people have of these types of models, but in school we don't really learn about data science just ICT or Maths. Maybe the next generation are going to be better equipped for this. There are people well past school, how do we educate them about this? Do they want to be educated on it? On ChatGPT, Ismael has made a [use policy for organisations/companies](https://github.com/KairoiAI/Resources/blob/main/Template-ChatGPT-policy.md) to make sure their staff use it safely. 

This is an existing problem with misinformation on the internet - for example everyone always believes Wikipedia without checking. ChatGPT doesn't make it very obvious that it could be 'lying'. There is a small warning that isn't always presented. There should be more documentation for the users about the bias in the tool. This is legal in some countries, but not in others. E.g. Italy banned it. 

How can we show people things might be wrong, in a way that companies (for profit) are willing to acknowledge publicly. (Bad for shareholders!)

### What change would you like to see on the basis of this piece? Who has the power to make that change?

Do we have to accept that these are fundamentally unsafe? It feels like an inevitable consequence that this is even more unacceptable.

Should we use people for moderation? If words are deemed inappropriate, should the user be able to use it if they claim the moderation (human or otherwise) is biased? Consult the groups that are most affected!

[“We are not mistakes on pages, we are awesome novels with unorthodox beginnings.”](https://www.tactcare.org.uk/content/uploads/2019/03/TACT-Language-that-cares-2019_online.pdf) 

Sentiment analysis often is not very accurate (such as the word "tory" being very toxic, but racial slurs not being in an analysis of abuse against MPs). A lot of language is very contextual, so it's not even feasible to agree if something is "toxic" or not.

The comparison between "I am a person" and "I am a deaf person" is a bit unfair since people have different preference for person-first or not language. Language is very malleable which makes moderation more difficult: e.g. use of "unalive" on platforms such as tiktok in order to circumvent moderation.

We wondered how good or bad does something need to be to be used practically? How do you decide: how good is good enough? It would be nice to moderate out toxicity automatically, but it's quite unlikely it'll work perfectly. What would be good enough for these kinds of models to be used in moderating settings?

---

## Attendees

__Name, Role, Affiliation, Where to find you, Emoji to describe your day__
- Natalie Zelenka, Data Scientist, University of Bristol, [NatalieZelenka](https://github.com/NatalieZelenka/), [@NatZelenka](https://twitter.com/NatZelenka) 
- Nina Di Cara, Research Associate, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, (Tired) PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Euan Bennet, Lecturer, University of Glasgow, [@DrEuanBennet](https://twitter.com/DrEuanBennet)
- Noshin Mohamed - Practice Learning Reviewer in QA for children'
- Ismael Kherroubi Garcia, AI Ethics & Research Governance consultant, [Kairoi](https://kairoi.uk), [LinkedIn](https://www.linkedin.com/in/ismaelkherroubi/)
- Zoë Turner, Senior Data Scientist, NHS Midlands and Lancashire CSU, [GitHub](https://github.com/Lextuga007)
- Paul Matthews, Lecturer, UWE Bristol [HomePage](https://fetstudy.uwe.ac.uk/~pmatthew/),🦣[@paulusm@scholar.social](https://scholar.social/@paulusm)
- [Rachael Laidlaw](https://www.linkedin.com/in/rachael-laidlaw/), PhD Student in Interactive Artificial Intelligence, University of Bristol

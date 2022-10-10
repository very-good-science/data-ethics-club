# Data Ethics Club: [The Failures of Algorithmic Fairness](https://senseoffairness.blog/2020/12/17/the-failures-of-algorithmic-fairness/))
<!--Please don't edit the info panel below-->

```{admonition} What's this? 
This is summary of Wednesday 5th October's Data Ethics Club discussion, where we spoke and wrote about the [The Failures of Algorithmic Fairness](https://senseoffairness.blog/2020/12/17/the-failures-of-algorithmic-fairness/), a blog post by Paul Lee.
The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with the final edit.
```

## Discussion

```{image} images/AlgoFair.png
:width: 200px
:align: center
:alt: Gru meme. First panel reads: "Recruiters make an algorithm to rank applicants for particular jobs". Second panel reads: "Applicants work out which proxies to optimise for". Third and fourth panel read: "Algorithm eventually ranks all candidates the same", this makes Gru sad. Meme made by Huw Day.
```

### Are impacts of fairnesses always fair? 

Some of our reactions to this piece were "we agree, and now what?" We keep reading these sorts of articles looking for an answer but still no one has solved algorithmic unfairness. Similar question to what we've looked at before: why are we doing all this work to gather more and more information, will it actually solve anything? Human-created problems need human-created solutions.

The article seems to shy away from making any strong statements. Using proxies in a black box way, even with protected variables say for example with insurances. The unfairness of certain algorithms is the point. The article could've pushed a bit more towards this. The article is very accessible and not aimed at subject matter experts, but occassionally generalises a bit too much: e.g. failing to make a distinction between an AI model and a hand written algorithm, for example. It feels like there is a bit of a push for people to comment on AI and unfairness in this area. 

We spotted an error where the picture shown for the cameras is about false negatives not false positives. The probability of getting away with the crime. 

There were divided opinions on the subject of the A-level results algorithm. Many of us felt that if you get some kind of automated system to assign A-level grades without proper input from humans then on day one, would it just give everyone their grades at birth based on postcode? Adding algorithms into unfair systems just encodes the unfairness while pretending it's objective.

If you are improving over years, that was accounted for predicted and taken into account or if you got better results in GCSE results. Exam results are always biased by class and that wasn't increased by the algorithm. Some argued that there are a fixed number of places at universities and that A-level grades are essentially used to assign these places. We had a brief aside to question: are these grades good at predicting people's success in universities? Are the critiques just with how exams assess us at all? If you automate a flawed system, it will remain flawed and become systematically so. Perhaps more efforts should be made to understand *why* and *how* this particular system was flawed to give arguments (whether they be for or against) more weight.

### What do you think we lose or gain from trying to make our lives more and more efficient?

More and more of this "clean your room in the spirit of efficiency" ethos is getting dull. It tries to measure our lives as almost economical. If we optimise everything, do we just become really lazy? It feels like the wrong question to ask sometimes. Whether or not we seek to optimise something is irrelevant but it is going to happen because of competitiveness.

How often is increased "efficiency" used as a way to try and squeeze more work from people rather than making their life better? Is optimising good or bad? Is it certain? If efficiency means automating tasks that takes time, then is there a risk of losing expert knowledge? Will this become a problem if we put too much trust in automated processes? Do algorithms just make it clear that we are already really unfair? Is algorithmic fairness different from justice of outcomes?

Under capitalism, people *should* get back what you put in. But this is completely at odds with everyone getting to survive. Society is preserved in some ways by inefficiencies - e.g. public services are often privatised in search of "efficiency" (this is a often a lie in order to sell the idea that a few rich people should profit from public services while everyone else gets worse service). Inefficiency at least gives us time to think.

In the discussion about fairness in society being elusive, we have to recognise that there would never be a time when we get to say "we did it folks, the world is now fair". Working for incremental improvements is always going to be the aim of the game. As Viv put it: "we need to accept that we'll always be at sea - we're never going to land". 

### What different ways could we measure ‘fairness’?

Here are [21 definitions of fairness](https://fairmlbook.org/tutorial2.html) according to one perspective, which includes technical definitions of fairness after data collection but before application. There are some other examples of some benchmarks like the
[80% rule](https://en.wikipedia.org/wiki/Disparate_impact#The_80%_rule), although they frequently run into 

Before you can measure fairness you have to decide on your definition of fairness. You can very easily end up with conflicting intuitive definitions of fairness for a given problem. Is fairness bringing everyone to the same point or giving everyone the same amount of help? Is it more about equality or equity.

Do we have to consider lots of different ways of considering fairness? Fairness is context-specific. No point in looking for "one weird trick" to "fix" fairness. Conceptually sometimes we think about "sources of bias" rather than thinking positively about how to make processes/algorithms fair (having something to aim for). You either have to be quite rigid or quite subjective.

We are so far away from "fairness" in the current system that it's actually hard to quantify a good outcome. Perhaps we need to measure "unfairness", not "fairness". Measuring things give a route to people arguing "things are fine because the measured thing isn't changing".

Are there benchmarks for these sort of systems? Yes but part of the problem with set benchmarks is people then optimise towards those. Automated hiring practises mean candidates have optimising for certain keywords. Once candidates know all the keywords they're all evaluated as the same. If you can only measure something with proxy variables, then you can only optimise for these proxy varibles.

We can't let the perfect be the enemy of the good, work towards incremental change. Increased efficiency loses the connection to the messiness of how unfairness can be challenged - the unfairness gets abstracted.

We would like to see training in how to evaluate ethics and fairness be a much bigger part of computer science and maths training rather than being treated as an afterthought. When models are being developed that are going to affect people then the people being affected need to be involved, and so do experts in understanding issues of bias and algorithmic fairnes.

### Is there an acceptable level of fairness we could require before releasing new technologies? How would this work in practice?

It's in the financial interest of companies to appear to be fair, and sometimes even to be fair (i.e. you will get worse staff if you force out good staff who have *protected characteristic*). After some floods in Australia, [some insurance companies didn't pay out](https://www.theguardian.com/australia-news/2022/mar/10/insurance-fine-print-may-mean-thousands-of-flood-victims-are-unable-to-claim-report-says) because they could get away with it legally. Others insurance companies did pay out, but consumers then left theunethical insurance and those who acted ethically (as well as legally) won more customers.

In medicine, an adverse reaction to medication can be reported with a "yellow slip" - goes back to manufacturers and is logged by public health. There is a process to give feedback. This ends up being how side effects get listed on medication and is an essential informed consent. Could we do something similar for algorithms? This would of course need to account for spurious reporting (e.g. people yellow-slipping that vaccines made their child autistic). Tech companies lobby that their algorithms shouldn't be regulated because "it's too complicated for you to understand" but that should mean the onus should be on them to make it understandable and to justify that it's safe to use!

We feel regulation needs to force tech companies to make it make sense and include the community in the process, allowing for a continual feedback loop. Who has responsibility for fairness? Should there be legal frameworks in place? How much of the fairness economy in the big tech world is trying to buy legitimacy? It's possible to create the illusion of legitimacy without fairness. When it comes to large companies or government bodies, you start off with quite a strict definition of something because you have to write it down, but then when it is actively applied it becomes more nebulous in terms of a person.

--- 

## Attendees

__Name, Role, Affiliation, Where to find you, Emoji to describe your day__
- Natalie Zelenka, Data Scientist, University of Bristol, [NatalieZelenka](https://github.com/NatalieZelenka/), [@NatZelenka](https://twitter.com/NatZelenka) 
- Nina Di Cara, Research Associate, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Euan Bennet, Lecturer, University of Glasgow, [@DrEuanBennet](https://twitter.com/DrEuanBennet)
- Ismael Kherroubi Garcia, self-unemployed, Kairoi (website underway), [@hermeneuticist](https://twitter.com/hermeneuticist), :sleepy:
- Viv Kuh, Lecturer, University of Bristol, no useful web links for me :)
- Darcy Murphy, PhD student, University of Manchester
- Kamilla ['Milli'](https://www.linkedin.com/in/kamilla-wells/) Wells, Citizen Developer, Australia
- Ola Michalec - Researcher, University of Bristol
- Sion Bayliss - Research Fellow, University of Bristol [@SionBayliss](https://github.com/SionBayliss/)
- Liam James-Fagg - Data & Insights Manager at allpay ltd
- Helen Sheehan - PhD student, University of Bristol
- Charlie Newey - Machine Learning Engineer

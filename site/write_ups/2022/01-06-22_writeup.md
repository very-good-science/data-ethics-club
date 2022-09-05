# Data Ethics Club: [Participatory Data Stewardship](https://www.adalovelaceinstitute.org/wp-content/uploads/2021/11/ADA_Participatory-Data-Stewardship.pdf)
<!--Please don't edit the info panel below-->

```{admonition} What's this? 
This is summary of Wednesday 1st June's Data Ethics Club discussion, where we spoke [Participatory Data Stewardship](https://www.adalovelaceinstitute.org/wp-content/uploads/2021/11/ADA_Participatory-Data-Stewardship.pdf), a report from the Ada Lovelace Institute. 
The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with the final edit.
```

## Introduction

```{image} ../../images/ButIfYouDid.png
:width: 300px
:align: center
:alt: American Chopper Argument Meme. "Consent to my super cool study using your data" "But I don't understand your study" "But if you did, you'd love it and think it was super ethical." "But I don't understand it!" "But if you did..." Meme made by Huw Day.
```

We read [Participatory Data Stewardship](https://www.adalovelaceinstitute.org/wp-content/uploads/2021/11/ADA_Participatory-Data-Stewardship.pdf), a report from the Ada Lovelace Institute. The report is fairly long, and so we recommended if attendees were very short on time to just look at the helpful overview image on Page 14 and table on Pages 17-18. People who had a bit more time then had a look over the descriptions of each type and case studies on Pages 19-47.

The framework for participation in data stewardship includes 5 key layers. The following descriptions are taken directly from Figure 3 of the paper (page 14).
Inform: We will keep you informed about how your data is being governed
Consult: We will listen to acknowledge and provide feedback on concerns and aspirations for the governanance of your data
Involve: We will work with you to ensure your concerns and aspirations are directly reflected in data governance.
Collaborate: We will look to you for advice and innovation in design of data-governance models, and incorporate your advice and recommendations where possible.
Empower: We will advise and assist in line with your decisions about your own data-governance models.

The frameworks are presented in a sort of implicit hierarchy, the nature of which we discussed. We also talked about how to decide on what level of participation to implement, the optimal amount of participation (in theory and in practice) and the barriers to the implementation of participatory frameworks.

## What factors should guide decisions about what level of participation best suits a project? Does this happen in practice?

The five frameworks seem high-level and there wasn't much advice on practical application, which might be difficult. We liked that there was a critique included though. Factors that should influence level of participation will vary widely from project to project.

We wondered why might we feel inclined to think "empower" is the "best" framework? In theory we would like to think that the most participation is always the best, but there's a question about feasibility: how feasible is it to "empower" the relevant communities?

What about *limiting* participation? There might be circumstances where you don't want too much public access/input (e.g. clinical trial participants).

The people who have capacity to involve themselves more may not be too representative (possibly missing out on less privileged voices). Is it possible that including participatory practice might be seen as just another layer of red tape? ... has GDPR regulated 'inform' now?

There is a need for teams to be diverse and, therefore, open to empowering different voices from the outset.

Some think you shouldn't collect data without consulting those affected by it. But given that this usually requires time and financial investment, how often does it actually happen in practice?

From our own experiences, in the subfield of social media, data collection is not very ethical at all. The NHS, on the other hand does a really good job of protecting people's data (PPI etc).

## Is the most participation always the best?

We were of the opinion that most partcipation is *not* always the best. 

You need to commit to a certain level of maintenance for data to be worked with. If this needs to be run by the participants, this can really bog things down. (This will be evident to anyone who has ever tried to organise a group holiday).

There's a difficulty of presenting it as a hierarchy, implying one is better and one is worse. Often data is collected about specific sub-populations who are being 'studied', and they are often being 'studied' because they may have particular health conditions or life circumstances we are trying to research. However, these life circumstances or health conditions may mean that these population groups may not necessarily appreciate having to put a lot of time in managing their participation and data. On the other hand, it would be a particularly effective measure against the exploitation of under-served communities, many of whom have histories of being exploited for the purpose of research.

We did appreciate that this report seemed to have a section on how to make each action meaningful. That's not often addressed, usually it's just awareness.

When thinking about large data sets for training ML models (e.g. image recognition), how do you handle participation levels/consent? If you have 100k pictures of people trying to guess your hair colour, do you need to sign off on every new study/model or give blanket consent?

Can you give consent for something you didn't know was going to happen? Often large data sets are not curated for a particular purpose so you just have to trust that the people who publish them collate the data in an ethical way. The scale of these datasets makes this pretty much impossible. Caution has already been warned on handling such [large datasets](https://arxiv.org/abs/2110.01963).

Even when you do open source, public research, it'll be difficult sometimes to explain every single project to everyone. Even when you can't get informed consent (be it because people are bad at stats or because your subjects can't consent, like plants), you can still have legal frameworks to ensure the data is ethically used and maintained.

Because humans are sentient, it opens you up to negotiations. With data about plants for example, there is no negotiation with the objects. You make a lot of decisions on their "behalf".

"If you did understand, you'd love it and think it was super ethical I swear." 

"But I don't understand it." 

"But if you did..."

There has been some interesting research on how privacy statements are worded got you more access (even if they were legally equivalent, but with behaivoural nudges). Why would anyone ever do anything bad with this data? E.g. adobe releasing video editing software that enabled deep fakes.

Is it always good to have participation? Maybe it's good to mandate some level of participation, even if it's not the most stringent level. Thinking about people who are underrepresented for example.

## What do you see as being barriers to participatory data stewardship, and how could these realistically be overcome?

This effort can be demanding on researchers, and if the level of participation is high it can be demanding on participants too. Perhaps there should be "centralised" institutional support, creating "pools" of relevant participants to reduce duplication of effort. There is a lack of funding to practically implement this framework.

In general, there is a need for a mindset change. Instead of building technology as quickly as possible, we might want to build it slowly and mindfully. 

Teams handling data could be compared to flowers. They can bloom if they are diverse, should cross-pollinate to ensure they aren't duplicating efforts, and they cannot grow on barren lands or within nerd caves. Budding flowers will naturally include these kinds of participation questions, while in a barren desert data scientists won't have space, or colleague input, to ask these kinds of questions.

---

## Attendees

__Name, Role, Affiliation, Where to find you__
- Natalie Thurlby, Data Scientist, University of Bristol, [NatalieThurlby](https://github.com/NatalieThurlby/), [@StatalieT](https://twitter.com/StatalieT) 
- Nina Di Cara, PhD Student, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara), :thinking_face: 
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Vanessa Hanschke, PhD Student Interactive AI, University of Bristol
- Ismael Kherroubi Garcia, MSc student, LSE, [@hermeneuticist](https://twitter.com/hermeneuticist)
- Chantel Davies, part-time MSc Student, University of Aberdeen, [CDavieSTEM](https://twitter.com/CDavieSTEM)
- Zosia Beckles, Research Information Analyst, University of Bristol
- Robin Dasler, research software product manager, [daslerr](https://github.com/daslerr/)
- [Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/), Citizen Developer, Australian Public Service, Brisbane

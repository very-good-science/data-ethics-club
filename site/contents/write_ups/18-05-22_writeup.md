# Data Ethics Club: [Why data is never raw](https://www.thenewatlantis.com/publications/why-data-is-never-raw)
<!--Please don't edit the info panel below-->

```{admonition} What's this? 
This is summary of Wednesday 18th May's Data Ethics Club discussion, where we discussed the article [“Why Data is Never Raw”](https://www.thenewatlantis.com/publications/why-data-is-never-raw) by Nick Barrowman.

The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with the final edit.

```

## Introduction

```{image} images/RawData.png
:width: 200px
:align: center
:alt: A meme with a man slowly applying clown makeup. "The process of observation is not unbiased." "Any time datapoints are gathered together some decisions are made." "Biases and assumptions are injected at every step." "That doesn't apply to my data though." Meme made by Euan Bennet.
```

This week at Data Ethics Club we discussed the paper the article [“Why Data is Never Raw”](https://www.thenewatlantis.com/publications/why-data-is-never-raw) by Nick Barrowman. 

There is no theory-free observation. Data is engineered, the article challenges the raw/cooked dichotomy. In order to measure resistance, counting requires assumptions about what magnitude means, or what a number means. This article explores the nature of data, as well as the claim that some data is "raw", often used to reinforce a data-driven approach.

In this talk we discussion we considered the nature of data, if data is truly "raw", what analogies can we use for the "raw-ness" or "cooked-ness" of data and how these ideas apply to our own work.

## Can you think of any examples of data that you would consider truly “raw”?
 
It's hard to find an example of raw, non-subjective data. The amount of money in your bank account is in some sense objective but the value of that money itself is subjective. The list of the balance in customer bank accounts at a certain bank - is that subjective? Grades for a degree are "raw" because no one can change them but they are still subjective. 

Lots of variables are often proxies for something else. But the assumptions, decisions and process that go into making any data set into the form that it exists in are not neutral. Any results from any data cannot be "unbiased" or "neutral". All data *can* be raw but not when it is used for an actual purpose. 

What do we mean by "data"? Is the amount of money in a single bank account "data"? Or does it only become data when it is grouped in amongst a number of other people's bank accounts? We never usually use just one point of data - we use groups, so there is always some processing going on. Applying a purpose to the data makes it no longer raw. We have discussed in the past the idea of labelling datasets for their purposes, outlining the potential (and potential limitations) of the data set. 

There is an evolution analogy here. Some data just exists "naturally", but also some we engineer. Data is kind of "out there", but it's up to us what we collect.

## What are the different types of raw-ness in data?

At first glance, all data you first collect is "raw". For example, [John Snow](https://doi.org/10.1016/S0277-9536(99)00345-7) collecting data that uncovered the epidemic, but many others were collecting less useful data too! 
But there is a rather contentious history around this example.

How we collect, what we do, how we interpret matters. "Raw-ness" is very subjective. Do we always have to do something to data to make it useful? What are the intentions with what we're doing? 

Some of us considered this a slightly tortured metaphor. Most data is not raw as such, nor cooked (the expression "cooking the books" springs to mind), but something in the middle like sushi. To tortue the analogy some more, when we work with data we want the full recipe and to know how the dish is prepared. With the food prep metaphor, there is a whole chain going on before we think the process starts, the same with data processing! When we declare data is "raw", we lose the history behind it; provenance gets forgotten. All the collection methods are also relvant. They contextualise data (as priviledged over "raw" data) requires preservation.

Some of us were suspicious of the raw/cooked metaphor, perhaps a comfortable framing for us to begin with. There seems to be "local" raw-ness; data before we've done the work to it and then "global" raw-ness; data we just throw into the model and see what shakes out. Arguably we have two different, distinct concepts under the guise of "raw".

We are certainly not the first to notice tortured metaphors relating to [data](https://osf.io/preprints/socarxiv/2xguw/).

What are the different types of raw-ness? Is it a heirarchy? Is it about how many people are involved in collecting data, and the level of coordination required.

Depending on what the question is, and what you are collecting. Perhaps raw-ness is determined by the number of aggregations you make, or deletions. For example when you go on Twitter, you aren't seeing raw data. Start off raw then as you pre-process it becomes less and less raw. Before even collecting data, declaring our positionality isn't common in quantitative research, but it is in qualitative research.

Researchers like to think we're independent, but in reality you have to write a certain way for a certain journal, or if you're from a certain research group you are expected to fit with a certain research culture. How much are we "cooking" our work?

We don't necersarily need to know everything about how a network was created. But how does that change with different processes? For example, a biologist's processed data about protein-protein interactions would become a mathematicians raw data when investigating properties of that network. Raw-ness/cooked-ness is contextual, even linked with intention. 

There's a lot more space in some data than we realise. How do we define our categories such as sex and gender in our medical datasets? Who gets to do that? How do we divide up and understand colours in different cultures/languages. There is no natural colour division and this differs between cultures and languages. Some classification methods are closer to physics where others are closer to cultural/anthropological.

## How “raw” or “cooked” is the data that you work with?

Large databases of horse racing might appear "raw" as they come to academics, but there were loads of decisions involved in what to collect, how to collect it, and the risk of mistakes/lies in the collection. People can also use the data very differently to produce very different results.

One of our members works in neuroscience, looking at interactions between molecules. Doing calculations with the reactions they observe are still based off of previous studies, including studies on animals. We can become disconnected from the reality of where the data comes from and forget that these numbers came from animals and humans. We think there is such a thing as completely rationalising data but it always comes with a bias (including saying "these are just numbers"). Gathering parameters for models, usually these are based off assumptions and calculations. Someone else might use the same data and parameters and end up with different results based on how they interpret it, leaving reproducability issues.

We divorce the data from the animal or cell that the molecules came from. Also the specific setup to isolate molecules from their normal environment is really complicated! Lots of specific steps of abstraction to introduce long before any "numbers" are collected. Lots of assumptions are inherent in experiments as well as simulations.

Data that has been cleaned is not raw. One of our members, having worked with large data sets about DNS lookups in a large computer network - this is "raw" for the purposes that they were using it for. However, then making a product from that to sell to other people there is inevitably a "cooking" process. There is a differences between networks (when they used it for themselves it was raw data but it was cooked when used by other people). The process of measuring the DNS lookups is a computer contacts a server and a record is made that the request was made. The purpose was to measure successful lookups not attempted lookups.

## What would an ideal process for decision making be in your opinion? How much would it rely on data or politics? How would this vary by the type of decision?

For policymakers making decisions about safety measures in horse racing (for example), it's easier and cheaper to do the lazy analysis than the rigorous academic analysis. It's totally inherent to the decision making process that the more careful analysis will lose out. 

Even within the same organisation, priorities can vary and politics can override the data as policy makers go with the path of least resistance. 

The least we can do is make it clear what assumptions are made when working with the data - to avoid policymakes concluding that the data doesn't matter.

In science we often approach problems by assuming that the data is raw, but it's probably safer to come from the assumption that data is never raw, and then maybe it can be argued that certain cases are raw (in those rare occasions that it is appropriate).

The first people who looked through microscopes at sperm thought a little [fully formed person](https://en.wikipedia.org/wiki/Homunculus#/media/File:Preformation.GIF) would be sitting inside the sperm cell. They believed this from their theoretical background and that's how they interpreted. 

Another example; in the first discovery of pulsars using radio telescopes, people thought these regular radio signals couldn't possibly exist in nature and had to be aliens.

Just as with quantum physics, the observation changes the nature of the observed item, and we need a way to set out how the observation has happened so that we truly understand the data and can perhaps get back to a more raw form. Too often material is just adopted by others without sufficient knowledge of what went before, and there seems a presumption that it is indeed raw when it has all been processed multiple times before. Too often then we find we have triple-cooked chips.

The food prep (food chain - as in from seed to field to plate) analogy/extension is maybe a better way of understanding this. We also need to keep things such as our frameworks in mind to healthiest use our "final" data. 

Alternatively primary/secondary source, as applied in [historical research](https://umb.libguides.com/PrimarySources/secondary). Primary vs. secondary data is perhaps a better framing because we don't make judgements on truth based on that, but it tells us about the data's provenance. The primary source can still get things wrong!

Arguably the raw/cooked metaphor is a good starting point, but can be improved as our understanding deepens. How do we better make decisions? The data/politics distinction is also a flawed distinction, with e.g. sex/gender questions in census data that's gathering data where the decision around how to gather the data is inherently political.

In the Australian census, funnelling of the census based on previous drop down choices, different questions served based on answers to gender questions.

Knowing where/how the data is sourced allows us to understand it better, decouple it from "truth". Even "raw" data dodges the question of primary vs. secondary sourcing. 

## What change would you like to see on the basis of this piece? 

In principle we agreed with some of these ideas, but how do you make this part of bigger cultural change? Like in a large company.

We should try to put the burden of proof on people who claim their data is "raw" - the assumption should be that no data is raw, but in some specific cases it can be successfully argued. This is safer than the converse which is currently the default assumption!

We need a language to understand what underlies the data. We've explored various analogies and metaphors to deconstruct this. But we need to build a conscious consumer base for this, the users of the data have to be part of the answer. They need better questions to ask, better ways to interrogate the partialities that are buried within the data. We also require publishers and researchers to provide greater insight, and not imply the data is raw. Where did the meal come from?

## Closing Thoughts 

The article makes assumptions explicit, which may be a little obvious to people who are into this area of data ethics already. It's still a good checklist of things to do, best practice.

It's valuable to have resources which can introduce these ideas from epistemology in a way that's easier to digest.

Funnel of observations, how do we fit the real world into data? We also aim towards simple metrics, quantifiable improvements over other models/approaches, but is this a great way to understand the world?

Data can be biased, but surely not our data! Should we keep or junk the metaphors?

DISCLAIMER: THIS WRITEUP IS *NOT* RAW DATA.

---

## Attendees

__Name, Role, Affiliation, Where to find you, Emoji to describe your day__
- Natalie Thurlby, Data Scientist, University of Bristol, [NatalieThurlby](https://github.com/NatalieThurlby/), [@StatalieT](https://twitter.com/StatalieT) 
- Nina Di Cara, PhD Student, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Euan Bennet, Senior Research Associate, University of Bristol, [@DrEuanBennet](https://twitter.com/DrEuanBennet) 
- Emma Tonkin, Research Fellow, University of Bristol, [@emmatonkin](https://twitter.com/emmatonkin)
- Brendan Clarke, Digital Learning Lead, NHS Education for Scotland [bclarke-nes](https://github.com/bclarke-nes)
- Lucy Bowles, Junior Data Scientist at Brandwatch
- Melanie Stefan, Computational Neuroscientist, Medical School Berlin, [MelanieIStefan](https://github.com/MelanieIStefan) [@MelanieIStefan](https://twitter.com/MelanieIStefan)
- Susana Roman Garcia, PhD student, University of Edinburgh, susanaromangarcia@gmail.com :revolving_hearts:
- Amy Joint, Publishing Manager, F1000, @amyjointsci
- Vanessa Hanschke, PhD Student Interactive AI, University of Bristol
- Zoë Turner, Data Scientist, Nottinghamshire Healthcare NHS Foundation Trust [Lextuga007](https://github.com/Lextuga007)
- Robin Dasler, Data Software Product Manager, [daslerr](https://github.com/daslerr)
- [Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/), Citizen Developer, Australian Public Service, Brisbane

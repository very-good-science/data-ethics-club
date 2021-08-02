# Data Ethics Club discusses [Critical perspectives on Computer Vision](https://slideslive.com/38923500/critical-perspectives-on-computer-vision)

```{admonition} What's this? 
This is summary of Wednesday 12th May's Data Ethics Club discussion, where we spoke and wrote about the conference talk [Critical perspectives on Computer Vision](https://slideslive.com/38923500/critical-perspectives-on-computer-vision) by Emily Denton.

The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with the final edit.
```

## The View from Nowhere

The idea of the [view from nowhere](https://www.jstor.org/stable/3178066) is to be completely impartial when reporting/drawing conclusions. By 
some it's considered a holy grail in unbiased reporting (be it journalistic or scientific). By others 
it's considered a place that doesn't even exist, a naively idealistic goal that leads to sloppy writing 
filled with a narrator trapped in an argument with themselves, often at the expense of the reader's 
understanding.

Anyone with a technical but largely theoretical background (for example, abstract maths, computer 
science or theoretical physics), might understand the view from nowhere as not only a place that exists, 
but the only logical place from which to argue theoretical results. In the axiomatic approach to proofs 
in abstract maths for example, statements don't come with bias, only true, false or as yet unproven. If 
you've ever scribbled a mathematical proof that 0.9 recurring is the same 1 on the back of a napkin, 
only to have your mathematically complete logic refuted by a bartender, you know what I'm talking about 
here. And if you don't...probably for the best.

The real world however, is a little less black and white. Whilst you can still reach objective truth 
among certain parameters, there's a whole lot of maybes out there. As soon as you deal with anything 
concrete but potentially uncertain, the view from nowhere starts looking like a lost cause. A set of 
points can fit a statistical distribution with a certain level of confidence, but it takes a leap to say 
that this correlation implies causation. 

Meanwhile anthropologists and ethnographers have understood for a long time that you can't have a 
viewpoint-less view and that the very nature of our observations is affected by the lens through which we 
view the world. To reach scientific conclusions, hypotheses must still be made and tested and those 
hypotheses are nothing more but guesses, fueled by our bias. Even in abstract problems with no real 
world consequences, many results are guessed before they are proven. 

## Better accounting for our views

> In the days when Sussman was a novice, Minsky  once came to him as he sat hacking at the PDP 6.
> 
> "What are you doing?", asked Minsky.
>    
> "I am training a randomly wired neural net to play Tic-tac-toe", Sussman replied.
>     
> "Why is the net wired randomly?", asked Minsky.
>     
> "I do not want it to have any preconceptions of how to play", Sussman said. Minsky then shut his eyes.
>     
> "Why do you close your eyes?" Sussman asked his teacher.
>     
> "So that the room will be empty."
> At that moment, Sussman was enlightened.


Machine learning requires a mapped dataset for training, usually with a binary result. There is little 
to no accounting for the grey of the world if the model is built on true/false prediction accuracy. 
Worse, this can encourage us to think of the world in a binary way, and flatten complex concepts down 
into a binary. It could be relevant to think about how to change machine learning inputs/outputs to move 
away from boiling down the world in this way. 

This will require much more detail and thought in our methods: if we're not viewing from nowhere, where is the view from?
Rather than 
seek out neutrality from where we are now, we should use detailed annotations and descriptions in our 
data sets to understand where our bias comes from. 
For example, perhaps in an Italian data 
set, a higher % of men would be described as "bello" (beautiful), as that's more common than describing 
men as beautiful in English.

Documenting our view means publishing who your annotator(s) are, their demographics, what instructions you gave them. Perhaps as the field evolves, further information might be the norm as we ask what is annotating data useful for? What should it be useful for? 

However, a distict problem that is common in data science is that it's rare to use your own data; typically you use what 
other people have collected. Reusing pre-made datasets can smuggle 
in a lot of preconceptions that we aren't explicitly aware of (this especially applies to collecting 
personal data). [Datasheets for Datasets](https://arxiv.org/abs/1803.09010), an approach introduced to computer science by Timnit Gebru, is probably a great place for us to start handing over our data sets with care. But there are many existing datasets that are widely used that we know next to nothing about. 



## Sharing is caring?

While we all agreed that sharing data, and the details that go with it is a good solution, there are also some practical challenges. For instance sometimes data has been managed by a colleague who has left. Sometimes academia incentivises people to keep valuable datasets to themselves. Even so, the focus on reproducibility in the last few years has meant that "trust me, the data says so" is not going to cut it in today's academic culture. 

This does need to 
be balanced delicately though with confidentiality of personal data and ensuring that those who shared their 
data consent to its use. Potentially there is a need for sharing applications of the data back to the 
primary sources. This can be slower and more restrictive in some applications and is limited by the scale of some
data sets. 

Lastly, it's also a good idea to think about the potential consequences of sharing datasets. Data on court verdicts of crimes along with the nature of crimes could allow 
you to explore varying crime/conviction rates - but they could also allow you to attempt to 
"predict" guilty or not guilty verdicts based on a variety of parameters.
We should always be asking each other "what are the potential ramifications of your work?".

When you're so far removed from the problem as a data/computer scientist, it's important to be reminded: 
the data is people. Is the solution to force interdisciplinarity? To make a compelling argument, you 
should certainly have a better understanding of the context and not just the data that compells your 
ideas. Perhaps there needs to be better liability for software and a way of enforcing industry standards (such as 
for doctors and lawyers) on anyone who writes code? 

That being said, with strict regulation comes reduced accessibility. Some of the best coders in the world start learning 
in their bedrooms without taking any certified course. We should find a way to keep the tech sector 
accessible to all but to avoid gatekeeping. In some ways an approach similar to medical treatment might 
be sensible: I don't need a certificate or a qualification to help someone with a nose bleed or a paper 
cut, provided I have the right knowledge, but I certainly shouldn't attempt brain surgery without the 
right training (of which a degree certificate happens to be a byproduct).

## Let's think carefully

In the video Denton discusses [biological essentialism](https://www.oxfordreference.com/view/10.1093/oi/authority.20110803095507973), and the harm that it can do. Its a flaw that many fields fall into, so how could we do better?

One suggestion was that data scientists should think critically about the variable we want data for, and separate that from variables that we assume are related/correlated. For example, asking someone's gender (to ask for potential pregnancy in medical setting), instead of asking are you potentially pregnant. If we use these "pseudo variables" instead, we may end up encoding our own biases and assumptions in the model without realising. Since data scientists are quite likely to be white cis men, it's more than likely that they will display (unwillful or otherwise) ignorance on certain categories.


For all of us as data scientists do this effectively though we'll need to keep challenging our own understanding of socially constructed concepts. For instance, how on earth can we account for race, when racial identity is socially constructed? It also requires us to think carefully about the research problems we are trying to solve: there's a big difference between saying "we should collect this data and then control for it" and "we can predict this person's sexuality/gender etc."


## So, computer vision: good or evil?

Overall, we recognised that there are lots of benefits to computer vision - we use it all the time in our day to day lives! But as with most ethical problems, the question is more about when should we use it, and what for. 

This discussion will keep coming back to fundamental problems of epistemology and perception - these 
problems are not necessarily exclusive to data science and machine learning, they crop up everywhere in 
science! We need to be aware that machine learning is the systematisation of (flawed) human perception 
and understanding. This might 
wind up a few logiciains and topologists, but getting scientists to consider the potential downsides of 
their work could be an important step towards more ethical research practices.


---

## Related Links
- A really interesting paper on controlling for gender: ["This whole thing smacks of gender: algorithmic exclusion in bioimpedance-based body composition analysis"](https://arxiv.org/abs/2101.08325), by Kendra Albert & Maggie Delano at FAccT 2021.  
- Book recommendation: "Sorting Things Out", Geoffrey Bowker 
- Recommended talk by Peter Flach: "Computer Says I don't know"
- Recommended project with co-design: - https://www.nesta.org.uk/feature/eight-ways-councils-are-using-data-create-better-services/damp-sensing-frogs/ 


---

#### Attendees

Note: this is not a full list of attendees, only those who felt comfortable sharing their names.

__Name, Affiliation, Links to find you__

- Natalie Thurlby, Data Scientist, University of Bristol, [NatalieThurlby](https://github.com/NatalieThurlby/), [@StatalieT](https://twitter.com/StatalieT)
- Nina Di Cara, PhD Student, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, Maths PhDoer, Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Paul Lee, investor @pclee27
- Robin Dasler, research software product manager on hiatus, [daslerr](https://github.com/daslerr)
- Kamilla Wells, Citizen Developer, [Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/)
- Miranda Mowbray, honorary lecturer, [mirandamowbray](https://www.linkedin.com/in/mirandamowbray)


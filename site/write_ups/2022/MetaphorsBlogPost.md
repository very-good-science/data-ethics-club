# Cleaning the oil spill of data metaphors

```{admonition} What's this? 
This is a standalone blogpost written by Roman Shkunov in September 2022 about the use of metaphors when discussing data science and the implications of their usage. All opinions expressed are strictly his own. 
Huw Day, Nina Di Cara, Natalie Thurlby and Ola Michaels helped with the final edit.
```

## Introduction

When we talk about data, we talk in metaphors. 
As any data professional will recognise, when we’re trying to get a handle on a complex process like addressing anomalous records, we say that we’re doing ‘data cleaning’; when trying to prove how useful data are, we may claim that ‘we’re sitting on a data gold mine!’ 
But data metaphors are more than just window-dressing with words; they reflect how we think about data within our profession, and they encourage others to think about data in the same way. 
Unfortunately, the dominant metaphors of today present a skewed view of data; they obscure the subjective, human side of data while foregrounding its economic potential and claimed objectivity.  

The power of metaphors stems from their importance in how humans understand the world. 
As Lakoff and Johnson argue in their seminal work, Metaphors We Live By (2008), humans use metaphors in almost every sphere of life to reason about the world. 
Take the metaphor, time is a resource. 
We can see how in daily life we structure how we think of time in terms of a resource through its entailments, or consequences. 
A resource is a finite reserve of something that can be quantified (‘how much time do we have left?’), used up (‘we’re running out of time’) or converted into something useful through work (‘they used their time well’).

Metaphors are by nature partial; they only explain part of the target concept. 
Consequently, we choose metaphors with the entailments we think best explain the target concept. 
When we say that time is a resource, we seek to emphasise how time is finite, but obscure how time never stops, or how different people perceive it. 

The choice of metaphor is dictated not only by context, but also by one’s ideology (or worldview); the metaphor is chosen to match the ideology one wishes to promote. 
Consequently, metaphors provide a window through which we can understand the dominant ideologies in the world of data science. 
After looking at tens of data science presentations, promotion material, and learning guides, I identified two key data ideologies, which I represent by their main metaphors.

## Data as unprocessed economic potential/resource 

*Example metaphors: “data is the new oil”, “data gold mine”, “data mining”, “knowledge extraction”, “data is the new electricity”*

This data ideology, borne of the business world, takes data as material – often as a natural resource like oil – which when first obtained is unsuitable for generating economic value. 
To turn the ‘raw’ economic potential into actual economic value, data must be processed (e.g., filtered, aggregated, visualised, and modelled), or as Peter Sondergaard, Senior Vice President of tech-hype-cycle consultancy Gartner put it in 2011,

    “Information is the oil of the 21st century, and analytics is the combustion agent.” (Gartner, 2011, cited in Haupt, 2016)

The key claims in this data ideology are that data can be processed to obtain information that can be exchanged for financial gain, and that profit generation is necessarily good. 
It follows from these assertions that we should be recording/creating more data and processing it in order to drive economic growth. 
This is a clearly capitalist view of data, and its metaphors are typically used by data scientists or managers in sales pitches where they appeal for investment in a data-driven project by emphasising the economic value of data.

By treating data as economic potential/resource, this ideology and its metaphors background the human side of data: data are recorded about humans and are used to make decisions that affect humans. 
This can have serious negative consequences for the data subjects as witnessed by numerous case studies (Marsan, 2012), such as the introduction of Google’s Street View, which was initially launched without the blurring of faces and vehicle numberplates, leading to people’s privacy being compromised (Shankland, 2008). 

## Data as inherent and objective source of knowledge

*Example metaphors: “raw data”, “data collection”, “the data speaks for itself”, “the data doesn’t lie” *

A large number of data metaphors evidence the view held in the wider data science community that data is, in some way, natural. 
Metaphors falling under the umbrella of data as a natural resource imagine data to be ‘out there’, a resource waiting to be tapped; the often-used phrase ‘data collection’ conjures the image that data are ‘lying on the ground’, ready to be picked up. 
Taking data as ‘natural’ so that they merely need to be ‘collected’ leads to the view that data are inherent to the world, and not that they need to be created. 
The resulting assertion of this data ideology is that data are an objective source of knowledge; the information they give about the world transcend individuals’ opinions and biases. 
This is accompanied by a similar moral claim as in the last data ideology: because data give us insight into how the world truly is, one should collect as much data as possible to best enable ‘data-driven’ decision making, regardless of the consequences of expanding the measurement of humans’ lives. 

We should altogether dispense with the loaded statements that ‘data is natural’ and ‘data is objective’ if we are to honestly reflect on data science. 
While no doubt it is natural there many things that can be measured to produce data, all data are created: an analyst must choose what to measure, how to measure it, and how to represent these measurements [Note 1].
 Omitting or obscuring these choices can give a false impression of certainty and objectivity, reducing the validity of inferences and decisions made on those data. 
 What’s more, we must maintain awareness of the labour involved in creating data; especially for machine learning tasks, labelled data are created by workers on low-paid temporary contracts for platforms like Mechanical Turk (Irani and Silberman, 2013).

## Conclusion: How Can We All Clean the Oil Spill?

Metaphors are ubiquitous in describing data, but are we just muddying the linguistic and data-ideological waters with our current data metaphors? 
The answer is, in general, yes. 
In accordance with the profit-incentivised culture of business, which dominates data science, data scientists, managers, journalists, and others seek to promote the economic value and objective nature of data while, as Hwang and Levy (2015) point out, “people are nowhere to be found” in these data metaphors; the role of humans and ethical concerns regarding data are missing.

What can we do about the oil spill of data metaphors? 
In keeping with projects like Better Images of AI (2022) that aim to improve representations of data science, I urge data professionals who care about data ethics to create new data metaphors and actively re-interpret existing data metaphors [Note 2].

Devising new metaphors allows for altogether different ways of conceptualising data that may not be allowed by dominant metaphors. 
In the context of the ‘data as inherent and objective source of knowledge’ data ideology, Benjamin Garfield (2021) offers three alternatives for replacing the term ‘data collection’ that help mitigate the backgrounding of labour and human subjectivity: data creation, data curation, and compiling data.
For metaphors falling under ‘data as unprocessed economic potential/resource’, Sara Watson (2015) argues that embodied metaphors can help ‘bring big data back down to a human scale and ground data in lived experience’, helping counter the distancing of data from the humans who created it. 
To that end, she recommends metaphors from the quantified-self community, such as data is a body (e.g., ‘data is a foot/fingerprint’, ‘data double’). 

In contrast to metaphor creation, reinterpretation provides an avenue for subverting rather than replacing metaphors such as ‘data is the new oil’ that reinforce dominant data ideologies. 
Instead of solely focussing on the financial profits gained from data being treated as a resource, one can explore alternative entailments of the metaphor to highlight aspects of data usually backgrounded such as environmental externalities; just like extracting oil, processing data can result in significant environmental consequences (see [Note 3] for an example of how you could re-interpret ‘raw data’.) 
The benefit of reinterpretation as opposed to metaphor creation is that one can more easily build a bridge between existing data ideologies and new data ideologies by simultaneously activating familiar entailments (such as, data has economic value) and new entailments (data processing has environmental costs), helping establish dialogue between people with different perspectives. 

Thank you to the Data Ethics Club for suggesting Barrowman’s (2018) ‘Why data is never raw’ which inspired this blogpost (and for some of their wonderful analysis which fed, either consciously or subconsciously, into the making of this blogpost. Oh god, that’s another metaphor I just used)!

## Notes

[1] This results in what philosophers of science call the theory-dependence (or theory-ladenness) of observations: all recorded observations require some prior framework (or paradigm) to create a way to measure and make sense of the world (Okasha, 2016). Even measurements for supposedly objective quantities like electrical charge rely on theories of electricity and, at a more fundamental level, numbers. 
This concept is important when considering one of the key activities of scientists: to choose a theory that best explains some phenomenon, as recorded in data. The problem, according to Thomas Kuhn, is that one cannot choose between two conflicting paradigms (frameworks of science) based on data alone, as what meaning you attach to the data will depend on your paradigm of choice, and hence one could ‘explain away’ the data within the terms of either paradigm. Consequently, for Kuhn, there is no objective way to choose between conflicting paradigms (Okasha, 2016). 

[2] Beyond data metaphors, entire workshops have been devised for generating new metaphors for reframing ideas. One such kind of workshop was recorded in (Lockton et al., 2019), and I’d highly recommend reading it for inspiration regarding workplace activities for raising how we talk about technology, and how this links to ethics.

[3] One example of a data-ethical or data-feminist reinterpretation that can bring new perspectives to an existing metaphor is that of data as food. Although data are often called ‘raw’, I suggest that the metaphor is extended further. Firstly, raw data is grown: humans ‘feed’ the raw data as they grow (i.e. structure how they go about collecting data) which then determines what the fully-grown raw data look like. Moreover, by harvesting/collecting the data by ‘tearing’ them from the tree/bush/ground (the person/data source), one is capturing what used to be whole with the person but is now dead in some sense (although it remains important to them), they no longer grow from and hence do not truly reflect the living organism from which it arises; the data are a reification of the person’s characteristics. Finally, as before, the raw data must be cooked for something edible to appear (although what would a data sashimi or sushi look like? Discuss.) 
Adopting such an interpretation leads to increased attention to the process that generates data and not solely to the output (data to be analysed). Instead of just asking, ‘how can we analyse these data?’ and ‘how reliable are these data?’, this interpretation encourages us to ask, ‘how do the people who create this data shape it?’ and hence ‘how can we support the people involved in the data creation process?’. Finally, it emphasises the relationship of the data subject to their data in more personal terms than is usual; the data are conceptualised as not just being ‘about’ a person, but in some ways a part of them that needs to be treated with respect. 

## References

Barrowman, N., 2018. [Why data is never raw](https://www.thenewatlantis.com/publications/why-data-is-never-raw). The New Atlantis, 56), pp.129-135.
Benjamin, G., 2021. [What we do with data: A performative critique of data "collection"](https://policyreview.info/articles/analysis/what-we-do-data-performative-critique-data-collection). Internet Policy Review, 10(4), pp.1-27.
Betterimagesofai.org. 2022. [Better Images of AI.](https://betterimagesofai.org/)
Haupt, M., 2016. [“Data is the New Oil” — A Ludicrous Proposition.](https://medium.com/project-2030/data-is-the-new-oil-a-ludicrous-proposition-1d91bba4f294) Medium
Hwang, T. and Levy, K., 2015. [“The cloud” and other dangerous metaphors](https://www.theatlantic.com/technology/archive/2015/01/the-cloud-and-other-dangerous-metaphors/384518/) The Atlantic, 20. 
Irani, L.C. and Silberman, M.S., 2013, April. [Turkopticon: Interrupting worker invisibility in amazon mechanical turk.](https://dl.acm.org/doi/10.1145/2470654.2470742) In Proceedings of the SIGCHI conference on human factors in computing systems pp. 611-620.
Lakoff, G. and Johnson, M., 2008. Metaphors We Live By. University of Chicago press.
Lockton, D., Singh, D., Sabnis, S., Chou, M., Foley, S. and Pantoja, A., 2019. [New metaphors: A workshop method for generating ideas and reframing problems in design and beyond.](https://dl.acm.org/doi/10.1145/3325480.3326570) In Proceedings of the 2019 on Creativity and Cognition pp. 319-332.
Marsan, C., 2012. [15 Worst Internet Privacy Scandals of All Time.](https://www.csoonline.com/article/2130748/15-worst-internet-privacy-scandals-of-all-time.html ) CSO Online. 
Okasha, S., 2016. [Philosophy of Science: A Very Short Introduction.](https://academic.oup.com/book/517) Oxford: Oxford University Press, pp. 151-153.
Puschmann, C. and Burgess, J., 2014. [Big data, big questions| Metaphors of big data.](https://ijoc.org/index.php/ijoc/article/view/2169) International Journal of Communication, 8, p.20.
Shankland, S., 2008. [Google begins blurring faces in Street View.](https://www.cnet.com/culture/google-begins-blurring-faces-in-street-view/) CNET. 
Taffel, S., 2021. [Data and oil: Metaphor, materiality and metabolic rifts.](https://journals.sagepub.com/doi/10.1177/14614448211017887) New Media & Society, p.14614448211017887.
Watson, S.M., 2015. [Metaphors of Big Data. DIS Magazine.](https://dismagazine.com/discussion/73298/sara-m-watson-metaphors-of-big-data/)


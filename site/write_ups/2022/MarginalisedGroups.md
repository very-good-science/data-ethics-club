# Garbage in, garbage out: How bad use of data harms marginalised groups  

```{admonition} What's this? 
This is a standalone blogpost written by Euan Bennet and Hannah O’Donoghue in September 2022. 
Euan Bennet is a university lecturer and Hannah O’Donoghue is a trainee nursing associate and disability advocate. 
All opinions expressed are strictly their own. 
Nina Di Cara, Natalie Thurlby and Huw Day helped with the final edit.
```

## Introduction

A common theme in data ethics discussions is the harm that can be caused to marginalised groups in society through the bad use of data. There are many, many manifestations of this – usually unintentional – harm, and the responsible data ethics ethos is that data scientists should be aware of this potential and take steps to avoid it from happening. 

In this blog post we want to present a general example of an area where the bad use of data has historically caused, and continues to cause, harm to one particular marginalised group of people. As a specific example we will address a recent paper which is an excellent example of this. This post is by no means intended to be exhaustive and is intended to serve as just one example of a field where ‘data hazards’ are commonly found. 

The field which this blog post seeks to highlight is research into the genetics of autism. This is a contentious area because of the history of autism research and the related treatment of autistic and neurodivergent people. There is far too much to get into here, but suffice it to say that many autistic people are generally squeamish around any research relating to potential screening of autism in utero, or of a “cure”, due to the potential route to eugenics that such tools might very well enable. For the purposes of this blog post however, we want to highlight how studies involving genetics and autism cause harm by not only furthering these routes of investigation, but also just being based on bad data and thus producing inherently unreliable results. 

The three fundamental problems affecting the wider field of autism research are:  
1.	Every data set of people ‘medically diagnosed’ as autistic are heavily biased, because of systematic under- and mis-identification of autistic people who do not fit into harmful stereotypes. 
2.	Any focus on genetics ignores a whole host of social and societal factors which cannot be neglected as part of a complex picture. 
3.	Many researchers continue to frame autism entirely under the medical model of disability (hence the use of medical databases), and completely ignores the social model of disability which is a far more appropriate framework for properly understanding autism and other neurodiverse neurotypes.

## Systematic bias in the data

Autism is commonly under- and mis-identified in several groups in society. The reasons for this include historical biases dating back to the earliest identification of the neurotype - even today the myth that “autism is only found in boys” is pervasive. This is compounded by historical biases in identifying autism in anyone who isn’t a white boy conforming to a very [narrow range of behaviour stereotypes](https://pubmed.ncbi.nlm.nih.gov/30143373/). 
Assumptions based on outdated and wrong information have contributed to diagnostic bias against [women, non-binary people, and anyone of colour](https://pubmed.ncbi.nlm.nih.gov/26544750/).

## Social and societal factors

These historical biases are amplified by other social and societal issues. Autistic people report that one of the biggest challenges to thriving in a society designed around neurotypical social norms is the constant pressure to “mask” their autism by conforming to the expected norms of society which [neurotypical people take for granted](https://www.liebertpub.com/doi/abs/10.1089/aut.2021.0021).  

One reason for the under-diagnosis of autistic women is that societal pressures are much stronger on people socialised as women to behave in certain ways. As a result, it has been estimated that as much as [80% of autistic women are unidentified as autistic at age 18](https://pubmed.ncbi.nlm.nih.gov/35204992/). Far from the 1:4 ratio of autistic women to autistic men that are currently recognised by existing diagnoses, attempts to estimate the true ratio have found it is at least 3:4. Again due to historical biases of diagnostic criteria, these estimates are by definition not exact, but equally there seems to be [no evidence as to why the ratio shouldn’t be 1:1](https://www.scientificamerican.com/article/we-need-better-diagnostic-tests-for-autism-in-women/).  

## Medical vs Social models of disability 

A proper discussion of different models of disability is beyond the scope of this post  . To summarise, the medical model of disability says that a disabled person has something “wrong” with them, to be “fixed”. The [social model] (https://inclusionscotland.org/get-informed/social-model) recognises that a disabled person might have different support needs in order to fully participate in society, but since society does not currently provide such support, the disabled person is in effect, disabled by society.
 
Suffice it to say that for many autistic (and neurodivergent) people, applying the medical model of disability is outdated, [has no measurable effect on improving the lives of autistic people] (https://pubmed.ncbi.nlm.nih.gov/31763860/), and has even [contributed to significant harm] (https://hennykdotcom.files.wordpress.com/2018/02/aia_evidence-of-increased-ptsd-symptoms-in-autistics-exposed-to-applied-behavior-analysis.pdf,https://www.reddit.com/r/autism/comments/ub3skp/lets_talk_about_aba_therapy_aba_posts_outside/).     Autistic and neurodivergent people cannot be “fixed” or “cured” as the authors’ use of the medical model of disability implies. Instead the focus should be on ensuring equitable access to society for everyone. Understanding society using the social model of disability is essential in building a more equal society for everyone.  

## Specific Example

A [recent paper published in Cell Genomics] (https://www.cell.com/cell-genomics/fulltext/S2666-979X(22)00063-5) claims to have found evidence of a “female protective effect” against autism. They combined two studies to reach this conclusion: an epidemiological study of a Danish medical database, and two genetic libraries. The authors claim that the findings “strongly support a [Female Protective Effect] against [Autism Spectrum Disorder’s] common inherited influences”. 

In the final section of this blog post, we will use this paper as an example of how biased data can be used to draw conclusions that have the potential to harm marginalised groups, and set out the case for doubting the conclusion that there is a “female protective effect” against autism. 

As discussed above, medical ‘diagnosis’ of autism still suffers from historical biases and stereotypes which have yet to be corrected. As such attempting to draw conclusions about a “Female Protective Effect” using a data set based   on past “diagnoses”   is akin to the ghost of Steve Jobs conducting a survey of people’s favourite Android phones in the Apple Store: you just wouldn’t be looking in the right place for the answers that you seek.   

In focussing on genetic effects, the authors neglect all of the social and societal factors that further contribute to bias in the medical databases used in the study. Finally, the language used throughout the paper clearly demonstrates the authors’ commitment to the medical model of disability, which adds a further layer of bias to the study design given the historic under- and mis-identification of autism in anyone who isn’t a white boy. 

It is perhaps beyond the scope of the paper to also consider the historic under- and mis-identification of people of colour, but this is not mentioned. The paper specifies that only people of “European ancestry”     were included. This methodology is not clearly explained in the paper but this seems to be their euphemistic explanation that they only considered white people in the study cohort. [This is a problem in wider genetics research as well] (https://www.theguardian.com/science/2018/oct/08/genetics-research-biased-towards-studying-white-europeans).

## Summary

Many researchers studying the genetics of autism use data sets (medical ‘diagnoses’ of autism) which: 
1.	Have an inherent systematic bias due to historical and current diagnostic criteria.
2.	Fail to account for additional social/societal bias due to different experiences of socialised gender expression.
3.	Fail to account for additional social/societal bias due to historic mis-identification of people of colour. 

In the Cell Genomics paper we saw how the authors use these data to attempt to ascribe a genetic basis for the observations and extrapolate this to the entire population, without accounting for the acquisition bias inherent in the data set. To use a less technical term, this is a perfect example of “Garbage In, Garbage Out” (GIGO). 

## Data Hazards  

The [Data Hazards](https://datahazards.com/) project exists to encourage data scientists to consider the ethical implications of their work. The creators have designed a series of labels which are similar to the classification system used for hazardous chemicals. As with chemicals, the intent is not to discourage people from using them, but to ask people to proceed with care. For further explanation of the Data Hazards labels, see https://datahazards.com/contents/data-hazards.html. 

Let’s look at the Data Hazards that could apply to the research study we have been discussing:  

1.	Reinforces existing biases - it turns out that if you use data based on outdated and biased diagnostic tools then you get results that reflect the inherent bias of the data! This would include the underrepresentation of people of colour in the data, and the existing bias regarding the historic under-diagnosis of women that the data reflects. 
2.	Classifies or ranks people - this is more present in the language used to present the results (https://annsautism.blogspot.com/2022/06/research-that-dishonours-and-harms.html). One could equally conclude that “maleness protects from neurotypicality”. 
3.	Lacks community involvement – the [funders] (https://autismsciencefoundation.org/about-us/) of this research advocate for ‘treatment’ and, like the researchers, clearly subscribe to the medical model of disability. Best practice for this research would have been to gather perspectives from those in  the autistic community who prefer the social model of disability (https://www.liebertpub.com/doi/10.1089/aut.2022.0017) and taking care to avoid ableist language such as describing autism as a “disorder”, and describing autistic people as “disorder cases” (https://www.liebertpub.com/doi/10.1089/aut.2020.0014).
4.	Danger of misuse   - this is the most serious Data Hazard involved in the study, because some of the conclusions are edging in the direction of eugenics. It would not be a stretch to imagine certain groups who have a desire to “cure” autism latching on to this paper and using it as part of their campaign to actively harm autistic people. Research that wrongly attributes genetic causes to observations which are heavily influenced by social and societal effects could easily be misused and abused by those who wish to avoid addressing the societal effects.   

## Conclusions

This paper is a fantastic example of how bad use of data can misrepresent marginalised groups in society and reinforce existing stereotypes. By framing these conclusions in ableist language and failing to even consider the social model of disability, many researchers in the genetics of autism are contributing to harming people who their work affects. Work such as this impedes progress to a more equal society, and could even be misused by those who have an interest in making society even less equal. 

Do better, researchers !



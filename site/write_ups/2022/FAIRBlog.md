# But is it FAIR?

```{admonition} What's this? 
This is a standalone blogpost written by Paul Lee in December 2022 about the FAIR Data Principles. Paul has worked in the investment world for more than two decades and is author of [The Sense of Fairness blog](https://senseoffairness.blog/)
which, in his own words, is all about: "Exploring what fairness is, why it matters and what we should do to reawaken the sense of fairness." All opinions expressed are strictly his own. 
Huw Day, Nina Di Cara and Natalie Thurlby helped with the final edit.
```

## FAIR in Theory

Information technology often, sadly, fails to be fair. Some in the sector, though, are trying – and even occasionally beginning to gain traction.

It’s what makes the FAIR Principles (sometimes called the FAIR Data Principles) so interesting. The abbreviation stands for Findability, Accessibility, Interoperability and Reusability, and it’s a set of standards for datasets that are used in analytics. If data lives up to these principles, it is more likely to be capable of reuse and thereby enable others to test if results are replicable – one of the foundations of the scientific method. Allowing others to reuse data and to attempt to replicate results may help remove some errors from new technology – including creating or perpetuating unfairnesses. At present for example, there is a tendency to ossify past unfairness through the biases embedded in the data that is used to train artificial intelligence.

The FAIR principles were launched in a 2016 paper [1](https://www.nature.com/articles/sdata201618). This makes clear that the ambition for the principles extends beyond narrow definitions:
“Importantly, it is our intent that the principles apply not only to ‘data’ in the conventional sense, but also to the algorithms, tools, and workflows that led to that data.”

The creators of the FAIR Principles appear to have a touching confidence in the ability of the human mind to deal with data in context and to understand nuance, which feels a little like overconfidence to me. But the point of the principles is the recognition that modern techniques rely on machines (they use the term to cover the wide spectrum of technologies that might be applied) to deal with the vast quantities of data that are available, and those machines are usually even less good than humans at grasping context and nuance. The FAIR Principles won’t change that, but they provide enough visibility for other scientists to probe and test the extent of the errors that will have arisen because of those failures, including errors of unfairness.

While the FAIR Principles are not explicitly expected to be fair, their nature and application should lead to fairness as well as FAIRness. ‘Findable’ requires data to have rich metadata attached, which needs also to be ‘Accessible’ by enabling universal free and fair access; ‘Interoperable’ and ‘Reusable’ mean that the data is in a form that can be widely understood and applied and put to use by others without inappropriate restrictions. It’s a level playing field for data availability and use – ensuring that fair access can enable ongoing checking and testing.

Others have since taken the concept further, such as the Dutch moves to create a data stewardship profession that reflects the FAIR Principles [2](https://zenodo.org/communities/nl-ds-pd-ls/?page=1&size=20). This profession would take responsibility for the shared endeavour that good data stewardship requires, across time and involving individual researchers, other scientists in the research project, their sponsoring body or institute, and indeed from the funders of the research [3](https://zenodo.org/record/7225070#.Y4IIduzP0qw). Recent presentations as part of this project, including ones dated October and November of this year, suggest strong progress in acceptance of the Principles (at least in the healthcare data sector that is the project’s initial focus) but also that there is much more to be done [4](https://zenodo.org/record/7188375#.Y4IRIOzP0qw). 

## FAIR in Practise

A further development has been a move towards automatic testing of the FAIRness of datasets [5](https://www.sciencedirect.com/science/article/pii/S2666389921002324). This aims to avoid the significant workload implied by the prior manual approaches to such assessments. The range of 17 core metrics developed by the team helps mitigate against the risk of a single measure being applied to a complex area, which would lead to less insight being offered – as well as the risk of gaming. Each core metric has between one and three practical tests that can be applied to test whether it is met or not.

The initial test, on some common datasets, wasn’t encouraging, with around average expected scoring on findability and interoperability, and significantly below average scores for accessibility and reusability (though the academics note that the particularly poor accessibility result is based just on a single metric, which every dataset failed – they were only applying 13 out of the total 17 metrics at this stage):
 
```{image} ../../images/FAIR1.png
:width: 500px
:align: center
:alt: FAIR Scores of Data Objects by Principles (First Interation n=2500)
```

The good news is that after engagement with the data repositories and subsequent relatively straightforward improvements to the metadata, the results improved notably (though the result for reusability oddly seems to show a little deterioration in quality by a fifth of the data at the top end):

```{image} ../../images/FAIR2.png
:width: 500px
:align: center
:alt: FAIR Scores of Data Objects by Principles (Second Interation n=2500)
``` 

Applying transparency and accessibility standards more broadly in the data and technology world is of growing importance. Citizens often feel disempowered and disenfranchised in the face of the technology that is all around us. Making tech, including the underlying algorithms that shape our modern experience of the world, more transparent is a necessary step to build confidence and to prevent democratic backing for technology further eroding.

This matters. The algorithm is the echo chamber. It ushers and tempts us from the babble of the town square down narrower side-streets, sometimes forcing us into the most squalid and awful thoroughfares with a one-way traffic of angry bile. Unless we have sufficient transparency to understand how algorithms usher and force people in these ways we cannot address and reverse the harms that they are causing. Unfairness makes people more prone to accept conspiracy thinking, and at present social media algorithms are feeding and exaggerating that process. FAIRness may help fairness over time.

## Bibliography

1) [The FAIR Guiding Principles for scientific data management and stewardship, Mark Wilkinson et al, Nature Scientific Data, March 2016](https://www.nature.com/articles/sdata201618)

2) [Professionalising data stewardship: Dutch projects](https://zenodo.org/communities/nl-ds-pd-ls/?page=1&size=20)

3) [Towards FAIR Data Steward as profession for the Lifesciences, Salome Scholtens et al, ZonMw/Zilveren Kruis, October 2019](https://zenodo.org/record/7225070#.Y4IIduzP0qw)

4) [FAIR data stewardship: the need for capacity building & the role of communities, Mijke Jetten, E4DS Training, October 2022](https://zenodo.org/record/7188375#.Y4IRIOzP0qw)

5) [An automated solution for measuring the progress toward FAIR research data, Anusuriya Devaraju, Robert Huber, Patterns 2, 100370, November 2021](https://www.sciencedirect.com/science/article/pii/S2666389921002324)




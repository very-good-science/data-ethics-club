# Data Ethics Club: [Data Ethics Checklist at Seattle Children's Hospital](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7936507/pdf/ocaa307.pdf?fbclid=IwAR17HKoYE8dgy0nB4K6RZlrd3XRGJZr62G_McYd7sZg6HXDhHjxhtgBbSk4) 
 

```{admonition} What's this?  

This is summary of Wednesday 22nd November's Data Ethics Club discussion, where we spoke and wrote about the article "The case for information fiduciaries: The implementation of a data ethics checklist at Seattle Children’s Hospital" by Elizabeth Montague, T. Eugene Day, Dwight Barry, Maria Brumm, Aaron McAdie, Andrew B. Cooper, Julia Wignall, Steve Erdman, Diahnna Nunez, Douglas Diekema and David Danks. 
The summary was written by Jessica Woodgate, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club".  
Vanessa Hanschke, Huw Day, Nina Di Cara and Natalie Thurlby helped with the final edit. 

``` 
 

SUGGESTED TITLE FOR THE WRITE-UP -  

"SHOVELWARE PUBLISHING AND INSTITUTIONAL REPUTATION-WASHING: A CAUTIONARY TALE" (upvoted) 

(Side note: this is the second DEC in a row where we've gone Reviewer 2 on the paper) 

 

## Do the paper and the checklist effectively address the ethical considerations data users should consider when collecting and processing health data? 


The effectiveness of the checklist is constrained by unclear wording, which could lead to problems around the interpretation of the questions. Questions should be clear and concise; comprehensive enough not to require additional information or disclaimers. However, we found several areas where questions were presented in a confusing way. One example is the use of quotation marks around “consent”; we weren’t sure why it is written this way. We wondered if most people would be able to answer the questions on the list or know the items that the list is referring to. For example, the first question asks if people have consented to having their data used. However, we wondered how easy it is to judge whether people have given properly informed consent. Explanations of data usage are often confusing and opaque for the people we’re collecting data from, especially if those people are distressed or unwell (e.g. because they or their children are in hospital). The abstractness of the wording makes it difficult for readers to connect the issues with problems that might arise. This could be improved by including theoretical scenarios, or more methodological questions e.g. “is there enough missing data that it could potentially bias your results?”. We also thought that the language used in the paper to describe patients/families is quite condescending. 


In addition to unclear wording, the checklist is ambiguous in the way scoring is presented. It is an odd mix of scoring for an “objective” metric, as there is no specific suggestion of what the scores mean, or what to do with the scores afterwards. Why should questions be scored in the first place; is this the most effective critical thinking tool? The checklist seems more like an opportunity for self-reflection, as opposed to something actionable. This does have its merits in making the prospect of data collection and usage visible, and we can appreciate the aggregation of ideas to produce an artefact which is manageable for busy people to work with. However, the article isn’t very accessible in its wording, links within it don’t work (including the link to the supplementary information including questionnaire - i.e. one of the most important parts of the paper), and there is nothing to indicate whether the checklist is being used as intended (or specifics on what the intended use of the checklist actually is). 


Including information about how the authors intend the checklist to be used would improve the effectiveness of the paper. It would be beneficial to know how the checklist is presented to users, e.g. if it is handed out independently, or alongside a workshop/additional instruction. There is not a clear definition of who the intended users of the checklist are, or who classifies as “data personnel”. There is nothing about potential reuse of existing data, and the danger of bad or missing data. Missing data has a huge effect on the robustness of models, and there should be more emphasis on “what are we not seeing”. There is also no indication of what happens to the outcome of the checklist, if there is any processing of the results, or if people are implementing the checklist at all. These factors regarding how the checklist is used are important, as there are biases that could emerge along various stages of the pipeline. 


As well as misuse of the checklist, biases could emerge in the way the checklist was created. The paper does not say whether the checklist was co-designed with the people who put it into practice, or patients who would be affected by it. Issues with the way questions are worded suggest that co-design was not an aspect of the checklist’s development. Some of the ideas in the checklist might be brand new to the people using it, and there is no indication to where people might find more information. Co-design is important because those who implement and use the checklist, like healthcare practitioners, would have knowledge and experience that desk-sitting researchers don’t have. Healthcare practitioners would also be familiar with the idea of threshold checklists in other contexts as part of their training. It’s possible that ideas from other healthcare checklists have been adopted in this paper but have then been overcomplicated. 


Today, there are many different ethics checking frameworks and tools circulating, and we wondered if there were any existing frameworks that we would prefer to this checklist. Most of us hadn’t worked with such checklists. For those of us who had, there were “threshold data ethics checklists” which had to be completed before projects could progress. These threshold checklists were presented as a series of questions about what you have/haven’t done, with room for expanding where necessary, as opposed to the sliding scale in the checklist presented here. The threshold checklists we worked with were also accompanied by implementation teams to support the process. We thought it was likely that there are many similar in-house checklists developed across government agencies in the last couple of years, but these departments won’t publish papers about it. 


Overall, the paper comes across as a bit of a shovel-ware paper, churned out as part of new medics’ professional development, without much regard to quality or purpose of ‘research’. This is a major problem across several fields. The hospital can then use the paper as a performative opportunity, to point to a paper about something which they may or may not be doing. Reputation successfully washed. 


## Do you think the Best Practices described in the paper would be effective for managing data ethics in healthcare? 

 

For some of us, our answer was: no. Next question. 

 

For others, there were some aspects of the suggested best practices that we liked. For example, we liked the suggestion of training people in data ethics. We thought that best practices could be broken down into ensuring that people are properly trained; doing an ethical review any time you look at something fresh (new projects or updating legacy ones); including oversight from people outside of the project. 


However, we also thought that the rigor of the best practices as presented in the paper left much to be desired. The paper is quite vague in how to go about addressing problems such as bias, for instance. If people filling out the form don’t know about existing biases, the checklist won’t do much to help them. Yet it is possible to analyse algorithms for bias, and we should insist that people do this. 

 

## Can paediatric healthcare data effectively be used to inform data ethics across all branches of healthcare? 


Any information relating to healthcare has some sort of ethical impact, but different areas of healthcare will have different considerations. We expect that the primary difference would be consent, for example consent in paediatrics will be obtained from parents rather than the children themselves. Each branch of healthcare has their own culture, minutiae, etc., and generalising is very difficult. Rolling out a paediatric framework across all areas wouldn’t be desirable without considering the specific risks of each area. As well as department dependent, risks are also institution dependent. On the other hand, use cases and proof of concepts can always be helpful to inform others. Saying that, we wondered if this paper really counts as a proof of concept, or if it is the opposite of a proof of concept. 


The aim to create a generalisable artefact is laudable, but the cost is that a lot of important ethical detail is lost. There is oversimplification of concept, and overcomplication of language. We thought that the last two questions might as well be “are you a good person”, which seems pointless to ask in this scenario. 

 

## Bonus question: Should data scientists and analysts involved in healthcare be considered “Information Fiduciaries”? 


A big yes from some of us. We all have the ability to highlight potential problems in data usage. Considering everybody information fiduciaries is a good ideal. However, there are differences between the way that data is controlled to the way that money is controlled (where the traditional use of fiduciary comes from - [“the responsibility to take care of someone else’s money in a suitable way”](https://dictionary.cambridge.org/dictionary/english/fiduciary)). Money is an [intermediate good, or abstract credit relationship](https://plato.stanford.edu/entries/money-finance/#WhatMone), where owners and subjects to the relationship can be clearly denoted. Data, on the other hand, are [“recordings of observations or events”](https://plato.stanford.edu/entries/statistics/#StaMod) of which ownership can be much harder to determine. This might mean there is some sentiment drift when we apply the concept of fiduciaries to data. 

 

## Attendees 

- Nina Di Cara, Research Associate, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara) 

- Amy Joint, free-range publisher, [@AmyJointSci](https://twitter.com/amyjointsci) 

- Vanessa Hanschke, PhD Interactive AI, University of Bristol 

- Chris Jones, Mathematics PhD graduate, (formerly) University of Bristol 

- Euan Bennet, Lecturer, University of Glasgow, [@DrEuanBennet](https://twitter.com/DrEuanBennet) 

- Melanie Stefan, Computational Biologist, Medical School Berlin (also what are y’all still doing on Twitter?!) 

- [Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/), Citizen Developer, Australian Public Service, Brisbane 

- [Jessica Woodgate](https://jessica-woodgate.github.io/), PhD student, University of Bristol 

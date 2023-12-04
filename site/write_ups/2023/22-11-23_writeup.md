# Data Ethics Club: [Data Ethics Checklist at Seattle Children's Hospital](https://academic.oup.com/jamia/article/28/3/650/6065836) 
 

```{admonition} What's this?  

This is summary of Wednesday 22nd November's Data Ethics Club discussion, where we spoke and wrote about the article "The case for information fiduciaries: The implementation of a data ethics checklist at Seattle Children’s Hospital" by Elizabeth Montague, T. Eugene Day, Dwight Barry, Maria Brumm, Aaron McAdie, Andrew B. Cooper, Julia Wignall, Steve Erdman, Diahnna Nunez, Douglas Diekema and David Danks. 
The summary was written by Jessica Woodgate, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club".  
Vanessa Hanschke, Huw Day, and Nina Di Cara helped with the final edit. 

``` 
 
## Do the paper and the checklist effectively address the ethical considerations data users should consider when collecting and processing health data? 

To begin with, we discussed how nice it was to see a proactive approach to data ethics being taken by individual organisations, where thought has been put into how to address complex ethical issues concerning health care data. 

It's a difficult topic, and while many ethics checklists do exist they may not apply well to secondary data in a healthcare setting. Most of us hadn’t worked with such checklists. For those of us who had, there were “threshold data ethics checklists” which had to be completed before projects could progress. These threshold checklists were presented as a series of questions about what you have/haven’t done, with room for expanding where necessary, as opposed to the sliding scale in the checklist presented here. The threshold checklists we worked with were also accompanied by implementation teams to support the process. We thought it was likely that there are many similar in-house checklists developed across government agencies in the last couple of years, but these departments won’t have published their work in the same way. 

We were also interested by the specific requirements that might come up in this paediatric setting, where analysts are working with data from children and young people whose consent might be given by a parent. 

Our conversations focussed on a few themes of questions we had about the checklist itself and the article that accompanied it... We suspect that the answers to some of our questions were limited by the length of the article - something that academic publishing has to answer for, rather than the authors! 

### Checklist development and wording

To start with we wondered why the checklist didn't feature more heavily in the actual article. It would have been nice for it to be included as a table, for example. This might make it more accessible. The link to the supplementary materials in the pdf didn't work, and so for some that made it a bit trickier to work out how to see the checklist. 

Several of us wondered about how the questionnaire was designed - we considered how valuable it would have been for a checklist like this to be co-designed with the people who put it into practice, or patients who would be affected by it. Co-design is important because those who implement and use the checklist, like healthcare practitioners, would have knowledge and experience that desk-sitting researchers don’t have. Healthcare practitioners would also be familiar with the idea of threshold checklists in other contexts as part of their training. 

We suspect that some of the ideas in the checklist might be brand new to the people using it, and there is no indication to where people might find more information. That said, making sure all analysts go through some kind of training was a big yes from us! It would also help make sure people using the checklist understood what it was asking them. Co-design or testing with a user-base would also have been a valuable step, and it wasn't clear whether this was done. 

Ideally questions should be clear and concise; comprehensive enough not to require additional information or disclaimers. However, we found several areas where questions suggested subjective interpretation. One example is the use of quotation marks around “consent”; we weren’t sure why it was written this way. 

We wondered how easy it is to judge whether people have given properly informed consent, especially as a secondary user of the data. Explanations of data usage are often confusing and opaque for the people we’re collecting data from, especially if those people are distressed or unwell (e.g. because they or their children are in hospital). The abstractness of the wording makes it difficult for readers to connect the issues with problems that might arise. This could be improved by including theoretical scenarios, or more methodological questions e.g. “is there enough missing data that it could potentially bias your results?”. These are the sorts of areas that data analysts have expertise in and control over in their analysis. There are many tools now for assessing bias in data science, and we should be encouraging people to use them much more strongly than we do at present.

Perhaps including some case studies in the paper of how these questions might change the way someone uses the data would have been valuable here, and the contexts/processes in which it has been implemented.

### How should we interpret the 'results' of the scoring?

We found the purpose of the checklist scoring ambiguous, as there is no specific suggestion of what the scores mean, or what to do with the scores afterwards. Why should questions be scored in the first place; is this the most effective critical thinking tool? The checklist seems more like an opportunity for self-reflection - this is an important step if we want to increase ethical awareness amongst data scientists and analysis. But perhaps this should be more explicit if it is the case.  

This does have its merits in making the prospect of data collection and usage visible, and we can appreciate the aggregation of ideas to produce a short artefact which is manageable for busy people to work with. 

### When should  this questionnaire be used?

Including information about how the authors intend the checklist to be used would improve the effectiveness of the paper. It would be beneficial to know how the checklist is presented to users, e.g. if it is handed out independently, or alongside a workshop/additional instruction. There is not a clear definition of who the intended users of the checklist are, or who classifies as “data personnel”. 

We also thought there were some missed opportunities to highlight some practical ethical risks that data analysts and data scientists should be conscious of. For example, the danger of bad or missing data. Missing data has a huge effect on the robustness of models, and there should be more emphasis on “what are we not seeing”. There is also no indication of what happens to the outcome of the checklist, if there is any processing of the results, or if people are implementing the checklist at all. These factors regarding how the checklist is used are important, as there are biases that could emerge along various stages of the pipeline. 


Overall, we appreciated the aims of the paper and thought it was great to see how people are thinking about ethics within their organisations. However, it did also give us a lot to think about in terms of how you make sure checklists like these are effective for the people who are intended to use them, and effective in making the work being done more ethical overall. Without this, it can be easy to say that an organisation *has* a data ethics checklist, which sounds/looks good, but might not actually be making a practical difference. Performative ethics is something we have seen many examples of, and is often a worry as ethics becomes more of a recognised issue in data science around the world.

## Do you think the Best Practices described in the paper would be effective for managing data ethics in healthcare? 

For some of us, our answer was: no.

For others though, there were aspects of the suggested best practices that we really supported. For example, we liked the suggestion of training people in data ethics. We thought that best practices could be broken down into ensuring that people are properly trained; doing an ethical review any time you look at something fresh (new projects or updating legacy ones); including oversight from people outside of the project. 

## Can paediatric healthcare data effectively be used to inform data ethics across all branches of healthcare? 

Any information relating to healthcare has some sort of ethical impact, but different areas of healthcare will have different considerations. We expect that the primary difference would be consent, for example consent in paediatrics will be obtained from parents rather than the children themselves. Each branch of healthcare has their own culture, minutiae, etc., and generalising is very difficult. Rolling out a paediatric framework across all areas wouldn’t be desirable without considering the specific risks of each area. As well as department dependent, risks are also institution dependent. On the other hand, use cases and proof of concepts can always be helpful to inform others. 

The aim to create a generalisable artefact is laudable, but the cost of this can be an oversimplification of the core concepts. We thought that the last two questions would be difficult to answer objectively about yourself, because they essentially ask whether you think you are a good and trustworthy person - most people would probably like to say yes! This highlights the importance of getting outside input on data ethics, and the value in ideas such as the Ethics Board proposed. 

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

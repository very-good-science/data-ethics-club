---
blogpost: true
date: March 13, 2024
author: Dwight Barry
category: Blog
tags: dataethics, children, research ethics, healthcare
---

# Data Ethics Checklist - Author's Response

```{admonition} What's this? 
Back in November 2023, we spent a Data Ethics Club session discussing [The case for information fiduciaries: The implementation of a data ethics checklist at Seattle Children’s Hospital”](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7936507/pdf/ocaa307.pdf?fbclid=IwAR17HKoYE8dgy0nB4K6RZlrd3XRGJZr62G_McYd7sZg6HXDhHjxhtgBbSk4), a Perspective paper outlining the importance of ethical data practices in healthcare,
which also presented a checklist for evaluating this. You can read our write-up on the discussion around this paper [here](https://dataethicsclub.com/write_ups/2023-11-22_writeup.html).

[Dwight Barry](https://www.linkedin.com/in/dwight-barry), co-author of the Perspective paper and checklist, is Principal Data Scientist at Seattle Children’s Hospital. He's kindly taken the time to respond to our discussion with some additional context below, with the final edit overseen by Amy Joint and Huw Day.
```

Thank you for reading and critiquing our paper—I wish I could have been there but 5AM Seattle time was just too early! And thank you for the chance to respond to some of your thoughts. We hear a lot about data/machine learning/AI ethics these days, but what’s often hidden in the
hype is that *every* phase of the data lifecycle—from data capture to database design to analytics to deletion—has an ethical component. To facilitate assessment across such a broad scope, we—the data analysts, data scientists, and data engineers at Seattle Children’s Hospital, along with academic ethicist David Danks, PhD and bioethicist Doug Diekama, MD—created a data ethics checklist to allow for ethical consideration of *any* data product.

This is the permanent short-link to the [checklist](https://is.gd/dataethics). We thought that existing checklists and assessment methods we found in the literature were too long and too detailed to be practical for our day-to-day use of database engineering,
dashboard building, and data science tasks (e.g., predictive modeling, biostatistics, etc.). We also felt that simpler threshold-type approaches wouldn’t allow for nuanced discussion—wewanted something at least a little open ended to facilitate pro/con-type discussions between
the data professionals and the clinical end users of data products, instead of a go/no-go. In instances in our work where this cross-profession discussion has happened because of the checklist, it has been quite successful toward meeting that end.

Unfortunately, we had a very small word count limit for the publication, which severely limited what we could discuss, and we had some editorial/peer-review guidance that asked for our thoughts on the larger picture, which of course precluded more discussion of the checklist itself. We would have liked to go into more detail about each section of the checklist that might help direct future readers, but it just couldn’t fit. Hopefully I can respond to some of the points
you all made to provide a little more clarity.

The questionnaire was designed by David Danks (University of California at San Diego), who was in constant communication and testing with the rest of us, the Seattle Children’s Hospital data professionals. He had the knowledge of the field of data ethics to ensure the major themes were included, while we had the knowledge of how our day-to-day work processes would play out in relation to checklist uses. So it was indeed co-designed with the people who would use it.

The ideas were definitely brand new to some of us, especially those who were surprised to learn that data practices that seemingly did not contain ethical issues (such as database design; [cf](https://doi.org/10.1080/15358593.2021.1934521)) actually *did* contain ethical issues. Honestly, not everyone believed it though, except in cases of clear ethical problems such as disparities analysis or patient privacy—the arguments were either too academic and opaque, or too difficult to parse for those who spoke English as a non-native language. We held several workshops as a combined training for checklist use and a venue to discuss ethical issues in data, but they were voluntary, and mostly only those already convinced of the wide-spread implicit ethical issues in data attended them.

“…is this the most effective critical thinking tool?” No, most definitely not. “The checklist seems more like an opportunity for self-reflection…” Yes, that is indeed the underlying aim. We originally hoped that a “job-aid” might instill more ethical thinking, even amongst the unconvinced, by the process of self- (and team-) reflection.

Topics like missing data and similar problems are indeed ethical problems, but we felt that since there are decent technical answers to those problems, including them would detract from the main intent of (quick) discussion of truly open-ended issues. (GIGO is a well-recited mantra in our work, and we are well aware that many of our data points exist not at random.)

The paper was written and published in the heyday of its initial use here, and it was used in several projects that I am personally aware of or participated in. However, in an anonymous survey to our institution’s data professional community (n~120) soon after its implementation,
several respondents said they saw no usefulness of the checklist and didn’t see using it in their daily activities. Further, in the intervening years, with staff turnover and distance from the original impetus, I have seen it used less and less, and am unaware of any near-recent use of it
(including by myself). What I had hoped would be a panacea was in fact something of a failure.

How do you make “…work being done more ethical overall”? I don’t know. I have read several articles recently about how ethical codes or tools aren’t effective in promoting more ethical
thinking in technical fields ([example](https://doi.org/10.1145/3236024.3264833)). Then what does?? I would love to know what this might be.

Hopefully folks like you all are able to create something that does promote more ethical thinking in industry data contexts. As for me, I think more and more about two elements thatmight work better than a checklist, or definitely better than our checklist: top-down policies
(e.g., requiring an ethical review of any ML/AI model put into production) and working more on the fiduciary idea. While you rightly point out that fiduciary responsibilities are often about
money, they are in fact also about legal (and medical!) responsibilities. I prefer the definition I found [here](https://dictionary.law.com/Default.aspx?selected=744):

  **fiduciary, n.**
  from the Latin fiducia, meaning &quot;trust,&quot; an entity (person, company, etc.) who has the power and obligation to act for another under circumstances which require total trust, good faith, and honesty. 

We are currently working towards establishing top-down policies and requirements for putting models into production, and I imagine we will be able to instill at least some ethical principles in those directives. And I will keep hammering on the fiduciary concept as defined above, because I think it makes a great deal of sense in the medical data context. After all, we are granted
access to databases of incredibly sensitive information on the strong assumption that we will use it to support patient care. Making that assumption explicit I think will be an important next step, alongside formal policies.

On the applied-academic side, we (specifically Seattle Children’s Bioethics Center) are hosting a conference this summer called *Thinking Big, Responding Ethically: Big Data and AI in Pediatrics.* Agenda and details are forthcoming, and will be available at the [webpage](https://www.seattlechildrens.org/research/centers-programs/bioethics/events/pediatric-bioethics-conference/)

Thanks so much for your consideration and critique of our paper, it is so appreciated and welcome—we need much more of your work to move forward in this field!

*Thank you Dwight for this really insightful look behind the curtain of this paper! Intrigued? Us too – you can read more about Dwight’s work [here](https://www.linkedin.com/in/dwight-barry) and can see him speak at the [Pediatrics Bioethics Conference in July](https://www.seattlechildrens.org/research/centers-programs/bioethics/events/pediatric-bioethics-conference/).

This blog has been a first for us in getting to hear an author’s response to a discussion we’ve had on their work, and we’d love to continue this in the future! If we’ve discussed one of your articles and you’d like to take part in a Q&A or present a response, please do get in touch with
us by emailing us: grp-ethicaldatascience@groups.bristol.ac.uk. You can also put forward material to be considered for our reading list [here](https://dataethicsclub.com/reading-list-suggestions.html).*

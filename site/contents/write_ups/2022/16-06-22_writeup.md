# Data Ethics Club: [Automating Inequality](https://www.youtube.com/watch?v=ADYxJU0WyJA)
<!--Please don't edit the info panel below-->


```{admonition} What's this? 
This is summary of Thursday 16th June's Special Data Ethics Club discussion for the JGI's Data Week, where we discussed the video [Automating Inequality](https://www.youtube.com/watch?v=ADYxJU0WyJA) featuring Virginia Eubanks.

The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with the final edit.

```

```{image} ../../../../images/AutomatingIneq.png
:width: 200px
:align: center
:alt: Gru's Plan Meme, "Let the Algorithm decide exam grades" "People won't complain until it affects them" "Even Middle class people are affected". Meme made by Euan Bennet.
```

## Discussion

As part of the Jean Goulding Institute's Data Week conference, we put on a special edition of Data Ethics Club, inviting our usual members as well as anyone attending Data Week to attend. Rather than give reading for the session beforehand, we watched a short video in the session. This video featured Virginia Eubanks talking about some of the ideas in her book (one our favourites here at DEC), Automating Inequality.

In this brief piece, Eubanks brings up some of the more familiar ideas that regular DEC members will be familiar with about automating decision making. Additionally, she touched on ideas about flattening people into data and "maths-washing". We had less time than usual but endeavoured to discuss as many of these ideas as we could.

## What are the pros and cons of automating decisions that affect people’s lives using algorithms compared to having humans make these decisions? 

Pros: 
In theory, automating decisions could reduce administrative load. Government programmes could *in theory* reduce resources spent on this stuff. Automation could reduce workload and streamline services. Take the example of student loan determination - deciding how much money students get. How much work would a single caseworker have to do for each student without some sort of automation? It's just bureaucracy in different forms. Humans reliably produce biases in problematic ways. If (BIG "if") automated decisions have carefully defined definitions of fairness then they could improve these decision making processes. Some things are easy to automate and can save a lot of people's time for more important things.

Cons:
Where do you set the boundaries for data inputs? Humans can widen inputs as they see fit.

People object to disparity between the speed at which decisions are made about them, and the time it takes to object to a decision and appeal. Because "computer says no", but a human needs to take into account additional information that the computer cannot look for (without being told). If automated decisions are made, then there needs to be a streamlined process to object to decisions. This might make people feel a bit better about what's being done to them by automated systems. We felt that automatic the appeal process was *not* the appropriate measure here.

The automated systems often ignore the point of what we're trying to achieve - a system might be designed to reduce government welfare spending rather than actually help people get the support they need. What you optimise for is an important variable to consider?

Choosing what to measure and what not to measure - and also who you can actually get into the data (availability bias) is a big issue. In some of our experience, people often don't consider if the data set is complete or not.

One example of automating decision making is the [UK civil service personel being cut](https://www.civilserviceworld.com/professions/article/reesmogg-sets-out-plans-to-shrink-civil-service-and-get-it-under-control) in favour of [automated decision making](https://www.publictechnology.net/articles/news/rees-mogg-cites-potential-%E2%80%98automation-and-tech%E2%80%99-plans-are-unveiled-axe-91000-officials). If we cut roles in Civil service to save on head counts will this result in codifying bias and inequality? 

When we think about codifying inequality is it that we've removed the humans in the loop? Or is it that the human in the loop will still have prejudice?

Whenever we optimise, we need to consider carefully: what constitutes success? 
To the people who are having decisions made about them, algorithmic decision making might not be success but to those who are trying to cut head count or reduce outgoing costs, it is a success.

It is quicker and cheaper to just give a developer a computer and a piece of paper with the job, rather than co-designing and testing and engaging stakeholders. We don't have an ethics committee in every area trying to automate. People aren't recognizing that the algorithm only reproduces bias though, a lot of people are convinced it improves decision making; specialist in organizational behaviour.

## How can we better listen to the voices of those currently targetted by automated decision algorithms, i.e. primarily people in low rights environments?

The people designing these systems are too focussed on turning the world into a giant game of factorio for themselves. Industry often prioritise profit. Government often prioritise spend less money on disadvantaged individuals. The intersection of these motives inevitably leads to problems for people!

We can't go around asking people "what variables do you want us to use to build an automated system that decides if you're going to lose your job?" It's not just about how difficult people are to reach (e.g. people without an address), it's also their justified mistrust of engaging with people collecting data.

How do people complain against systemic issues? We can complain individually, or write reviews online.

Huw gave outreach talks to some school students, teaching linear models and getting students to design algorithmic decision making systems to evaluate teachers. He was being asked to explain what went wrong with the GSCE results because the students had no one else to challenge. With the school grades debacle, public opinion overturned a terrible decision (eventually). Public outcry only came about in exam results because it affected more people - it affected people who didn't expect to be affected by it.

## Have you previously experienced any examples of “maths washing” of systems and problems addressed by automated systems?

Have we ever maths washed someone? By "maths washing" we essentially mean gloss over an explanation of something technical, potentially in a condescending or patronising manner.

Maths washing is an interesting idea that we hope to discuss further in the future. In the context of algorithmic decision making, it typically comes up where a decision made by an algorithm is questioned (a request to "look under the hood/inside the black box") and that query is dismissed as "you wouldn't understand the complex inner workings of this system". Often times very few people *do* understand these algorithms.

In general, it's very difficult to the get the level of communication just right. Do we hide some details or just not mention it? "Follow the science" is often used to justify any decision. This May devalue people's trust in science if over-used.

"If you're giving a talk to a technical audience, give a non-technical talk. If you're giving a talk to a lay audience, give a really technical talk. Then no one will question you!"

### What are the risks associated with flattening people into data?

We discussed what risks could be associated with “flattening” people’s stories into data and had some ideas about that. Is this always a negative thing? 

A kneejerk reaction is to blanket consider data flattening as always negative. After all, every data point is a person. Every person is more than a data point. Flattening data reduces implicit input from the subjects of your study. 

However, some would argue that the point of data science is to reduce the amount of information in front of you and somehow focus only on something more meaningful. Too much information can often be overwhelming, cumbersone and difficult to interpret. Of course too little information risks drawing conclusions that lack foundation or "significance". 

A key element appears to be advocacy. When we flatten people into data, we mitigate their ability to advocate for themselves. Sometimes the initial data doesn't provide much ability for advocacy, particuarly if it's quantitative the measurement outcomes don't allign with the wants/needs of those being "measured". However, if among those conducting the study are people with values and objectives alligned with those being measured, there is arguably a greater potential to prevent against flattening. A good example of this might be the pharmaceutical industry, in particular pharmaceuticaul review boards. If the role of those on the review board is to ensure all medication meets a certain threshold for promoting health, then at the very least, the medication approved will typically be beneficial to health of those it is perscribed to. Of course, whether or not it's beneficial ot their bank account is another issue.

---

## Attendees

__Name, Role, Affiliation, Where to find you, Emoji to describe your day__
- Natalie Zelenka, Data Scientist, University of Bristol, [NatalieThurlby](https://github.com/NatalieThurlby/), [@StatalieT](https://twitter.com/StatalieT) 
- Nina Di Cara, PhD Student, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Euan Bennet, Senior Research Associate, University of Bristol, [@DrEuanBennet](https://twitter.com/DrEuanBennet)
- Vanessa Hanschke, PhD Student, University of Bristol
- [Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/), Citizen Developer, Australian Public Service, Brisbane

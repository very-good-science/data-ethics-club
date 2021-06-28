# Data Ethics Club discussion: [We created poverty. Algorithms won't make that go away](https://www.theguardian.com/commentisfree/2018/may/13/we-created-poverty-algorithms-wont-make-that-go-away)

```{admonition} What is this? 

This is summary of Wednesday 28th April’s Data Ethics Club discussion, where we spoke and wrote about the piece ["We created poverty. Algorithms won't make that go away" ](https://www.theguardian.com/commentisfree/2018/may/13/we-created-poverty-algorithms-wont-make-that-go-away), which is an article written by Virginia Eubanks, author of "Automating Inequality". As one of the attendees pointed out, the article was in some senses a summary of some of the ideas from the book, which comes highly recommended!

The summary was written by Huw Day, who tried to synthesise everyone’s contributions to this document and the discussion. “We” = “someone at Data Ethics Club”.
```

## Summary

Algorithms are being deployed to decide who can access scarce public resources.

We are constantly making personal decisions about resource allocation - do you deserve takeout tonight? 
A day off next week? 
A holiday this year? 
In doing so, we consider available resources (both our own and those of others), expected payoff and how deserving we are. 
No algorithm required. 

Are algorithms just shields for people to hide behind?
When used in that way, is AI decision-making fundamentally different to using people or government departments as the scapegoat for failures instead? 

You can’t fix the problem of not enough resources with distributing those resources more “efficiently”, but does that mean you shouldn’t try?

## Intro

In [this piece from The Guardian](https://www.theguardian.com/commentisfree/2018/may/13/we-created-poverty-algorithms-wont-make-that-go-away), Virgina Eubanks shares her experiences of travelling the United States to study and write about the impact of hi-tech tools on public service programs. 
She notes: "We are increasingly turning to digital tools to rank and rate which struggling families most deserve support." 

Since the ethical dilemmas are plentiful when attempting to share out insufficient resources among many needing and deserving causes, someone has to make the difficult decision as to what (and perhaps more crucially, who) constitutes a more or less "deserving" cause. 
As Eubanks puts it, this task is of ranking deservingness is being outsourced to algorithms because "humans know better". 
Deceptively though, this means that whoever designs the algorithms gets to decide what the metrics are for "deservingness" - and surely they should know better?

## How deserving of help are we? Is this a reasonable question (or is it just uncomfortable)?

We can all understand the potential benefit of efficiency in decision-making.
However, it's one thing to optimise the distribution of sufficient resources, and another to allocate insufficient resources to the most "deserving" cause.

Any form of optimising requires choosing parameters to optimise and this evaluation will inevitably be done from an outsider's perspective. 
If we put these optimisation decisions in the hands of technology, we need to ask if they are effective in reducing harm. 
If they are ineffective, then it adds insult to injury because in addition to making the situation worse, you're paying for it.

Meritocracy is often a story the successful tell about themselves, forgetting their starting advantages and luck along the way. 
In contrast, blame is placed on the unsuccessful for perceived "failure". 
This means "deservingness" may be exactly the wrong lens to look through.

## In projects that involve direct impacts on people's lives, does everything need to be automated and optimised?

When resources are inadequate, inefficient distribution of what resources there are is unlikely to help persuade politicians or other decision makers to increase the resources. 
This decreases the opportunity for creative solutions that are not accounted for in the parameters. 
Applying an algorithmic solution to a resource management problem has the external appearance of a "fix" whilst hiding the fact that the best "fix" is to have more resources. 

If you have three people and two chairs, you can run a complex algorithm to decide who is most deserving of a seat at the table based on medical historical, gym memberships and perhaps how altrusistic each person is. Or you could just get a third chair? 

However, these impossible decisions about resource allocation are the day-to-day reality of many public sector services and local government.  
As a result they are continually being pitched software solutions to "smartify" certain processes by tech companies coming from the outside and not understanding how local government works. 
These can be very expensive and well-marketed but unless their resource saving utility over the original system exceeds the costs of implementation, you are inevitably making a loss in the short term and reducing your already inadequate resources.

Algorithmic decision making is not all bad news. Consider the issue of food waste; automation and optimisation could do a great deal of good there. 
But do these optimisations give us a free ride to avoid looking at other deeper issues e.g. dumpster locking/participation? 
Algorithms can't fix everything, but sometimes it is possible that they can ensure the most vulnerable get more help they would get from human decisions.
If there isn't a third chair and an algorithm can make a fairer choice than a human, perhaps algorithms have their place in decision-making after all.
Crucially, it is often unclear which situation we are in.

Even if we were to know that the resources are being more efficiently allocated on average, we also want to ensure that they are not benefiting certain groups over others.

There is also a distinction to be made between "automated" and "digital". 
Automating a task to free up resources can often be more cost effective than getting a person to do it, but potentially at the cost of taking a vital input of human empathy out of the decision making. 
Digitising a process is simply moving from information into a form that can be read, stored and processed by a computer. 
Digitising a task both increases the scope of automation but also potentially allows a human decision maker to more easily consider all the variables at play in their decisions.

In general, we need more empathy in our decision making and should not forget to be human when that's the better answer to the challenges we face. 

## In what ways can data scientists positively contribute fair algorithmic decision-making?

Often data scientists choose to work on areas like poverty because they want to use their technical skills to help.
However, doing that alone could cause more harm than good.

It's not possible to "outsource our ethical choices to machines", because machines can't make ethical choices, the ethical choices are made by the humans in the way they implement system. 
This means we must take responsibility for these choices as we make them. 
Similarly, we should do what we can to ensure anyone who uses our code understands that they take on the responsibility for how it is deployed.

There's a sense in the article that technology becomes a solution to cowardice: "The goal of automated decision-making, they told me is... also to help make the heartbreaking choices of whom among the most exploited and marginalized people in the United States will get help." 
Decision makers are avoiding hard decisions in considering issues like job applications, austerity measures etc. 
Rather than dealing with the lack of resources head on, they circumvent dealing with the issue head on in a manner which will actually propogate the issue.

Data scientists can contribute by advocating for "non-technical" forms of knowledge (e.g. from the user-centred research).
Communicating the limits of their work can also help to ensure that data science is used to assist human case workers rather than replace them and/or to simply allocate more resources to the situation, where appropriate.

## Closing thoughts

We don't want to make difficult decisions, so it's easier to pass that decision to an algorithm who can take the blame, but you can't apply software fixes for hardware problems. 
The feeling is that we are generally pessimitic about what you can do to do good with algorithms, although there is potential scope for good.

Making arguments against optimisation wasn't the point of the article or our discussion - data scientists decide what to optimise for, and in what context. 
Is it so bad to optimise things that will help people (such as who is most likely to surive a kidney transplant)? 
Algorithms can add value in certain settings and data scientists could help optimise certain outcomes.

But it it can be difficult decide how "deserving" people are of help, and even to decide if "deservingness" is the correct metric to try to use. 
If you automate a problem, you often won't get creative solutions so whilst optimisation is useful, you have to marry it with strong policy proposals. 

In order to help, we constantly need to be ethically reviewing our approaches - this can be difficult if you're the sole data scientist in your context. 
Constantly discussing these ideas with peers and colleagues is a great way to get this process of self evaluation going and our best bet to apply algorithms more ethically. 
This is the best way to avoid making poorer/marginalised people the "guinea pigs" for the algorithms of the future.

## Voting 
Our vote for the next meeting was to discuss: 

[Critical Perspectives on Computer Vision](https://slideslive.com/38923500/critical-perspectives-on-computer-vision) - a ~20 minute video about image recognition/categorisation by Emily Denton, a Senior Research Scientist on Google’s Ethical AI team

and save these two for another time:

[Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/pdf/1607.06520.pdf) - paper about how to make word embeddings in language models less biased

[A manifesto for big team science](https://psyarxiv.com/2mdxh/) - preprint about barriers to doing science as a team (based in psychology)

Our members also said:
- 100% (12 people) that the content this week sparked interesting discussion.
- 92% (11 people) said that they'd recommend that others read the content.

## Contributors:

```{admonition} Who contributed?
:class: tip
This is the list of contributors who were comfortable sharing their names publicly.
```

- Natalie Thurlby, Data Scientist, University of Bristol, [NatalieThurlby](https://github.com/NatalieThurlby/), [@StatalieT](https://twitter.com/StatalieT), :sun_with_face: 
- Nina Di Cara, PhD Student, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara), :writing_hand:
- Huw Day, Maths PhDoer, Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Robin Dasler, data product manager on hiatus, [github:daslerr](https://github.com/daslerr)
- Paul Lee, investor, @pclee27 www.senseoffairness.blog
- Kamilla Wells, Citizen Developer, Australia [Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/)
- Miranda Mowbray, honorary lecturer, University of Bristol, mirandamowbray on LinkedIn 
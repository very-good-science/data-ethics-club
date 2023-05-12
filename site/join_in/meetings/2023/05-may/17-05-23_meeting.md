# Data Ethics Club meeting [17-05-23, 1pm UK time][timedate]

<!-- 
TODO:
- [ ] Change to a new branch (DD-MM-YY_meeting)
- [ ] Copy this template to meetings/YEAR/DD-MM-YY_meeting.md (put in actual year + date)
- [ ] Put in the Event time on: https://www.timeanddate.com/worldclock/fixedform.html and copy result to LINK-TO-TIMEDATE
- [ ] Change all ALL-CAPS placeholders in this form
- [ ] Update the hyperlinks at the bottom of the template
- [ ] Add link to the new file in meetings.md
- [ ] Update the next-meeting.md file
- [ ] Pull request!
- [ ] Create or edit the calendar invite to copy and paste this info over and send it/send an update.
- [ ] Maybe tweet it? #DataEthicsClub @jgiBristol

Repeat meeting link is currently: https://bristol-ac-uk.zoom.us/j/94475153265


Usual time 13:00-14:00
-->
## Meeting info

### Quick links

[Zoom link][zoom]

Link to content: [Designing Accountable Systems][content]

### Description 

You're welcome to join us for our next Data Ethics Club meeting on [17th May at 1pm UK time][timedate]. 
You don't need to register, just pop in. 
This time we're going to watch/read [Designing Accountable Systems][content] by Kacianka and Pretschner, which is a paper about how we can analyse accountability in technical systems.

**Brief summary of the paper**  

There are many different definitions of accountability. Some of these come from computer science, but earlier definitions are from more philosophical fields. 
A recent review has found the most common type of accountability in algorithmic accountability studies is the one given by Mark Boven which states that: 
(1) There is a relationship between an actor and a forum  
(2) in which the actor is obliged  
(3) to explain and justify  
(4) his conduct,  
(5) the forum can pose questions,  
(6) pass judgement,  
(7) and the actor may face consequences [6, p. 12].  

There was a time when there was an emphasis on transparency of systems for accountability, but this is not sufficient if humans cannot understand the system, even if they can view it.
"Miller [35] gives the example of a machine learning classifier that categorized an insect as a spider or a beetle. An explanation it would give is that a result is categorizes as a spider because it has eight legs instead of six. In contrast to the weights in a neural net or the layout of a decision tree, such an explanation would be useful and understandable for a human." 

The authors then argue that causality is a necessity for accountability, and so being able to define causality in a system is very important. 
Causality is often modelled using diagrams, and it is important to note that causal relationships have more requirements that correlations. 
For example:  
- Texting <-> Accidents (Correlation)  
- Texting -> Accidents (Texting suspected as the cause)  
- Testing -> Distraction -> Accidents (The actual mechanism is identified)

The paper goes on to explain that these models can be used with technical systems, and give definitions of the concepts 'cause', 'blame', 'responsibility', 'transparency' and 'accountability'. 
It then describes how causal models can be used to map accountability in systems (which actions performed by which 'agents' lead to a given outcome), and that this mapping may depend on which definition of accountability you want to use. 
An important concept is also counter-factuals which ask, if this part of the system had behaved in the opposite/different way, would the outcome be altered? If not, they cannot be causally responsible. 
Different approaches may also be needed to design a system so there is clear causality (which is called type causality), versus analysing an event that has already happened (called actual causality). 

They give the example of the relatively infamous Uber crash in 2018. "Ms. Herzberg was pushing a bicycle while crossing a dimly lit road and the software of the car repeatedly misclassified her, ultimately hitting and killing her. The safety driver on board the vehicle was distracted and did not brake in time."

We can consider that neither Uber nor the driver, nor Volvo tried to change the trajectory, therefore the car crashed into the pedestrian.
And then test what happens if any of these (Uber, Volvo, the driver) made evasive manouvers using the causal diagram they have built (see the paper).
This depends on the model of causality we are working with - if the model allows for no human intervention, even if the driver did act to avoid the crash, the causal system states that the crash would still have happened, and so we can say that the driver cannot be held accountable. 

In conclusion they say that "while SCMs are not sufficient to ensure accountability, a correct understanding of the underlying causal mechanisms is necessary for any notion of accountability... SCMs are a powerful tool to analyze systems and, if they are not accountable, provide a well-reasoned argument why this is the case, and how the system should be improved."

*Note for references mentioned here, please refer to the paper link*

### Discussion points

There will be time to talk about whatever we like, relating to the paper, but here are some specific questions to think about while you're reading.
- How does this paper fit into your existing understanding and beliefs about what accountability should look like?
- What did you think about being about to have different definitions of accountability that might imply different outcomes about who/what is accountable?
- Do you agree that an understanding of causality is necessary for accountability? Are the instances where this isn't the case?

---

<!--

## Meeting notes

### Who came
Number of people:

### What did we think?
Notes here!
Shall we email the author? If so, who'll send the email?

-->

[timedate]: https://www.timeanddate.com/worldclock/fixedtime.html?msg=Data+Ethics+Club&iso=20230517T13&p1=299&ah=1
[content]: https://arxiv.org/pdf/2101.08102.pdf  
[zoom]: https://bristol-ac-uk.zoom.us/j/94475153265  

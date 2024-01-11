# Data Ethics Club meeting [06-12-23, 1pm UK time][timedate]

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

Link to content: [Anatomy of an AI-Powered Malicious Social Botnet][content]

### Description
You're welcome to join us for our next Data Ethics Club meeting on [Wednesday 6th December at 1pm UK time][timedate]. 
You don't need to register, just pop in. 

This time we're going to watch/read [Anatomy of an AI-Powered Malicious Social Botnet][content] by Yang and Menczer, which is a case study about a network of bots deployed on Twitter that used ChatGPT to generate realistic-looking content. It is a pre-print available on ArXiv, posted in July 2023. 
This piece is fairly long, so we would recommend focusing on sections 1-3 and the discussion in section 6 if you are pressed for time and/or reading our summary below.

In the paper, the authors argue that LLMs pose a new cyber-social threat because (1) they generate text, which is more convincingly human than traditional text generation methods and (2) because they are affordable and readily accessible though APIs. Therefore, they are likely to be employed for scams and for mis-/disinformation. Current methods to detect LLM-generated content have so far not proven to be reliable. When LLM technology meets social media bots they have the potential to cause even more havoc. These bots imitate human social media users, by displaying fake profiles, posting content and engaging with users by following, liking or retweeting.

The authors identified a network of such bots they call *fox 8* by manually looking for tweets which seemingly unintentionally revealed that they were ChatGPT responses. For example, when ChatGPT is faced with a request for something outside its capabilities or against OpenAI policies, it may reply "I'm sorry but as an AI language model I cannot browse Twitter and access specific tweets to provide replies".
By searching the phrase “as an ai language model” and manually annotating the tweets, the authors came across a network of twitter users that were closely connected through interacting with each other and consistently posting the same content about cryptocurrencies and blockchain. The three main websites they promote are suspicious in many ways, for example they present themselves as news publishers, but have neither original content nor an editorial team and are full of pop-ups suggesting to install software.
 
Finally, the authors examine different ways of using LLM detectors to automatically identify bots. They find none of the methods to be fit for purpose, as current detectors are unreliable for short texts and show a high false positive rate. The authors conclude with a calll for more effective detection methods, regulation specific to LLMs in bots and raising public awareness.

### Discussion points

There will be time to talk about whatever we like, relating to the paper, but here are some specific questions to think about while you're reading.
- Have you interacted with bots in the past or do they play a part in your social media consumption? What were your experiences?
- Do you think LLMs will exacerbate misinformation on social media in particular or the internet in general? What do you think the Internet will look like in 5 years time if/when LLM use becomes mainstream?
- The authors call for more LLM detection methods, regulation and public awareness. What do you think needs to be put in place against social media bots? Whose responsibility is this?

---

<!--

## Meeting notes

### Who came
Number of people:

### What did we think?
Notes here!
Shall we email the author? If so, who'll send the email?

-->

[timedate]: https://www.timeanddate.com/worldclock/fixedtime.html?msg=Data+Ethics+Club&iso=20231206T13&p1=299&ah=1
[content]: https://arxiv.org/pdf/2307.16336.pdf  
[zoom]: https://bristol-ac-uk.zoom.us/j/94475153265  

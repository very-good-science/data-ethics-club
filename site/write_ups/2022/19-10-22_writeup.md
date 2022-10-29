# Data Ethics Club: [Patient and public involvement to build trust in artificial intelligence: A framework, tools, and case studies](https://www.sciencedirect.com/science/article/pii/S2666389922000988)
<!--Please don't edit the info panel below-->

```{admonition} What's this? 
This is summary of Wednesday 19th October's Data Ethics Club discussion, where we spoke [Patient and public involvement to build trust in artificial intelligence: A framework, tools, and case studies](https://www.sciencedirect.com/science/article/pii/S2666389922000988), 
a paper written by Soumya Banerjee, Phil Alsop, Linda Jones and Rudolf N. Cardinal.

The summary was written by Huw Day, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Nina Di Cara and Natalie Thurlby helped with the final edit.
```

## Introduction

```{image} images/RAG.png
:width: 200px
:align: center
:alt: Drake Meme. Drake doesn't like "Generic consent form to use people's health data in ways they don't understand." Drake does like "Use well informed research advisory groups to allow participants to understand and inform how their data is used." Meme made by Huw Day.
```

## Do you agree that it is important to increase public and patient trust in AI?

Many of us said yes. It's easier to say that we should do this, but harder to implement it in practise.

People often don't trust AI (or automated systems in general) because they don't trust the people behind the scenes. If people trust organisations, they are more likely to trust plans to do things with their data. Terminology is an issue and we need to get understanding across to people.

It's quite hard to make trust out of thin air. It can sometimes come across as manipulative. Perhaps instead of trust we want more education and understanding.

There's a clear conflict of interest between the data scientist being the same people explaining stuff to the patients. Good general start but there's a conflict of interest there that would need to be addressed in a more systematic setting. It's more democratic than most research. But they didn't bring anyone in until they had their research questions. They should have asked the patients questions, but potentially quite hard for them to vocalise. But individuals don't have the birds eye view that the data scientists.

Just because something is trusted, doesn't mean it's trustworthy. Maybe we'd want to talk less about trust and more about understanding.

We don't know how much trust there currently is, because how much do people think about what their data is used for?

Many of us don't trust big tech solutions now, but when did we. In the 1950s/1960s trust was asserted but not necessarily clear - trust was perhaps taken rather than given.

If their doctors trust a new tech and recommend it, patients are more likely to go for it. But for clinicians, they're less like to recommend a tool. They're more likely to recommend something that is a supplementary tool than a replacement treatment to the norm.

Ethics committees considering drugs untested on pregnant women gave rise to real concerns. AI is sci-fi to many and so awakens peoples' doubts and worries. We need to get beyond that immediate negativity if trust is to succeed.

In Australia every time you have a procedure you have an opt-out from your results being included in data aggregation. In the UK most people probably just think of some big scandals involving massive costs and attempts to integrate data. 

If you want participants involved with data that requires you to be in a trusted research environment, then it'll be very unlikely that you'll be able to share all the stages of research with the patients, e.g. data analysis.

The study is a bit of a role model for others - this sort of patient participation is exactly what's needed if we are going to implement AI stuff in healthcare.

## When should we let automated systems make these decisions for us?

As Kamilla put it "if you're using an AI model for treating my kidney problem, I want to trust *that* model - I don't really care about the Terminator coming in."

If you know that an unintelligible black box model performs better, but can't explain it to a patient that it's better than a more explainable model, then what's the best approach?

Why not run both? White box and black box. Many feel the bottom line is that a human should always be deciding. If you have a doctor reviewing results, the human interaction adds an extra layer - the doctor might not trust the models and that would affect their interpretation. Can we build an external validation process for this?

Is applying these models actually useful? What do we gain by implementing them? It turns out - yes they are! Computer systems are better at reading x-rays/scans than humans. e.g. Blood testing machines feed results to a model that then lists recommended treatment (e.g. medicine dosages, or blood product suggestions).

There are specific quality assurance processes that can be applied to software-as-medical-device. e.g. [FDA proposal for SAMD](https://www.fda.gov/media/122535/download)

The co-design model is great, but the software developers/data scientists have the responsibility to establish a review procedure, test the outputs to make sure everything is properly validated, but then continue to review periodically. Leaving a model/AI to run on its own without review can quickly go wrong and have big impacts 

Kamilla is working on how to do this for social decision making (e.g. judges in court) #shamelessplug [#ILPC2022](https://www.ials.sas.ac.uk/events/event/25893).

Legal precedent supercedes the models, dictating acceptable thresholds. If the model outputs are past those thresholds, an exception needs to be flagged... but as always - a human gets to make the final decision!

## What would you consider good evidence that research advisory groups are successful in their aims of more ethical and/or trustworthy research?

The paper doesn't show a lot of evidence that it's working, even if we liked the paper. But what would good evidence look like to us?

Could we adopt this program elsewhere? Is there any repeatability? But we still need to be nuanced on how to measure success? If a study is capable of being reproduced at a later stage, that might amount to good evidence of success. Confidence is never universal and isn't representative of the public.

You can ask patients to demonstrate understanding. "We showed you this earlier, now we're showing you this. What do you find easier to understand?" Maybe getting them to explain it to a different patient so you can measure outreach. It's quite intensive and only had 6 patients, so best case scenario it's still just a drop in the ocean.

Do the Research Advisory Groups (RAG) only deliver confidence for the individuals who have participated in the process? Some of us felt this type of study can only really be a success if it increases confidence among the broader patient community, not just those directly involved.

Informed consent as a model perhaps for assessment as to whether patients agree for their data to be included in the processes. 

Is there increased trust? A better patient experience?

Having patients living with conditions being able to feed experiences directly to researchers and healthcare providers is hugely useful - many patients find that they know more about doctors about their conditions (because living with it tells you far more than any other way to learn about something) - maybe the research groups of patients engaging with researchers should be the norm for everything.

Nina gave an example about trying to study children in care after they've left the system. It's tricky to get everyone on board (and get funding without being able to get in touch with people first).

Pharmaceutical trials sometimes have reporting systems in place to report problems with models for example.

Do we want approval or trust from patients? These are two slightly different things. Perhaps we need understanding, then we can understand why we don't sometimes get approval and what methods can we use that get approval.

As long as the patients get to decide for themselves (which seem to be what the authors were encouraging), that's the priority, with the long term goal to get rid of misconceptions about AI.

## Is there anything that you think research advisory groups should not have a say in? Or anything that they don’t have a say in that you think they should?

Is it too early? Do we know the right questions to ask patients? Should the RAG patients be co-authors on the paper? As much as possible without compromising patient confidentiality?

Does it depend on the views of the patients - should more sceptical patients get more information to help convince them it's trustworthy?

There's a risk of overwhelming the patients with information. Are we going to give the patients their medicine plus homework?

To what extent do the patients have veto power? Can't they just ask another group of 5 people until they get approval? It's unclear how much their current say actually matter. In product development, the veto can be a setback to product development because things would be less likely to sell. Take what they don't like on board and go back.

The power dynamic comes into it a lot. Are you just asking the patient or are you asking them with a doctor present? How might they be influenced? Should you ask patients their views on various stakeholders? 

We would need to make sure our selection of participants was as broad as possible, including considering cultural background, any cognitive impairments or mental health backgrounds. The paper did a good job of addressing this (e.g. with bipolar people). In all cases there seemed to be a high level of trust between doctor and patients.

How do we reach people who are distrusting of doctors? If you're going to volunteer for this, then you're probably not going to be someone who trusts your doctor.

---

## Attendees

__Name, Role, Affiliation, Where to find you, Emoji to describe your day__
- Natalie Zelenka, Data Scientist, University of Bristol, [NatalieZelenka](https://github.com/NatalieZelenka/), [@NatZelenka](https://twitter.com/NatZelenka) 
- Nina Di Cara, Research Associate, University of Bristol, [ninadicara](https://github.com/ninadicara/), [@ninadicara](https://twitter.com/ninadicara)
- Huw Day, PhDoer, University of Bristol, [@disco_huw](https://twitter.com/disco_huw)
- Euan Bennet, Lecturer, University of Glasgow, [@DrEuanBennet](https://twitter.com/DrEuanBennet)
- Zoë Turner, Data Scientist, NOttinghamshire Healthcare NHS Foundation Trust [@Letxuga007](https://twitter.com/Letxuga007)
- Paul Lee, investor
- Helen Sheehan, PhD Student, University of Bristol
-[Kamilla Wells](https://www.linkedin.com/in/kamilla-wells/), Citizen Developer, Brisbane

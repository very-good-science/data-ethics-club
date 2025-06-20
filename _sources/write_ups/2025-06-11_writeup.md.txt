---
blogpost: true
date: June 11th, 2025
author: Jessica Woodgate
category: Bookclub
tags: predictive AI, LLMs, generative AI, hype
---

# Data Ethics Club: [AI Snake Oil](https://www.aisnakeoil.com/) Book Club: [Chapter 1 – Introduction](https://press.princeton.edu/books/hardcover/9780691249131/ai-snake-oil#preview)

```{admonition} What's this? 
This is summary of Wednesday 11th June’s Data Ethics Club discussion, where we spoke and wrote about the [AI Snake Oil](https://www.aisnakeoil.com/) Chapter 1 – [Introduction](https://press.princeton.edu/books/hardcover/9780691249131/ai-snake-oil#preview) by Arvind Narayanan and Sayash Kapoor.
The summary was written by Jessica Woodgate, who tried to synthesise everyone's contributions to this document and the discussion. "We" = "someone at Data Ethics Club". 
Huw Day helped with the final edit.
```

## Chapter Summary

The term “AI” has been appropriated for a multitude of different technologies and applications, confusing discussions about its strengths and limitations, and misleading people about its capabilities. The introduction begins by distinguishing between generative AI, which produces various types of content such as text or images, and predictive AI, which produces outputs forecasting the future to inform decision-making in the present. 

The waters surrounding the definition of AI are muddied; influenced by historical usage, marketing, and more. Some problems AI attempts to address, like vacuuming, are solvable; others, like predicting whether someone will commit a crime, are not. Some applications were once thought difficult, but AI has proven to be very good at, such as facial recognition. However, even if the mechanism is good, the tool can fail in practice, e.g., if the data is noisy, biased, or abused for malicious intent.

Sold as an accurate and capable technology, predictive AI has been widely adopted. However, there are significant issues with the premises predictive AI is based on, as it attempts to translate and reduce high dimensional phenomena to computationally feasible outputs. In practice, there is missing data, bias, and participants attempting to game the system. Generative AI, the chapter argues, holds more promise and yet also runs into significant issues. Factual inaccuracies in outputs are common, leading to rampant misuse such as error-filled news articles or AI-generated books. 

Misinformation, misunderstandings, and mythology about AI are fed by a combination of researchers, companies, and the media. In research, the buzzier the research topic, the worse the quality of research tends to be. Companies feed off of hype, seeking to maximise profits whilst rarely being transparent about the accuracy of their products. Crumbling revenue in the media combined with access journalism, where outlets rely on good relationships with companies to be able to interview subjects, further propagate hype narratives dictated by AI companies. 

The limitations, hype, and misconceptions surrounding AI leads the chapter to analogise AI as a “snake oil” product: a miracle cure advertised under false pretences. The book aims to identify AI snake oil – AI that does not and cannot work.

## Discussion Summary

## What do “easy” and “hard” mean in the context of AI? Does it refer to computational requirements, or the human effort needed to build AI to perform a task, or something else? And what does easy/hard for people mean?

The idea of “easy” or “hard” problems for AI weren’t specifically defined in the chapter, but it did give some examples of problems previously thought to be difficult for AI which the technology is now very capable of solving, such as image classification. Spellcheck is another example of an application previously thought to be hard but is today so embedded in our everyday lives that we might not even think of it as AI.

Sometimes what is “easy” or “hard” for AI is contrary to what is easy or hard for humans – a phenomenon coined [Moravec’s paradox](https://en.m.wikipedia.org/wiki/Moravec%27s_paradox). Moravec’s paradox is the observation that reasoning (which is difficult for humans) requires little computation, but sensory and perception skills (which are easy for humans) are highly computationally expensive. [Computational complexity](https://en.m.wikipedia.org/wiki/Computational_complexity) is a well-studied field examining the amount of resources required to run an algorithm. We wondered if easy and hard in relation to AI are somehow related to how difficult it is for AI to produce an accurate output.

Tasks that are easy for humans are those that we can do quickly and without much concentration. Pinpointing what these tasks are is tricky; we don’t know what we know. People aren’t good at breaking tasks down into smaller levels than humans are typically used to or deducing which of these tasks are easy. The difficulty with breaking down tasks is why some people find programming really tricky. What counts as easy might depend on the sample population, e.g., a roomful of mechanics will find it much easier to replace an engine than a roomful of mathematicians.

Discerning what is easy or hard for AI is not straightforward, as it depends on the lens you examine the tool through and the context it is situated within. LLMs now seem to be very good at predicting text, giving the impression that the task is easy. However, an extraordinary amount of resources goes into training an LLM, suggesting it is actually a hard problem. Facial recognition is accurate under the right conditions, but there are many drawbacks for how it is used, making it hard to delineate appropriate use cases. Perhaps easy and hard aren’t the right terms; we should instead be asking how much context is needed to solve the problem, and how hard the execution is.

The underlying message of the introduction is that certain tasks are made easier or harder from the application of certain AI systems, and the way we sell those systems affects how they are used. For example, linear regression is really good at some statistical modelling problems. However, if we sold it as a silver bullet to solve any problem, it would be (and, as the chapter demonstrates, has proven to be) rubbish.

The barriers to entry for AI have been drastically lowered over recent years. On the deployment side, LLMs are now very easy to set up on a personal laptop. On the user side, generative AI interfaces are widely accessible. It is actually starting to require more effort *not* to use LLMs in some settings such as [searching](https://www.bbc.com/news/articles/cpw77qwd117o), where search engines are displaying an “AI overview” before presenting the results. Tasks that LLMs previously found difficult are slowly getting easier and easier, making their deployment and user friendliness increasingly accessible. For example, maintaining context over time was something that LLMs previously found very difficult. 

However, the [context window](https://www.techtarget.com/whatis/definition/context-window), which dictates how much input the LLM can consider when calculating its output, is slowly getting larger. A larger context window entails that an LLM can consider more information in its answers. In addition, ChatGPT now incorporates some [“memory” functionality](https://openai.com/index/memory-and-new-controls-for-chatgpt/), where information from previous conversations is maintained. However, sometimes relevant context goes beyond conversations, such as body language. This raises important questions about what kind and how much information goes into the model, e.g. whether it should consider current affairs or interpersonal relationships.

More data and computational power could mean that AI gets better, but this is not always true. It may depend on the use case and type of AI. For example, given enough training, AI can beat the best human chess player, but how long will it be before AI can make a cup of tea to your preferences, and is more computational power enough to solve this? If the task is something that the user doesn’t know much about, or is difficult to express, the usefulness of AI goes down. Training and human feedback is required on both sides. It is difficult to know where the improvements will stop or how the evolution of AI will unfold, especially considering the transformative effect of previous industrial revolutions.

## Based on your definitions of these terms, pick a variety of tasks and try to place them on a 2-dimensional spectrum where the axes represent people’s and computers’ ease of performing the task. What sort of relationship do you see?

| Difficulty  | Computer | Human | Both |
|----|----|----|----|
|  EASY | Coding | Sense of right and wrong   | Image classification |
|   |  Pattern recognition in big sets of data |  Ironing  |  Speech to text |
|  |  Analytical decision-making (depending on algorithm and input data) |  |  |
|  | Chess |  |  |
|  | Remembering lots of information |  |  |
|  | Recall (for some computers but difficult for LLMs) |  |  |
|  | Writing a poem in a certain style  |  |  |
|  | Sucking in created content  |  |  |
|  HARD | Ironing | Coding | Creativity |
|  |  Ethical decisions / judicial |  Content creation |  Reading emotions |
|  |  Holding/understanding context |  |  |
|  |  Sarcasm/jokes |  |  |
|  |  Moving around in a new environment |  |  |
|  |  Certainty of answers |  |  |
|  |  Language manipulation |  |  |
|  |  [Counting “r’s” in the word “strawberry”](https://www.youtube.com/watch?v=FAspMnu4Rt0) |  |  |

## The text gives many examples of AI that quietly work well, like spellcheck. Can you think of other examples? What do you think are examples of tasks that AI can’t yet perform reliably but one day will, without raising ethical concerns or leading to societal disruption?

Applications of AI that we could envision being less ethically concerning include scientific pursuits, such as animal conservation for tracking animals, biodiversity monitoring, birdsong recognition, weather prediction, pollution analysis, or finding biomarkers for diseases. These use cases do not directly dictate outcomes for people’s lives and can be verified by complementary scientific methods.

With respect to AI being used in everyday life, AI should act as a facilitator for human flourishing, rather than a supplement. We would much rather have AI do our laundry whilst we make art, rather than have AI generate “art” whilst we do laundry. If ChatGPT was reliably accurate, we could imagine it being useful as a learning tool e.g. by quizzing students on their homework. Tools like Grammarly are great in certain contexts, because native English speakers can be harsh when assessing people’s writing. When people don’t have English as a first language, grammar correcting tools can help them to be sure they are saying the right things. 

There are many AI tools we use every day without noticing, but that does not mean that they are working well. Spellcheck is integrated in many applications, however, we do not think it works well. If you write in more than one language, it falls apart and doesn’t understand what context it’s in. We tend to have counterintuitive expectations of the abilities of these tools; we recently encountered someone praising ChatGPT for being helpful with writing code about 60% of the time. If someone was asking us for help, and we were getting it wrong 40% of the time, we would not expect them to ask us for help again.

We would be hard pushed to find an AI tool that won’t raise ethical concerns or cause some disruption. If something could replace a job, it could cause disruption. There are lots of areas in which people don’t care how good the labour is, they just want an output – even if it’s inaccurate generative AI nonsense. Even seemingly innocuous applications like spellcheck or Grammarly have rippling implications, e.g. for students. We have experienced spellcheck changing our answers leading to a quiz fail. If students can use something to do their work, it affects the work of teachers.

Once a tool can provide an answer it would take a human a while to come up with, it is easy to slip into [cognitive offloading](www.mdpi.com/2075-4698/15/1/6). We’ve noticed that tools like Grammarly are now pitched at native English speakers, potentially discouraging them from improving their own grammatical abilities. Lots of native English speakers who should already have these skills will defer to grammar checking tools, assuming that the tools will be better. People have [authority bias](https://thedecisionlab.com/biases/authority-bias), doubting their own knowledge because the tool has told them something different. 

The disruptive potential of AI may depend on the application and sensitivity of the data. It is important to take into account the whole pipeline, considering not just what the tool does but the energy it consumes and where the data used to train it comes from.

## What change would you like to see on the basis of this piece? Who has the power to make that change?

Careful consideration of our attitudes towards AI is crucial in shaping the role it plays in our lives. It is difficult to maintain healthy scepticism of AI in the face of overwhelming hype. In general, the chapter sets a good tone, balancing criticisms with an awareness of potential benefits. Some of us have come to the book with a pro-AI attitude, looking to engage with it as a challenging view. Predictive and generative AI have beneficial use cases, e.g., generative AI can help people get started with a prototype for an idea even if they don’t know how to code. Others among us are looking to ask whether these benefits are worth the costs.

Some of us are becoming increasingly hardline anti-AI, finding that the chapter doesn’t go in as hard as it could (or maybe should) against AI. The chapter focuses, rightly, more on predictive AI, but it could have been more critical of generative AI. Fundamentally, many of us believe generative AI cannot do anything new. The outputs might be useful but are fundamentally unreliable in the sense that there is no validation of their correctness. The chapter talks about how “facial recognition works well enough to be harmful, and badly enough to be harmful” – this probably applies to LLMs as well.

To highlight the problems with applying AI, we considered the difference between using facial recognition to block someone from attending an event, and having a bouncer at the door with a list of people not allowed in. The difference may lie with accountability; you can argue with a person or ask them to take action, but with an automated system you will get nowhere. A person might lose their job if they do it incorrectly; if a system makes a mistake, it does not pay for the consequences, and the costs of rollback are often too high to warrant a system change. A human security guard can’t be scaled up to surveil 100,000 people at once and get 5% wrong with no recourse.

Distinguishing between the technology itself and the people behind it is increasingly tricky, as the people behind it are [increasingly distanced and invisibilised from the tool itself](https://dl.acm.org/doi/10.1145/3630106.3658543).

## Attendees

- Huw Day, Data Scientist, University of Bristol: [LinkedIn](https://www.linkedin.com/in/huw-day/), [BlueSky](https://bsky.app/profile/huwwday.bsky.social)
- [Jessica Woodgate](https://jessica-woodgate.github.io/), PhD Student, University of Bristol
- Liz Ing-Simmons, Research Software Engineer, King's College London: [Mastodon](https://genomic.social/@liz__is) 👩‍💻
- Vanessa Hanschke, Lecturer, University College London
- Julie-M. Bourgognon, Lecturer in neurosciences, university of Glasgow
- Euan Bennet, Lecturer, University of Glasgow: [LinkedIn](https://www.linkedin.com/in/euanbennet/), [BlueSky](https://bsky.app/profile/dreuanbennet.bsky.social)
- Paul Matthews, Lecturer, UWE Bristol [BlueSky](https://bsky.app/profile/paulusm.jellytussle.org), [Mastodon](https://scholar.social/@paulusm)

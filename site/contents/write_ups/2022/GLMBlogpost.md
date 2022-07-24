# The G in GLMs sometimes stands for “Garbage” – what I learnt getting students to design algorithms for hiring and firing teachers

```{admonition} What's this? 
This is standalone blogpost written by Huw Day in July 2022 on his experiences teaching data ethics outreach in schools. All opinions expressed are strictly his own. 
Nina Di Cara and Natalie Thurlby helped with the final edit.
```

## Impact

The following is a short except from Cathy O’Neil’s book, Weapons of Math Destruction:

“In 2007, Washington D.C’s new mayor, Adrian Fenty, was determined to turn around the city’s underperforming schools. He had his work cut out for him: at the time, barely one out of every two high school students was surviving to graduation after ninth grade, and only 8 percent of eighth graders were performing at grade level in math. Fenty hired an education reformer named Michelle Rhee to fill a powerful new post, chancellor of Washington’s schools. 
The going theory was that the students weren’t learning enough because their teachers weren’t doing a good job. So in 2009, Rhee implemented a plan to weed out the low-performing teachers. This is the trend in troubled school districts around the country, and from a systems engineering perspective the thinking makes perfect sense: Evaluate the teachers. Get rid of the worst ones, and place the best ones where they can do the most good. In the language of data scientists, this ‘optimises’ the school system, presumably ensuring better results for the kids. Except for ‘bad’ teachers, who could argue with that? Rhee developed a teacher assessment tool called IMPACT, and at the end of the 2009-10 school year the district fired all the teachers whose scores put them in the bottom 2 percent. At the end of the following year, another 5 percent, or 206 teachers, were booted out.”

As part of my Data Ethics Club new year’s resolution, I’ve been giving a series of talks that are aimed to inspire school students (ages 15-18) to study maths. I decided to talk about data ethics. Inspired by Cathy O’Neil’s work I entitled the talk “Weapons of Maths Destruction.” I got students to design their own version of IMPACT, a tool for ranking, hiring and firing teachers (using the dread on their teachers’ faces to fuel participation). 

## Regressing

The talk had two main parts. First, I (re-)introduced ideas of linear regression and correlation by showing a series of scatter plots. I introduced the product moment correlation coefficient (PMCC) as a value “r” between -1 and +1. Rather than give them a formula, I told them that r was indicative of linear correlation (i.e. how well a straight line of best fit, fits the data) and that: 
-	r>0 implied positive linear correlation
-	r<0 implied negative linear correlation
-	r=0 implied little linear correlation

I tested their understanding by looking at a few different datasets, using these datasets to introduce some basic ideas along the way. 

I used a constructed data set of “Time spent playing video games in a week” vs “Number of police visits per year” with only two points to illustrate the importance of the size of a dataset. I also asked “Does this data prove that there’s a link between violent behaviour and playing video games?”

Of course, the students said no, not least because of their own personal bias. But they frequently identified why, from a rigorous data scientists’ point of view, using number of police visits as a proxy variable for violent behaviour is problematic and even if there was correlation, it does not mean there is causation.

The next example was inspired by some [spurious correlations](https://www.tylervigen.com/spurious-correlations): “% of people wearing seatbelts in cars in the US per decade” vs “Number of astronaut deaths on mission in the US per decade”. I was keen to stress that the x-axis only considered seatbelts in cars that were specifically not in space and that the y-axis considered astronauts deaths that were not in cars and who were attempting to go into space. There is reasonably significant negative linear correlation (r=-0.61) between the two variables. 

Everyone knows the phrase “correlation does not imply causation” but that doesn’t mean it’s not a fun exercise to try and explain correlation anyway. I invited students to suggest ideas, prompting them by asking about how the two variables in question changed over time. The point is that both variables have a relationship with time. With time as the hidden proxy variable in-between the two, the stronger than casual correlation becomes more apparent. However, if I worked at NASA and wanted to improve astronaut safety standards, it would likely not be a good use of resources to get more members of the public to wear seat belts in this endeavour.

For the final example, I had some data of age in years (ranging from 0 to 100) versus time to “traverse” 100 metres (apparently, it’s neither scientific nor ethical to get babies/grandparents to run). The linear correlation here is understandably very low (r=+0.24) but this doesn’t mean that there isn’t a strong relationship between the two variables. Perhaps splitting ages 0-25 and 25-100 into two different analyses would be more insightful. This also illustrates that perhaps a straight line isn’t the best tool here, perhaps a quadratic or exponential curve would model the data better. As any student who makes mistakes on a calculator knows, a calculator (or a computer) will always do the calculation you ask it to do, even if it’s the wrong one to do. 

All of this illustrated that when we use data science tools like averages or PMCCs to zoom in on the data, we inevitably lose information and we have to be careful how we use these statistics to summarise data.

## The Hidden Bullseye

Building off the final example, we tried to improve this model by adding additional variables based on students’ suggestions (BMI, hours of exercise per week, injuries/health conditions etc.) We go from a linear model to a so-called Generalised Linear Model (GLM). The premise is the same as using a single predictor variable, but we just have a different correlation coefficient for each predictor and the outcome variables allowing us to weight how important different factors are. We had already mentioned the importance of having a sufficiently large and diverse dataset when using linear models involving only one predictor variable. All of a sudden, with multiple input variables, we desired a dataset of significant size and variability before we could start drawing meaningful conclusions from any models we deduced.

We used this to introduce the idea of the importance of feedback loops. When we are attempting to predict an outcome, we can make a guess and then look at how close we are and adjust accordingly. We can’t always tell what’s making us miss, but if we are predicting something, we can usually see retrospectively how far off target we are (an archer can take a shot at a target and see how far off they are). As the authors of Noise (Daniel Kahneman, Oliver Sibony and Cass R. Sunstein) point out, the key to this adjustment is being confident that your shots are not noisy. A skilled archer with a misaligned sight can be confident that they are shooting where the sight points. When they miss the target, they can more confidently adjust their sights to compensate and move a tight grouping towards the bullseye. An unskilled archer with properly aligned sights might have shots with a wide scatter but generally around the bullseye. All they need to do now is tighten the grouping.

But what happens when you can’t see the bullseye?

## What could go wrong?

The second part of the talk we (either as one group or in smaller groups depending on audience size) designed an algorithm for hiring and firing teachers. We break this down by answering three questions:

1)	What makes a good teacher? 

I asked students to stop thinking like data scientists and just tell me what makes a good teacher (or indeed, a bad one). Whilst discouraging naming names, it was particularly interesting to see students reflect on their own experiences of when they’ve enjoyed teachers’ lessons and to just list things that were good attributes. Common suggestions: subject knowledge, empathy, classroom management, subject enthusiasm, interpersonal schools, being able to take critical feedback.

2)	How would you measure the above variables? What proxy variables would you want to use? 

Now we must put our data science caps on. I had students think about what sort of data was collected about them and their teachers. To make the problem as realistic as possible, we considered data that was already collected on them, excluding data that could be tested (e.g. handing out empathy quotient tests to every teacher as a metric for their empathy). This massively restricts the variables we can work with and starts hinting towards the students at how difficult this problem is. In the first question we captured what makes a good teacher, in the second question we try to ask what proxy variables we can use to measure this? Common suggestions: grades, grade increase, attendance, number of detentions given out, teacher’s education level, number of complaints against teachers. 

3)	How would you weight the dependence on different variables? Give an r number for each one.

The premise here is simple. For each proxy variable we came up with from the second question, what is their correlation coefficient with good-teacher-ness? These judgement calls were based on discussions among students as to how important each variable was and whether its effect was positive (grades, grade improvement, % attendance) or negative (number of complains, number of detentions given out).

One student suggested to me that age should be a variable that should be considered because “Old people are boring and boring people make bad teachers”. This led us to an interesting discussion on discrimination based on various attributes inherent to us as people (race, gender, etc.) and the utility of protected variables.

Another student suggested that as our models tended to prioritise grade and grade improvement, we should consider how this would rank teachers at more prestigious schools more highly. If students must pass an entrance exam to attend a certain school, then it might be fair to assume the grades of students there would be higher than average. Should teachers working at such a school benefit from the school’s inherent prestige, should this be a protected variable or should our model actively penalise teachers from more prestige schools to offset this inherent advantage? 

## Reflections

We explored and discussed the pros and cons of these systems. Whilst some students were quick to claim there was no bias in these systems, most were quick to note that their bias was actually encoded into these systems by their choices of correlation coefficient. At least this bias was consistent -  someone evaluating teachers might evaluate the same two teachers differently depending on their mood that day (or how soon their lunchbreak was). 

We had already touched on the importance of sample size in our running speed example, and this became more apparent. Some variables were (e.g. % attendance) per class. If a teacher teaches 5 classes, they have 5 data points to work with (most models had at least 5 input variables). For variables which were per student (e.g. grades, grade improvement), if we say 30 students to a class, we still only have 150 data points to work with – not enough. Even if these models were perfect predictors of how good a teacher is, the data going into them was insufficient to make them work well.

Perhaps the most important was the lack of feedback loop. When you try and hit a target and you miss, you can adjust your aim to get closer next time. This is the case when your model is used to predict the outcome of an event. When you have a system that is evaluative instead of predictive (be it for teacher good-ness, how long of a prison sentence someone should serve or indeed what grade students should get if they can’t sit their exams due to a global pandemic), you can no longer see the target and so there is no built-in feedback loop. When you can’t see a target, evaluations often become more like judgements, some how given more value. This is true often whether a computer makes the judgement or a so-called “expert” does. 

At the end of a talk I gave in a school in south Bristol, one student asked me “what went wrong with the GCSE grades over covid?” I fumbled with my answer, trying to appease and validate a roomful of understandably frustrated bright minds who felt like they had been unfairly penalised by an unseen algorithm in ways they didn’t understand – much in the way teachers in Washington DC  had been penalised by IMPACT. 

On the bus home I thought more about the answer and even made a meme about it. 

There are two answers; one is a nuanced discussion about how predictive models have value but are not the unbiased, omniscient systems they are often lauded and expected to be. Such an answer is explored in books like Weapons of Math Destruction by Cathy O’Neil, Automating Inequality by Virginia Eubanks and Noise by Daniel Kahneman, Oliver Sibony and Cass R. Sunstein, all books which influenced this talk and that I highly recommended to anyone interested in this topic. 

The other answer is a lot more simple: The G in GLMs sometimes stands for “Garbage”. 

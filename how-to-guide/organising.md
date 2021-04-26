
# Guide to organising a Data Ethics Group

## How to start
1. Find a co-organiser
2. Have your first meeting (you can use our [organisers meeting template](./templates/organisers_meeting_template.md) if you like!)
3. Decide on when and how often you will be meeting
4. Make a mailing list
5. Fork this repo.
6. Update the README with details of your group
7. Update the [MEETINGS.md file](./templates/meetings_overview_template.md) with your upcoming meeting dates and times
8. Make your first meeting file
9. Advertise!


## Deciding on material to read
The [reading list](./../READING-LIST.md) is organised into lots of different sections - some are philosophical, some are technical. It will depend on your audience, but we've enjoyed doing a variety of pieces across philosophical, regulatory and technical themes. For inspiration you can [have a look at our previously discussed pieces](./../MEETINGS.md). 

## Contributions

### How do people contribute to the reading list?
Since we organise around a GitHub repository people can submit issues using our [issue template](./templates/reading-suggestion-issue-template.md) ([see here](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) for how to set up issue templates in GitHub). People can also submit pull requests, or simply email us and we upload their suggestions on to the repository.

### How do people contribute in meetings?
We use HackMD as a collaborative writing space, and have [included our meeting template here](./templates/HackMD_meeting_template.md). We've described how we use this template in the [facilitation guide](./facilitating.md).

### How do we acknowledge contributions?
Contributions can be lots of different things, and so we use [All Contributors](https://allcontributors.org/) to capture a variety of contribution types. These include suggesting material, fixing broken links, organising and producing artwork.  To suit our purposes we've made slight changes to the [emoji key](#all-contributors-emoji-key).  


#### Using the all-contributors bot
To use the bot, follow the [installation instructions provided](https://allcontributors.org/docs/en/bot/installation). You should then be able to comment in an issue or pull-request something like:  
```
@all-contributors please add @NatalieThurlby for organising  
```
The bot will then set up a pull-request (PR) to add the named person to the list, and the PR will update the list of contributors at the bottom.  

Some people aren't on GitHub of course, so to add them to the contributions list you can manually edit the file `.all-contributorsrc` by adding the following object to the list:  
```
    {
      "login": "",
      "name": "FirstName SecondName",
      "avatar_url": "https://www.example.com/profile-pic.jpg",
      "profile": "https://mywebsite.com",
      "contributions": [
        "content"
      ]
    },
```
This person's contribution will then show up the next time you use the All Contributors bot to add someone to the repo.  

The slightly edited emoji key that we use is: 
🖋 (content) for submitting suggestions to the "reading" list (suggestions can be any medium!)
💬 (question) for leading the discussion in a meeting
📝 (blog) for writing in the HackMD in a meeting
📋 (eventOrganising) for organising
🤔 (ideas) for ideas and planning of the group
🎨 (design) for visual design (e.g. logo)
🚇 (infrastructure) for infrastructure (e.g. bots, CI)
🚧 (maintenance) for repository maintenance (e.g. fixing links)


## Equality, diversity and inclusion 

Meeting times - be inclusive with timings. 

Reading selection - we believe that data ethics needs to be discussed as an intersectional issue, which includes colonialism, capitalism, white supremacy, ableism and oppression of marginalised groups in general. We aim for the reading list to incorporates multiple differing perspectives, and think it's helpful to reflect everyone few months 
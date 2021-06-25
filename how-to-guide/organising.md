
# How we organise Data Ethics Group

We've described how a typical meeting would run in the ['Facilitating'](./facilitating.md) document, and so this document is more about how people can contribute to the repository, and how we operate more generally. 

## Deciding on material to read
The [reading list](./../READING-LIST.md) is organised into lots of different sections - some are philosophical, some are technical. Our [previously discussed pieces are available in our Meetings Overview](./../MEETINGS.md). We like to check off things we have discussed [in the reading list](./../READING-LIST.md), and include a link to the meeting info page which summarises the content.  

To decide on material to read the organisers pick three pieces from the list based on recent suggestions, and then the whole group votes on these for the following meeting. 

We try to consider the following when picking what to put to the vote each week:  
 * If someone recently said they'd like it to make the list  
 * If there is a reason to prioritise looking a particular piece soon, for example if there is a deadline for feedback, or if something is a preprint or topical paper that would benefit from being looked at soon.  
 * If there are certain topics that missed out on being discussed due to the group make-up, (whether these relate to particular protected characteristics, e.g. disability, race, gender) or types of scholarship (e.g. data science keeps winning in votes over social science), then consider having a themed meeting, where all three choices are all within that category, to ensure we get a chance to discuss it.   

It's useful to prepare a very short (1-2 sentence) summary about each piece of content to introduce it to the group, so that they know what they're voting for.   

## Contributing

### How can I contribute to the reading list?
Since we organise around a GitHub repository people can submit issues using our [issue template](./templates/reading-suggestion-issue-template.md). People can also submit pull requests, or simply email us and we upload their suggestions on to the repository - we know not everyone is comfortable using GitHub!

### How can I contribute in meetings?
We use HackMD as a collaborative writing space ([see our meeting template here](./templates/HackMD_meeting_template.md)). If you come to a meeting and leave your name and GitHub username in the document then we will credit you on the repository! 

### How do we acknowledge contributions?
Contributions can be lots of different things, and so we use [All Contributors](https://allcontributors.org/) to capture a variety of contribution types. These include suggesting material, fixing broken links, organising and producing artwork. To suit our purposes we've made slight changes to the [emoji key](#all-contributors-emoji-key).  

#### Using the all-contributors bot
All Contributors provides a GitHub bot that makes it easy to add new contributors. 
To use it, comment in an issue or pull-request something like:  
```
@all-contributors please add @NatalieThurlby for eventOrganizing  
```
The bot will then set up a pull-request (PR) to add the named person to the contributors list, and the PR will update the list of contributors at the bottom. We have [an open issue](https://github.com/very-good-science/data-ethics-club/issues/38) that we use to call the all-contributors bot.   

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
This person's contribution will then show up the next time you use the bot to add someone to the repo.  

#### All Contributers emoji key
The slightly edited emoji key that we use is:   
🖋 (content) for submitting suggestions to the "reading" list (suggestions can be any medium!)  
💬 (question) for leading the discussion in a meeting  
📝 (blog) for writing in the HackMD in a meeting  
📋 (eventOrganizing) for organising  
🤔 (ideas) for ideas and planning of the group  
🎨 (design) for visual design (e.g. logo)  
🚇 (infrastructure) for infrastructure (e.g. bots, CI)  
🚧 (maintenance) for repository maintenance (e.g. fixing links)  


## Communicating
We primarily use [MailChimp](https://mailchimp.com/) for our mailing list and to communicate with the group. MailChimp is free, and manages people subscribing/unsubscribing which saves time and effort. It's also easy to make nice looking templates ! We typically send out two emails about each session, one the week before and one on the day.   

We have templates set up in MailChimp to make it quicker for us to write these emails, and for consistency. 

### Tips for communication
- Using a reusable zoom link simplifies things for us and attendees. 
- Providing multiple avenues for communication helps us get lots of different types of feedback (e.g. GitHub issues, email, even Twitter!)
- Using [Time And Date](https://www.timeanddate.com/worldclock/fixedform.html) makes it easy to show which timezone the meeting will be in. There's a link to this in our [meeting info template](./templates/meeting_info_template.md) to remind us to do make it time! 

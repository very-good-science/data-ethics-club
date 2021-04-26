
# How we organise Data Ethics Group

## Deciding on material to read
The [reading list](./../READING-LIST.md) is organised into lots of different sections - some are philosophical, some are technical. Our [previously discussed pieces are available in our Meetings Overview](./../MEETINGS.md). We like to check off things we have discussed [in the reading list](./../READING-LIST.md), and include a link to the meeting info page which summaries the content.  

To decide on material to read the organisers pick three pieces from the list based on recent suggestions, and then the whole group votes on these for the following meeting. 

## Communicating
We primarily use [MailChimp](https://mailchimp.com/) for our mailing list and to communicate with the group. MailChimp is free, and manages people subscribing/unsubscribing which saves time and effort. It's also easy to make nice looking templates ! We typically send out two emails about each session, one the week before and one on the day.   

We have templates set up in MailChimp to make it quicker for us to write these emails, and for consistency. 

### Tips for others
- Using a reusable online meeting link simplifies things for us and attendees. 
- Provide multiple avenues for communication (e.g. GitHub issues, email, even Twitter!)
- Using [Time And Date](https://www.timeanddate.com/worldclock/fixedform.html) to make it easy to show which timezone the meeting will be in. There's a link to this in our [meeting info template](./templates/meeting_info_template.md) to remind us to do make it time! 

## Managing contributions

### How do people contribute to the reading list?
Since we organise around a GitHub repository people can submit issues using our [issue template](./templates/reading-suggestion-issue-template.md) ([see here](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) for how to set up issue templates in GitHub). People can also submit pull requests, or simply email us and we upload their suggestions on to the repository - we know not everyone is comfortable using GitHub!

### How do people contribute in meetings?
We use HackMD as a collaborative writing space, and have [included our meeting template here](./templates/HackMD_meeting_template.md). We've described how we use this template in the [facilitation guide](./facilitating.md). It usually means people writing up the thoughts from their group as they discuss each piece. 

### How do we acknowledge contributions?
Contributions can be lots of different things, and so we use [All Contributors](https://allcontributors.org/) to capture a variety of contribution types. These include suggesting material, fixing broken links, organising and producing artwork. To suit our purposes we've made slight changes to the [emoji key](#all-contributors-emoji-key).  

#### Using the all-contributors bot
All Contributors provides a GitHub bot that makes it easy to add new contributors. 
To use it, comment in an issue or pull-request something like:  
```
@all-contributors please add @NatalieThurlby for organising  
```
The bot will then set up a pull-request (PR) to add the named person to the contributors list, and the PR will update the list of contributors at the bottom.  

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
📋 (eventOrganising) for organising
🤔 (ideas) for ideas and planning of the group
🎨 (design) for visual design (e.g. logo)
🚇 (infrastructure) for infrastructure (e.g. bots, CI)
🚧 (maintenance) for repository maintenance (e.g. fixing links)


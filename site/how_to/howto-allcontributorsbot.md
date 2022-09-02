# Using the all-contributors bot

Contributions can be lots of different things, and so we use [All Contributors](https://allcontributors.org/) to capture a variety of contribution types. These include suggesting material, fixing broken links, organising and producing artwork. To suit our purposes we've made slight changes to the [emoji key](#all-contributors-emoji-key).  

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

## All Contributers emoji key
The slightly edited emoji key that we use is:   
🖋 (content) for submitting suggestions to the "reading" list (suggestions can be any medium!)  
💬 (question) for leading the discussion in a meeting  
📝 (blog) for writing in the HackMD in a meeting  
📋 (eventOrganizing) for organising  
🤔 (ideas) for ideas and planning of the group  
🎨 (design) for visual design (e.g. logo)  
🚇 (infrastructure) for infrastructure (e.g. bots, CI)  
🚧 (maintenance) for repository maintenance (e.g. fixing links)  

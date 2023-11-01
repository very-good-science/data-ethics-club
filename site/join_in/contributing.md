# Contributing to our materials

The Data Ethics Club [repository][repo] is a hub of information where we collect the discussions we've had as a group, our reading list, information about our past or upcoming meetings, and advice on running your own online journal club. 

The Data Hazards project is always welcoming new contributors! This page gives you an overview of how you can get involved. You can see all of our wonderful existing contributors [on the front page of this website](https://dataethicsclub.com/index.html#our-community).

We strongly welcome first-time GitHub users and are very happy to provide support if you would like to learn how to edit the repository. Please just get in touch by [email][dec-email] if that is the case.

## What kinds of contributions are we looking for?

We're open to any suggestions on how to improve the Data Ethics Club resources, from increasing [accessibility][accessibility] to changing the structure of our content. 

That said, we are particuarly open to additions for our **[reading list](../reading-list)** - the data ethics landscape is pretty huge and so its a group effort keeping on top of new pieces and issues to consider. We welcome videos, blog posts, white papers or journal articles relating to ethics and data science - these can cover anything from be the impact of algorithms on the people who are deploying them, to the ethics of surveillance and buying/selling personal data, to a more technical paper on the specifics of an explainable AI algorithm.

Usually if you are contributing to the reading list we will ask you to also provide three discussion points about the piece to help guide our discussion if we read (or watch/listen to) it for a Data Ethics Club meeting. You can look at our past meetings for an idea of the kinds of questions we consider. 

```{admonition} Choosing accessible reading
:class: tip
:name: choosing-accessible-reading

Our aim with Data Ethics Club is to provide an [accessible][] and interdisciplinary space where people can think about data science and ethics and discuss it together. 

With this in mind, we have the following guidelines for choosing reading:
- Materials should be short enough to read/watch/listen to in an hour (maximum). If you suggest a longer piece, we will include it in the reading list, but won't include it in a meeting until we've identified a smaller part of the piece to discuss.
- Try to avoid closed access articles.

If you have further suggestions for choosing accessible reading, we'd love to hear them via [GitHub][new-issue] or [email][dec-email]
```

## How can I contribute?

We accept contributions in a variety of ways. You could:  
* [Get in touch with us over email or Twitter](../contact)  
* [Make a Pull Request](https://github.com/very-good-science/data-ethics-club/pulls) to [our repository][repo] - instructions {ref}`below<pr-instructions>`.
* Open an issue
  - To suggest some discussion material use [this issue template](https://github.com/very-good-science/data-ethics-club/issues/new?assignees=NatalieZelenka&labels=reading+suggestion&template=reading-suggestion.md&title=%5BSUGGESTION%28S%29%5D+You+suggestion%28s%29+here).  
  - To suggest anything else, use [a blank issue][new-issue].

We welcome any form of contribution so don't worry if you do not use GitHub, just get in touch with us however works for you and we'll be happy to hear from you.  

```{admonition} Writing accessible content
:class: tip
:name: writing-accessible-content

We want the content on our website to be [accessible][accessible]. For this reason, we:
- Use alt text on all images. See a guide to writing alt-text [here](https://supercooldesign.co.uk/blog/how-to-write-good-alt-text).
- [Check](https://www.color-blindness.com/coblis-color-blindness-simulator/) any images included on the site for colour-blind friendliness.

If you have further suggestions for writing accessible content, we'd love to hear them via [GitHub][new-issue] or [email][dec-email]
```

## Credit for contributors

While there is a smaller group of people who send the emails and welcome people to the event, Data Ethics Club wouldn't be what it is without any one of its contributors.
Whether they have made suggestions to our reading list, Pull Requests to our GitHub repository, or firey hot takes in our discussions: thank you to each and every one of them!
 
We try to record all of these contributions [on our GitHub repository](https://github.com/very-good-science/data-ethics-club#contributors-). When you suggest something to us please let us know your GitHub username or a link to your personal site so that we can credit you, if you'd like us to.
If you have not been properly credited, please let us know [via email](mailto:grp-ethicaldatascience@groups.bristol.ac.uk), or by commenting on [this GitHub issue](https://github.com/very-good-science/data-ethics-club/issues/38) and tagging one our GitHub usernames (e.g. `@NatalieZelenka`).

<!--
## Directory structure

It can be useful to know what's where in our GitHub repository if you're thinking about making a contribution. 
The most important parts of the directory structure are explained here.

```
site
```
-->

(pr-instructions)=
## Contributing via Pull Request on GitHub

Here we have some guidelines for making your first GitHub contribution to Data Ethics Club a good experience. 

If you think of something you'd like to work on, then first:
1. Check if there is an existing [issue][issues] describing the issue. If not, make a new one :).
1. Comment on the issue before you start working to let us know you'll be working on it, this helps us not to repeat work and gives and opportunity to discuss how to make your contribution most useful.
2. [Fork](https://help.github.com/articles/fork-a-repo) this repository to your own GitHub account
3. Check that you are happy with the changes by [building the site locally](#build-the-site-locally).
4. Then, once you've made your changes, submit a [pull request](https://help.github.com/articles/creating-a-pull-request): we'll review it as quick as we can 😄.

### Build the site locally
In order to build the site locally, you'll need to run the following from your root directory:
`sphinx-build site/ site/_build/` 

These require some Python packages to run. 
You may want to set up a [virtual environment](https://docs.python.org/3/library/venv.html) first, so that you don't install these packages system-wide.
Then you can install the packages using `pip install -r requirements.txt`

[repo]: https://github.com/very-good-science/data-ethics-club/
[issues]: https://github.com/very-good-science/data-ethics-club/issues
[new-issue]: https://github.com/very-good-science/data-ethics-club/issues/new?assignees=NatalieZelenka
[dec-email]: grp-ethicaldatascience@groups.bristol.ac.uk
[accessibility]: https://dataethicsclub.com/how_to/accessibility-plan.html

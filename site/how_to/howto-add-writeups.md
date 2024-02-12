# How to add a write up to the website

Since the Data Ethics Club repository is primarily served by a website we have to update this site with the latest write ups. This file contains instructions on how to make these updates, assuming we've written a draft in HackMD. 

1. From the repository root, navigate to the `site>contents>write_ups` directory.
2. Above the file browser, on the right, choose the option `Add file > Create New File`, name the file `YYYY-MM-DD_writeup.md` (date of the Data Ethics Club meeting).  
3. Copy in the contents of the write up (click next to the `1` in GH which is indicating the first line of the file). Add the admonition code at the top just below the title, but before the rest of the write up and change the text accordingly. Put the attendees at the bottom of the write up.  
4. Add the frontmatter to the top of the post so that it gets recognised as a blog. As an example, this should look like:
```yaml
---
blogpost: true
date: March 17, 2021
author: Nina Di Cara, Huw Day
category: Write Up
tags: a category, another
---
```
So, multiple authors are separated by a comma, so are tags.  

5. IMPORTANT: to save, scroll down the the bottom and choose the "Create a new branch for this commit and start a pull request" option (this is not the default). Name the new branch something relating to the write up, e.g. "PrivateSpies", then click "Propose New File".  
6. You will be taken automatically to create a pull request. Write in any things that you'd like any particular feedback on, in the comments. You can also add reviewers here.  
7. Lastly, you can now also update the main list of meetings and write ups. This is in `contents>join_in>join_in.md`. Move the first line of the table under `Upcoming Meetings` to be the first line of the lower table `Past Meetings`. You need to add one column to the row, which you do by adding a `|` symbol to the end of the row. You can then write something like "Read the write up" and link to the write up you have just created using the link `../write_ups/YYYY_MM_DD_writeup`. Commit this change to your branch again like you did in Step 6. 
8. All done! 

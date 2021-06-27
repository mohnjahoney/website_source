Title: Remodeling website
Date: 2021-06-22
Author: John Mahoney
Category: pelican
Tags: pelican, website

This is my first post in the remodeled version of my website.

I had a few goals in this remodel:

- Continue with pelican as a site generator
- Use jupyter notebooks as a content source
- Have a "nice" directory structure
- Host on GitHub
- Allow custom javascript for interactive demos

While these targets seemed relatively modest, it took some doing even with the many resources available.
Luckily, I found an existing site with many of these features. 
![https://jackmckew.dev/](https://jackmckew.dev/)
My goal then became to adapt Jack's website.

I wanted to use a different theme and also strip some of what I thought was unnecessary.
This was not trivial and not completely solved.
Please steal my sourcecode from GH.

I don't want to create a formal writeup here because things change quickly.
But here are a few thoughts:

- `pelican` has some nice features, but it is not clear to me that it is on a path toward long-term development and support. E.g. look at how recently plugins and such have been updated on GitHub. 
- Related, I had hopes that various related packages would be well-functioning enough so that I could install them and not worry about versions. This appears to be not at all true. In fact, it seems like this might be more the norm. So get yourself a virtual environment and get used to it. I am using `venv` and my requirements file is in the source.
- Certain little things can be terribly frustrating. For example, sizing images in Markdown appears to be a big pain with many conflicting styles. Prepare for that. 
- `pelican` plugins used to be all on in one GH repo. Now it seems that things are moving toward separating them into separate but connected repos. Some versioning issues lurk there. Also it looks like some plugins are not better available as packages to install via pip, e.g. ghp-import.
- Github really falls down sometimes. For example, rendering jupyter notebooks is an issue that has plagued people for years. It's a wonder folks still use it in this way. (Do they? Am I the only one foolish enough to try?) It also seems that GH does some funny things w.r.t. hosting and updating your website. There are several times where the site did not render correctly and then fixed itself - something about the css not being found. Also, every time you push your new site to GH, it takes at least a minute or maybe 5 for it to appear live.
- File structure, articles, pages, categories, tags, menu building, internal site referencing, arg.. This is easy when it works and really painful to debug when it doesn't.
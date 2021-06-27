Title: About this site
Date: 2020-08-18 16:27
Author: John Mahoney
Tags: pelican, website, tips
Category: 
Slug: about-this-site

I want to share the basic ideas behind how to *create*, *share*, and *maintain* this website.

You can find the python source code for this website 
[here](https://github.com/mohnjahoney/website_source).
I hope you find something useful!

# Overview

## Here's the basic idea:

- Write files in Markdown (basically human readable) locally.
- Use python package `pelican` to compile this into a website (HTML)
- Push the HTML to GitHub (in a way where GH agrees to serve your website)

## What's nice?

- You write in Markdown rather than HTML. This is a plus for me.
- You can make use of various themes developed for `pelican` so that you can input the same content, but get differently styled webpages.
- If you move to another system (e.g., Jekyll or Hugo) the process appears to be relatively painless because the content is pretty well separated from the style.
- Hosting is easy and free.

## What's not so nice?

- Markdown has some limitations and you sometimes end up having to write HTML yourself. Sometimes I think I waste more time trying to coax the Markdown than I would have just writing HTML.
- The themes seem to have their own quirks and requirements so that switching themes is not as effortless as you might desire.
- Plugins and related packages change ways such that the ecosystem seems somewhat fragile. I don't know if this is a sign that pelican is losing momentum or what..

# More details

## How to *create* this website?

This website is created using the Python package `pelican`.
You can install this with,

    :::shell
    pip install pelican

There are a few other dependencies you may need to also install with pip like `Markdown`.

I didn't begin this process using virtual environments, but I do now and certainly recommend it.
The upshot is that you choose particular packages (and versions) that you want to use with this website.
These choices can differ from what you have running at large on your machine (or what you use in other virtual environments for other projects).
You specify these in the `requirements.txt` file.
Whenever you recompile the site, you do this from within the virtual environment.
I use `venv` where activation looks like this:
    
    :::shell
    source env/bin/activate

The site content is written in the Markdown language (easier to write than HTML and more limited).
Then pelican, along with a pelican theme, compiles the content into a website.
This is done by running,

    :::shell
    make html

The website is written to a directory named `output`.

You can then view this website locally by running,

    :::shell
    make serve

and pointing your browser to `http://localhost:8000/`, or `http://127.0.0.1:8000/`.
This is a chance to see how things will look before committing your changes.

## How to *share* this website?

There are various options for how to share the website.
I chose to host it on Github.
This was fairly straightforward.

Turn the `output` directory into a local git repository by running,

    :::shell
    cd output
    git init

Create a repository on Github named `yourusername.github.io` and push your local `output` repository here.

    :::shell
    git commit -am "first commit"
    git remote add origin https://github.com/yourusername/repo_name.git
    git push origin master

Your website will then be hosted at `yourusername.github.io`.
Note: it can take a few minutes for pushed changes to be reflected on the website.

Note: compiling the website clobbers the existing output directory. So you have to set up the git process from the beginning each time.
I wrote a simple script `mypublish.sh` (in the source) that I use to accomplish this.

## How to *maintain* the website?

For starters, you'll want to turn your website source into a git repo.
And likely push it to GH too.

It is recommended to set up an appropriate `.gitignore` file.

The basic flow:

* Make some change locally. E.g., write a new article.

* Check out the effect. Compile the website and serve it locally and view `http://localhost:8000/`,

        :::shell
        make html
        make serve

* Push changes to GitHub - remember that you have source *and* website repo.

        :::shell
        git add content/insightful_article.md
        git commit -am "added yet another insightful article"
        git push

        ./mypublish.sh

Related resources I found useful:
- https://appliedcaffeine.org/navbaritems.html


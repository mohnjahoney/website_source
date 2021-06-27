#!/bin/bash

# This script compiles the website using the `publish` settings,
# then pushes the output to GitHub.

# Compile
pelican content -s publishconf.py

# Move to compiled html
cd output

# (re)-establish git. Publishing wipes it out.
git init

# Put everything in the commit
git add .
git commit -am "publishing"

# Sync by overwriting the current content.
# Note that we are overwriting the website (HTML), not the website source (python)
git push -f


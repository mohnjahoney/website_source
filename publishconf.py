#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://mohnjahoney.git.io"

# Note about RELATIVE_URLS:
# With the pure-single theme, it appears that things work fine locally with either setting. However, for publishing to GH, you need True. I believe this same behavior is *not* true for other themes, but I'm not sure.
# RELATIVE_URLS = False
RELATIVE_URLS = True # Careful

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

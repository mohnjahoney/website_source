#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from typing import Any

RELATIVE_URLS = False # Appears to not matter for this theme. It *does matter in publishconf.py

DEFAULT_LANG = "en"
#DEFAULT_LANG = "English"
_DEFAULT_LANGUAGE = "en"
TIMEZONE = 'America/Los_Angeles'

PATH = "content"
AUTHOR = "John Mahoney"
SITENAME = "John Mahoney"
SITETITLE = SITENAME
SITESUBTITLE = "Data Scientist | Applied Mathematician"
SITEURL = "https://mohnjahoney.github.io"

IGNORE_FILES = ["*.html", "*.rst"]
DISPLAY_PAGES_ON_MENU = True
RELATED_POSTS_SKIP_SAME_CATEGORY = True

# USE_TIPUE_SEARCH = True
USE_TIPUE_SEARCH = False

GITHUB_CORNER_URL = "https://github.com/mohnjahoney/mohnjahoney.github.io"

ARTICLE_URL = "{slug}.html"
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
ARTICLE_SAVE_AS = "{slug}.html"
# YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
# DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/index.html'

#THEME = "./themes/Flex"
THEME = "./themes/pure-single"
#THEME = "./themes/Peli-Kiera"

# STATIC_PATHS = ["content/img","static"]
STATIC_PATHS = ["img", "images", "pdfs", "extra", "pages"] # , "2018", "2019", "2020", "2021"
# STATIC_SAVE_AS = "{dirname}"
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    # "extra/jm-photo.jpg": {"path": "jm-photo.jpg"},
    # "images/me.jpg": {"path": "me.jpg"},
    "extra/CNAME": {"path": "CNAME"},
}
# SITELOGO = "/jm-photo.jpg"
# EXTRA_PATH_METADATA = {
# 'img/favicon.ico' : {'path' : 'favicon.ico'}
# }
FAVICON = "/favicon.ico"
# CUSTOM_CSS = THEME + "static/custom.css"

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = False

# TAG_URL = 'tags/{slug}.html'
# TAG_SAVE_AS = 'tags/{slug}.html'
# PAGINATION_PATTERNS = (
#     (1, '{name}.html', '{name}.html'),
#     (2, '{name}/page/{number}.html', '{name}/page/{number}.html'),
# )

MENUITEMS = (
    ('Resume', '/pdfs/John_Mahoney_resume.pdf'),
    # ('rad menu item', '/images/schwartzwald.jpg'),
    ('Projects', '/pages/projects.html'),
    # ("Authors", "/authors.html"),
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
    ("Sitemap", "/sitemap.xml"),
    # ('RSS', "feeds/all.atom.xml")
    # ("Search","/search.html")
)

NOTEBOOK_DIR = ""
CODE_DIR = ""

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.8, "indexes": 0.6, "pages": 0.7},
    "changefreqs": {"articles": "weekly", "indexes": "daily", "pages": "monthly"},
}

PLUGIN_PATHS = [
    "./plugins/",
    # './plugins/pelican_javascript'
    # './plugins/pelican_youtube'
]

# Looks like this might be important for the TIPUE_SEARCH
DIRECT_TEMPLATES = ("index", "authors", "tags", "categories", "archives", "search")

PLUGINS = [
    "sitemap",
    # "better_codeblock_line_numbering",
    "better_code_samples",
    "bootstrapify",
    "deadlinks",
    "more_categories",
    "neighbors",
    "pelican-ert",
    "liquid_tags.notebook",
    "liquid_tags.include_code",
    "representative_image",
    "share_post",
    "show_source",
    "tipue_search",
    "dateish",
    "post_stats",
    "pelican_javascript",
    "render_math",
    "related_posts",
    # "autostatic", # now a pip package
    "clean_summary",
]
CLEAN_SUMMARY_MAXIMUM = 1
# MARKUP = ('md', 'ipynb')
MARKUP = ("md",)
IGNORE_FILES = [".ipynb_checkpoints"]
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "linenums": "True",
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.tables": {},
    },
    "output_format": "html5",
}
# IPYNB_USE_METACELL = True

DELETE_OUTPUT_DIRECTORY = True

# ARTICLE_PATHS = ['articles']
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'

# # Feed generation is usually not desired when developing
# FEED_ALL_ATOM: Any = "feeds/all.atom.xml"
# CATEGORY_FEED_ATOM: Any = "feeds/{slug}.atom.xml"
# TRANSLATION_FEED_ATOM: Any = None
# AUTHOR_FEED_ATOM: Any = None
# AUTHOR_FEED_RSS: Any = None
# FEED_MAX_ITEMS = 5


# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/johnmahoney3/"),
    ("github", "https://github.com/mohnjahoney"),
)

DEFAULT_PAGINATION = 10

# import wordsum

# POST_TICKER = wordsum.count_files('./content',['.md','.ipynb'])
# WORD_TICKER = wordsum.count_words("./content", [".md", ".ipynb"])
# WORD_TICKER = f"{WORD_TICKER:,}"

# import sys

# sys.path.append(".")
# import count_loc

# custom_js_files = [
#     "content/2020/virus-outbreak-simulation/js/virus_part_1.js",
#     "content/2020/canvas-javascript-bouncing-balls/js/bouncing_balls.js",
# ]

# language_stat = count_loc.get_total_loc(
#     "content", [".py", ".md", ".ipynb"], custom_js_files
# )

# LOC_TICKER = sum(language_stat.values())
# LOC_TICKER = f"{LOC_TICKER:,}"

PROFILE_IMG_URL = '/images/me.jpg' # NOTE: leading slash was important
TAGLINE = 'DATA SCIENTIST | APPLIED MATHEMATICIAN'
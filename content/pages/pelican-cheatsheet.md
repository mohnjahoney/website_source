Title: Cheatsheet
Date: 2020-08-16 15:05
Author: John Mahoney
Tags: pelican, website, tips
Category: 

---
### First is the Markdown input.

### Second is the rendered output.

---
## Links

Make intra-site links in Markdown format.

---
```
[a link relative to the current file]({filename}../pages/article-template.md)
```
[a link relative to the current file]({filename}../pages/article-template.md)

---
```
[a link relative to the content root]({filename}/pages/article-template.md)
```
[a link relative to the content root]({filename}/pages/article-template.md)

---
Need something like STATIC_PATHS = ['images', 'pdfs'] in pelican_conf.py

---
```
[a link to a nonstandard subdirectory]({static}/pdfs/John_Mahoney_resume.pdf)
```
[a link to a nonstandard subdirectory]({static}/pdfs/John_Mahoney_resume.pdf)

---
To control the size of an image, append the parameters in curly brackets.

> How to control the height and width together? 
> There appears to be an auto height in this theme that clobbers the one I set.

---
Set in pixels
```
![smiley]({static}/images/music_image.png){height=50 width=50}
```
![smiley]({static}/images/music_image.png){height=50 width=50}

---
Set as a percent
```
![smiley]({static}/images/music_image.png){height=50% width=50%}
```
![smiley]({static}/images/music_image.png){height=50% width=50%}

---
## Code
Use three colons followed by the language identifier.
Start each line with 4 spaces.

---
```
    :::python
    print("The triple-colon syntax will *not* show line numbers.")
```
    :::python
    print("The triple-colon syntax will *not* show line numbers.")

---
```
    #!python
    print("The path-less shebang syntax *will* show line numbers.")
```
    #!python
    print("The path-less shebang syntax *will* show line numbers.")

---
```
print("Another possibility is to use triple back-ticks to create a code-fence.")
```
print("Another possibility is to use triple back-ticks to create a code-fence.")

---
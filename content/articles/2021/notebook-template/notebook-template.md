Title: Notebook template
Date: 2021-01-01
Author: John Mahoney
Category: python
Tags: python, jupyter notebook, template, website

### Notes:

- $\LaTeX$: It renders correctly from the markdown file. The $\LaTeX$ within the notebook markdown cells renders the equations, but not the inline math. TODO: fix this
- When you reference a single cell, you can't say cells[4], you have to write cells[4:5].
- The numbers in cells[m:n] don't refer to the "input numbers" you see in the notebook. The markdown cells are counted too. This makes it a bit of a pain to locate particular cells within a larger notebook.

## Here I am selecting a cell from the notebook.

{% notebook articles/2021/notebook-template/notebooks/notebook_template.ipynb cells[7:8]%}

## Now I am displaying the whole notebook.

{% notebook articles/2021/notebook-template/notebooks/notebook_template.ipynb %}
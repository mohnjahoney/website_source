Title: K-Nearest Neighbors
Date: 2021-05-15
Author: John Mahoney
Tags: data science
Category: 

> “If it walks near `k` other ducks, then it probably *is* a duck.”

### Setup
Imagine there is a lake with lots of birds hanging around: ducks, geese, cranes, herons, and so on.
We can see each bird clearly enough to tell what type it is.

### Problem:
Now imagine there is one bird out there that we *can’t* see well enough to identify its type.
Maybe there is a bit of glare from the sun or something.

How might we guess the type of this bird?

### Solution:
One way to do this is to assume that birds tend to hang around birds of the same type.
So, we can look at the nearby birds (the “neighbors”), see what kind they are, and assume that our mystery bird's type is that of the most common neighbor.

And that's the k-Nearest Neighbors algorithm!

The `k` in kNN is simply the number of nearby birds we should include in our decision.
You can see that if we include just one neighbor, we might be subject to some sporadic errors.
Alternatively if we let `k` be equal to the total number of birds at the lake, then our guess would be the same no matter where the mystery bird is located - not very useful.

kNN can also be used to provide numeric rather than categorical output.

For example, we might want to guess the mystery bird's height.
We would collect the height of each neighboring bird, and then simply take the average (or something similar) to get our prediction.

- Supervised learning: We need to know the type (or size) of all birds except the bird of interest.
- Potentially slow: Naive distance computations are.. well.. slow. There are ways to improve that.
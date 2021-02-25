# Function : from subscript to parameter

## subscript
Roughly speaking, a program is an arrangement of **finite** many characters, which make it impossible to define infinite many concepts in a program. It is terrible. The notation of subscript is exactly created to write all of definitions into a file.

### Index of Concept
In analysis, we would write a sequence of points as `a`<sub>`i`</sub>, with the natural numbers (`1`, `2`, ..., `n`, ...) plays the role of index. By this notation, if we have a uncountable index set `I`, we can define uncountable many concepts by `a`<sub>`i`</sub>. 

### Ownership of Concept
Under some context, for example, if we have a group `G` and another group `H`, we can denote their group operator as `*`<sub>`G`</sub> and `*`<sub>`G`</sub>, repspectively.

### Commentary of Concept
Under some other context, for example, when we are studying Mechanics, we should see `F`<sub>`net`</sub> `=` `F`<sub>`1`</sub> `+` `F`<sub>`2`</sub>. `F`<sub>`net`</sub> here means it is a "net force".

### Subscript is Normal
Subscript is such a natural construction since we can view it as a component of **name**, like
* `a`<sub>`1`</sub> => `a_1_`
* `a`<sub>`100`</sub> => `a_100_`
* `a`<sub>`G`</sub> => `G.a`
* `a`<sub>`happy`</sub> => `a_'happy'_`

Names with index inside is of course too weak to realize the functionality of subscript, and I write it down for giving your another point of view.

In `gm` language, I use the square bracket instead to guarantee we can write a program "linearly".
* `a[1]` => `a`<sub>`1`</sub>
* `a[100]` => `a`<sub>`100`</sub>
* `a[G]` => `a`<sub>`G`</sub>
* `a["happy"]` => `a`<sub>`happy`</sub>

### Beyond the Sub
Although I call the `1` inside `a[1]` "subscript", it is your own choice to place it anywhere you like. After define a suitable rule, we can print
* `a[1][2]` => `a`<sub>`1`</sub><sup>`2`</sup>
* `a[1][1]` => <sub>`2`</sub>`a`<sub>`1`</sub>
(due to the restriction of markdown, I cannot write the form `a_1^2` as in Latex here)

Another powerful (maybe) using (用法) is "put the subscript inside a name", like (I haven't used it up to now)
* `vector_space_over[ℝ]_with_dim[n]` (undetermined)

Warning: it is not allowed to put the bracket in the front of the name, and if so, it would become a block comment.
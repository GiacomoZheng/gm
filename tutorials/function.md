个人整理思路用，尚未正式发布
# Function: from subscript to parameter

## subscript
<!-- Roughly speaking, a program is an arrangement of **finite** many characters, which make it impossible to define infinite many concepts in a program. It is terrible. In order to solve it, I'll introduce the notation of subscript. -->


### Index of Concept
In analysis, we would write a sequence of points as `a`<sub>`i`</sub>, with the natural numbers (`1`, `2`, ..., `n`, ...) plays the role of index. Now, `x`<sub>`1`</sub> and `x`<sub>`2`</sub> might represent two different numbers.
<!-- By this notation, if we have a uncountable index set `I`, we can define uncountable many concepts by `a`<sub>`i`</sub>.  -->

### Ownership of Concept
Under some context, for example, if we have a group `G` and another group `H`, we can denote their group operator as `*`<sub>`G`</sub> and `*`<sub>`H`</sub>, repspectively. Equivalently, we can write these two group as `(G, *)` and `(H, •)`, but it would be difficult when dealing more groups.

### Commentary of Concept
Under some other context, for example, when we are studying Mechanics, we should see `F`<sub>`net`</sub> `=` `F`<sub>`1`</sub> `+` `F`<sub>`2`</sub>. `F`<sub>`net`</sub> here means it is a "net force".

### Subscript is Natural
Subscript is such a natural construction since we can view it as a component of **name**, like
* `a`<sub>`1`</sub> => `a_1_`
* `a`<sub>`100`</sub> => `a_100_`
* `a`<sub>`G`</sub> => `G.a`
* `a`<sub>`happy`</sub> => `a_'happy'_`

Names with index inside is of course too weak to realize the functionality of subscript, and I write it down just for giving your another point of view.

In `gm` language, I use the square bracket instead to guarantee we can write a program "linearly".
* `a[1]` => `a`<sub>`1`</sub>
* `a[100]` => `a`<sub>`100`</sub>
* `a[G]` => `a`<sub>`G`</sub>
* `a["happy"]` => `a`<sub>`happy`</sub>

**Remark**: It is notable that we haven't define what is `a` even if you have define every `a[x]` you can recall. (It is easy to understand for math people, and the CS students should pay attention on it)

### Define Subscript with Indeterminant
A traditional definition of sequence in math looks like,
* `∀n: ∈ ℕ, ∀a[n]: ∈ ℝ,`

You can still do the same thing in `gm`.

While, a traditional definition of function in a program looks like,
```rust
fn a(n : u32) -> f64;
```
I learnt a lot from it and thus we can simplify the defeinition above as
* `∀a[∀n: ∈ ℕ]: ∈ ℝ,`

An obvious benefit is that we can write this definition into one sentence; a potential benefit is that we can drop the variable `n` as soon as possible.

### Order is Important, Almost Always
<!-- ? Maybe I can define something like relation here. -->
Sometimes we need to use more than 1 subsript, like `a[1][2]`, which is of course maybe not the same as `a[2][1]`.

**Remark**: For the ones who have read the `basic.md` carefully, pay attention with the "equality" here, which is "absolutely equality".



### Beyond the Sub
Although I call the `1` inside `a[1]` "subscript", it is your own choice to place it anywhere you like. After define a suitable rule, we can print
* `a[1][2]` => `a`<sub>`1`</sub><sup>`2`</sup>
* `a[1][1]` => <sub>`2`</sub>`a`<sub>`1`</sub>
(due to the restriction of markdown, I cannot write down the form `a_1^2` as in Latex here)

Another powerful (maybe) using (用法) is "put the subscript inside a name", like (I haven't used it up to now)
* `vector_space_over[ℝ]_with_dim[n]` (undetermined)

**Warning**: no square brackets are allowed before the name, and otherwise, it would become a block comment.

### Why We Need Function
Subscript is so natural and useful. Why we need to define function? The answer is that it is too natural making it indeed just a trick of program but not a object for researching. When we define `a[n]`, we cannot say `a` is the integration of all of its subsripts; however, after we define `f(x)`, we can say taht `f` is a function with its `input` and `output`.

---

## Function
Pay attention please, especially for math people. When we say "function" in math, normally we mean a map from one set to another set (may be the same set). While here use the word `map` (or `mapping`) to represent this stricter concept and let's lower the criteria of function here.

The `function` in `gm` is something stricter than the function in CS and weeker than the function (map) in math. It is similar to "pure function" in CS.

**Warning**: the codes below are undetermined yet since I'm still considering about it.

A function over `classlevel` 0 is,
```gm
function[◉][◉]:
(
	∀f: ∈ function[◉][◉],
	f.input: ⊆ ◉, f.output: ⊆ ◉,

	f.of[∀x: ∈ f.input]: ∈ f.output,

	...
),
```
then we can simply write `f.of[x]` as `f(x)`.

**Remark**: the `◉` above means the universal class, not an indeterminant or a parameter.

**Remark2**: The [wikipedia](https://en.wikipedia.org/wiki/Function_(mathematics)) says that `f(x)` reads "`f` of `x`", though I just read "`f` `x`".

Up to now, a function has given a fixed input type and output type, and we also want to gain the unique result, i.e. `x = y ⇒ f(x) = f(y)`, formally speaking,
```gm
function[◉][◉]:
(
	...
	∀x: ∈ f.input, ∀y: ∈ f.output,
	x f.input.= y ⇒ f.of[x] f.output.= f.of[y],
	...
),
```
Or equivalently (but more clearly)
```gm
function[◉][◉]:
(
	...
	@f,
		∀x: ∈ input, ∀y: ∈ output,
		x input.= y ⇒ of[x] output.= of[y],
	■
	...
),
```

It is nearly the formal definition of function in `gm`, you can find the formal version in [`gm.h.function`](https://doc.gm-lang.org/src/gm.h) in the [gm/h/.gm](../h/.gm). You can think about why I write it a bit more complicated.

Consider the "equality" under  `function[◉][◉]`, we see `f`, `g` are equal iff they have the same input type, the same output type and the same mapping rule.

Let's see some further examples in mathematics

### Map / Mapping
Basically, in mathematics, almost every time when we say `function`, we means a map from a set to another set. Here I use the `map` or `mapping` to represent this meaning.
```gm
mapping:
(
	⊆ function[◉][◉],
  ∀f: ∈ mapping,
  f.D: ∈ set, ; domain
  f.C: ∈ set, ; codomain
	@f,
  	input = D.element,
  	output = C.element,
  ■
)
```
which means a input of this function should be an element in `D` (a set as domain) and a output of it should be an element in `C` (a set as domain).

You can see the equality here is nearly the same with `function` (in addition with `D` and `C`).

(The [formal version](https://doc.gm-lang.org/src/gm.h.set) of it is more complicated)

### (Associative) Algebra Homomorphism
In some sense, a map is exactly a `set.homomorphism` (or set morphism, of Category Theory's manner). Consider an algebra, a set with three operations (addition, multiplication, scalar-multiplication) and two special elements (`0`, `1`) defined, then the homomorphism of it is a map preseveres the items above.

You can check the criteria of equality here by yourself.

### Polynomial
A polynomial is a special algebra homomorphism (sometimes we may only consider the format of it). However, two polynomials can be the same as homomorphisms (or functions) but different as polynomials. Let's consider `x` and `x`<sup>`2`</sup> on `𝔽`<sub>`2`</sub> field (the field with characteristics 2). They are differenet polynomials since they have different format, but you can see they are the same homomorphism.

These three examples follows the general rule of equality stated in `basic.md` file.
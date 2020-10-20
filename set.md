个人整理思路用，尚未正式发布

# From Class to Set

Many mathematicians regrad the `sets` as primitive objects in math, they would assume there is something named `set`, and
* for any set, for any "object", we can judge whether it is in not in this 
* for any two sets, we can get the intersection and union of them.
or there is an even more powerful proprty,
* for any set of sets, we can get the intersection and union of them.

<!-- All of us agree that the set is a fundamental concept in math, but some of us want a concrete definition for it.  -->

<!-- Later, after the query of Ressell, some mathematicians proposed a axiomatic definition for the set, the Zermelo–Fraenkel set theory.  -->

The Zermelo–Fraenkel set theory is builded up under this common sense, and it also answer us what cannot be a set ([axiom of regularity](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory#2._Axiom_of_regularity_(also_called_the_axiom_of_foundation))). However, the quesion now becomes what is a set?

Some mathematician think the ZF system is enough for mathematician to understand the `set` and to use it in their own research field, and it is meaningless to ask what is it, as we can only understand something with the help of something else, and the set has been the simplest and most fundamental things in math (and in the world).

Generally speaking, I don't appreciate this answer. `Set` is the core of math, but it is not simple enough for us to ignore the detail of it. Since there is still some criteria on it and we would really meet some "proper class" like `ordinal` without these restriction.

For me, I think the concept of `class` is simple and intuitive enough for everyone, including mathematicial beginners and passers-by. Here, I'll use it to define the `set` and prove it follows the ZF (No AC up to now).

To begin with, although we always ignore, a set has its "type", or mathematically speaking, it has a `universe`, and it is meaningless for us to discuss whether anything else in inside or outside this set. A set may not (and may not be able to) contains everything in the `universe`, so we call the subclass contains elements in the set as `element` i.e.
```gm
set:
(
	⊆ ◉,
	(
		∀A: ∈ set,
		A.universe: ⊆ ◉, ; in some sense define the `=`
		A.element: ⊆ A.universe, ; x ∈ A means x ∈ A.element
		A.=: = &A.universe.=&, ; you can ignore the `&`
		; for two instance of element, even they may not be
		; `A.element.=` to each other, they can be the same
		; `element` (same in universe) of this set.
	),
),
```
This definition, satisfies the **Axiom of extensionality (1)** under the same (absolutely equal) universe trivially as it is the property of `class.=`; it also satisfies the **Axiom schema of specification (3)** under the same universe as
```gm
∀A: ∈ set, ∀cls: ⊆ A.universe, ; may be ◉ is enough
Bcls:
(
	⊆ A.element,
	⊆ cls,
),
B: (∈ set, universe = A.universe, element ⊆ Bcls),
```
Remark.
1. when the `cls` above is an empty class, this set would be the empty set under this universe;
2. for another set `C` under this universe, pick `cls` above as "is also a `C.element`", we call the `B` as the intersection of `A` and `C`, denoted as `A ∩ C`.
3. also, for another set `C` under this universe, pick `cls` above as "is not a `C.element`", we call the `B` as the relative complement of `C` with respect to a set `A`, denoted as `A \ C`.

As for **Axiom of union (5)**, I don't want to "union" two sets with diffferent universe. To avoid these weird cases, let's refine the definition of `set` into,
```gm
set:
(
	⊆ ◉,
	(
		∀A: ∈ set,
		...

		∀x: ∈ A.element,
		x ∈ set ⇒ x.universe = A.universe
	),
),
```
which means the set elements of a set should have the same universe with the set of them.

It is so powerful that I can define the `pure_set` simply
```gm
pure_set:
(
	⊆ set,
	(
		∀S: ∈ pure_set,
		S.universe = set
	)
),
```

Now we can also define `set_of_sets` (compare to `pure_set`) as
```gm
set_of_sets:
(
	⊆ set,
	(
		∀𝒜: ∈ set_of_sets,
		𝒜.element ⊆ set,
	),
),
```
Thus, the **Axiom of union (5)** would look like,
```gm
∀𝒜: ∈ set_of_sets,
∃B: ∈ set, B.universe = 𝒜.universe,
∀x: ∈ 𝒜.element, x.element ⊆ B.element,
```
To prove it, we need define the `B.element` as
```gm
Bcls:
(
	⊆ 𝒜.universe,
	∀b: ∈ Bcls,
	∃x: ∈ 𝒜.element, b ∈ x.element
),
```
However, I cannnot say it have proved the **Axiom of union (5)** since up to now, since I can define a "universal set" under this universe as
```gm
U:
(
	∈ set,
	universe = 𝒜.universe,
	element = 𝒜.universe,
),
```
which satisfies the axiom already. Of course, it might be meaningless as we have the Russell's Paradox and **Axiom of regularity (2)**. I'll go back and prove the `Bcls` is suitable after I complete the definition of `set`.

Similarly, to contruct a set from **Axiom of pairing (4)**, at least I need to give some support for the set of sets.
```gm
set:
(
	⊆ ◉,
	(
		∀A: ∈ set,
		...

		A ∈ A.universe,
		; in some sense, if A is a set, {A} is also a set
	),
),
```
Just as I claimed above I cannot say that I have proved it now.

---
Before talking about the **Axiom of regularity (2)**, let's see something interesting, let's consider about sets with the universe the universal class i.e. `A.universe = ◉`. In this case, there are only and exactly 2 sets, an empty set and a singleton set, as
```gm
∅: (∈ set, universe = ◉, element ∈ empty_class), ; empty set
s: (∈ set, universe = ◉, element = ◉), ; singleton
```
Remark. `∅.element ∈ empty_class` means `∅.element` is a empty class, in some sense, no elements in `∅`; on the contrary, there seems lots of elements in `◉`, but as I claims, all of them are the same in the sense of instances of `◉`.

What about `{∅}`, `{s}` and other sets of sets? It is easy to answer as `{∅}` and `{s}` are singleton, so that `{∅} = s` and `{s} = s`; `{∅, s} = {∅} = s` are singleton as `∅ ◉.= s`; moreover, we can always reduce any `set` of sets into the singleton `s` as they are nonempty.

Let's call this subclass of `set` as `set◉`, 
```gm
set◉:
(
	⊆ set,
	∀s: ∈ set◉, s.universe = ◉
),
```
which has only two instance `∅` and `s`.

It is beautiful, isn't it? While, let's recall the **Axiom of regularity (2)**.
```gm
∀x: ∈ set, x ≠ ∅ ⇒ (∃y: ∈ x, y ∩ x = ∅)
```
(this axiom also holds if there exists `y` not a set)

As `s = {s}`, it is of course a set, while `s ∩ {s} = s ∩ s = s ≠ ∅`, which means it violates the **Axiom of regularity (2)**.

I think it is foolish to give up the right of `s = {∅}` to be a set. Remember the mathematicians proposed the `Z` or `ZF` system in order to solve the `Russell's Paradox`, so let's consider that "set"
```
WARNING: this is not a `gm` code,
A = { a ∈ set◉ | a ∉ a }
```
What is `A` here? As `set◉` is a class, we can regrad `A` as a subclass as
```gm
A:
(
	⊆ set◉,
	∀a: ∈ A, a ∉ a
),
```
If so, `∅` is in `A` and as `s = {s}` it is not in `A`; while `A` is a class, even if it is a singleton class with the only instance `∅`, it is distinct from `s`. Indeed, for
```gm
A':
(
	⊆ set◉,
	∀a: ∈ A', a ∈ a
),
```
`A'` is a singleton class with the only instance `s`, is different from `A` as well as `s`.

Then we can try to collect `A` into a set `{∅} = s`, which is not in `A` as `s ∈ {s} = s`. (no contradiction as `A` is not `s`).

What if we fisrtly collect `set◉` into a set `S`, and define `A` as a subset of it? Now, intuitively, `S = {∅, s}`, so that is `S = s` (As I proved above). The important point is that the set `S = s = {∅}` do not contains all of instances of `set◉`, and due to it, `set◉` is a `uncollectible` class (another `uncollectible` case is that a  class is "too big" to be collected, like `orindal`, which is called "proper class" in K.Kunen's book).

Anyhow, even if there is no **Axiom of regularity (2)**, there won't be any contradiction in `set◉` case.

If you are confused about what I have claimed, just remember that `s ◉.= ∅` and `s set.≠ ∅` i.e. `s` and `∅` are identical as elements but distinct as sets. Consequently, at least in `set◉`, there is no such a "universal set" able to replace the `set◉`.

Following this idea, I think the **Axiom of regularity (2)** should relate to the property of universe.

<!-- Another important effect of `set◉` is that it surely not satisfies the **Axiom of infinity (7)**, but it doesn't matter, as I can still construct it in the `pure_set`. -->
<!-- For **Axiom of infinity (7)**, assume the **Axiom of union (5)** let's try the general case at first,
```gm
U: ⊆ ◉, ; universe
0: (∈ set, universe = U, element ∈ empty_class),
1: = {0} ∪ 0 = {0}, 
2: = {1} ∪ 1 = {0, 1} = {0, {0}}, 
3: = {2} ∪ 2 = {0, 1, 2} = {0, {0}, {0, {0}}},
; ...
ℕ-like_space:
(
	⊆ set,
	∀N: ∈ ℕ-like_space,
	N.universe = U,
	0 ∈ ℕ, ∀x: ∈ ℕ, x ∪ {x} ∈ ℕ,
),
``` -->



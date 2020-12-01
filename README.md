# gm

my source gmfile

Go to the [tutorials](https://github.com/GiacomoZheng/gm/wiki) (it has been out of date)

## name of folders
* folders whose name begin and end with `_` are transparent, and it is just used for typesetting; the words insides are just comments.
	- Specially, `_/` and `__/` are transparent.
	- `_vector_space_/` would appear together with `vector_space/` and means the topics related to vector space.
<!-- * There should be no `.gm` file for it.  -->

* **the folder names** are the true name of the `.gm` file inside, like `group/.gm` is the definition of group.

* The names start with `_` but not end with `_` is the ones I think would be deleted or renamed later.

* The folder `gm/h` is the entry of the main files (about the math-related concepts). I may rename it.

* The file `.tree` is the menu this project.

<!-- * The file `.size` records the size of all of the files. -->

## about the better comment
* `; *` is equal to `; NOTE`, meaning it is important.
* `; +` is equal to `; TODO`, meaning I'll add something or complete here later.
* `; ?` is equal to `; WAIT`, meaning I haven't determined about whether I'll keep on use it.
* `; !` is equal to `; WARN`, meaning it is something wrong here, and I'll fix it later.

## TODO
<!-- * add `idempotent` operation -->
* rewrite `R.algebra` as something like `ring.algebra` or some similar thing.
* delete all the `|…|`
* define the `set` and complete the `set.md`
* remove the `_ring_theorem.gm`
* remove the the last part of `field/theorem.gm`
* define the `variable`
* adjust the output of `relation` into `variable` 

## DONE
* adjust all the `Hom`, `End`, `Aut`, into the `structure`

## Definition order (only for reference)
`class`, `set`, `structure` (`category`), other structures like `poset`, `group` e.t.c

**I'll move the below ones to the tutorials.**

## about classlevel
`◉` (universal class) has classlevel 1, and any instance of it has classlevel 0, any subclass of it has classlevel 1 as well. For `class ∋ ◉`, it has classlevel 2 and similarly we can define something with higher classlevel.

## about equal

### absolute equal (or alias)
If no other definitions, `=` means absolute equal, i.e.
```gm
a: = b,
```
To avoid ambiguity, we can use
```gm
a: gm.= b
```
"Absolute equal" means a is defined as a reference (or alias) of b, in other words, all the identifier `a` below can be regarded as `b`. During the complier procedure, things like
```gm
a.something
```
would be replace by
```gm
b.something
```
specially, if `a`, `b` are both has nonzero class level, like if they are both subclass of `◉`, we can also replace
```gm
something ∈ a
```
by
```gm
something ∈ b
```
Remark. `x.a` may have no relationship with `a`, so that it may not equal to `x.b` (which may not even be defined).
### class equal
From the name we can see, the absolute equal induce any class equal. Although it has the name "`class` equal", every identifier with nonzero classlevel (i.e. not an instance of `◉`) defiend a "equal" automatically and recursively for their instances. Intuitively, it means two of its instances are "the same" as this class, like
* a n-dimensional Euclidean space `topological_space.=` a n-dimensional real space.
* a `quotient_group` of `group` `G` `set.=` a `partition` of `G`
* a `cardinal_number` `set.=` a `set` of `set` of `set` of ... of `set`.

As `A.=` is defined automatically with `A`, I do not allow any rewrite on it.

Remark. `gm` is an instance of `◉` so that the absolutely equal `gm.=` is not a class equal. Similarly, we can define anything like `a.=` if `a` is an instance of `◉`.  

Formally speacking, we can define this "`class` equal" with recursion,
* To begin with, `◉.=` satisfies any two instances of it, in other words, `◉` is a `singleton_class`.
* For a subclass `A` of `◉` with every instance `a` of it has an attribute `a.s` as an instance of `◉`, as
```gm
A:
(
    ⊆ ◉,
    ∀a: ∈ A,
    a.s: ∈ ◉
),
f(∀a: ∈ A): ∈ B, ; B ⊆ ◉
```
then for `a, b` instances of `A`, `a A.= b` if and only iff `a ◉.= b` (as `A ⊆ ◉`), `a.s ◉.= b.s` and `f(a) = f(b)` (absolute equal, due to definition of function, ?though I haven't defined the functions well?). Of course, in this example, `A` is still a `singleton class`.
<!-- + function -->
<!-- ? function -->
* To construct a non-singleton class, we need something else than the instance of `◉`, that is the subclass of `◉`,
```gm
A:
(
    ...
    a.s: ⊆ ◉
),
...
```
Intuitively, `a.s` now is a class, to define `a A.= b`, we need `a.s class.= b.s`. Recall the definition of class,
```gm
class:
(
	∋ ◉, ; * it means `class` contains ◉ and all of its subclasses
	; loaction
		sub(∀c: ∈ class):
		(
			⊆ class,
			∀b: ∈ sub(c),
			∀x: ∈ b, x ∈ c
		),
    ...
)
```
so that `a.s class.= b.s` means `class.sub(a.s) = class.sub(b.s)`


which can be defined as `a.s ⊆ b.s` and `b.s ⊆ a.s`. <!-- ? I may define it strictly later -->
```gm
a: (∈ A, a.s = ◉),
b: (∈ A, b.s = A),
```
in this case, `a` and `b` is different from each other in the sense of instance of `A`, as `A` is not equal to `◉` in class sense.
* For `A` with higher classlevel, the idea is similar.<!-- , there is always something simple as `◉` (for classlevel 2, it is `class`)  -->
* To aviod the risk of "the third great crisis in mathematics" and "stack overflow", let's consider about the "self-reference".
```gm
A: (⊆ A),
```
In syntax, it is correct, but it is of course meaningless and would arise some error, since  `⊆ A` do not tell us what the classlevel of `A` is.
```gm
A:
(
    ⊆ ◉,
    ∀a: ∈ A,
    a.s: ∈ A,
),
```
It looks similar to the above one, but I think it should be allowed, as we have got enough info from it,
```gm
... ; continue from above
a: (∈ A, a.s = a)
```
If there is no error in definition of `a`, then `a` would be an instance of `A`. Of course, `a` is legitimate, as it is an instance of
```gm
A':
(
    ⊆ ◉,
    ∀a: ∈ A',
    a.s: = a,
),
```
In pactice, for example, when we define the [`probablity_space`](h/_/ℝ/probability_space/.gm), we would define the `.sample_space` as itself,
```gm
probability_space:
(
	⊆ measure_space,
	(
		∀Ω: ∈ probability_space,
		...
		Ω.sample_space: = Ω,
		...
	)
),
```
I may use this interesting setting in the definition of `set`.

## about inherentance
The main idea is
```gm
a ∈ B ⊆ A ⇒ a ∈ A,
a ⊆ b ∈ B ; may not ⇒ a ∈ B
```
for example,
```gm
set ∈ structure ⊆ class,
set ⊆ ◉ ∈ singleton_class
```
the deeper reason is that, `structure ⊆ class` is defined as
```gm
∀s: ∈ structure, s ⊆ class
```
but say nothing about the higher classlevel.

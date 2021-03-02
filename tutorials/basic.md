个人整理思路用，尚未正式发布

## about classlevel

Roughly speaking, `classlevel` is an measurement of "how abstract a concept is". For the concretest case, `classlevel` 0 case, it means something like the objects around us, like "the chair" you are sitting on and "the screen" you are looking. On the other hand, I use "chair" to mean everything like the thing you are sitting on. We see, "chair" is a little bit "abstract"-er than "the chair" you are sitting on; therefore, they have the `classlevel` 1.

In the beginning time I call the things (concepts) with `classlevel` 0 as `sample` (or `instance`, if you prefer) and the things (concepts) with `classlevel` 1 as `class`. I thought it is enough to differ everything in the world into these two types; of course I was wrong. What the `class` itself is? A `class`? or a `sample`?

To figure out the detail of it, let's look at some daily sentences,
```txt
Giacomo is a person.
A person is a animal.
```
We can see `Giacomo` (me) is a `sample` here and both `person` and `animal` is a class. I used `is-a` to connect a sample to a class and used `a-is-a` to connect a class to another class.

But wait, I said
```txt
person is a class
```
just a moment ago. What does it mean? It means the `classlevel` of `class` has exactly one larger than the `classlevel` of `person` i.e. `class` has `classlevel` 2.

I assigned the `classlevel` 0 to `this chair` and `Giacomo` (me) since I cannot say something like, `you are a this chair` or `I am a Giacomo`. Formally speaking, they are not `instantiable` anymore.

Similar to set theory, I use `∈` to mean `is-a` relation and `⊆` to mean `a-is-a` relation. What different from set theroy is there is a special class called "the universal class" notated as `◉`, meaning the the superclass of every class. Specially, `◉` has `classlevel` 1.

(This symbol is introduced by [@SkyrimWing](https://github.com/SkyrimWing))

## about equal

### absolute equal (or alias)
If no other claims, `=` means absolute equal, i.e.
```gm
a: = b,
```
To avoid ambiguity, we can use
```gm
a: gm.= b
```
"Absolute equal" means `a` is defined as a alias (or reference, pointer) of `b`, in other words, all the identifier `a` below can be regarded as `b`. During the complier procedure, things like
```gm
a.something
```
would be replace by
```gm
b.something
```
Obviously, 
```gm
a ∈ A
```
would be replaced by
```gm
b ∈ A
```
**Remark**: `x.a` may have no relationship with `a`, so that it may not equal to `x.b` (which may not even be defined). 

### class equal
From the name we can see, the absolute equal induce any class equal. Although it has the name "`class` equal", every identifier with nonzero classlevel (i.e. not an instance of `◉`) defiend a "equal" automatically and recursively for their instances. Intuitively, it means two of its instances are "the same" as this class, like
* a n-dimensional Euclidean space `topological_space.=` a n-dimensional real space.
* a `quotient_group` of `group` `G` `set.=` a `partition` of `G`
* a `cardinal_number` `set.=` a `set` of `set` of `set` of ... of `set`.

As `A.=` is defined automatically with `A`, I do not allow any rewrite on it.

**Remark**. `gm` is an instance of `◉` so that the absolutely equal `gm.=` is not a class equal. Similarly, we can define anything like `a.=` if `a` is an instance of `◉`.  

**Warning**: there are still some error under below lines. This version is only reference.

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
```
then for `a, b` instances of `A`, `a A.= b` if and only iff `a ◉.= b` (as `A ⊆ ◉`) and `a.s ◉.= b.s`. Of course, in this example, `A` is still a `singleton class`.

* To construct a non-singleton class, we need something else than the instance of `◉`, that is the subclass of `◉`,
```gm
A:
(
    ...
    a.s: ⊆ ◉
),
...
```
Intuitively, `a.s` now is a class, to define `a A.= b`, we need `a.s class.= b.s`,

<!-- Recall the definition of class,
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
),
```
so that `a.s class.= b.s` means `class.sub(a.s) = class.sub(b.s)` -->

which can be defined as `a.s ⊆ b.s` and `b.s ⊆ a.s`. (I will define it strictly later) <!-- + -->
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
a: (∈ A, a.s = a),
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
but say nothing about the subclass.

# gm

my source gmfile

Go to the [tutorials](https://github.com/GiacomoZheng/gm/wiki) (it has been out of date) or [tutorials folder](https://github.com/GiacomoZheng/gm/wiki) (it is under construction)

## the trouble I met
* I can differ the definitions from statements easily for `classlevel` 0 case, but it would become confusing for the higher case.
* Define `Rel` category (structure).
* What is function?
* Model Theory or Category Theory?
* What is `concept`

## name of folders

* The file [`contents.md`](./contents.md) is the menu this project.

* folders whose name begin and end with `_` are transparent, and it is just used for typesetting; the words insides are just comments.
	- Specially, `_/` and `__/` are transparent.
	- `_vector_space_/` would appear together with `vector_space/` and means the topics related to vector space.
  - There should be no `.gm` file for it. 

* **the folder names** are the true name of the `.gm` file inside, like `group/.gm` is the definition of group.

* The names start with `_` but not end with `_` is the ones I think would be deleted or renamed later.

* The folder `gm/h` is the entry of the main files (about the math-related concepts). I may rename it.


## about the better comment
* `; *` is equal to `; NOTE`, meaning it is important.
* `; +` is equal to `; TODO`, meaning I'll add something or complete here later.
* `; ?` is equal to `; WAIT`, meaning I haven't determined about whether I'll keep on use it.
* `; !` is equal to `; WARN`, meaning there is something wrong here, and I'll fix it later.

## TODO
* add content
  * affine scheme, scheme, projective scheme
  * local ring, graded ring
  * localization 
  * more about `algebra`
  * `ideal` and `sub-algebra` 
  * `dense set` and `dense subset`
  *  [Noetherian ring](https://en.wikipedia.org/wiki/Noetherian_ring)
  * [`Reduced ring`](https://en.wikipedia.org/wiki/Reduced_ring) and `Reduced algebra`
  * a `ring` is `C.algebra` where `C` is the center of it .
* define the `set` and complete the `set.md`
* rewrite `function` with class.
* delete all the `|…|`
* define the `variable`
* adjust the output of `relation` into `variable` 
* remove the `_ring_theorem.gm`
* remove the the last part of `field/theorem.gm`
* adjust all the `Hom`, `End`, `Aut`, into the `structure`

<!-- ## DONE -->
<!-- * add `idempotent` operation -->
<!-- * rewrite `R.algebra` as something into `algebra` -->

<!-- ## Definition order (only for reference)
`class`, `set`, `structure` (`category`), other structures like `poset`, `group` e.t.c -->

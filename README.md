# gm

my source gmfile

Go to the [tutorials](https://github.com/GiacomoZheng/gm/wiki) (it has been out of date)

## the trouble I met
* I can differ the definitions from statements easily for `classlevel` 0 case, but it would become confusing for the high case.

## name of folders
* folders whose name begin and end with `_` are transparent, and it is just used for typesetting; the words insides are just comments.
	- Specially, `_/` and `__/` are transparent.
	- `_vector_space_/` would appear together with `vector_space/` and means the topics related to vector space.
<!-- * There should be no `.gm` file for it.  -->

* **the folder names** are the true name of the `.gm` file inside, like `group/.gm` is the definition of group.

* The names start with `_` but not end with `_` is the ones I think would be deleted or renamed later.

* The folder `gm/h` is the entry of the main files (about the math-related concepts). I may rename it.

* The file [`contents.md`](./contents.md) is the menu this project.
<!-- * The file `.tree` is the menu this project. -->

<!-- * The file `.size` records the size of all of the files. -->

## about the better comment
* `; *` is equal to `; NOTE`, meaning it is important.
* `; +` is equal to `; TODO`, meaning I'll add something or complete here later.
* `; ?` is equal to `; WAIT`, meaning I haven't determined about whether I'll keep on use it.
* `; !` is equal to `; WARN`, meaning it is something wrong here, and I'll fix it later.

## TODO
* define the `set` and complete the `set.md`
* rewrite `function` with class as domain.
* rewrite `R.algebra` as something like `ring.algebra` or some similar thing.
* delete all the `|…|`
* define the `variable`
* adjust the output of `relation` into `variable` 
* remove the `_ring_theorem.gm`
* remove the the last part of `field/theorem.gm`

<!-- ## DONE -->
<!-- * adjust all the `Hom`, `End`, `Aut`, into the `structure` -->
<!-- * add `idempotent` operation -->

<!-- ## Definition order (only for reference)
`class`, `set`, `structure` (`category`), other structures like `poset`, `group` e.t.c -->

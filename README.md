<h1> <center> gm </center> </h1>

my source gmfile

Go to the [tutorials](https://github.com/GiacomoZheng/gm/wiki) (it has been out of date)

## name of folders
* folders named `_` are transparent, and it is just used for typesetting.
<!-- * There should be no `.gm` file for it.  -->

* **the folder names** are the true name of the `.gm` file in it, like `group/.gm` is the definition of group.

* The names start with `_` is the ones I think would be deleted or renamed later.

* The folder `gm/h` is the entry of the main files (about the math-related concepts). I may rename it.

* The file `.tree` is the menu of the whole file

* The file `.size` records the size of all of the files.

## about the better comment
* `; *` is equal to `; NOTE`, meaning it is important.
* `; +` is equal to `; TODO`, meaning I'll add something or complete here later.
* `; ?` is equal to `; WAIT`, meaning I haven't determined about whether I'll keep on use it.
* `; !` is equal to `; WARN`, meaning it is something wrong here, and I'll fix it later

## about inherentance
```gm
set: ∈ structure,
group: ⊆ set,
; then automatically we have
group ∈ structure,
; in addition,
group.homomorphism ⊆ set.homomorphism
group.epimorphism ⊆ set.epimorphism
; and so on
; ! what about ≌ or, in general, the other classlevel 0 attributes defined in struture?
; ! A fatal problem occurs, a subclass of a nonempty_class might be an empty_class
; ! also, the a subclass of a universal structure might not be a universal structure
```

## TODO
* delete all the `|…|`
* adjust all the
    - Hom
    - End
    - Aut
* remove the `_ring_theorem.gm`
* remove the the last part of `field/theorem.gm`
* define the `variable`
* adjust the output of `relation` into `variable` 

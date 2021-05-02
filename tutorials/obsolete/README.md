# what is gm

* Object Oriented Programming Language
    - with structural type system
    - with countable classleval. (there will be class of samples/instances, "class" of classes, and forth)
* static policy for (pure) locations and dynamic policy for (pure) pointers
    ```gm
    A: ∈ set, ; static policy
    B: = A ; dynamic policy
    ```
* static scope
    - with `Constant Block` and `Temprary Block`:
    ```gm
    A: ( ... ), ; Constant Block
    ( ... ) ; Temprary Block
    ```
* Does not distinguish between the quantities (loctions/varibales in Jragon Book and l-value in `C`) and values (r-value)
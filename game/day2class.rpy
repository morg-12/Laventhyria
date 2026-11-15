label class_2:
    play music "Main_BGM.ogg"
    scene bg_classroom
    with fade
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Quarter One{/font}"
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Day Two{/font}"
    $ player.show("idle",genpos,dis,True)
    p "Yesterday was pretty fun."
    p "I wonder what we're learning about today."
    p "Hold on, I can probably check my schedule."
    pause 0.5
    play sound "Bell.ogg"
    p "No time! Well, I guess the teacher'll tell us what we're studying."
    scene bg_classroom
    t "Hello, class! Today, we will be studying Echelon Form, Row Reduced Echelon Form, and Row Reduction!"
    t "First off, what {i}is{/i} Echelon Form, anyway? Well, to know how we can have a matrix in Echelon Form and to identify one that is, we need to know what a {b}leading entry{/b} is."
    t "A {b}leading entry{/b} is the first non-zero entry of a row."
    t "Now that we've got that out of the way, let's go over the conditions for a matrix to be in Echelon Form.\nFirst, all of its zero rows, if it has any, must be at the bottom. Second, the leading entry of a given row must be to the right of any leading entries in the row above it, if there are any."
    t "Finally, all of the entries below a leading entry must be zero. Now, let's identify some matrices!"
    show c2m1 at lefpos
    with dis
    show c2m2 at ripos
    with dis
    t "Let A be the matrix on the left and B be the matrix on the right."
    menu:
        t "Which, if any, of these two matrices is in Echelon Form? Raise your hand when you're done and tell me what your answer is!"
        "Raise hand":
            pass
    menu:
        t "Yes, you there! [pname], if memory serves? What is your answer?"
        "Neither":
            jump c2q1wrong
        "A":
            jump c2q1right
        "B":
            jump c2q1wrong
        "Both":
            jump c2q1wrong
label c2q1wrong:
    t "Not quite, [pname]! Let's go through both of the matrices together."
    hide c2m1
    with dis
    hide c2m2
    with dis
    show c2m1 at genpos
    t "Let's first check if there are any zero rows in matrix A." 
    pause 0.5
    t "There is one, and it's at the bottom. Great! That's our first condition off the list."
    t "Now, for leading entries. In matrix A, the leading entry of the first row, 2, is all the way on the left, and all the entries below it are zero. The leading entry of row 2 is 5, because it's the first nonzero entry in that row. Sure enough, 5's to the right of 2. Since the last row's a zero row, the entry below 5 is 0."
    t "So it looks like we've got ourselves "
    







jump break_2
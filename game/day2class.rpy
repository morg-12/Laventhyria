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
            t "Excellent work, [pname]! That's correct!"
            jump c2postq1
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
    with dis
    t "Let's first check if there are any zero rows in matrix A." 
    pause 0.5
    t "There is one, and it's at the bottom. Great! That's our first condition off the list."
    t "Now, for leading entries. In matrix A, the leading entry of the first row, 2, is all the way on the left, and all the entries below it are zero. The leading entry of [row2] is 5, because it's the first nonzero entry in that row. Sure enough, 5's to the right of 2. Since the last row's a zero row, the entry below 5 is 0."
    t "So it looks like we've got ourselves a matrix in Echelon Form! How about matrix B?"
    hide c2m1
    with dis
    show c2m2 at genpos
    with dis 
    t "Matrix B doesn't have any zero rows, so we don't have to worry about those! The leading entry of [row1] is 3 and the leading entry of [row2] is 2, but they're in the same column!" 
    t "That means that matrix B isn't in echelon form, since all entries below a leading entry need to be zero and any leading entry needs to be to the right of the one in the row above it."
    t "So that means that matrix A is in echelon form, while B is not!"
    t "Hopefully that's helped you understand what you did wrong there. Now, on to the next topic!"
    hide c2m2
    with dis
    jump c2postq1
label c2postq1:
    hide c2m1
    with dis 
    hide c2m2
    with dis
    t "Now, it's all well and good to have your matrices in Echelon Form, but there's another form that makes some other calculations easier. This form is called Row Reduced Echelon Form, or RREF for short."
    t "As you might imagine, the rules for having a matrix in RREF are stricter than just having it in Echelon Form. In fact, we have two new rules!"
    t "A matrix in echelon form is in RREF if all of its leading entries, if it has any, are equal to one, and if leading entries are the only nonzero entry in their respective column."
    t "Now, let's take a look at some matrices in echelon form and determine if they're in RREF!"
    show c2m4 at lefpos
    with dis 
    show c2m3 at ripos
    with dis 
    t "Let matrix A be the one on the left and matrix B be the one on the right."
    menu:
        t "Which of these two matrices is in RREF, if any? Raise your hand and tell me when you're ready!"
        "Raise hand":
            pass
    menu:
        t "[pname]? Go for it!"
        "None":
            jump c2q2wrong
        "A":
            jump c2q2wrong
        "B":
            t "That's right! Excellent work once again, [pname]!"
            jump c2q3
        "Both":
            jump c2q2wrong
label c2q2wrong:
    t "That's not quite right, but thank you for putting in your best effort."
    t "Now, let's go over this answer together."
    hide c2m3
    with dis
    hide c2m4
    with dis
    show c2m4 at genpos
    with dis
    t "Let's go over A first. A has two nonzero rows and one zero row. The leading entries are both 1, so that's that off the list. However, in [col3], there's an eight above the one. Since that one is a leading entry, there should be nothing else in its row. The fact that there is means that while A is in echelon form, it is not in RREF."
    hide c2m4
    with dis 
    show c2m3 at genpos
    with dis
    t "Next up is B. You might notice that B looks very similar to A, but with a zero where A had an eight. This will be important later."
    t "B has two nonzero rows, and the leading entries of both are 1, so that's off the list. Next, we have to check the columns of each leading entry. [col1], where [row1]'s leading entry is, is all zeroes except for the leading entry, and the same can be said for [col3], where [row2]'s leading entry is."
    t "This means that matrix B {i}is{/i} in fact in both echelon form and RREF."
    hide c2m3
    with dis 
    show c2m4 at lefpos
    with dis 
    show c2m3 at ripos
    with dis 
    t "Like I mentioned going into this one, that difference between A and B, slight as it was, impacted whether the matrix was in RREF or not. Since matrix A had a nonzero entry above a leading entry, while matrix B didn't, A is not in RREF, while B is!"
    hide c2m3
    with dis 
    hide c2m4
    with dis 
    t "Hopefully my explanation helped you understand where you went wrong. Now, let us venture forth!"
    jump c2q3
label c2q3:
    t "We know how to tell the difference between matrices in RREF, Echelon Form, and neither now, so why don't we try and tell the difference?"
    scene bg_classroom
    with dis
    while (matNum < 5):
        menu:
            "Identify any and all of the matrices below that are in RREF. When you're done, raise your hand to call me over so that I can check over your answers."
            "{image=c2m5}"if not selectedMatrices[0]:
                $ selectedMatrices[0] = true
            "{image=c2m6}"if not selectedMatrices[1]:
                $ selectedMatrices[1] = true
            "{image=c2m7}"if not selectedMatrices[2]:
                $ selectedMatrices[2] = true
            "{image=c2m8}"if not selectedMatrices[3]:
                $ selectedMatrices[3] = true
            "{image=c2m9}"if not selectedMatrices[4]:
                $ selectedMatrices[4] = true
            "All RREF Matrices have been selected (Raise your hand)":
                $ matNum = 5
        $ matNum += 1
    jump c2q3solutions
label c2q3solutions:
    $ matNum = 0
    t "Okay, let's see here."
    $ boolsList = multiChecker(correctMatrices,True,receivedAnswers=selectedMatrices)
    t "You said that the statement that {image=c2m5} is in RREF was [selectedMatrices[0]]. It was [correctMatrices[0]]."
    t "You said that the statement that {image=c2m6} is in RREF was [selectedMatrices[1]]. It was [correctMatrices[1]]."
    t "You said that the statement that {image=c2m7} is in RREF was [selectedMatrices[2]]. It was [correctMatrices[2]]."
    t "You said that the statement that {image=c2m8} is in RREF was [selectedMatrices[3]]. It was [correctMatrices[3]]."
    t "You said that the statement that {image=c2m9} is in RREF was [selectedMatrices[4]]. It was [correctMatrices[4]]."
    t "Out of these [len(selectedMatrices)] questions, you correctly answered [rightCounter(boolsList)[0]], meaning that you were [rightCounter(boolsList)[1]*100]\% correct."
    if(not boolsList[0]):
        scene bg_classroom
        with dis 
        t "So you got the first one wrong, huh? Let's go over it together!"
        show c2m5 at genpos, sxtnX
        t "The leading entry of [row1] is 1. However, the leading entry of [row2] is 2. For a matrix to be in RREF, all of its leading entries must be 1." 
        t "As such, this matrix is not in RREF."
    if(not boolsList[1]):
        hide c2m5
        with dis
        t "The second one's wrong, is that right?"
        pause 0.25
        t "Okay, let's go over it together!"
        show c2m6 at genpos, sxtnX
        with dis
        t "Neither row in this matrix has any leading entries. Since there's no leading entries and no nonzero entries, we don't need to worry about any issues with leading entries."
        t "As such, this matrix is in RREF."
    if(not boolsList[2]):
        hide c2m5
        with dis 
        hide c2m6
        with dis 
        t "You got the third one wrong, then? I'll walk you through it, and hopefully you won't get any similar problems wrong in the future!"
        show c2m7 at genpos, sxtnX
        with dis 
        t "In this matrix, the only leading entry is in the [row2], and all other entries in its column, [col1], are zero. However, [row1], [row3], and [row4] are zero rows, and [row1] is not at the bottom. As such, this matrix is not in echelon form and therefore cannot be in RREF."
    if(not boolsList[3]):
        hide c2m5
        with dis 
        hide c2m6
        with dis 
        hide c2m7
        with dis 
        t "The fourth one, then? Let's go for it!"
        show c2m8 at genpos, sxtnX
        with dis 
        t "This matrix only has one row. As such, there are no entries in the columns above or below the leading entry. Now, to check the leading entry itself."
        t "The leading entry is the first in its row. Since the leading entry is 1 and there's no entries above, below, or to the left of it that would need to be 0, this matrix is indeed in RREF."
    if(not boolsList[4]):
        hide c2m5
        with dis 
        hide c2m6
        with dis 
        hide c2m7
        with dis 
        hide c2m8
        with dis 
        t "Okay, the fifth one! Let's figure this out."
        show c2m9 at genpos, sxtnX
        with dis 
        t "The leading entry in [row1] is 1, in the first column. The leading entry in [row2] is also 1, in the third column. In [row2], all of the entries to the left of the leading entry are 0, while the entry above it is also 0."
        t "The leading entries are 1, all of the entries in their respective rows to the left of them, if any, are zero, and all of the entries in their respective columns are zero, meaning that this matrix is in RREF."
        jump c2postq3
label c2postq3:
    hide c2m3
    with dis
    hide c2m4
    with dis 
    scene bg_classroom
    with dis 
    t "Well, now you know what a matrix in RREF looks like and how to identify it. But how do you get a matrix into RREF, anyway?"
    t "Well, there's an algorithm you can use for that job! It's called the Row Reduction Algorithm, and it's used to, well, reduce a matrix to RREF!"
    t "First! You swap [row1] with a lower row so that the leftmost nonzero entry in all the land's in the first row. Or, well, in all the matrix."
    t "Second! You scale the first row so that its leading entry is equal to one."
    t "Third! Use row replacement to make sure that all entries above and below this leading entry are equal to zero."
    t "Then repeat this for the second row, the third row, and so on until you're out of rows!"
    t "This is probably a bit difficult to understand from me just saying it, so let me show you!"
    show c2m10 at lefpos
    with dis 
    t "Take this matrix here. How can we get it into RREF?"
    show c2rowop1 at ripos
    with dis 
    t "Well, we first need to swap [row1] and [row3], since [row3] has the leftmost leading entry. Since [row3] and [row4] both have a leading entry of 12 in the first column, we need to subtract [row3] from [row4] to make all of the entries in [col1] besides the leading entry of [row1] zero."
    t "This row operation is shown on the right side of the board."
    t "We could have also swapped [row1] with [row4], then subtracted [row4] from [row3]."
    hide c2m10
    with dis 
    hide c2rowop1
    with dis
    show c2m11 at lefpos
    with dis 
    t "The row operation I described earlier results in the matrix shown."
    show c2rowop2 at ripos
    with dis 
    t "We'll now need to divide [row1] by 12 to make its leading entry 1, after which we can move on to the next row. [row2] already has the leftmost leading entry of the remaining rows, so it doesn't need to swap with any rows."
    t "Since the leading entry of [row3] is 42 and the leading entry of [row2] is 6, we subtract 7[row2] from [row3] to make the entry of [row1] in [col2] zero."
    hide c2m11
    with dis 
    hide c2rowop2
    with dis 
    show c2m12 at lefpos
    with dis
    t "This makes it so that all of the entries in [col2] are zero, save for the leading entry of [row2]. The matrix now appears as shown on the board."
    show c2rowop3 at ripos
    with dis
    t "Since [row4] only contains entries in [col3], while [row3] contains entries in [col3] and [col4], it is best to swap the two."
    hide c2m12
    with dissolve
    hide c2rowop3
    with dis 
    show c2m13 at lefpos
    with dis 
    t "All of the rows have entries in [col3], so it is necessary to row replace to make all entries zero except for the leading entry of [row3]."
    show c2rowop4 at ripos
    with dis
    t "In [row1], the entry in [col3], 3, is equal to negative one-eighth of -24, the entry in [col3] for [row3]. As such, we must subtract -[row3]/8, or add [row3]/8, to [row1]. The entry in [col3] for [row2] is 2, which is negative one-twelfth of the leading entry in [row3]. As such, we must subtract -[row3]/12, or add [row3]/12, to [row2]."
    t "The entry in [col3] for [row4] is -54, which is equal to 9*(-6). -6 is one fourth of -24, which is the leading entry in [row3]. 9*1/4=9/4. This means that we must subtract 9[row3]/4 from [row4]. Finally, we must scale the leading entry of [row3] so that it is equal to one. This means dividing [row3] by -24."
    hide c2m13
    with dissolve
    hide c2rowop4
    with dis 
    show c2m14 at genpos
    with dis
    t "Finally, since the only remaining entry in [row4] is 1, no more row operations are necessary. This results in the matrix shown on the board here. Any questions?"
    hide c2m14
    with dis 
    $ al.show("idle",genpos,dis,true)
    r1 "I think I remember this matrix. The Identity Matrix, right?"
    scene bg_classroom
    with dis
    t "Correct, Alva! This is in fact [id4], the 4-by-4 Identity Matrix. Pretty interesting, don't you think?"
    t "Row reduction's a pretty useful thing to know. It can even be used to help you solve a linear equation! But that's a topic for tomorrow."
    jump c2q4
label c2q4:
    t "For now, we've got another fun practice problem! I'll put it up on the board. When you're done, call me over to take a look at it."
    show c2m15 at genpos
    with dis 
    t "Please row reduce the shown matrix. When you're done, raise your hand so I can come over and check over your answers."
    $ boolies = matrixProblem(righties)
    # t "[boolies]"
    hide c2m15
    with dis 
    $ rice = []
    $ i = 0
    while i<len(boolies):
        $ rice.append(rightCounter(boolies[i]))
        t "You got [rice[i][0]] entries in Row [i] right, meaning that you got [rice[i][1]*100]\% of them right."
        # t "[rice]"
        $ rightynum += rice[i][0]
        $ rightyperc += rice[i][1]
        $ i+=1
    $ rightyperc /= i
    t "Overall, you got [rightynum] of the [len(boolies)*len(boolies[0])] entries in the matrix correct, or [rightyperc*100]\%."
    if (rightyperc<1):
        t "Okay, so you got [len(boolies)*len(boolies[0])-rightynum] of the [len(boolies)*len(boolies[0])] entries wrong here. Let's go over how to do this right."
        show c2m15 at lefpos
        with dis 
        show c2rowop5 at ripos
        with dis
        t "We begin with the matrix shown on the left side of the board. [row1]'s leading entry is in [col2], while [row2] and [row3]'s leading entries are in [col1]. As such, we need to swap [row1] with a lower row to make it have the leftmost leading entry."
        t "Since we also have to scale this row to make the leading entry equal to 1, it's easier to take one in which the leading entry is either 1 or -1, as neither of those would require dividing the row to bring the leading entry to 1." 
        t "This means that the best option is [row2]. [row3] also has an entry in the first column, so we need to row replace to make its leading entry 0."
        t "-2, the leading entry of [row3], is twice -1, [row2]'s leading entry. As such, we can subtract 2[row2] from [row3] to make it zero."
        hide c2m15
        with dis 
        hide c2rowop5
        with dis 
        show c2m16 at lefpos
        with dis 
        t "This results in the matrix shown on the left."
        show c2rowop6 at ripos
        with dis
        t "The leading entry of [row1] is -1, and we need it to be 1, so we can multiply [row1] by -1."
        t "Now, we move on to [row2]. [row2] already has one of the leftmost leading entries, so we just need to scale it. -3/-3 = 1, so we divide [row2] by -3 to make its leading entry 1. [row3]'s leading entry of 1 is equal to -1/3*-3, the leading entry of [row2] before this set of row operations. As such, we can subtract -[row2]/3, or add [row2]/3, to [row3]."
        hide c2m16
        with dis
        hide c2rowop6
        with dis 
        show c2m17 at lefpos
        with dis 
        t "That series of row operations leaves us with the matrix on the left."
        show c2rowop7 at ripos
        with dis
        t "Since [row1] has an entry in the same column as the leading entry of [row2], it is necessary to row replace to make this entry 0. The entry is 2, twice [row2]'s leading entry of 1, so we can subtract 2[row2] from [row1]. Since [row3] is a zero row and it's the bottom row, nothing needs to be done involving it."
        hide c2rowop7
        with dis 
        hide c2m17
        with dis
        show c2m18 at genpos
        with dis
        t "This results in the matrix shown on the board."
    else:
        show c2m18 at genpos
        with dis
        t "Congratulations, [pname]! You correctly row reduced the matrix!"
    t "Now, let's continue to the last parts of the lesson."
    jump c2postq4
label c2postq4:
    scene bg_classroom with dis
    t "Here are a few more terms that'll be important tomorrow and later on in this course."
    t "A {b}pivot position{/b} in a matrix A is a location in A that corresponds to a leading 1 in the RREF of A. A {b}pivot column{/b} of A is a column of A that contains a pivot position."
    show c2m10 at lefpos
    with dissolve
    show c2m14 at ripos
    with dis 
    t "Let's go over the concept by looking at the matrix on the left of the board and its RREF, which we found together earlier."
    t "In the matrix on the left, every column is a pivot column because in its RREF, shown on the right, every column has a leading entry."
    t "Now, let's look at the matrix from the problem we just did."
    hide c2m10
    with dis 
    hide c2m14
    with dis 
    show c2m15 at genpos
    with dis 
    while (colmNum < 4):
        menu:
            "Which of the following columns are pivot columns? Select all that apply. When you're done selecting, please raise your hand to call me over so I can check them."
            "[col1]"if not selCols[0]:
                $ selCols[0] = true
            "[col2]"if not selCols[1]:
                $ selCols[1] = true
            "[col3]"if not selCols[2]:
                $ selCols[2] = true
            "[col4]"if not selCols[3]:
                $ selCols[3] = true
            "All Pivot Columns have been selected (Raise your hand)":
                $ colmNum = 4
        $ colmNum += 1
        t "Let's see here."
        $ beans = multiChecker(corrCols,True, receivedAnswers = selCols)
        t "You said that the statement that [col1] is a pivot column was [selCols[0]]. It was [corrCols[0]]."
        t "According to you, the statement that [col2] is a pivot column was [selCols[1]]. It was [corrCols[1]]."
        t "According to you, the statement that [col3] is a pivot column was [selCols[2]]. It was [corrCols[2]]."
        t "You said that the statement that [col4] is a pivot column was [selCols[3]]. It was [corrCols[3]]."
        t "Out of these [len(selCols)] questions, you correctly answered [rightCounter(beans)[0]], meaning that you were [rightCounter(beans)[1]*100]\% correct."
        if (rightCounter(beans)[1]<1):
            t "Okay, so you were a bit off on the pivot columns. Let's go over it."
            show c2m15 at lefpos
            with dis
            show c2m18 at ripos
            with dis
            t "When we row reduced the matrix on the left, we found that [row1] and [row2] had their leading entries in [col1] and [col2], respectively."
            t "This means that their pivot columns are [col1] and [col2]."
            t "At least in this class, when you're doing these types of problems, you'll likely be finding the pivot columns after row reducing the matrix itself, so if you forgot what the row reduced matrix looked like, that won't really be an issue for you moving forward."
        else:
            t "Nice work there. Or, well, nice work remembering."
        t "Now, let's go back to basic echelon form for a second."
    hide c2m15
    with dissolve
    hide c2m18
    with dis 
    show c2me1 at genpos
    with dis
    t "On the board is the basic structure for a matrix in echelon form. While the number of rows and columns may not match this across all echelon form matrices, this can still be a helpful tool in identifying one in the wild."
    t "You'll especially want to remember the details about where nonzero digits would go. Remember, in echelon form, the entries in the columns above a leading entry don't need to be zero."
    t "Well, that's all for today. Have a good break period, and remember to keep all this knowledge in good shape for tomorrow."
    #call screen matrixproblem()
jump break_2
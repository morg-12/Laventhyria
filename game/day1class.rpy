label class_1:
    scene bg_classroom
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Quarter One{/font}"
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Day One{/font}"
    $ player.show("idle",genpos,dis,True)
    p "It's the first day of school."
    p "And from what it sounds like, this one is pretty hardcore."
    if (noEep==1):
        p "I was up all night last night, and I'm not sure how well I can make it through..."
    menu:
        "I'm so excited for class, though!":
            p "That's right!"
            p "I was up all night thinking about how excited I was to meet my classmates and start my classes!"
        "I've been dreading this...":
            p "I was up all night worrying about how it'll go. Will they like me? What kind of people are they?"
            p "I mean, I guess I know that Lily'll be here."
            default word = "something."
            if (dmp.aff == 0.2):
                $ word = "comforting."
            elif (dmp.aff >= 0.10):
                $ word = "calming."
            elif (dmp.aff >= 0.01):
                $ word = "something, I guess?"
            elif (dmp.aff >= 0):
                $ word = "okay."
            elif (dmp.aff >= -0.1):
                $ word = "irritating."
            elif (dmp.aff >= -0.2):
                $ word = "annoying."
            p "That's [word]"
    play sound "Bell.ogg"
    p "Oh, the bell's rung!"
    p "Regardless of my doubts and my worries, I should give it my all!"
    p "O-or at least the best I can..."
    p "H-hopefully that's enough..."
    $ player.hide(dis,true)
    t "All right, settle down now, class."
    t "I hope that we'll have a productive session today."
    t "You may call me 'Your Lordship'."
    t "Today, we'll be talking about Systems of Linear equations. Oh, and we'll also be talking about some elementary row operations. You probably don't know what that is yet, but you will."
    t "So, I'm sure you all know what linear equations are, right?"
    t "Well, if you don't, linear equations have the form a₁x₁+a₂x₂+...+aₙxₙ=b, where a₁,...,aₙ and b are coefficients, x₁,...,xₙ are variables or unknowns, and n is the dimension, or the number of variables."
    t "So, here's some examples of linear equations to help it stick a bit better in your heads."
    t "2x₁+4x₂=4 is a line in two dimensions, as the keen-eyed among you might be able to tell from how the highest subscript is 2."
    t "Now, then, how many dimensions do you think 3x₁ + 2x₂ + x₃ = 6 is in?"
    $ renpy.say(t, f"Ah, the blue-haired {p1genterm} in the front!")
    default ansRight = false
    default ansExp = false
    menu: 
        "One!":
            $ ansRight = false
        "Two!":
            $ ansRight = false
        "Three!":
            $ eepNum = renpy.random.random()
            if(eepNum < 0.01*(2)**noEep and noEep != 0):
                p "3!"
                p "{i}Curses! I messed up and said it wrong!{/i}"
                t "Your answer is..."
                $ ansRight = true
                t "{size=+20}Wrong!"
            else:
                $ ansRight = true
        "3!":
            $ eepNum = renpy.random.random()
            if(eepNum < 0.01*(2)**noEep and noEep != 0):
                p "Three!"
                p "{i}Curses! I messed up and said it wrong!{/i}"
                t "Your answer is..."
                $ ansRight = true
                t "{size=+20}Correct!"
            else:
                $ ansRight = false
                t "This one was a bit of a trick question, so I must apologize."
                t "It does feel good seeing people fall for it, though."
                t "Now, this isn't quite in my job description, but I'll tell you it anyway. When you put an exclamation mark after an integer, like I did with 3!, it's called a factorial and means that you multiply the integer with all the integers that come before it."
                t "So like here, 3! = 3*2*1=6, so that's why you're wrong."
                t "Your mind was certainly in the right place, though! Heehee!"
                $ ansExp = true
        "N!":
            $ ansRight = false
    if (ansRight):
        t "Excellent work, young...?"
        $ renpy.say(p,f"{pname}, Your Lordship.")
        t "Such respect! I like that in a pupil."
    elif (ansExp):
        t "Teehee! Thanks for amusing me, young..."
        $ renpy.say(p,f"{pname}, Your Lordship.")
        t "Such respect! I like that in a pupil."
    else:
        t "That's not right, but I can see you were trying pretty hard there."
        t "The number of variables can tell you the dimension of a linear expression. For example, if there's three variables, it's going to have three dimensions, like here."
    t "Now, when you have a set of one or more linear equations, you've got a linear system of equations!"
    t "The solutions of a system of linear equations are pretty important. Now, you may be wondering how we describe those solutions, or even what they are."
    t "The set of solutions for a linear system is the set of all possible values of x₁,x₂,x₃,...,xₙ that satisfy all of the equations. Not just one, not just two, not just n-1, alllll of them."
    t "For any system of linear equations, regardless of the dimension or the number of equations, there's only three possible solution cases. There's either one unique solution, infinite solutions, or no solutions."
    t "We can use these things called Elementary Row Operations to find the solution set for a system."
    t "The first is called Replacement/Addition. In this operation, you add a multiple of one row to another. Another is Interchange, where you interchange two rows. Finally, there's Scaling, where you multiply a row by a nonzero scalar."
    t "An important thing to remember is that conducting row operations does not change the solution set."
    show c1rowop1 at genpos
    with dis
    t "Let's go through an example. R₁ is the linear equation x₁-2x₂+x₃=0, R₂ is 2x₂-8x₃=8, and R₃ is 5x₁-5x₃=10. We can start by adding R₂ to R₁, or R₁+R₂→R₁. This eliminates the x₂ term in R₁."
    scene bg_classroom
    show c1rowop2 at genpos
    with dis
    t "Next, we can divide R₂ by two, R₂/2→R₂, which makes the new value of R₂ x₂-4x₃=4. This'll make it a bit easier to deal with later. We can then subtract 5R₁ from R₃ to eliminate the x₁ term. This leaves the third row as 10x₂-10x₃=10."
    t "You may notice that R₂ and R₃ both only have x₂ and x₃ terms. This means that we can use replacement to have just one variable. Since R₃ has 10x₂ and R₂ has x₂, it's easier to eliminate x₂ by subtracting 10R₂ from R₃."
    scene bg_classroom
    show c1rowop3 at genpos
    with dis
    t "Subtracting 10x₂-40x₃=40 from 10x₂-10x₃=10 leaves us with 30x₃=-30, which simplifies to x₃=-1. We can now substitute this into the other equations. Substituting it into R₁ results in x₁+7=8, which means that x₁=1. Substituting it into R₂ results in x₂+4=4, so x₂=0."
    t "This means that the solution set for the system R₁: x₁-2x₂+x₃=0, R₂: 2x₂-8x₃=8, R₃: 5x₁-5x₃=10 is the point (1,0,-1)."
    scene bg_classroom
    t "It's a bit awkward to keep writing x₁, x₂, and x₃, right? Fortunately, these can be rewritten as augmented matrices. For example, {image=c1lq1} can be written as the augmented matrix {image=c1am1}. The vertical line is basically a reminder that the columns before it are the coefficients to x₁, x₂, and x₃."
    t "Now, here's a couple of important terms. A linear system is {b}consistent{/b} if it has ≥1 solution. It could have one particular solution or it could have infinitely many, but as long as it has solutions, it's consistent." 
    t "Two matrices are {b}row equivalent{/b} if a sequence of row operations can transform one into the other. An important thing about row equivalence is that if the augmented matrices of two linear systems are row equivalent, they have the same solution set."
    t "Now, here's something to hopefully get it to stick a bit better."
    t "Suppose that A={image=c1m1}, B={image=c1m2}, C={image=c1m3}, and {image=c1v1}. Are A and B row equivalent? What about A and C? Are the augmented matrices \n(A|b⃗) and (C|b⃗) consistent?"
    t "I'll give you some time to work on this, so move forward when you have an answer for both."
    menu:
        t "Have you finished?"
        "Yes":
            pass
    t "Well, to answer the first part, we need to think about what row operations we could use to make them the same. For A and B, if we subtract row 2 of A from row 1, that leaves us with B. However, there's no way that we can make the second row have two 0s with the rows we have."
    t "As such, A and B are row equivalent, while A and C are not."
    t "For the question about (A|b⃗) and (C|b⃗), it's a bit easier to think of these as a linear system. In A, the two equations are x₁+x₂=1 and x₂=1. We can find a solution from these. If x₂=1 and x₁+x₂=1, then the solution is (0,1). Since it has a solution, this augmented matrix is consistent."
    t "For (C|b⃗), we get x₁+x₂=1 and 0x₁+0x₂=1. Since 0 is not equal to 1, there are no solutions. As such, this augmented matrix is not consistent."
    t "Okay, we've finished all of our course content for today, so it's time for the break!"
    scene bg_classroom
    $ dmp.show("idle", genpos, dis, True)
    dpc "Hi again, [pname]! It's nice to be able to talk to you again!"
    menu:
        "Nice to see you too, [dname]!":
            $ dmp.aff += 0.1
            dpc "Thanks!"
        "Ah, it's that one annoying person who can't stop talking.":
            $ dmp.aff -= 0.1
            dpc "I see you haven't changed at all since our last meeting. What, have you never heard of acting like a decent person to people?"
    jump introductions
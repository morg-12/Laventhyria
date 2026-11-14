label break_1:
    menu:
        "What would you like to do during your break?"
        "Talk to Alva":
            if not alTalk:
                jump alva1
            jump alvaBreak1
        "Talk to Gwynedd":
            if not gwTalk:
                jump gwy1
            jump gwyBreak1
        "Talk to Hoshi":
            if not hoTalk:
                jump ho1
            jump hoBreak1
        "Talk to Lily":
            jump dmpBreak1
        "Go up to the rooftop":
            jump roofBreak1
        "Go into the hallway":
            jump hallBreak
label roofBreak1:
    "You feel a calling to the rooftop."
    scene bg_staircase
    "You walk up the staircase. It is quiet, your only companion the echo of your footsteps in the hall."
    "Until..."
    unk "It is very nice to meet you."
    p "What in the-"
    unk "Oops, sorry! I forgot that I was still a disembodied voice."
    unk "A moment, please..."
    $ gb.show("",genpos,dis,True)
    g "That's better."
    p "Are you... a sentient piece of garlic bread?"
    g "I suppose you could say that. I do, however, go by another name."
    g "The Patron of the Order of the Chosen of the Garlic Bread, the Garlic Bread itself."
    g "At your service."
    p "Okay, so why are you meeting with me?"
    g "I felt that you may be a good fit for my Order."
    p "What makes you think that?"
    g "Just a feeling, nothing more."
    g "I haven't Chosen you yet, of course, but if I feel that you will be a good fit, it may only be a matter of time..."
    p "Okay, so what will this impact for me?"
    g "Nothing much, really. I'll just be keeping an eye on you, you know? Seeing if you'd make a good fit for my Order or not."
    g "Anyways, fare thee well!"
    $ gb.hide(dis,True)
    scene bg_stairs
    with dis
    p "Wait, you still haven't answered all of my questions!"
    g "All in good time, young one."
    $ gb.aff += 0.1
    jump bedroom
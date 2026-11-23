label break_2:
    dpc "Hi again, [pname]! I know yesterday must have been overwhelming, but I'm glad to see that you're still doing well."
    dpc "Now, enjoy your break! The school is your oyster!"
    if (hallBanned):
        dpc "Well, except for the hallway. You know how that went last time, and I really don't want you to die. None of us do."
        dpc "We may never know what that entity is getting up to, but I certainly don't trust it."
    scene bg_classroom
    menu:
        "What would you like to do during this break period?"
        "Talk to Alva":
            jump alvaBreak2
        "Talk to Gwynedd":
            jump gwyBreak2
        "Talk to Hoshi":
            jump hoBreak2
        "Talk to Lily":
            jump dmpBreak2
        "Go up onto the rooftop":
            jump roofBreak2
        "Go into the hallway":
            if (hallBanned):
                $ al.show("idle",lefpos, dis, True)
                $ gw.show("idle",genpos,dis,True)
                $ ho.show("idle",ripos,dis,True)
                r1 "I apologize, but we have received explicit orders to prevent any attempt by you to enter the hallway."
                r2 "That's right! Since when were you stupid enough to go back to something that's tried to kill you before?"
                r3 "I-if you were to die, I would be quite sad... So could you please not die? I got really scared when I heard..."
                r1 "No matter how you may beg or whimper, we will not let you past."
                if (al.aff >= 0.3):
                    r1 "Though I would find that entertaining..."
                    r2 "Are you missing a screw or something up there?"
                    $ ho.show("embarassed",ripos,dis,true)
                    r3 "W-what?"
                if (gw.aff >= 0.3):
                    r2 "That would be pretty fun, though..."
                    r1 "Gwynedd, are you quite certain that your brain has not been replaced by... some other organs of yours?"
                    r3 "U-um..."
                if (ho.aff >= 0.3):
                    r3 "I m-might like to see that some other time, though..."
                    r1 "Hoshi?"
                    r2 "Wow, I didn't expect that from you of all people, Hoshi! Good for you, though~"
                    $ ho.show("embarassed", ripos, dis, true)
                    r3 "N-no, I... Um..."
                    "Hoshi appears to be having trouble responding."
                r1 "Please, find something else to do."
                r2 "You've got plenty of other options, after all. Why try and get yourself killed?"
                r3 "Y-yeah! We know there's an evil monster thingy trying to kill you, so why're you letting it?"
                jump break_2
            else:
                jump hallBreak
label roofBreak2:
    "You head up to the roof. The stairs are a bit creaky, but it's not too much of a concern."
    "The lock up here seems to be crumbling a bit. It's pretty easy to pull out the curved bit and unlock it." 
    "However, you do have to be careful to avoid it actually breaking, since that could tell the teachers that it was broken and that people have been coming up here. Worse, it could lead to them replacing the lock, making it much harder to get up here."
    scene bg_rooftop
    with dis 
    "Even without anyone being up here, it's still a pretty nice place. The wind blows through your hair as you look up and around."
    $ player.show("idle",genpos,dis,true)
    p "Wow... It's super pretty up here..."
    "You head near the protective fence to look out at the area below."
    scene bg_view
    with dis
    p "Wow, you can see so much from up here! There's the pond below, and the statues, and then the city."
    scene bg_rooftop
    with dis 
    p "It really is a special view."
    menu:
        "I wonder if it would be more special with a special someone...":
            p "A special someone, huh..."
            p "I don't think I've ever really thought about that kind of stuff before, but come to think of it, that does sound like a fairly couple-ish thing to do, doesn't it?"
            p "But who would I want to do it with?"
            p "Oh, look at me, thinking about something else with this incredible view before me."
            p "It is an interesting thought, though... Maybe I can think about it more later?"
            play sound "Bell.ogg"
            p "Oh! Time for bed, I suppose!"
            "You rush down the stairs and to your bedroom."
            jump bedroom
        "It would probably be more special if everyone could come up here and see it...":
            p "I'd love to bring the others up here to take a look at it. I wonder how they'd respond..."
            p "Lily probably already knows, since she's the one who told me, but there's a chance she might be surprised."
            p "As for the others, I doubt any of them have come up here before, so they'd probably be really surprised. Somehow, the thought sounds really nice."
            p "Maybe I should invite them up here sometime?"
            "You ponder this for some time."
            play sound "Bell.ogg"
            "The bell cuts off your train of thought."
            p "Oh, it's already this time? I suppose I'd best get to my bedroom, then."
            jump bedroom
        "It's a nice view to see alone.":

    jump bedroom
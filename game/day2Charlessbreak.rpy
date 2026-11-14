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
    "This text is a placeholder. Please proceed to the bedroom."
    jump bedroom
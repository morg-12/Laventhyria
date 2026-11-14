label introductions:
    dpc "I wanted to introduce you to some of our classmates! Here's Alva, Gwynedd, and Hoshi! You should go introduce yourself to them!"
    menu:
        "Who do you want to introduce yourself to first?"
        "Alva":
            $ meetNum+=1
            jump alva1
        "Gwynedd":
            $ meetNum +=1
            jump gwy1
        "Hoshi":
            $ meetNum += 1
            jump ho1
        "Nobody":
            dpc "Are you sure?"
            dpc "Well, I suppose if you don't want to speak with any of them now, you can talk to them during other breaks..."
            $ dmp.aff -= 0.01
            $ al.aff -= 0.1
            $ gw.aff -= 0.1 
            $ ho.aff -= 0.1
            $ cameFromBreak = True
            scene bg_classroom
            jump break_1
label alva1:
    $ dmp.hide(dis, True)
    $ alTalk = true
    scene bg_classroom
    $ al.show("idle",genpos,dis,True)
    r1 "Hello there, [pname]. It's very nice to meet you."
    r1 "My name is Alva Miloquis, and my family's holdings are in the county of Skorg."
    p "So you're..."
    r1 "Yeah, those Miloquises. Formerly the House of Skorg-Miloquis itself."
    menu:
        "Would you like to use the Taskbringer?"
        "Yes":
            $ renpy.say(r1,al.taskHandler())
        "No":
            r1 "This was my family's palace back in the day. I mean, it hasn't been for a loooooong time now."
            r1 "Heck, we're lucky to have escaped with our lives, much less with a county our own and all that."
            r1 "I'm actually kind of surprised that we've managed to remain nobility under the new system, but I guess we're not quite as indulgent as we were back in the old days."
            r1 "Not like we're a branch of the Levants and can get bailed out of any financial crisis we find ourselves in or anything."  
    p "Huh."
    menu: 
        p "That's..."
        "Interesting.":
            r1 "I suppose it would be for an outsider."
        "Pretty cool!":
            r1 "Really? I suppose being from a royal family, even a deposed one whose name is spat upon across the country, is pretty cool."
            $ al.aff += 0.1
        "Kinda weird...":
            r1 "I suppose it is a bit weird to be from a deposed royal family, huh?"
            $ al.aff -= 0.1
    if(cameFromBreak):
        jump expression ("break_"+str(day))
    r1 "Well, it was quite nice to meet you, but I'm afraid I must be taking my leave now."
    $ al.hide(dis,true)
    jump expression ("talkChoice"+str(meetNum))
label gwy1:
    $ dmp.hide(dis,True)
    scene bg_classroom
    $ gwTalk = true
    $ gw.show("idle",genpos,dis,True)
    r2 "Hiya there, [pname]! I'm very glad to meet you!"
    r2 "My name's Gwynedd, and I'm one of those rare commoners who managed to get in off the big wheel of names."
    r2 "I do find it preeeetty unfair how they advertise it as '500 people get to go to this excluuuuuusive school! It could be any of you!' and then behind- no, not even behind our backs, in broad daylight, they sell off those spots to nobles."
    menu:
        "Would you like to use the Taskbringer?"
        "Yes":
            $ renpy.say(r2,gw.taskHandler())
        "No":
            r2 "To be honest, I'm quite tired of this whole separation between nobles and commoners. Like, it's not even about 'bloodlines' or whatever they used to justify it with anymore."
            r2 "It's literally all about the money, and often, the only commoners who rise up and become nobles are either the merchants or the fallen nobles who got their act back together."
            r2 "So it really is just a bunch of 'rich people trade places with other rich people and the poor stay where they are'."
            r2 "I have heard rumors about some kind of 'People's Revolution' movement that's trying to cause some real change in here, and I'm kinda for it."
            r2 "Now, I don't think that destroying the nobility's buildings like those Revolutionary Pirates or whoever are will cause something to change, but I guess it does send a message to the nobility that the common people have had enough."
            r2 "I am scared that the nobles'll take it out on the rest of us commoners, though..."
    r2 "Sooooooo... Yeah! Basically, I'm one of those 'rare common specimens' who sometimes manage to get into the school. Ugh, I hate that term, though."
    menu: 
        "It does seem rather annoying.":
            r2 "It is! I mean, I suppose a noble might not fully understand how much, but it's basically just another way of othering me."
            r2 "Hehe, they're poor! Hehe, they're a commoner! Oh, look, it's that common specimen in the halls!"
            r2 "It's quite tiring, honestly."
            $ gw.aff += 0.1
        "It does seem rather fitting, though...":
            r2 "Really? After all of that conversation, you say something like that to me?"
            r2 "I suppose you're just like all the other nobles, after all..."
            r2 "Well, thanks for showing your true colors early. At least now, I know who to avoid."
            $ gw.aff -= 0.2
            r2 "Hopefully I never see you again, you scum of the earth."
            jump expression ("talkChoice"+str(meetNum))
        "What does that even mean?":
            r2 "I think I just explained it..."
            r2 "Well, I suppose I can do it again. See, basically, there's that wheel that decides if you get to go, right? But a lot of the slots get bought up by nobles beforehand, so there's often only a couple spots left for anybody else."
            r2 "Add in the fact that nobles who weren't bought in can still get in, and there's not too many seats for us commoners, even though there's a lot more of us than there are nobles. As such, it's a bit of a rare sight to see one of us here, which is why I'm called that."
            " "
            r2 "Ohhhhh, you meant it as in it's weird and stuff, not literally asking."
            r2 "Sorry, I do get a bit confused sometimes."
    if(cameFromBreak):
        jump expression ("break_"+str(day))
    r2 "Well, it was quite fun talking with you, but I have to go now!"
    $ gw.hide(dis,True)
    jump expression ("talkChoice"+str(meetNum))
label ho1:
    scene bg_classroom
    $ ho.show("idle",genpos,dis,True)
    $ hoTalk = True
    r3 "Hello, [pname]. My name's Hoshi."
    r3 "My family only recently became nobility, so I'm still getting used to it."
    r3 "I'm sorry for being a bit nervous. It's just that it's all very intimidating."
    menu:
        "Would you like to use the Taskbringer?"
        "Yes":
            $ renpy.say(r3,ho.taskHandler())
        "No":
            r3 "A couple of my realllly old relatives (although they're not technically considered part of our family due to the distance) recently passed and left us with some pretty sizable inheritances that were enough to get our net worth above the nobility threshold, and the census last year made us nobility."
            r3 "It's still a bit shocking, though. After all, we were a, well, still a well-to-do common family, but now we have our own land and our own manor and all that stuff."
            r3 " "
            r3 "Um..."
            r3 " "
    r3 "Sorry for being so nervous and awkward..."
    menu: 
        "No, it's fine!":
            r3 "Oh, really? Thanks..."
            $ ho.aff += 0.1
        "I actually think it's quite cute!":
            if(cameFromBreak):
                r3 "That's very nice of you to say, but I'm not sure if I can trust it..."
            else:
                r3 "Cute? Me? Cute? Nervousness? Cute? Cute?"
                $ ho.show("embarassed",genpos,dis,True)
                "They seem to be struggling to process your statement."
                r3 "U-um... T-thanks..."
                $ ho.aff += 0.2
        "You're about as annoying as [dname]...":
            if (dmp.aff >=0):
                r3 "So I'm not annoying? Thanks, I guess?"
            else:
                r3 "Okay, then..."
                r3 "I'll just shut up, then..."
                $ ho.aff -= 0.1
    if(cameFromBreak):
        jump expression ("break_"+str(day))
    r3 "I did have fun talking with you, and I hope I wasn't too annoying..."
    r3 "I think I have to go now, though..."
    $ ho.hide(dis,True)
    scene bg_classroom
    $ hoTalk = true
    jump expression ("talkChoice"+str(meetNum))
label talkChoice1:
    $ meetNum += 1
    menu:
        "Who would you like to speak to next?"
        "Alva" if not alTalk:
            jump alva1
        "Gwynedd" if not gwTalk:
            jump gwy1
        "Hoshi" if not hoTalk:
            jump ho1
label talkChoice2:
    $ meetNum += 1
    menu:
        "Who would you like to speak to last?"
        "Alva" if not alTalk:
            jump alva1
        "Gwynedd" if not gwTalk:
            jump gwy1
        "Hoshi" if not hoTalk:
            jump ho1
label talkChoice3:
    scene bg_classroom
    $ dmp.show("idle",genpos,dis,True)
    dpc "You talked to all of them!"
    dpc "It's probably a bit annoying to be asked to talk to three people you don't know before you can actually go off and enjoy your break, so I'm glad you did it."
    dpc "Well, I suppose you can go off and do your fun break time stuff now!"
    $ dmp.hide(dis,True)
    scene bg_classroom
    jump break_1
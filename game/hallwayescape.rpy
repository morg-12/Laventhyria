label duckWork:
    menu:
        "It's a big red button. Do you press it?"
        "Yes.":
            if(escRand > 2):
                "It explodes into a brilliantly bright light. You quickly shut your eyes."
                unk "What in the-NOOOOOOOOOOOO"
                unk "I'm melting! I'm melting! Well, I suppose I would be burning, actually, but it doesn't matter. How did you get your hands on Divine Light?"
                unk "Wait, don't answer, I'm too busy dying."
                scene bg_hallway
                with fad
                "When your eyes open, the entity has vanished and the darkness has retreated."
                p "What in the-"
                unk "Divine Light, packed inside a duck with a detonating mechanism to release it. Kills ghosts, specters, poltergeists, and the like in an instant. Quite the ingenious invention, wouldn't you say?"
                p "Another mysterious voice?"
                $ gb.show("",genpos,dis,True)
                g "No, quite the opposite, my child."
                g "I am the Garlic Bread!"
                p "The... what?"
                g "If you want to know more, speak with Lily. Be well, child!"
                $ gb.hide(dis,True)
                p "What even was that?"
                p "Wait, what's the time?"
                "You check your watch."
                p "Morning, huh?"
                pause 0.5
                p "Oh, wait, I have to get to class!"
                jump expression ("class_" + str(day))
            elif (escRand > 1):
                "It bursts loudly, releasing an incapacitating airborne sedative towards your face. You don't have time to figure out what it is, as you are quickly incapacitated by it."
                unk "Oh, was someone trying to run away from me? Well, I guess this has done the job of taking you out for me, so I'll just leave you here."
                unk "Or should I just kill you outright?"
                jump escFail
            else:
                "As it turns out, inside the duck was a high explosive, which you just detonated with your detonator. Unfortunately for you, it was also quite close to your body."
                $ hw()
                play sound "Explosion.ogg"
                unk "What in the-"
                unk "Well, I guess you did the job of taking care of yourself for me, didn't you?"
                default duckNames = ["Figure out the ducks"]
                default duckLabs = ["duckWork"]
                default duckMes = "What did you even think the big red button would do?"
                call screen death(duckNames,duckLabs,duckMes)
        "No":
            "Though it is difficult, you prevent yourself from pushing the big red button."
            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}I'm probably meant to use it as a distraction, right?{/font}"
            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Like so?{/font}"
            "You toss the duck out towards the entity. When it lands, it makes a loud squeaking sound."
            play sound "Duck.ogg"
            unk "Huh?"
            "The entity turns around to investigate."
            unk "A rubber duck? Seriously?"
            menu:
                "The button calls to you."
                "Run.":
                    "You take off, running like your life depends on it. Maybe it does..."
                    # Maybe add a quicktime event here instead of the hallRun jump, once you figure out multiclick quicktimes?
                    jump hallRun
                "Press the button, then run.":
                    "You push it, then take off."
                    if (escRand > 2):
                        "As you run, you hear loud screams of agony coming from behind you."
                        $ hw()
                        play sound "Screech.ogg"
                        "When the screams stop, the halls flash with a blinding light. You close your eyes."
                        scene bg_hallway
                        with fad
                        p "It's suddenly bright enough to see again."
                        p "I wonder what happened to that entity..."
                        p "Wait, what time is it?"
                        "You check your watch."
                        p "Morning, huh?"
                        pause 0.5
                        p "Oh, wait, I have class!"
                        jump expression ("class_" + str(day))
                    elif (escRand > 1):
                        "As you run, a cloud of gas follows close behind."
                        p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}I don't know what it is, so I should probably close my mouth and nose...{/font}"
                        $ player.run()
                        "Thankfully, the cloud fades away as your lungs are beginning to burn."
                        unk "YOU CAN'T RUN FOREVER, LITTLE WRETCH!"
                        $ player.run()
                        "The entity follows close behind you."
                        p "How much you wanna bet?"
                        unk "BETTING IS FOR LOSERS."
                        $ player.run()
                        "You're keeping pace with the entity, but on the flip side, that means it's keeping pace with you, and your legs are aching for a rest."
                        "Eventually, you see a light at the end of the void."
                        p "Looks like... you'd better pay up."
                        $ player.run()
                        "Your legs feel like they're about to fall off, but given the choice between your life and your legs, you'd choose the former."
                        jump escSuccess
                    else:
                        "You hear a tremendous explosion behind you and a cloud of dust covers everything, making it difficult to breathe or see."
                        $ hw()
                        play sound "Explosion.ogg"
                        unk "Where is it? WHERE IS THAT REPREHENSIBLE LITTLE FACSIMILE OF A HUMAN BEING?!"
                        "You hear the entity's screams, but the cloud of dust is on your side, making it difficult to find you."
                        unk "Aha! If I do that, I'll have more time!"
                        $ hw()
                        play sound "Screech.ogg"
                        "The entity lets out a paralyzing screech that immobilizes you."
                        unk "COME OUT, COME OUT, WHEREVER YOU ARE~"
                        p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}I can move? I guess it's wearing off, but I can't even see the entity..."
                        jump hallHide
                "Press the button and watch what happens.":
                    "You push the big red button. Truly, the compulsion to press a big red button is worthy of study."
                    if (escRand > 2):
                        "A bright light bursts out from the duck. You quickly close your eyes."
                        unk "Wait... How did they get..."
                        unk "OH, IT bubble.clear_retain_statements! IT BURNS!"
                        "When you open your eyes, the entity is gone and the darkness has retreated."
                        p "I wonder what happened to that thing... Well, I suppose it's for the best."
                        p "I should probably be getting to class..."
                        jump expression ("class_" + str(day))
                    elif (escRand > 1):
                        "The duck releases a cloud of gas. You hurry to close your nostrils and mouth."
                        unk "Huh? What's this supposed to do? It's certainly blocked my vision, but I don't know what else it would do..."
                        "You begin to crawl, keeping low to the ground to hopefully avoid the majority of the gas."
                        "However, as you start making your way away, the gas fully dissipates, allowing for full visibility once again."
                        "Unfortunately for you, this means that you are perfectly visible on the ground."
                        unk "Why, you little..."
                        $ qw(qtWarned)
                        $ qtWarned = true
                        call screen quicktime(gasCho,1.0,gasLab)
                    else:
                        "The duck explodes. The explosion blows the entity backward into a wall, stunning them, and creates a cloud of dust."
                        p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Well, this could be useful. After all, if I can't see through this fog, I don't think it can.{/font}"
                        p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}I was skeptical of the duck before, but it could just save my life here.{/font}"
                        p "Well, I should be going."
                        "You take off running. It's hard to see through the dust, but that makes it a good cover for your escape."
                        "Its effect on your breathing isn't as nice, but you don't have much room to lodge complaints, given that it, and by extension, the duck, is saving your life."
                        unk "Curses... How does a duck pack that much of a punch? And why does it pack that much of a punch? Who thought, 'Oh, let's stuff a bloody bomb inside a rubber duck'?"
                        unk "And I can't even see a thumb_align through all of this dust..."
                        unk "Maybe I should just go back into my realm for now..."
                        "You feel the entity's presence wane, and the void surrounding you with it."
                        scene bg_hallway
                        with fad
                        $ player.show("idle",genpos,dis,true)
                        p "Guess I've won, then!"
                        "You do a small party with yourself, then remember that you're at school."
                        p "What time is it?"
                        "Checking your watch, you find that it is morning. In particular, it is that part of the morning between when breakfast is eaten and when classes start."
                        p "I need to get myself on down to class!"
                        jump expression ("class_" + str(day))
label hallRun:
    "You take off running, the entity at your heels."
    $ player.run()
    play music "BG_Chase.ogg"
    unk "YOU CAN'T RUN FOREVER!"
    $ player.run(speed = 28.0)
    "Unfortunately, it's right. You can already start to feel yourself starting to slow down, and if the entity catches you, it's probably lights out."
    menu:
        "How do you respond?"
        "Push everything in you towards a singular, immense burst of speed.":
            "You use all of your power to increase your speed. You feel your legs starting to burn, but it doesn't matter. Nothing matters except getting out of this alive."
            $ player.run(speed = 36.0)
            unk "How... Well, you'll surely be done for soon!"
            "You feel an urge to respond, but keep yourself quiet, knowing that using any unnecessary energy could cause your demise."
            $ player.run()
            "Eventually, you see a light in the void. Focusing on it, you push yourself to the limit."
            jump escSuccess
        "Keep going at a steady pace and conserve what little energy you can.":
            "You slow down a bit to allow yourself to maintain a steady pace while still avoiding using all that you have in reserve."
            $ player.run(speed = 24.0)
            "While this is an intelligent choice for energy conservation, it's not as much for staying ahead of the entity. In fact, you can feel its arms reaching for your back."
            unk "What's wrong, scum? Are your 'human' lungs getting tired?"
            p "Not... not yet!"
            "Taking advantage of your reserves and the conserved energy from earlier, you speed up, going as fast as you can. The hallway and floor become a blur, and you can feel the entity falling behind."
            $ player.run(speed = 40.0)
            menu:
                unk "How..."
                "Boast":
                    "You turn back to taunt the entity."
                    p "I'm just too good for you, huh?"
                    "Unfortunately, you're so focused on taunting that you fail to notice a rather large ridged portion of the floor, and you fall onto your face."
                    unk "So this is what you call being 'too good', huh?"
                    p "U-um..."
                    unk "It's quite adorable, but you're still absolutely loathsome. Now, how should I bring about your demise?"
                    unk "Poison would be too good for you, torture isn't painful enough..."
                    unk "It's funny, but I don't think any standard means of killing are good!"
                    jump escFail
                "Focus on keeping yourself going":
                    unk "Wow, has the grand quipper lost their edge? I wouldn't have thought it possible, if it were not happening before my very eyes."
                    "You ignore the taunts and keep running, one foot after the other."
                    $ player.run(36.0)
                    unk "Hey, are you ignoring me?"
                    "You see a light shining at the end of this hall. There's a few students milling about, but not that many."
                    $ player.run()
                    p "Yes."
                    jump escSuccess

label hallHide:
    menu:
        p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}What should I do now?{/font}"
        "Check your backpack for more tools to use." if not checkedBag:
            "You look inside, but all the old tools are gone."
            "It seems that they were a boon only for that encounter."
            $ checkedBag = true
            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Well, looks like that option's off the table...{/font}"
            jump hallHide
        "Make a break for it.":
            "You start running as fast as you can."
            $ player.run()
            "The pattering of your feet upon the stone floors echoes throughout the hallway, alerting the entity to your presence."
            unk "Why, you little..."
            "The entity begins to chase after you."
            play music "BG_Chase.ogg"
            $ player.run()
            p "Why's this hallway so long?!"
            unk "Did you seriously think that you could get away from me?"
            $ player.run()
            "Your legs start to burn, but you keep running, knowing that if you stop, you're likely done for."
            $ player.run()
            p "How much longer?!"
            "Eventually, a miracle occurs. Or at least, it feels that way to you."
            jump escSuccess
        "Surrender yourself to the entity.":
            "You throw up your hands in surrender."
            p "I give up! I'm sorry for trying to get away."
            unk "Sorries won't cut it, you deceitful little wretch."
            jump escFail
label escFail:
    unk "No, I'll have to punish you some other way..."
    unk "I know! I'll just leave you out in this hallway. It's so far off into the unknown that nobody'll find you, and you'll rot here."
    unk "You will die alone, and they'll all be none the wiser!"
    unk "The perfect punishment for one such as yourself. Now, descend into your eternal sleep!"
    with fade
    scene bg_dark
    $ ogDay = day
    $ renpy.say(p,str(ogDay))
    "You collapse onto the floor. Into your eternal rest..."
    if (day%5==0):
        $ day += 1
        $ dayDiff = 2
        $ weekend = true
    else:
        $ dayDiff = (math.ceil(day/5.0))*5-day
        $ day = (math.ceil(day/5.0))*5
    $ noEep += dayDiff
    
    scene bg_hallway
    with fad
    $ dmp.show("idle",genpos,dis,True)
    dpc "Wake up!"
    dpc "What're you doing, collapsed out here on this floor? It's been [dayDiff] days since you walked off into the hallway, and nobody's known where you've been!"
    if (ogDay%5!=0):
        dpc "This week's quiz is today! Oh my, you've missed so much content..."
        dpc "I'll ask the teacher to do some review for you, okay? Of course, if you think you're good on it all, you can skip it, but I really think you'll need it!"
    else:
        dpc "Nobody's been able to find you all weekend! What, did you just wander off into the hallway after last week's quiz, hoping everyone would just forget about you?"
        p "N-no, I-"
        dpc "Oh, I'm so sorry. I really shouldn't have... It's just... we've all just been so worried about what happened to you."
        dpc "You walked off into that hallway, and when you didn't come back after a day, and then two... I thought something had happened to you. That, or you had done something..."
    dpc "But what even happened to you?"
    p "Well, let's see... I walked off into the hallway, since I wanted to check it out and all. It sounded like it would be pretty interesting to go out exploring a bit, you know?"
    p "But then I kept walking, and I felt this pull bringing me deeper and deeper..."
    p "Before I knew it, I was surrounded by darkness, and that's when this weird entity appeared."
    p "It was going on and on about me being a traitor and lying to everyone, but I don't really get what it was talking about..."
    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}I think I do, but I probably shouldn't tell her... I don't know how she'd react...{/font}"
    dpc "That sounds very weird... I've certainly never heard of some kind of ghost that goes around the halls to accuse them of being evil liars or whatever."
    dpc "Maaaaaybe you should stay out of the hallways in the future, though. Just in case."
    p "Oh, yeah, and when it caught me, it said something about how it would leave me out in the hallway deep inside where nobody goes, so that I can rot like I deserve to..."
    dpc "In that case, we need to keep you out of that hallway at all costs. It almost killed you just now, and it could strike again."
    dpc "And since leaving you out here didn't work, it might just kill you outright next time. Cut the chitchat, the nonsense, and your throat with it."
    p "That is a possibility, huh..."
    dpc "Pretty dark one, too."
    dpc "Well, I suppose we shouldn't linger on things like that. Class is soon, if you're feeling up to it."
    dpc "Well, I guess even if you're not, you can't really afford to miss more..."
    if (not weekend):
        dpc "Especially since the quiz's today, and all that..."
    dpc "So, I'm really sorry, but you'll need to go to class!"
    dpc "I'll tell Alva, Gwynedd, and Hoshi to keep you out of the hallway, and I'll also be doing that. We can't let this entity get its hands on you again."
    dpc "Well, time for class!"
    $ hallBanned = true
    jump expression ("class_" + str(day))
label escSuccess:
    scene bg_hallway
    with fad
    $ player.run()
    play music "Main_BGM.ogg"
    "You burst out of the void, but as you do so, you stumble and fall onto your face."
    p "No! Please don't!"
    $ dmp.show("idle", genpos,dis,true)
    dpc "Are you okay? What's going on?"
    p "W-where's the entity?"
    dpc "I don't see any entities..."
    $ dmp.show("pout",genpos,dis,true)
    dpc "More importantly, where have you been? You went off into that hallway during break yesterday, and you haven't been back in a day!"
    p "The hallways..."
    dpc "I know you were in the hallway, but how did you end up in there for a DAY?!"
    p "I don't know... I was walking, and as I kept walking, I felt this pull to keep walking, and then the night passed, and..."
    dpc "And what?"
    p "This mysterious voice appeared. It was going on about how I was lying to everyone about who I am and all that, or something."
    dpc "How bizarre..."
    p "Then I decided to try and get away while I still could. I felt a weird weight in my backpack, and when I checked inside, I saw a bunch of tools. Flash grenades, smoke bombs, a ten million levant coin, and a weird duck."
    p "I used the [escItem] to get away, but it managed to spot me. From there, I had to run for my life."
    p "It was talking about how I couldn't run forever or something, and it was right. My legs were burning like crazy by the end of it."
    p "Then I tripped on something and landed here, where you found me."
    dpc "Wow, it certainly sounds like you've had an adventure out there."
    dpc "Fortunately, you're just in time for class!"
    p "Well..."
    dpc "I know you haven't slept, but you need to learn!"
    dpc "And no more going back into the hallway! I'll get the others to stop you."
    dpc "You may have escaped this time, but there's no telling what that entity wants to do to you."
    dpc "And there's no guarantee that it won't just kill you outright next time."
    dpc "Now, off to class! The others are all worried about you, especially since you walked into the hallway and didn't come back until just now!"
    $ hallBanned = true
    jump expression ("class_" + str(day))
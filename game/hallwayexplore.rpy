label hallBreak:
    "You walk out into the hallway."
    scene bg_hallway
    with dis 
    play music "BG_Hallway.ogg"
    $ player.show("idle",genpos,dis,true)
    p "Huh. I would've thought there would be more people out here."
    menu:
        "Would you like to keep going down the hall?"
        "Keep going":
            "You continue further down the hallway."
            "Your footsteps are the only sound you can hear."
            "The darkness barely beyond your vision seems to almost call you deeper."
            menu:
                "Will you obey?"
                "Keep going":
                    jump hallway        
                "Turn back":
                    "Though your body seems to resist you, you wrench yourself away from the darkness."
                    "You return to the classroom, finding that it is already night."
                    p "How did it pass so fast? I could've sworn I just left the classroom."
                    "You decide to go to bed, ignoring the bizarre incident for now."
                    jump bedroom
        "Turn back":
            p "It seems a bit too eerie for my liking right now. Maybe later?"
            jump expression "break_"+str(day)
label hallway:
    "You keep moving, almost automatically. As you do, the void's call grows louder."
    "You check your watch. It's now past midnight. Looks like you won't be getting any sleep tonight."
    $ noEep += 1
    $ day += 1
    scene expression "/images/staying_up_late.png"
    with dis
    play music "BG_Hallway_Evil.ogg"
    "You can barely see anything anymore, but it feels as though what you seek is just beyond your reach."
    menu:
        "Do you wish to see what lies beyond the darkness?"
        "Yes":
            "You keep walking, drawn by both your curiosity and, increasingly, this mysterious force."
            "You can barely see, but you keep on walking."
            "Why do you even walk now? Is it for your own curiosity, or for this force that draws you?"
            "Do you know what it is? Can you know what it is?"
            unk "Hello there."
            "You let out a small scream and jump."
            unk "Hehe, didn't mean to scare you."
            unk "Or did I?"
            p "W-what are you?"
            unk "I know what you did. Or what you're doing, more accurately."
            p "And what does that mean?"
            unk "Stop pretending you don't know. You're probably laughing to yourself, aren't you?"
            p "No, I really-"
            unk "Shut it. You lie to me, just as you lie to everyone else in this world."
            unk "You aren't really [pname], are you?"
            unk "You're not a noble, either. Nor are you from here at all."
            unk "What are your goals in this world? To rob us of our dignity? To steal our wealth, then retreat to another world?"
            unk "You are an intruder. You are unwelcome in this world. And if nobody else will realize, then it's up to me to make sure this world is safe from you."
            unk "But how should I? All the classical methods would be too kind for one as despicable as yourself."
            jump escFail
        "No":
            "You tear your eyes away from the alluring void before you and force yourself to turn back, one step at a time."
            "With each step, you feel the force pulling you back grow stronger."
            "It's a struggle not to turn around, but you steel yourself and keep moving forward."
            "Forward and forward, until..."
            ""
            unk "You're quite a strong [p1genterm], aren't you?"
            "A voice in the darkness taunts you."
            p "Who are you?"
            unk "One who knows what you are."
            p "A student?"
            unk "So you claim."
            unk "You lie in your every breath to everyone around you, claiming that your name is [pname], you are a noble, you reside within this kingdom."
            unk "But I can see through your deceptions, vile one. I know that you are not of this realm."
            unk "You come to our world to fulfill your own heinous ambitions, is that it?"
            unk "An intruder, come to feast upon our riches, then leave without consequence."
            menu:
                "You sense that it may be wise to flee. Do you wish to flee?"
                "Yes":
                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}I need to get out of here before this thing flays me or something... but how?{/font}"
                    unk "You are a despicable facsimile of a human. In fact, I have never seen one in my life so despicable."
                    "You notice that your backpack seems to have suddenly become heavier. In the corner of your vision, you see what looks like... a bread crumb?"
                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Well, never mind that. What's in the bag?{/font}"
                    "The entity seems to be distracted with thinking of ways to berate you, so it does not notice opening it."
                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Let's see, let's see... wait, who left all this in my bag? Like, it's actually getting scary now!{/font}"
                    default checkedBag = false
                    default escItem = ""
                    default escRand = renpy.random.random()*3
                    menu:
                        "Which item would you like to use to try and disguise your escape?"
                        "Smoke bomb (comes with a face mask)":
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Perfect! It should obstruct the entity's vision for a bit, allowing me to go through and get out of sight without it noticing until way later!{/font}"
                            "You put on the face mask supplied, then toss down the smoke bomb beneath yourself."
                            "A sizable smoke cloud appears beneath and around you."
                            unk "Why's there a bunch of smoke? Is there a fire?"
                            "The smoke feels very thick as you run through it."
                            p "{font= NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}I wonder how much damage this could do to my lungs...{/font}"
                            "As the cloud fades, the entity notices your absence and lets out a paralyzing screech."
                            $ hw()
                            play sound "Screech.ogg"
                            unk "That should keep the vile creature in place. Now, where is it? Come out, come out, whereeeeever you areeeee~"
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}How do I get out of this?{/font}"
                            "Thankfully, it seems that the paralysis was only temporary, but it's allowed the entity to draw closer."
                            $ escItem = "smoke bomb"
                            jump hallHide
                        "Flash grenade (comes with protective goggles)":
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}This'll blind and stun it for a bit, I think!{/font}"
                            "You put on the goggles. They make it even harder to see, but you know you'll need it."
                            "You toss the flash grenade towards the entity."
                            unk "Huh? Whatever could that-"
                            if(escRand >= 2):
                                unk "No! Not the light!"
                                "You can hear the entity trying to flee, but it is unable to escape in time."
                                "It lets out a terrible shriek as it fades away."
                                $ hw()
                                play sound "Screech.ogg"
                                p "Wow, was it really that easy?"
                                "You take off your goggles."
                                scene bg_hallway
                                with dis
                                "Even accounting for the darkness from the goggles, the hallway is noticeably brighter now."
                                p "Was that thing making it darker in here?"
                                "You check your watch."
                                p "Oh, it's morning now. Wow, time really flies when you're..."
                                p "No, I wouldn't call that having fun... Maybe 'Time really flies when you're cursed by an evil entity?'"
                                p "Oh, whatever! I need to get to class!"
                                jump expression ("class_" + str(day))
                            else:
                                unk "MY EYES!"
                                p "Time to run!"
                                "You take off, getting pretty far away from the entity."
                                unk "Wait a second, that vile creature's gone!"
                                "The entity lets out a paralyzing screech."
                                $ hw()
                                play sound "Screech.ogg"
                                unk "Now, where did it go? Come out, vile one~ I won't hurt you... much..."
                                p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}It's getting closer! I need to get moving!{/font}"
                                $ escItem = "flash grenade"
                                jump hallRun
                        "A ten million Levant coin?":
                            "You turn it over in your hands. Even in this darkness, it seems to glow softly. You feel the imperial crest on the obverse and a detailed engraving of the capital city on the reverse."
                            show image "/images/coin_obverse.png" at genpos
                            with dis
                            "This is the highest denomination of currency in all of Laventhyria, rarely seen even within the treasuries of the loftiest nobles. Many die without even laying eyes upon one of these."
                            show image "/images/coin_reverse.png" at genpos
                            with dis
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Ten million levants, huh...{/font}"
                            menu:
                                p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}With that much money, I could...{/font}"
                                "Ensure that my family remains nobility for all time.":
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Ten million levants is a lot of money. If I had this coin, then even if we lost our entire fortune the day before the census, we would be able to keep our lands as long as I reported it.{/font}"
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}One hell of a rainy day fund, huh..."
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}The only way it'd run out is if someone drained all our savings and went into debt. I don't think anyone in our family would do that, though...{/font}"
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Or at least not someone who has the coffers at their fingertips. It might be small compared to our own accounts, but it's still worth holding on to.{/font}"
                                "Feed so many people.":
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}A day's meals for a commoner costs about a hundred levants. With this alone, I could feed a hundred thousand people for a day, over fourteen thousand for a week.{/font}"
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}I could probably feed close to three hundred people for a year. This coin alone could do a lot of good in the world...{/font}"
                                "Help a family get out of poverty":
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}There's a lot of families out there who're stuck in a dead end, doomed to live paycheck to paycheck while in eternal debt.{/font}"
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}With something this small, I could change everything for them. Housing in the better parts of the capital can cost upwards of fifty million levants, but outside of the cities, you usually only see prices go up to a million, and even in other cities, they tend to stay below ten mil.{/font}"
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}So with this, I could get them really good housing. Ten million levants could also be enough to get some good trading contracts, get to work on making your way up the ranks.{/font}"
                                    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}There's not a lot of upward mobility in Laventhyria, but with this, I could make a real difference for them. Maybe they'd pay it back to society, helping the populace as a whole.{/font}"
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}But I'm probably supposed to use it as a distraction, right? After all, if I die here, it's not like the coin'll be able to do anything anyway.{/font}"
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Farewell, good coin. We may not have known each other long, but I thank you for your noble sacrifice.{/font}"
                            "Looking back at the coin one last time, you toss it onto the ground behind the entity, the opposite direction from where you need to go."
                            play sound "coin.ogg"
                            default hallChoices = ["Run away!"]
                            default hallLabels = ["hallRun","escFail"]
                            unk "What was that?"
                            "The entity checks where the sound came from."
                            unk "Ten million levants? Did you seriously think that your mortal currency would-"
                            "Its eyes glow with a terrible rage."
                            unk "GET BACK HERE!"
                            $ qw(qtWarned)
                            $ qtWarned = true
                            $ escItem = "ten million Levant coin"
                            call screen quicktime(hallChoices,0.5,hallLabels)
                            # A quicktime event lasting half a second that has the option button Run away and jumps to hallRun in case of success and escFail in case of failure.
                        "A rubber duck with a note next to it and a strange button. You can't read the note in the darkness.":
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}A rubber duck? Seriously?{/font}"
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Well, I suppose it's better than nothing. What's this strange button, though?{/font}"
                            $ escItem = "rubber duck"
                            jump duckWork
                        "A crowbar, with the words \"For throwing only\" engraved into it.":
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}What am I supposed to do with a crowbar in a dark hallway where I can't see anything?{/font}"
                            "You look again at the instructions engraved on the crowbar."
                            p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}Hmm... Maybe these instructions have some merit?{/font}"
                            "You toss it deep into the hallway behind the entity."
                            play sound "Crowbar.ogg"
                            unk "What in the... Is there someone back there? I can't afford to let anyone find [p1obj], so I should go check..."
                            "The entity turns around."
                            unk "Hey, you! Stay right here until I come back. Don't move a muscle, you get me?"
                            p "Perfectly understood!"
                            unk "Good."
                            "The entity heads off to investigate. As it does, you take off."
                            unk "What's a crowbar doing here? I swear, people need to learn how to clean up after them-"
                            "It spots you in the distance."
                            unk "GET BACK HERE!"
                            jump hallRun
                        "Cancel your escape and stay here.":
                            "You close the bag and stay where you are."
                            p "I don't really think any of that would be the most useful, anyway, and I'm sure it would have a much worse punishment in store for me if I tried to resist."
                            "Still, it feels like there's a disapproving glare from behind you. When you turn around, however, you see only a small pile of crumbs."
                            unk "So you see, I know what you've done, I know what you are, and I know that you are quite possibly the worst thing in this world. As such, I seek to end you. Perfectly understandable, don't you think?"
                            p "No, not rea-"
                            unk "Did I ask you?"
                            p "Well, ye-"
                            unk "No, I did not. As a result of your insolence, I shall seek to make your punishment ten to fifteen times more painful."
                            p "Why?!"
                            unk "Because I want to. Now, let's see..."
                            unk "How should I make you die?"
                            "The entity ponders for some time."
                            unk "Well, all of the traditional methods of execution are designed around making it easy for the executioner, not painful for the executed. In fact, many of them seek to make it less painful."
                            unk "Meanwhile, many a method of torture is nonlethal, and I doubt any would be painful enough for what I desire..."
                            jump escFail
                "No":
                    unk "To allow such a repulsive thing to continue its existence in this realm would be contrary to my values and my duties."
                    unk "As such, you must die, despicable one!"
                    unk "But however shall I do it?"
                    unk "None of the usual methods would be sufficiently agonizing for one as abominable as yourself."
                    jump escFail
label alvaBreak1:
    $ al.show("idle",genpos,dis,True)
    if (al.denied):
        r1 "Did you not say earlier that you had no interest in speaking with me?"
        r1 "Regardless, I do not believe that I have any interest in speaking to you."
        r1 "Come back tomorrow, and I may have changed my mind."
        jump break_1
    if(al.aff < 0.0):
        r1 "Ah, it's you. The one who called me weird. [pname.capitalize()], right?"
    else:
        r1 "Hello, [pname]. A good day to you once again."
    r1 "I guess, since you're here, you probably want to talk to me."
    r1 ""
    r1 "Do you have any ideas about what we could talk about?"
    menu:
        "I hear there's some kind of revolutionary movement within Laventhyria.":
            r1 "Ah, right. They call themselves the Revolutionary Pirates, right?"
            r1 "I think this country could use a revolution."
            r1 "The Levants certainly have been doing quite a bit to antagonize the common people."
            menu:
                "Would you like to use the Taskbringer?"
                "Yes":
                    $ renpy.say(r1,al.taskHandler())
                    r1 "I thought I was on task here, though..."
                    $ al.aff -= 0.01
                "No":
                    r1 "You know, taxing them more, increasing prices on literally everything for them, sending them into war first for every single war of expansion they do..."
                    r1 "The Levants are pretty good at appeasing the nobles, and they've basically got the wealthy commoners begging for their attention, but that does come at the expense of the poorer ones."
                    r1 "After all, it's very rare that an actually new house joins the nobility. Usually it's just a fallen noble house that's managed to get its act back together."
                    r1 "As such, seeing the rich people playing a game of musical chairs while they rot in poverty's probably not the best."
            r1 "I don't quite agree with their ways, though..."
            r1 "The pirates, I mean."
            r1 "What good does destroying buildings even do? It just makes them look like a terrorist group..."
            r1 "I am also worried about what will happen if they succeed. If they're so anti-noble buildings, what'll happen to the nobles themselves? Will they just have them all tried by a kangaroo court and executed on the spot?"
            r1 "What's more, I'm a bit skeptical of any revolution. After all, even if they do succeed, who's to say that whoever backed them won't come along and take full control?"
            r1 "It's happened before, after all."
            menu:
                "What do you mean, it's happened before?":
                    r1 "Why, with-"
                    play sound "Bell.ogg"
                    r1 "Ah, curses, it's time for bed."
                    r1 "Come back and talk to me tomorrow during break and I'll tell you what I meant."
                    r1 "And thanks for talking with me!"
                    $ al.aff += 0.1
        "What happened with the fall of Skorgmiloquis?":
            r1 "Ah, yes, Skorgmiloquis."
            r1 "This one's a bit of a long story, so I might not get through all of it today."
            menu:
                r1 "That okay with you?"
                "Yes":
                    r1 "Okay, then! Let's go!"
                    r1 "Skorgmiloquis, or officially the Imperial Realm of the House of Skorg-Miloquis and its subsidiaries, was the nation that ruled over this area, where Laventhyria is now."
                    r1 "Well, the Levants have been very expansionist since they made the new nobility system, so it's actually more of just the central part of modern Laventhyria."
                    scene bg_map
                    with dis
                    $ al.show("idle",ripos,None,false)
                    r1 "Regardless, Skorgmiloquis ruled over those lands. It was formed about 1120 years ago, when the heirs to the House of Skorg, which ruled over much of the northern regions, including the modern day county of Skorg, and the House of Miloquis, which ruled over the south, married."
                    r1 "Prior to this, Skorg and Miloquis had been constantly at war, each aiming to rule over all of Hyria, so their people were overjoyed that the endless war had ended."
                    scene bg_map_preMar
                    with dis
                    $ al.show("idle",ripos,None,false)
                    r1 "However, the new Skorg-Miloquis monarchs soon found that it was rather difficult to rule over all of this land by themselves."
                    r1 "As such, they selected for themselves trusted houses to govern fairly and justly over the various regions of this new nation."
                    r1 "These are what later became known as the noble houses."
                    r1 "With this, the monarchy could set its sights beyond Hyria, and its people were all for it."
                    scene bg_map_expand
                    with dis
                    $ al.show("idle",ripos,None,false)
                    r1 "It managed to expand into the surrounding areas."
                    r1 "However, over the next couple centuries, the nation faced a number of challenges."
                    r1 "Skorgmiloquis fell under threat from the nations surrounding it, meaning that it was, in essence, perpetually at war."
                    r1 "Eventually, the people's fervor dwindled, especially since these were defensive wars, and they began to grow tired."
                    r1 "Over the years, many of the houses selected as nobility grew self-interested, not bothering themselves with the lives of their people as much as their own."
                    r1 "The endless warfare and the growing prodigality of the imperial house began to put a strain on the nation's coffers. As such, they opted to increase taxation and request greater tribute of their noble vassals."
                    r1 "As one might expect-"
                    play sound "Bell.ogg"
                    scene bg_classroom
                    with dis
                    $ al.show("idle",genpos,None,false)
                    r1 "Looks like our time to speak for today has sadly concluded. If you wish to continue hearing about this, please come talk to me again tomorrow!"
                    r1 "But not during class time, or the teacher will have your head!"
                    $ al.aff += 0.1
                    jump bedroom
                "No":
                    r1 "Fair enough. If you do end up wanting to hear it later, though, just come back to me and ask!"
                    $ alva.hide(dis,true)
                    scene bg_classroom
                    jump break_1
        "What do you think of the Levants?":
            r1 "Hmm..."
            r1 "Oh, would you like a candy?"
            p "Sure!"
            r1 "Okay, it's fine if you don't know the answer to my question, but..."
            menu:
                r1 "When the pearly fluid fell, what did the people who planted the bombshell found by the belle in a well deal in?"
                "What in the-":
                    r1 "Okay, good, you're not a government agent. Can't be too careful these days, what with the Revolutionary Pirates and the government being on higher alert as a result..."
                    p "What does that even mean, though?"
                    r1 "It's an obscure poem from the Skorgmiloquis days. At one time, it was well known, but eventually, the regime decided to use it as a code phrase for their secret agents."
                    r1 "If you know the answer, it's almost certain that you're a government agent trying to tell what side I'm on. That, or you somehow managed to find a copy of the ancient poem the government's kept under total lockdown for about a millennium at this point."
                    $ keyAnswer = ""
                    # Resets keyAnswer in case its value is actually the code
                "I think I know.":
                    $ keyAnswer = renpy.input("What is the answer? Please do not use any periods.")
                    $ keyAnswer = keyAnswer.lower().strip()
                    # $ renpy.say(p,keyAnswer)
                    if (keyAnswer == ("they dealt in the eggshell of the shelled gazelle") or keyAnswer == ("they dealt in the shell of the shelled gazelle") or keyAnswer == ("the bombshell found by the belle in a well was planted by a cartel who dealt in the eggshell of the shelled gazelle")):
                        jump spy
                    else:
                        r1 "Ah, phew! I thought you were one of those government agents, with how you had an answer almost the moment I asked."
                        p "What does that even mean, though?"
                        r1 "It's an obscure poem from the Skorgmiloquis days. At one time, it was well known, but eventually, the regime decided to use it as a code phrase for their secret agents."
                        r1 "If you knew the answer, it's almost certain that you're a government agent trying to tell what side I'm on. That, or you somehow managed to find a copy of the ancient poem the government's kept under total lockdown for about a millennium at this point."
            r1 "Well, since you're not a government agent, I suppose I can tell you."
            r1 "To be quite honest, I'm not exactly the biggest fan of the Levants. Not just because they took my family's lands, either."
            r1 "For one, they've always been more focused on their own profits than those of the nation. They also tend to pander too hard to the nobles."
            r1 "It makes them look bad to the commoners, or at least the poor ones. The people are, after all, the backbone of the nation, and they need to remember that."
            r1 "I also don't really like how they took power after Skorgmiloquis' fall, but that's another story."
            r1 "I think that's about all my opinions on them."
            r1 "Thanks for listening to me ramble on about my opinions."
            $ al.aff += 0.1
            jump bedroom
        "We could go up to the rooftop?":
            r1 "Isn't it off limits?"
            p "Well, it is, but from what I've heard, the lock's pretty old and rusty."
            r1 "Hmm..."
            r1 "I don't know..."
            r1 "What if we get caught?"
            menu:
                "We won't! They barely ever check up there, anyway.":
                    r1 "If you say so, but if we get in trouble, I'm pinning it all on you."
                    scene bg_rooftop
                    $ al.show(idle,lefpos,dis,True)
                    $ player.show(idle,ripos,dis,True)
                    r1 "Huh, you're right! It really was that easy."
                    p "Yup! There's a pretty nice view up here, too!"
                    "The two of you lay down on the floor and stare up at the sky."
                    r1 "It really is a pretty sky, huh?"
                    p "Sure is!"
                    r1 "I wonder what it would look like at night..."
                    p "So do I..."
                    ""
                    r1 "Maybe we should come up here sometime at night?"
                    p "Ah, acting a bit daring, are we?"
                    r1 "No, it's just..."
                    r1 "Well..."
                    r1 "It could be a nice experience, right?"
                    menu:
                        "It could be fun to bring along some of the others, too, right?":
                            r1 ""
                            r1 "Oh, right!"
                            r1 "Yeah, we could bring them..."
                        "True.":
                            r1 "Maybe sometime, I'll invite you up here!"
                            p "Maybe!"
                    $ al.aff += 0.2
                    jump bedroom
                "I guess you're right...":
                    r1 "It's a bit disappointing, I suppose, but it's probably better to be safe."
                    jump break_1
        "I don't know...":
            r1 "Then again, I suppose it's not undesirable to just sit together in silence."
            "The two of you sit together in silence, simply enjoying each other's presence."
            "Though it might ordinarily be boring, even something as simple as this feels enjoyable."
            "The hours seem to pass in an instant, and suddenly, the sky has turned a deep blue."
            r1 "Well, that was surprisingly enjoyable. A good day to you, [pname], and may our next meeting be favorable."
            $ al.aff += 0.05
            jump bedroom
        "Never mind.":
            r1 "Seriously? You come over to talk to me, then end it off immediately with 'Never mind.'?"
            $ al.show("pout",genpos,dis,True)
            r1 "Fine. Whatever. See if I care."
            $ al.aff -= 0.1
            $ al.denied = true
            jump break_1
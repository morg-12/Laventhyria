label gwyBreak1:
    if (gw.denied):
        r2 "Didn't you say you weren't interested in talking to me?"
        r2 "Well, I'm not interested in talking to you."
        r2 "Come back tomorrow and maybe I'll have changed my mind."
        jump break_1
    $ gw.show("idle",genpos,dis,True)
    if (gw.aff < 0.0):
        r2 "Hello again. Scum of the Earth, was it? Oh, wait, no, your name was [pname]. I had almost forgotten because of your behavior."
    else:
        r2 "Hiya there again, [pname]! How're you doing?"
        menu:
            "Great!":
                r2 "That's great to hear!"
            "Good!":
                r2 "Yay!"
            "Good...":
                r2 "Are you sure you're doing okay?"
            "Terrible :c":
                r2 "Oh, that's not good..."
                r2 "Hopefully I can help you feel a bit better..."
    r2 "So, you wanted to talk to me, so what should we talk about?"
    r2 "Or I guess if you wanted to go somewhere, we could go there!"
    menu:
        "What's going on with those 'Revolutionary Pirates'?":
            r2 "Ah, the revolutionaries."
            r2 "Way I see it, they're some of the common folk who decided they had enough of the nobles trying to push us down."
            r2 "Their ways of doing stuff are a bit destructive, but they do seem to avoid causing any harm to civilians."
            r2 "I think I've said it before, but I feel like this country needs a revolution."
            menu:
                "Would you like to use the Taskbringer?"
                "Yes":
                    $ renpy.say(r2,gw.taskHandler())
                    r2 "Was I really that far off task, though?"
                    $ gw.aff -= 0.01
                "No":
                    r2 "It feels to me like the monarchs and their noble cronies have gotten a bit too comfortable in the idea that the common people will just let them walk all over us."
                    r2 "We might need to teach them a little lesson about who we are."
                    r2 "Oh, sorry, I think I got a bit intense there!"
                    r2 "This kinda stuff does tend to get me pretty fired up."
                    r2 "As much as I like the way the Pirates do things, I don't think all of the commoners (I'm not a big fan of the word, but the common people is a bit of a mouthful to keep saying) would agree."
                    r2 "After all, not all of us are the biggest fans of destruction, and some (I'm guessing the older ones in particular) are probably going to be driven away from the idea of revolution by that."
                    r2 "They could be alienating a significant portion of the common people with that. After all, if parents don't trust the revolt's intentions and means, they may not approve of their children participating."
                    r2 "On the other hand, I suppose the youth coooould feel more drawn to it if their parents are so strongly opposed, but I feel like creating a generational divide like that for something as important as a revolution doesn't really work, or at least not too well."
            r2 "I guess my feelings on the matter are a bit complicated."
            r2 "We do need a revolution, but is destroying the buildings of the nobility the best way to go about it?"
            r2 "Will that portray the revolution as a force of liberation, or just one of terror?"
            r2 "Oh, come to think of it, this building's run by the nobility and the ruling regime, isn't it?"
            r2 "I wonder if they'll attack here..."
            r2 "But surely not, right? I don't think it would fit their M.O., nor would it really help their cause..."
            r2 "Maybe I should stop talking about such scary things, you know? You know what they say, when you say something could happen, fate might just will it into existence..."
            play sound "Bell.ogg"
            r2 "Well, that's the bell! Let's put these ominous thoughts aside for now and go sleep!"
            $ gw.aff += 0.1
            jump bedroom
        "What's your daily life like?":
            if (gw.aff < 0.0):
                if (p1sub = "they"):
                    r2 "Ah, so the wealthy noble finally bothers to ask the people they oppress about how they live."
                else:
                    r2 "Ah, so the wealthy noble finally bothers to ask the people [p1sub] oppress about how they live."
                r2 "What's wrong, did you grow a conscience or something?"
                r2 "I suppose I'd be willing to enlighten you. Who knows, maybe you really will grow a conscience or something. It's doubtful, though..."
            r2 "Well, I guess you'd say my family's not exactly the lower class."
            r2 "I mean, in that we aren't quite stuck living paycheck to paycheck or, even worse, out on the streets."
            r2 "We'd probably be classified as being among the middle class. Doesn't exactly mean we get treated any different, though..."
            r2 "My parents work pretty long hours at the local noble lord's manor."
            r2 "It's usually secretarial work, which, I suppose, is better than the alternative."
            menu:
                "Would you like to use the Taskbringer?"
                "Yes":
                    $ renpy.say(r2,gw.taskHandler())
                "No":
                    r2 "It's apparently super boring, though... I guess we are preeeetty lucky, though."
                    r2 "The noble governing our region actually bothers to pay us fairly and handles incident reports without significant bias."
                    r2 "Of course, noble-commoner incidents do slightly tend to end up with a ruling in favor of the noble, but there's been plenty where the ruling is in favor of the commoner." 
                    r2 "In such cases, they usually punish the noble with revocation of their status and, if they are a part of a noble house, the detachment of them from their house."
                    r2 "A pretty effective punishment, I'd say, for nobles who think they can get away with anything because of their status."
                    r2 "I believe if a noble is ruled against, the state confiscates half of their assets and redistributes them between the current petitioner and any others who have previously brought complaints against them."
                    r2 "It's a pretty fair system. If a noble's found to have acted badly toward someone, half of their wealth is distributed to their victims."
                    r2 "If the ruling is against the commoner, though, they usually just have them imprisoned. Not the best, in my opinion, but not as bad as in other areas, that's for sure."
                    r2 "In noble-noble disputes, the issue is usually left up to the houses of the nobles, while in common-common conflicts, the one ruled against is usually sentenced to pay reparations to their victim."
            r2 "Anyway, I am an only child, so it does get lonely sometimes. I have heard of families where having too many mouths to feed leads to less for everyone, so I suppose it's better than that."
            r2 "That said, being middle class doesn't necessarily mean that we're moving up in the world. We do get paid fairly, but fairly just means every year, our family's gained another hundred thousand levants or two."
            r2 "It's still a decent amount, but it's not like we're going to be nobles anytime soon."
            r2 "Being an only child does get lonely, though, especially with how long my parents' hours are..."
            r2 "I've gotten used to it, though, and I do have the neighborhood kids to play with! We do also have plenty of books for me to read when I get bored, and that boredom did mean that I could learn a lot of stuff!"
            r2 "So it's not that bad, I guess..."
            r2 "Wow, is it that time already? I suppose we'll be hearing the bell soon, then."
            play sound "Bell.ogg"
            r2 "Right on cue! Well, I'll see you tomorrow, then!"
            $ gw.aff += 0.1
            jump bedroom
        "How do you feel about the House of Levant?":
            r2 "You know that makes you sound really suspicious, right?"
            r2 "Like you're a government agent or something, you know?"
            r2 "Gah, if only there was a way to tell the difference!"
            r2 "Okay, I'm going to trust that you're not a government agent, and if you are, I'm going to feel very hurt and betrayed, okay?"
            menu:
                r2 "You don't want me to be hurt and betrayed and sad, right?"
                "Well, actually, I don't care that much...":
                    r2 "Seriously? How bad can you get?"
                    r2 "Okay, whatever. If you were actually a government agent, you'd be trying to get close to me, so you're probably not."
                    r2 "Doesn't mean you have to be like that about it, though..."
                    $ gw.aff -= 0.2
                "No, I wouldn't!":
                    r2 "Putting it on a bit much there, aren't you?"
                    r2 "Well, you seem sincere enough, so I'll be putting my life in your hands."
                    r2 "Please don't get me killed."
                    $ gw.aff += 0.01
            r2 "They feel to me like they're a buncha rich people on a power trip."
            r2 "Now, I don't know too much about Levanthyrian history from a couple centuries ago, but from what I've heard, the country was ruled by a democratic assembly for a bit."
            r2 "Then the Levants came in and decided that since they were rich, everything that you can see now is theirs."
            r2 "Councillors dying mysteriously left and right, while the Levants stood through it all."
            r2 "To be honest, they probably had them taken out."
            r2 "I wonder if they're still on good terms with the assassins they had do it."
            r2 "They've reshaped the old system with the Assembly so much that you can barely tell that it's what it used to be at all."
            r2 "Like how now, they've got their noble cronies running stuff that used to be run by democratically elected officials and stuff."
            r2 "They run a tight ship, though. Nobles can't just be lazy or they'll get kicked out, while the rich commoners are clamoring for those noble spots."
            menu:
                "Would you like to use the Taskbringer?"
                "Yes":
                    $ renpy.say(r2,gw.taskHandler())
                "No":
                    r2 "So, in essence, everyone with wealth and power's begging to be noticed by the royals, while everyone else is too poor to do much."
                    r2 "Despite all their work, though, there's still a revolution. I wonder if it scares them."
                    r2 "They don't usually care about the lower classes, but maybe when those classes start blowing their stuff up, they'll care a bit more?"
                    r2 "Hmm, what else?"
                    r2 "Well, they've been doing a lot of warfaring recently. My guess is that they've probably gotten too many houses rising and not enough falling in recent years."
                    r2 "That would mean that they're having to give away royal lands to some merchant family that's on the rise, and they probably aren't the biggest fans of that idea, so aggressive expansion could help..."
                    r2 "How long can they keep it up, though? We've been non-stop at war for the past twenty years, and they've always been victories for the regime, but how long can they keep it up?"
                    r2 "How many people are dying so that the Levants can crown the next Count of Nowherelandshire? If they make trade harder for the merchants, that goes against the idea of keeping them on your side, but if they don't, they'll always be running out of land."
                    r2 "Not to mention that the common people are livid about how they have to keep on fighting for rich people to give other rich people land."
                    r2 "In addition, the difference between the thresholds for commoners to rise and nobles to fall is pretty big, so it's not even that easy for someone to fall."
                    r2 "It's a good system to keep the rich and powerful under your control while avoiding them becoming lazy, but I don't know if it can truly be considered sustainable."
                    r2 "At some point, something's got to give, whether it's their capacity for war, their support from wealthy merchants, or their support from the populace."
                    r2 "When it does, what will they sacrifice?"
            r2 "They don't really seem to care much for the commoners, though, and that could be their downfall..."
            r2 "I wonder how the Revolutionary Pirates will do in their revolt. Will they be liberators, or a new set of oppressors?"
            r2 "It's a revolution of the common people, so I have hope, but you can't really let yourself have too much hope."
            r2 "Otherwise you'll always be disappointed."
            r2 "There's also the issue of how they'll handle the nobles..."
            r2 "Like there's going to be those who say the nobles should just be stripped of their titles and lands, and then there's those who'll want to, well..."
            r2 "Kill them all."
            p "K-kill us all?"
            r2 "Yeahhhh..."
            r2 "A lot of people've been wronged by the nobility, and that's led to a lot of frustrations about them."
            r2 "Some people would rather see them all dead."
            r2 "I'm not on that side, if you're worried about it. Like I said, our regional noble's not terrible like in other regions, and even if they were, I still feel like the systematic murder of an entire group of people is a bit much as punishment."
            r2 "Even if the nobles have done a lot of bad stuff to the common people, that doesn't mean that we should do terrible things right back to them."
            r2 "After all, we'd be just as terrible as them."
            play sound "Bell.ogg"
            r2 "Well, I suppose that ends this rather grim discussion."
            r2 "It was fun talking with you, though!"
            $ gw.aff += 0.1
            jump bedroom
        "I'm not sure...":
            r2 "That's kinda funny, isn't it?"
            r2 "Well, I suppose it's not altogether unpleasant to just sit together in silence."
            r2 "It is fun to think sometimes."
            r2 "Or something like that..."
            r2 "Wow, I'm not very good at this sitting together in silence thing, am I?"
            r2 "I should probably stop talking now."
            "The two of you sit together in silence."
            "It's a bit awkward at first, but as time goes by you can feel yourself growing more comfortable with their presence."
            "The time seems to pass in an instant, and the sky is now a fiery red."
            r2 "Wow, it's that time already, huh?"
            r2 "This was surprisingly enjoyable!"
            r2 "I'll see you tomorrow!"
            $ gw.aff += 0.05
            jump bedroom
        "We could go to the roof!":
            r2 "Isn't it off limits?"
            p "It is... Kinda..."
            p "But from what I hear, the lock's rusty and broken, so much so that you could poke it and it would open."
            r2 "But wouldn't they be checking it to make sure nobody's up there?"
            p "My sources tell me no."
            r2 "What sources? Also, didn't that one noble kid push a commoner off the roof once? ARE YOU TRYING TO KILL ME TOO?????"
            p "NO, I'M NOT!"
            r2 "O-okay... Well, I'm still not that sure, but if you want, I guess we can go up there..."
            menu:
                "Would you like to go to the rooftop?"
                "Yes":
                    scene bg_rooftop
                    with dis
                    $ gw.show(idle,lefpos,dis,True)
                    $ player.show(idle,ripos,dis,True)
                    r2 "Wow, that really wasn't that hard!"
                    p "Yeah, it wasn't. Oh, and look at the view!"
                    "The two of you lay down on the floor and stare up at the sky."
                    r2 "The sky sure is pretty, huh?"
                    p "That it is!"
                    r2 "I wonder how it would look at night..."
                    p "So do I..."
                    ""
                    r2 "Maybe the two of us should come up here at night sometime?"
                    p "Ah, being a bit daring, are we now?"
                    $ gw.show("embarassed",lefpos,None,false)
                    r2 "And what's that supposed to mean, hmm?"
                    p "Nothing, nothing! It would be nice to come up here at night, though..."
                    menu:
                        "It could be nice to come up here with the others sometime...":
                            r2 ""
                            r2 "Oh, right, the others! Yeah, it would..."
                        "It could be nice to come up here sometime, just the two of us...":
                            $ gw.show("pout",lefpos,None,False)
                            r2 "And who's the daring one now, hmmmmm?"
                            $ player.show("embarassed",ripos,none,False)
                            p "What's that supposed to mean, huh?"
                            r2 "I don't knoooooooow~"
                            r2 "Well, I might invite you up here someday..."
                            r2 "Or maybe I won't..."
                            r2 "I guess you'll just have to seeeee~"
                            $ player.show("pout",ripos,none,false)
                            p "Hey, no fair!"
                            r2 "Hehehe"
                    $ gw.aff += 0.2
                    jump bedroom
                "No":
                    p "You do raise some pretty big concerns..."
                    p "I don't really know that it's safe, I guess... So we probably shouldn't go."
                    r2 "Okay! I guess if you want to go some other time, I'm not exactly against it..."
                    r2 "But yeah, we probably shouldn't go until we figure out more about what exactly it entails."
                    r2 "Bye for now, I guess!"
                    menu:
                        "Would you like to keep speaking with Gwynedd or return to the break menu?"
                        "Gwynedd":
                            jump gwyBreak1
                        "Break Menu":
                            jump break_1
        "Never mind.":
            r2 "Really?\nReally?"
            r2 "You come all the way over to me."
            r2 "You ask to speak with me during MY BREAK."
            r2 "And you have the nerve."
            r2 "THE SHEER NERVE."
            r2 "To end it off immediately with 'Never mind.'?"
            $ gw.show("pout",genpos,dis,True)
            r2 "Fine. Whatever. See if I care."
            $ gw.aff -= 0.1
            $ gw.denied = true
            jump break_1
label hoBreak1:
    $ ho.show("idle",genpos,dis,true)
    if (ho.denied):
        r3 "I thought you said you didn't want to talk with me?"
        r3 "I'd probably be too annoying anyway..."
        r3 "I would appreciate if you could please leave me alone for today..."
        jump break_1
    if (ho.aff < 0.0):
        r3 "Oh, you've come to talk to me..."
        r3 "Sorry for being annoying earlier..."
    else:
        r3 "Oh, h-hello there, [pname]!"
        r3 "I hope you're doing well!"
    r3 "Do you want to talk about something?"
    r3 "I-if you want to go somewhere, that's fine too!"
    menu:
        "How do you feel about the revolution?":
            r3 "There's a revolution?"
            p "Well, a revolutionary movement. I hear they call themselves the 'Revolutionary Pirates' or something like that."
            r3 "P-pirates? That sounds a bit scary..."
            p "I think from what I've heard, they blow stuff up?"
            r3 "Really?"
            r3 "Blowing stuff up... I don't think it's too nice..."
            r3 "But then again, they probably have a reason for doing it, right?"
            p "I think they specifically target things owned by the monarchy and the nobility and stuff."
            r3 "Huh. I wonder if they have a specific reason for doing that. Maybe they're trying to send some kind of message to the nobles?"
            r3 "I still don't really agree with blowing stuff up to send a message, though..."
            r3 "I guess it's a bit of evidence that the common people aren't too happy with how things're going..."
            r3 "Are they hurting people when they blow stuff up?"
            p "I'm not sure, but I think they try to avoid it, at least."
            r3 "Oh. Well, that's good, at least."
            r3 "Wait, isn't this school run by the nobility?"
            r3 "I hope they don't blow up this school too..."
            p "Hopefully it doesn't happen..."
            r3 "Well, I guess if they're fighting for what they believe is good, that's good for them."
            r3 "I may not agree with their means of doing it, but if they think it's what's needed, who am I to stop them?"
            r3 "O-or something like that..."
            r3 "They do scare me, though..."
            r3 "That was a bit of a scary topic, but I did enjoy talking with you!"
            $ ho.aff += 0.1
            jump bedroom
        "How do you feel about the Levants?":
            r3 "Who were the Levants again? Oh, right, the royal family!"
            r3 "I guess I probably like them to some extent, at least?"
            r3 "After all, they're why my family has this noble title now..."
            r3 "To be honest, I don't really know too much about them..."
            r3 "I know the currency's named after them, but why does the symbol look like an S and a m when it's called the Levant?"
            p "I think it's something left over from the people who ruled before them. The House of Skorg-Miloquis, if I remember correctly?"
            r3 "Skorg-Miloquis, huh? Oh, isn't there a person in our class with the name Miloquis?"
            p "Alva? Yeah, they're descended from those Skorg-Miloquises."
            r3 "That's pretty cool!"
            r3 "Well, I guess the Levants did give my family our current standing and all that, so I should probably like them..."
            r3 "I wonder why they have this whole nobility system, though... After all, doesn't it just make it so that rich people keep getting richer?"
            r3 "Then again, I suppose I am one of those rich people now, so I should probably be really excited and happy about it, but I don't know..."
            menu:
                "Would you like to use the Taskbringer?"
                "Yes":
                    $ renpy.say(r3,ho.taskHandler())
                "No":
                    r3 "I don't know, though... It feels kind of unfair to just have some people have all this power and money and then most of the common people have nothing."
                    r3 "I don't really like them for making that kind of world."
                    r3 "Although I guess I do benefit from that kind of world..."
                    r3 "Aghhh, it's difficult to think about the differences between what I benefit from and what the world would benefit from..."
                    r3 "Do all nobles have to deal with this kind of thing?"
                    p "I doubt most worry themselves..."
                    r3 "That's an option?"
            r3 "Well, I suppose I'm not the biggest fan of this inequality they push for in our society."
            r3 "I do benefit from it, I guess, but it's not something I want to see in this world."
            r3 "So I guess that's my view on it."
            r3 "Thanks for listening to me just ramble on!"
            menu:
                r3 "I'm sure it was annoying sometimes, right?"
                "Really annoying...":
                    r3 "Oh... I'm sorry for being such a nuisance..."
                    r3 "{size=24}How do I always manage to make every situation I get involved in worse?{/size}"
                    r3 "{size=18}Bye...{/size}"
                    $ ho.aff -= 0.1
                "Not really, no.":
                    r3 "Are you sure?"
                    r3 "I hope you're not lying to me..."
                "It was quite fun, actually!":
                    r3 "Really?"
                    r3 "Are you quite certain?"
                    r3 "W-well, thank you for that..."
                    $ ho.aff += 0.1
                "You can get quite cute when you're excited about stuff...":
                    r3 "Excited? Cute? Me? Cute? Cute? Cute?"
                    $ ho.show("embarassed",genpos,None,false)
                    "They seem to be struggling to process your statement."
                    r3 "T-thanks..."
                    $ ho.aff += 0.2
            jump bedroom
        "How is it like, being nobility?":
            r3 "Being nobility, huh..."
            r3 "It's really strange, to be honest. I'm dealing with all of these new societal expectations and everyone expects me to act a certain way."
            r3 "Plus I'm not really sure what to think about anything."
            r3 "It's all so sudden..."
            menu:
                "Would you like to use the Taskbringer?"
                "Yes":
                    $ renpy.say(r3,ho.taskHandler())
                "No":
                    r3 "Like, before this we were a decently well off common family, and now, through some chance or fortune, we've become nobles."
                    r3 "Like, we were well-off before, but we weren't {font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf} noble {/font} level well-off..."
                    r3 "And now my family's gone from not really caring about our net worth to being obsessed with it and, well, it all feels so strange..."
                    r3 "I guess that's part of the system, though?"
                    r3 "I think there's also a whole bunch of movements against nobles that I just wasn't aware of before, but now I am because I have to be to stay safe."
                    r3 "It feels like the world's suddenly gotten more dangerous for me."
                    r3 "I know there's a lot of people out there who really don't like the nobility, and I'm not sure if they're going to care if I'm old nobility or new nobility."
                    r3 "After all, to them, I'm nobility all the same, and nobility's what's been keeping them down."
            r3 "Even if I say I became nobility by chance, that money could've helped them a ton, and now it's not."
            r3 "So there's people who want me dead and people who probably hate everything about my life."
            r3 "So I'd say I'm doing just great right about now..."
            play sound "Bell.ogg"
            r3 "Oh, is it that time already?"
            r3 "Thanks for listening to me ramble on about my experiences!"
            $ ho.aff += 0.1
            jump bedroom
        "I'm not really sure...":
            r3 "Funnily enough, that's probably what I'd say..."
            r3 "Well, I guess there's no problem with sitting together in silence..."
            "The two of you sit together in silence."
            "Though it feels a bit awkward at first, you soon become more comfortable in each other's presence, and the hours seem to drift by in seconds."
            r3 "Maybe it won't be so bad here..."
            "The sky darkens at a leisurely pace, and by the time you notice it, it has gotten quite late."
            r3 "Wait, it's that time already?"
            r3 "Well, that was quite fun..."
            r3 "Maybe we could do it again sometime?"
            $ ho.aff += 0.1
            jump bedroom
        "We could go upstairs to the rooftop!":
            r3 "Isn't that off limits?"
            p "Yes, but it's apparently super easy to get past the lock!"
            r3 "Wouldn't the teachers be monitoring it, especially after that incident with the noble kid?"
            p "Surprisingly enough, they don't really! I guess they just built a metal fence and went 'Welp, our work here is done!'"
            r3 "Weird..."
            menu:
                r3 "Well, I'm not entirely sure, but I guess if you want to go, we can go..."
                "Go":
                    p "Okay, then! Let's go on up and talk about stuff or whatever!"
                    scene bg_rooftop
                    with dis
                    $ ho.show("idle",lefpos,dis,True)
                    $ player.show("idle",ripos,dis,True)
                    r3 "Wow, it feels really nice up here!"
                    p "The view's amazing too..."
                    "The two of you lay down on your backs and look up at the sky."
                    r3 "This sky sure is pretty, huh?"
                    p "That it is..."
                    r3 "I wonder how it would look at night..."
                    pause 0.5
                    r3 "Maybe we could come up here sometime at night?"
                    p "Acting a bit daring, are we?"
                    $ ho.show("embarassed",lefpos,None,false)
                    r3 "W-well, wouldn't it be nice?"
                    p "That it would..."
                    menu:
                        "Maybe we could come up here sometime with everyone else...":
                            pause 0.5
                            r3 "Oh, right!"
                            r3 "That would be nice too..."
                        "It would certainly be fun...":
                            r3 "Maybe I'll invite you up here sometime!"
                            r3 "O-or not..."
                            r3 "It would be pretty embarassing..."
                            p "Wow, you really fizzled out on that one, huh?"
                            r3 "Well, it's embarassing, right?"
                    $ ho.aff += 0.2
                    jump bedroom
                "Don't go":
                    p "I guess it could be pretty bad to go somewhere I've never been before, especially if it could be a risk to my academic career..."
                    r3 "True..."
                    r3 "If you end up changing your mind or something, please tell me!"
                    r3 "Bye for now!"
                    jump break_1
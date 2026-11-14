label dmpBreak1:
    $ dmp.show("idle",genpos,dis,True)
    dpc "Oh, hello there, [pname]!"
    dpc "It's nice to be talking to you again!"
    if (not aroaceRouteStarted):
        dpc "Oh, yeah, I remembered that I neglected to mention something to you when I was introducing myself earlier!"
        dpc "So, I'm aroace. Aegoromantic and Black Stripe Asexual, to be more specific."
        menu:
            "Aego-what now?":
                dpc "Aegoromantic! It means that I like to experience romance vicariously (so like through books and stuff), but I don't experience any romantic attraction."
                dpc "Black stripe asexual basically means that I feel no sexual attraction at all."
                dpc "Since the term aroace(meaning aromantic and asexual) is the intersection of two pretty big spectra of people, I like to be a bit more specific on where I lie."
                dpc "After all, aromantic by itself could mean anything from feeling a small amount of romantic attraction to others or romantic attraction depending on certain conditions, or none at all, and the same could be said for sexual attraction and asexuality."
                dpc "If you don't want to get that deep into the bushes about who you are, though, that's perfectly fine!"
                dpc "I just find it fun to learn about these sorts of things, but someone else might find it super overwhelming, and that's completely valid."
                dpc "I'm also part of this thing called the Order of the Garlic Bread, but that's another thing..."
            "Black stripe?":
                dpc "Black stripe asexual! It basically means that I don't feel any sexual attraction at all."
                dpc "I'm also aegoromantic, which means that I like to experience romance vicariously (so like through books and stuff), but I don't experience any romantic attraction to anyone."
                dpc "Since the term aroace (meaning aromantic and asexual) describes the intersection of two pretty big spectra of attraction, I like to be more specific about where I lie on it."
                dpc "After all, being aromantic could mean that you feel a small amount of romantic attraction to certain people, you feel attracted to certain people after getting to know them, or you feel none at all, and the same could be said for sexuality and sexual attraction."
                dpc "If you don't wanna go that deep into who you are, that's perfectly fine as well."
                dpc "I find it pretty fun to learn about these kinds of things, but someone else might think it's overwhelming, and that's completely valid."
                dpc "I'm also part of this thing called the Order of the Garlic Bread, but that's a different thing..."
        p "Garlic Bread?"
        dpc "Yeah, it's a thing."
        dpc "I can tell you more about it a bit later if you want!"
        dpc "Okay, so a few more things."
        dpc "It took me quite a bit to figure out a lot of stuff about myself, so I would appreciate if you would respect that by not trying to make some kind of big romantic pursuit out of trying to woo me or anything."
        dpc "I was quite confused for a long time, and I don't appreciate people completely discounting that."
        dpc "If you keep on doing it, I'll just stop talking to you altogether."
        dpc "After all, if you keep doing it after I've asked you to stop repeatedly, you clearly just don't care about me at all, and I'd be better off without you."
        $ aroaceRouteStarted = true
    menu:
        dpc "So, what would you like to talk about? Or would you like to go somewhere?"
        "What was that about Garlic Bread?":
            dpc "Ah, yes, the Chosen of the Garlic Bread."
            dpc "Just a little warning, I'll be going into the history of aroace people here in Laventhyria and it could get a bit long."
            menu:
                "Continue?"
                "Yes":
                    $ gbRouteStarted = true
                    dpc "All right! Let's go on a journey into the past!"
                    jump aroaceRoute
                "No":
                    dpc "Fair enough! If you want to hear it, come back to me some other time and ask about it!"
        "How do you think our classmates feel about me?":
            dpc "That's an interesting question to be asking."
            dpc "Got anyone in particular you're thinking of?"
            p "W-what? No!"
            dpc "Hehe, I'm just teasing. All right, let's see here..."
            scene bg_mind
            with dis
            $ word = al.affOut()
            dpc "Alva seems to think that you are [word]"
            scene bg_mind
            with dis
            $ word = gw.affOut()
            dpc "Gwynedd seems to think that you are [word]"
            scene bg_mind
            with dis 
            $ word = ho.affOut()
            dpc "Hoshi seems to think that you are [word]"
            dpc "Now, I'll check how I feel about you."
            scene bg_mind
            with dis
            $ dmp.show("idle",genpos,dis,true)
            if (dmp.aff >= 2.0):
                $ word = "an excellent specimen of humanity."
            elif (dmp.aff >= 1.5):
                $ word = "a most honourable human being."
            elif (dmp.aff >= 1.0):
                $ word = "worthy of consideration for a prize in nobility of behavior."
            elif (dmp.aff >= 0.5):
                $ word = "one who is capable of great things, should they seek to apply themselves."
            elif (dmp.aff >= 0.0):
                $ word = "one who is worthy of further consideration."
            elif (dmp.aff >= -0.5):
                $ word = "one who is beginning to anger me."
            elif (dmp.aff >= -1.0):
                $ word = "a reprehensible human being."
            elif (dmp.aff >= -1.5):
                $ word = "beyond saving morally."
            elif (dmp.aff >= -2.0):
                $ word = "quite possibly the worst person I have ever met."
            else:
                $ word = "The Incorrect Dishonourable Inferior Employee of the Arcadian Lands of Loondom."
            dpc "I think that you are [word]"
            $ fav = gb.aff
            scene bg_mind
            with dis
            $ gb.show(None,genpos,dis,True)
            dpc "Your level of favor with the Garlic Bread is [fav]."
            dpc "We seem to still have some time during our break, so you can spend the rest of it as you wish."
            scene bg_classroom
            with dis
            jump break_1
        "Would you like to go to the rooftop?":
            dpc "I see you took the idea of going to the rooftop seriously, huh?"
            dpc "Well, it's still a pretty fun place!"
            dpc "It does have the sun, though..."
            dpc "Oh, well! I have an umbrella, and my socks are UV-resistant, so I should be fine out there!"
            scene bg_rooftop
            with dis
            dpc "It really is great out here, huh?"
            dpc "And we don't even have any sun!"
            dpc "It is still fun to hold my umbrella, though. It makes me feel a bit more regal and noble."
            dpc "A bit more distinguished."
            dpc "Or something like that."
            dpc "It is fun to lie down on your back out here and look up at the sky."
            dpc "I won't be doing that because I don't want to get this dress dirty, but it's really quite the fun experience!"
            p "Wow... The sky is really beautiful!"
            dpc "Yeah, it tends to be like that, especially from up here."
            dpc "I hear that's one of the reasons why it was built where it was. The House of Skorg-Miloquis wanted a nice vacation palace where they could just relax, away from the commotion of their duties and the city below."
            dpc "And, of course, what better way to relax than to look up at the sky, or at night, the stars."
            dpc "From what I hear, the night sky here is really beautiful."
            menu:
                "We should come up here to look at it sometime!":
                    dpc "It would be fun to watch it, yeah! Especially with all of our classmates."
                    dpc ""
                    dpc "That is, of course, what you meant."
                    dpc "Right?"
                    p "Of course!"
                    dpc "Good, good. It's just that people have tried to trick me into participating in some sort of romantic activity or the like with them before, so I'm a bit wary."
                "It would be fun to see it with the others!":
                    dpc "That it would, yeah!"
                    dpc "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf} Especially{/font} if you have someone you liiiiike~"
                    p "Oh, you!"
            $ dmp.aff += 0.1
            jump bedroom
        "How do you feel about the state of the nation?":
            dpc "Getting into the heavy questions, are we?"
            dpc "Well, I suppose I can bite."
            dpc "To put it quite simply, I don't think the nation as it is can sustain itself."
            dpc "The Levants are constantly getting into war after war as they keep on trying to expand the nation."
            dpc "Meanwhile, every ten years, they must give more and more land away to the new rising nobles."
            dpc "Additionally, the people are growing tired of these wars. Laventhyria has a powerful military and its technology is on the bleeding edge, but even with that, they need people to run it."
            dpc "If the people are tired of these endless wars of expansion, I don't think that they can keep it going forever without risking a popular revolt."
            menu:
                "Would you like to use the Taskbringer?"
                "Yes":
                    $ renpy.say(dpc,dmp.taskHandler())
                    dpc "I don't think I was off task, though?"
                    $ dmp.aff -= 0.05
                "No":
                    dpc "Heck, even now, we have a pretty large revolt against the regime. That's probably at least a bit intimidating, especially with how they are struggling to apprehend them."
                    dpc "Even if they stop expanding, however, the censuses will continue. More and more new nobles will be crowned, and with that, more and more land must be distributed."
                    dpc "If the new counties are significantly smaller than those distributed to nobles of the past, the newly crowned nobility will be displeased. A large amount of noble displeasure with the regime could lead to a revolt of the nobility."
                    dpc "Even if the Levants somehow manage to avoid both a common and a noble revolt when they stop their expansion, the lands available to the monarchy to grant to the nobility will decrease over time without anything to bolster them."
                    dpc "In addition to that problem, there is the problem of outside aggression. If the Levants cease their expansion, it is quite possible that neighboring nations will view this as weakness on Laventhyria's part and attempt to reconquer their lost lands."
                    dpc "This will force the Levants into a defensive war, which will go against the intent behind the ceasing of expansion. This will mean that war will resume again, causing even more displeasure amongst the populace, and since this would be a defensive war, there wouldn't even be conquests to boast of."
                    dpc "In fact, this quandary is quite similar to the one that faced the House of Skorg-Miloquis about half a millennium ago. The constant defensive wars against nations pushing into the Hyrian core led to a mass revolt among all classes."
                    dpc "The Levants are also the leading merchant house in the nation, so I don't think they will have as much issue with their coffers, and they have continued to satiate the nobility, so I doubt that is their greatest worry either."
                    dpc "However, they have neglected the commoners, and this may be their greatest folly."
                    dpc "The Revolutionary Pirates launch attacks on the buildings of the nobility. This causes terror about who could be next. Meanwhile, the regime's consistent failure to find and capture them creates an image of incompetence in the minds of the nobles."
                    dpc "Meanwhile, their movement brings revolution and equality to the forefront of the people's minds. Even if this revolution should fail, the seeds of thought have been planted in the minds of the many, and they shall soon find root."
                    dpc "So yeah, I'd basically say that Laventhyria as it is is doomed to perish. Maybe even soon."
                    dpc "The Levants really should've not neglected the commoners, but you know..."
                    dpc "I suppose nobles will be nobles. Too boastful of their own superiority, they believe others to be inferior without proper evidence."
                    dpc "It is only natural that they should fall, and that a new realm should rise up from their ashes."
                    dpc "I suppose the greatest hope of all of us is that this realm will be a democratic one, and that we should not fall back into the era of absolutism."
                    dpc "I believe that the last revolution may have failed due to the presence of powerful backers with ulterior motives. I hope that this one shall not fall into the same trap."
                    dpc "Money is, of course, endlessly alluring, but if gold's shine can be resisted, the nation will be all the better."
            dpc "So, yeah! That's basically my views on the state of the nation!"
            dpc "Laventhyria as a state's probably done for, for one reason or the other, and I hope that what comes out the other end is a better nation, and not a worse one."
            jump bedroom
        "Never mind.":
            dpc "Fair enough, I suppose. People change their minds all the time!"
            dpc "If you ever want to come back and talk to me again, though, feel free!"
            jump break_1
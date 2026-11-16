label bedroom:
    scene bg_bedroom
    if (day>1):
        menu:
            "Another day has drawn to an end. What would you like to do now?"
            "Sleep":
                if (noEep >0):
                    $ noEep -= 0.5
                $ day += 1
                $ al.denied = false
                $ ho.denied = false
                $ gw.denied = false
                $ dmp.denied = false
                jump expression ("class_" + str(day)) 
                with fade
            "Stay up":
                scene bg_dark
                with Fade(0.5,1.0,0.5,color="#000000")
                "You stay up until the morning doing who knows what."
                "You're very tired."
                "You might make some mistakes tomorrow, but at least you got that last book in, right?"
                $ day += 1
                $ noEep += 1
                $ al.denied = false
                $ ho.denied = false
                $ gw.denied = false
                $ dmp.denied = false
                jump expression ("class_" + str(day))
                with fade
    else:
        menu:
            "The day has drawn to an end. What would you like to do now?"
            "Sleep":
                $ day += 1
                $ al.denied = false
                $ ho.denied = false
                $ gw.denied = false
                $ dmp.denied = false
                jump expression ("class_" + str(day))
                with fade
            "Stay up":
                scene bg_dark
                with Fade(0.5,1.0,0.5,color="#000000")
                $ day += 1
                "You stay up until the morning doing who knows what."
                "You're very tired."
                "You might make some mistakes tomorrow, but at least you got that last book in, right?"
                $ noEep += 1
                $ al.denied = false
                $ ho.denied = false
                $ gw.denied = false
                $ dmp.denied = false
                jump expression ("class_" + str(day))
                with fade
label spy:
    r1 "Ah, so you're a government agent, then? You seem a bit young for the ol' trencher, but I suppose in these times, nobody's too young to serve their nation."
    r1 "At least, I'm guessing that's what they told you when they recruited you?"
    with vpunch
    r1 "Well, let me tell you something, [pname], if that's even your real name."
    r1 "You're serving one hell of a corrupt institution."
    r1 "And I will take great joy in taking you out of it."
    camera at dying
    $ al.hide(dis,true)
    scene bg_classroom
    $ player.show("scared",genpos,dis,True)
    p "{font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf} I can't breathe...{/font}"
    r1 "Acts fast, right? I call this one Azumarine. Your bosses aren't the only ones who have this on hand."
    with fade
    scene bg_dark
    default spyBut = ["Talking with Alva","Break Period"]
    default spyLab = []
    $ spyLab = ["alvaBreak"+str(day),"break_"+str(day)]
    default spyMes = "Never take candy from a stranger."
    call screen death(spyBut,spyLab,spyMes)
label aroaceRoute:
    if aroaceRouteStarted:
        dpc "People being openly aroace and accepted for it hasn't been around that long in Laventhyria, sadly. It was only within the last couple centuries that people began to actually allow us to be ourselves."
        dpc "Before that, it was commonplace for people who weren't heterosexual to be forced into heterosexual marriages, at least within the nobility."
        dpc "You know, the whole thing about how it's 'unnatural' and how they need an heir."
        dpc "But then..."
        if gbRouteStarted:
            dpc "As a young person was being forced to be wed, a voice came from far above."
            # placeholder for until the city asset is finished
            scene bg_city with dis
            $ gb.show("",genpos,dis,True)
            g "This person is one of my Chosen. If you continue to act against my and their wishes, I shall ensure that the consequences will be painful."
            dpc "The Garlic Bread descended from the heavens to protect them."
            dpc "It granted them the power to fight back, and they became the first Avatar of the Garlic Bread."
            dpc "They, along with the Garlic Bread, began to seek out others like them, founding an organization called the Chosen of the Garlic Bread."
            dpc "Those chosen by the Garlic Bread are typically individuals who experience little to no romantic or sexual attraction."
            dpc "Though at first, the organization was small, it has expanded greatly over the centuries since its formation."
            dpc "The Order of the Chosen of the Garlic Bread is sworn to neutrality during armed conflicts, although its members are not required to remain neutral, if they feel that doing so would be in violation of their values."
            dpc "Since the first, we have had a great many more Avatars of the Garlic Bread, the latest of whom is myself."
            dpc "The Avatar of the Garlic Bread possesses the ability to enter Avatar form, and in said form, can fire a powerful Garlic Bread Beam."
            dpc "The Avatar is typically the leader of the Order, as well as its most powerful member."
            dpc "I think I should be able to enter Avatar Form to demonstrate."
            $ dmpcolor = "#733b40"
            $ dname = "Avatar of the Garlic Bread"
            scene bg_city
            $ dmp.show("avf",genpos,dis,True)
            dpc "Behold my power."
            $ dmp.show("idle",genpos,dis,True)
            $ dmpcolor = "#eec2ff"
            $ dname = "Lily"
            dpc "And now I return to normal."
            dpc "Soooooooo..."
            dpc "Yeah! That's the Order of the Chosen of the Garlic Bread for you!"
            menu:
                dpc "What do you think?"
                "It seems pretty interesting, although I'm not interested in joining...":
                    dpc "That's fair enough! Not everyone's a good fit for the Order, and if someone were to deny themselves to join it, that would go against everything we stand for!"
                    dpc "That said, we are an interesting bunch."
                    dpc "Feel free to come join us if you make a realization about yourself and are chosen!"
                    $ dmp.aff += 0.1
                "How do I join?":
                    dpc "Well, you don't really join the Order. You get chosen by the Garlic Bread."
                    p "And how do I get chosen?"
                    dpc "Well, the Garlic Bread is probably keeping a closer eye on you since you've expressed interest in our order. If the Garlic Bread likes you and thinks that you would make a good fit, it will choose you to join the Order."
                    dpc "Of course, if you don't want to, you can refuse without any consequences. The Garlic Bread, and its order, believe that people should do what they feel best fits them, rather than what they are expected to do or what they think people want them to do."
                    dpc "So, if you feel that you would not be a good fit for the order, you can simply refuse entry. Of course, if you make a further realization about yourself later on, our doors will always be open."
                    dpc "Another thing is that the Order is sworn to neutrality. As such, even if you or any member is injured, I cannot call the Chosen to fight for you. As such, I might be a worse ally than others."
                    dpc "Then again, I do have that beam. I'm not entirely sure on how much power it has, though..."
                    $ dmp.aff += 0.1
                    $ gb.aff += 0.1
                "It seems a bit weird...":
                    dpc "Perhaps it would be, to someone as evidently close-minded as yourself."
                    dpc "Hey, maybe you should go talk with some of the elder nobles. I think their views might be more your style."
                    dpc "Come to think of it, are you even a kid at all? How do I know you're not some short eighty-year-old who's disguised [p1flex] as a teenager to come to this school and rant about how things were 'Back in my day'?"
                    $ dmp.aff -= 0.1
                    $ gb.aff -= 0.1
            dpc "Well, it seems like we're about out of time, so I guess it's time to go to sleep!"
            dpc "The Garlic Bread seems to have taken an interest in you, so that's fun!"
            dpc "That does mean that you have a divine entity watching your every move, but no pressure, right?"
            jump bedroom
        else:
            dpc "Oh, sorry, I must be boring you with all my rambling. I can just get like that sometimes, especially when it's something that I'm super interested in or passionate about."
            $ dmp.show("idle",ripos,dis,True)
            menu:
                "Oh, no, it's fine.":
                    dpc "No, really, you don't have to be so kind!"
                    $ dmp.aff += 0.01
                "Yeah, I was getting a bit bored.":
                    dpc "Jeez, I know I said it, but you don't have to be that blunt about it!"
                    $ dmp.aff -= 0.1
                "I actually found it really interesting!":
                    dpc "Wait, really? You don't have to lie to me if you didn't!"
                    dpc "Hmm... I find that your heart aligns with these words."
                    dpc "I have to resume the tour for now, but if you want to hear about it another time, come talk to me during break time! If you want, I can tell you all about the history of aroace people here!"
                    $ dmp.aff += 0.1
            jump schooltour
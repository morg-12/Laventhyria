label begin:
    # placeholder for until the hallway asset is made.
    scene bg_hallway
    $ player.hide(dis,true)
    $ dmp.show("idle",genpos,dis,True)
    
    dpc "Hi there, [pname]!"
    dpc "Welcome to the Laventhyrian Institute for Secondary Education! This is the leading institution for the education of the citizens of Laventhyria."
    dpc "It is primarily attended by the Laventhyrian nobility. In some exceptional cases, those without a noble background have been admitted, but that is exceedingly rare."
    dpc "But enough about the school! I'm [dname]. It's very nice to meet you, [pname]! "
    $ dmp.show("idle",ripos,dis,True)
    menu:
        "Likewise.":
            $ dmp.show("idle",genpos,dis,True)
            dpc "Short and to the point, I see! I'm sure you'll fit right in here!"
        "I, too, am eager to begin my studies at this institution.":
            $ dmp.show("idle",genpos,dis,True)
            dpc "Wow, a bit formal for talking to a fellow student, huh? I suppose we did just meet, though, so it's only understandable."
            dpc "Not to worry, though! I'm sure you'll be feeling a bit more comfortable soon enough."
        "It is as nice to meet you as it is to see you, and I am sure many would agree.":
            $ dmp.show("idle",genpos,dis,True)
            dpc "Quite the charmer, aren't we? Unfortunately for you, I'm aromantic and asexual, or what they would call aroace. Well, more specifically, I'm aegoromantic and black stripe asexual."
            $ dmp.show("idle",ripos,dis,True)
            menu:
                "Aego-what now?":
                    dpc "Aegoromantic. It means that I like experiencing romance vicariously (so like through books and stuff), but I don't feel any romantic attraction in real life, nor do I have any interest in engaging in a romantic relationship."
                    dpc "I think there are some people who're aegoromantic and feel some romantic attraction, but I'm not one of them, so I can't quite speak for them on their experiences."
                    dpc "As for black stripe asexual, it means that I don't feel any sexual attraction at all." 
                    dpc "Aroace itself means someone who experiences little to no sexual and romantic attraction, but since both aromanticism and asexuality are their own spectra with people who experience differing levels of various kinds of attraction in differing situations, I like to clarify."
                "Black stripe?":
                    dpc "Black stripe asexual. It means that I don't feel any sexual attraction at all."
                    dpc "As for aegoromantic, it means that I like to experience romance vicariously (so like through books) but I don't feel any romantic attraction in real life, nor do I have any interest in engaging in a romantic relationship."
                    dpc "I think there're some people who're aegoromantic and feel some romantic attraction, but since I'm not one of them, I can't quite speak on their experiences."
                    dpc "Aroace covers experiencing little to no romantic and sexual attraction, but since both aromanticism and asexuality are spectra with people who experience differing levels of various kinds attraction in different situations, I like to clarify."
            $ aroaceRouteStarted = true
            $ dmp.show("idle",genpos,dis,True)
            jump aroaceRoute
    jump schooltour
label schooltour:
    $ dmp.show("idle",genpos,dis,True)
    dpc "Anyway, this school's a boarding school, so you'll be living here. However, you will be granted your own room, as is tradition."
    dpc "You know, since this school was originally made for noble children and they would often demand their own rooms, and the school's funded by the government and nobility, so the school can afford it."
    dpc "Oh, yeah! I tend to refer to this school as 'the school' when I'm talking. Less annoyingly long than 'The Laventhyrian Institute for Secondary Education'. Just wanted to clarify that."
    dpc "Sooooo..."
    dpc "Yeah! Back to the explanation!"
    dpc "I'm guessing the common people aren't particularly happy about how the nobles get to live it up in this palace off their taxes."
    dpc "Technically, anyone can attend nowadays, but it's pretty rare to see a commoner here.\nBasically, there's a system where the next class is chosen every year by a random wheel. Five hundred seats."
    dpc "So in theory, you might think that everyone has an equal shot at attending, right? Well, that's where donations come in."
    dpc "See, if someone donates sufficient money, about a million levants, or {font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}\u20B7{/font}1,000,000, to the school, that grants their child or children (if they make multiple donations) of choice a seat. From the five hundred, of course."
    dpc "And even then, any children that they haven't chosen still have a shot at a seat. So they say it's super exclusive and all, but really, it's a noble children's romping ground. At least, that's what the newspapers that try to rile up the commoners say."
    dpc "Come to think of it, I think I've heard rumors about some kind of insurrection within Laventhyria. Some kind of 'Revolutionary Pirate Order' that goes around blowing stuff up that belongs to the nobility. I'm sure that would never happen here, though..."
    dpc "Oh, whoops, I've gotten myself sidetracked again! Hey, if you feel like I'm getting sidetracked, you can tell me and I'll get back on task! Of course, if you want to listen to me yap, that's all fine and dandy too!"
    play sound "Achievement.ogg"
    scene bg_hallway
    show taskinator at genpos
    with dis
    $ dmp.hide(dis,True)
    "Unlocked Taskbringer!"
    "When someone goes off on a ramble, you can get them back on task with this! Be warned, though. If you use it too much, they'll think you don't care about them and like you less in turn."
    hide taskinator with dis
    $ dmp.show("idle",genpos,dis,true)
    dpc "Hey! Hello?"
    dpc "Ah, you're back!"
    dpc "What even happened?"
    $ dmp.show("idle",ripos,dis,True)
    menu:
        "I saw this bright light...":
            dpc "What a bizarre occurence..."
        "A divine intervention...?":
            $dmp.show("excited",genpos,dis,true)
            dpc "DID YOU SEE THE GARLIC-"
            $ dmp.show("idle",genpos, dis, True)
            dpc "I apologize for my earlier lack of composure."
        "I heard this weird sound...":
            dpc "Is there a g-ghost around here?"
        "I got this strange item...":
            dpc "Are you sure you're not hallucinating? I don't see anything here..."
    $ dmp.show("idle",genpos,dis,True)
    dpc "Bizarre hauntings aside, I think I still have a bit to tell you!"
    dpc "Since our school building is the old palace of the Skorgmiloquis monarchs, we have plenty of rooms available. At least a hundred, I think. That, along with the demands of nobles for greater attention to their kids, has led to the school having a class size of ten."
    dpc "During break periods, however, you may wander the school as you please. This, too, was a demand from the nobles, as they felt the school needed to be more enriching for their children."
    dpc "The rooftop's locked."
    dpc "It's apparently because some kid decided to walk up there and lean over the balcony, and then a noble kid without a shred of sense pushed them off the railing 'as a practical joke'."
    menu:
        "Would you like to use the Taskbringer?"
        "Yes":
            $ renpy.say(dpc,dmp.taskHandler())
        "No":
            dpc "As you might expect, the noble faced no consequences whatsoever, because that kid was a commoner."
            dpc "What a world we live in, right?"
    
    dpc "Well, anyway, it's locked and they've put up giant wire to stop any more people from falling to their deaths. A little-known secret, however, is that the lock's so old and broken that if you poke it right it'll open up."
    dpc "So if you wanna do something {font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}in secret{/font}, that's the place ~"
    dpc "You didn't hear that from me, though!"
    dpc "Well, I think that's about it for the tour, so feel free to go back to your room and sle-"
    dpc "Wait, I just realized that you don't know the school's scheduling yet!"
    dpc "Oh, how could I forget? Well, the school has four quarters for each year, meaning that you'll be learning over the course of four four-week periods."
    dpc "It's a bit intense, but that's just life, huh? After all, you {font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}are{/font} at probably the most prestigious school in the nation, so it makes sense that it might be a bit on the intense side."
    dpc "So we'll be doing that, but you do also get time to hang out with your classmates!"
    $ dmp.show("excited",genpos, dis, True)
    dpc "Like, for exampleeeee, me!"
    $ dmp.show("idle",genpos, dis, True)
    dpc "Not too excited, are you?"
    $ dmp.show("pout",genpos, dis, true)
    menu:
        "I am, though!":
            dpc "Wait, really?"
            $ dmp.show("excited",genpos,dis,True)
            dpc "Yay! I'm super excited to be in the same class as you too!"
            $ dmp.aff += 0.1
        "It's just class placement, isn't it? You're a fun person, but I'm not sure if I care too much who's in my classes as long as I can learn well.":
            dpc "Hmph."
            $ dmp.show("idle",genpos,dis,True)
            dpc "Well, I suppose that's only fair. Come to think of it, if I was in the same position, I'd probably say the same thing."
        "Oh, nooooo, I'm sooooooo excited that you're in my class.":
            dpc "Rude."
            dpc "You know, if you keep talking to me like this, maybe I just won't talk to you anymore. How about that?"
            $ dmp.aff -= 0.1
    dpc "Come on now! Off you go! Your journey through Laventhyria awaits!"
    jump bedroom
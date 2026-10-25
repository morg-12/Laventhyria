# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
$ config.menu_include_disabled = true
default p = Character("[pname]")
define g = Character("Garlic Bread")
default dmpc = Character("[dname]", color = "#eec2ff")
# It's defaulted so it can change to be Avatar of the Garlic Bread and the color can change to #733b40 when it does that.
default dname = "Lily"
define r1 = Character("Alva")
define r2 = Character("Gwynedd")
define r3 = Character("Hoshi")
define unk = Character("???")
define t = Character("Teacher")
define dis = Dissolve(.5)
default pname = "Insert player name here."
default p1sub = ""
default p1obj = ""
default p1adj = ""
default p1pos = ""
default p1flex = ""
default p1genterm = ""
default term = 0
default day = 0
default termDay = 0
default noEep = 0.0
default eepNum = 0.0
#default pronoun2sub = ""
#default pronoun2obj = ""
#default pronoun2adj = ""
#default pronoun2pos = ""
#default secondarypronouns = false
transform genpos:
    xalign 0.5
    yalign 0.125
transform lefpos:
    xalign 0
    yalign 0.125
transform ripos:
    xalign 1.0
    yalign 0.125
init python:
    def live2d_there(characterFold) -> bool:
        return renpy.loadable(f"Live2D/{characterFold}/{characterFold}.model3.json")
    def Live2Ds(*args, charFold, fallback = Placeholder(base = "girl", text="No Live2D"), fallback1 = Image(""),**kwargs):
        if renpy.has_live2d() and live2d_there(charFold):
            return Live2D(*args,**kwargs)
        else:
            if (fallback1 != Image("")):
                return fallback1
            else:
                return fallback
image bg_room = Placeholder("bg",text = "room")
image taskinator = "images/Taskbringer.png"
image gbr = "images/Garlic_Bread.png"
init python:

    class Char:
        ima  = None
        taskNum = 0
        genChooser = 0
        aff = 0.0
        idNum = ""
        name = " "
        def __init__(self, idNum, gen, name, filepath, folder, isL2D, isGenChangeable, canBib, bass, customFallback = "noFall"):
            self.name = name
            self.idNum = idNum
            # Used as a unique identification number to differentiate between models of the same name
            self.filepath = filepath
            self.gen = gen
            # gen is a string that is "boy" or "girl"
            self.folder = folder
            self.bass = bass
            # usually .6, but can be customized
            self.alia = {"idle":"m01","scared":"m02","excited":"m03","pout":"m04"}
            self.isL2D = isL2D
            self.customFallback = customFallback
            if (isL2D):
                if (canBib):
                    self.alia["avf"]="bibac"
                if (isGenChangeable):
                    filem = filepath+"m"
                    filef = filepath+"f"
                    foldm = folder+"m"
                    foldf = folder+"f"
                    charm = Live2Ds(filem, charFold = foldm, fallback = Placeholder(base = "boy", text = self.name),base=self.bass,aliases = self.alia)
                    charf = Live2Ds(filef, charFold = foldf, fallback = Placeholder(base = "girl", text = self.name),base=self.bass,aliases = self.alia)
                    genChooser = renpy.random.random()*2
                    self.ima = ConditionSwitch("self.genChooser > 1", charf,"True", charm)
                else:
                    self.ima = Live2Ds(self.filepath,charFold = self.folder, fallback = Placeholder(base = self.gen,text = self.name),base=self.bass, aliases = self.alia, )
            else:
                self.ima = self.filepath
        def taskHandler(self) -> str:
            response = ""
            match self.taskNum:
                case 0:
                    response = "Oh! Thanks for bringing me back there. I might've gone off on a whole rant or something and you would've just had to listen to me {font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}keep on talking foreeeever!{/font}"
                case 1:
                    response = "Whoopsies! I did it again, didn't I? Silly me. Thanks for helping me keep myself in check!"
                case 2:
                    response = "I did it again, huh? Thanks, I guess..."
                case 3:
                    self.show("pout",genpos,"",False)
                    self.aff -= .01
                    response = "I'm starting to think you don't care about anything I'm saying..."
                case n if n>=4:
                    self.show("pout",genpos,"",False)
                    self.aff -= .02*(1+0.1*n)**(n-3)
                    response =  "Yeah, you definitely don't care about what I'm saying!"
            self.taskNum += 1
            return response
        def show(self,aliWanted,pos,wi,hasTrans):
            if (self.isL2D and live2d_there(self.folder)):
                nam = self.name + " " + aliWanted
                renpy.show(nam, at_list = [pos],what = self.ima,tag="char_"+self.idNum)
            else:
                renpy.show(self.name, at_list = [pos],what=self.ima,tag="char_"+self.idNum)
            if(hasTrans):
                renpy.with_statement(wi)
        def hide(self,wi,hasTrans):
            renpy.hide(self.name)
            if(hasTrans):
                renpy.with_statement(wi)
                
define false = False
define true = True
define none = None
default aroaceRouteStarted = false
default gbRouteStarted = false

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_room
    # play music "audio/Main_BGM.wav"
    
    play music "Main_BGM.ogg"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    default dmp = Char("001","girl",dname,"Live2D/dmpc","dmpc",True, False,True,.6)
    default al = Char("002","", "Alva", "Live2D/al","al",True, True,False,.6)
    default gw = Char("003","","Gwynedd","Live2D/gw","gw",True,True,False,.6)
    default ho = Char("004","","Hoshi","Live2D/ho","ho",True,True,False,.6)
    default gb = Char("005","","Garlic Bread","images/Garlic_Bread.png","Garlic_Bread",False,False,False,.6)
    $ pname = renpy.input("What would you like to name your character?")
    $ p = Character(pname)
    default playerf = Char("006","girl",pname,"Live2D/Playerf","Playerf",True,False,True,.6, customFallback = "playerf.png")
    default fb = Transform("playerf.png", zoom = 0.6)
    $ playerf.ima = fb
    # temporary means by which to add a custom placeholder until I can figure out how I can do that.
    default playerm = Char("007","boy",pname,"Live2D/Playerm","Playerm",True,False,True,.6)
    
    menu: 
        "What pronouns would you like to use for your character?"
        "She/her": 
            $ p1sub = "she"
            $ p1obj = "her"
            $ p1adj = "her"
            $ p1pos = "hers"
            $ p1flex = "herself"
        "He/him":
            $ p1sub = "he"
            $ p1obj = "him"
            $ p1adj = "his"
            $ p1pos = "his"
            $ p1flex = "himself"
        "They/them":
            $ p1sub = "they"
            $ p1obj = "them"
            $ p1adj = "their"
            $ p1pos = "theirs"
            $ p1flex = "themselves"
        "Other (A set of pronouns not included in the above options)":
            $ p1sub = renpy.input("What is the subjective form? (for example she)")
            $ p1obj = renpy.input("What is the objective form? (for example her as in 'I knew it was her!')")
            $ p1adj = renpy.input("What is the possessive adjective? (for example her as in 'It was her game.')")
            $ p1pos = renpy.input("What is the possessive form? (for example hers as in 'The victory was hers')")
            $ p1flex = renpy.input("What is the reflexive form? (for example herself)")
    menu:
        "What kind of gendered terms do you want to be used for your character?"
        "Feminine(girl, woman, etc.)":
            $ p1genterm = "girl"
        "Masculine(boy, man, etc.)":
            $ p1genterm = "boy"
        "Neutral(human, person, etc.)":
            $ p1genterm = "person"
    menu:
        "An example sentence using your chosen character name and pronouns will be displayed shortly. Please select whether it correctly uses your entered pronouns and name."
        "Okay":
            pass
    menu: 
        "'[pname] was quite confident in [p1flex], as [p1sub] believed that nothing could hurt [p1obj] on account of [p1adj] powerful weaponry. Being quite the intelligent [p1genterm], [p1sub] knew better than to count [p1adj] chickens before they hatched, but the game seemed all but [p1pos]. Or so [p1sub] thought...'"
        "Yes":
            jump cselect
        "No":
            jump start
label cselect:
    $ playerf.show("idle",lefpos,dis,true)
    "This is the first of the player character options."
    $ playerm.show("idle",ripos,dis,true)
    "This is the second."
    $ playerm.hide(dis, true)
    default player = Char("000","bg",pname,"Live2D/Player","Player",True,False,True,.6)
    menu:
        "Which player character do you prefer?"
        "1(Left)":
            $ player = playerf
            
        "2(Right)":
            $ player = playerm
    jump begin
label begin:
    image bg_hallway = Placeholder("bg","Hallway")
    # placeholder for until the hallway asset is made.
    scene bg_hallway
    $ player.hide(dis,true)
    $ dmp.show("idle",genpos,dis,True)
    
    dmpc "Hi there, [pname]!"
    dmpc "Welcome to the Laventhyrian Institute for Secondary Education! This is the leading institution for the education of the citizens of Laventhyria."
    dmpc "It is primarily attended by the Laventhyrian nobility. In some exceptional cases, those without a noble background have been admitted, but that is exceedingly rare."
    dmpc "But enough about the school! I'm [dname]. It's very nice to meet you, [pname]! "
    $ dmp.show("idle",ripos,dis,True)
    menu:
        "Likewise.":
            $ dmp.show("idle",genpos,dis,True)
            dmpc "Short and to the point, I see! I'm sure you'll fit right in here!"
        "I, too, am eager to begin my studies at this institution.":
            $ dmp.show("idle",genpos,dis,True)
            dmpc "Wow, a bit formal for talking to a fellow student, huh? I suppose we did just meet, though, so it's only understandable."
            dmpc "Not to worry, though! I'm sure you'll be feeling a bit more comfortable soon enough."
        "It is as nice to meet you as it is to see you, and I am sure many would agree.":
            $ dmp.show("idle",genpos,dis,True)
            dmpc "Quite the charmer, aren't we? Unfortunately for you, I'm aromantic and asexual, or what they would call aroace. Well, more specifically, I'm aegoromantic and black stripe asexual."
            $ dmp.show("idle",ripos,dis,True)
            menu:
                "Aego-what now?":
                    dmpc "Aegoromantic. It means that I like experiencing romance vicariously (so like through books and stuff), but I don't feel any romantic attraction in real life, nor do I have any interest in engaging in a romantic relationship."
                    dmpc "I think there are some people who're aegoromantic and feel some romantic attraction, but I'm not one of them, so I can't quite speak for them on their experiences."
                    dmpc "As for black stripe asexual, it means that I don't feel any sexual attraction at all." 
                    dmpc "Aroace itself means someone who experiences little to no sexual and romantic attraction, but since both aromanticism and asexuality are their own spectra with people who experience differing levels of various kinds of attraction in differing situations, I like to clarify."
                "Black stripe?":
                    dmpc "Black stripe asexual. It means that I don't feel any sexual attraction at all."
                    dmpc "As for aegoromantic, it means that I like to experience romance vicariously (so like through books) but I don't feel any romantic attraction in real life, nor do I have any interest in engaging in a romantic relationship."
                    dmpc "I think there're some people who're aegoromantic and feel some romantic attraction, but since I'm not one of them, I can't quite speak on their experiences."
                    dmpc "Aroace covers experiencing little to no romantic and sexual attraction, but since both aromanticism and asexuality are spectra with people who experience differing levels of various kinds attraction in different situations, I like to clarify."
            $ aroaceRouteStarted = true
            $ dmp.show("idle",genpos,dis,True)
            jump aroaceRoute
    jump schooltour
label aroaceRoute:
    if aroaceRouteStarted:
        dmpc "People being openly aroace and accepted for it hasn't been around that long in Laventhyria, sadly. It was only within the last couple centuries that people began to actually allow us to be ourselves."
        dmpc "Before that, it was commonplace for people who weren't heterosexual to be forced into heterosexual marriages, at least within the nobility."
        dmpc "You know, the whole thing about how it's 'unnatural' and how they need an heir."
        dmpc "But then..."
        if gbRouteStarted:
            dmpc "As a young person was being forced to be wed, a voice came from far above."
            image bg_city = Placeholder("bg", "city")
            # placeholder for until the city asset is finished
            scene bg_city with dis
            g "This person is one of my chosen. If you continue to act against my and their wishes, I shall ensure that the consequences will be painful."
        else:
            dmpc "Oh, sorry, I must be boring you with all my rambling. I can just get like that sometimes, especially when it's something that I'm super interested in or passionate about."
            $ dmp.show("idle",ripos,dis,True)
            menu:
                "Oh, no, it's fine.":
                    dmpc "No, really, you don't have to be so kind!"
                    $ dmp.aff += 0.01
                "Yeah, I was getting a bit bored.":
                    dmpc "Jeez, I know I said it, but you don't have to be that blunt about it!"
                    $ dmp.aff -= 0.1
                "I actually found it really interesting!":
                    dmpc "Wait, really? You don't have to lie to me if you didn't!"
                    dmpc "Hmm... I find that your heart aligns with these words."
                    dmpc "I have to resume the tour for now, but if you want to hear about it another time, come talk to me during break time! If you want, I can tell you all about the history of aroace people here!"
                    $ dmp.aff += 0.1
            jump schooltour
label schooltour:
    $ dmp.show("idle",genpos,dis,True)
    dmpc "Anyway, this school's a boarding school, so you'll be living here. However, you will be granted your own room, as is tradition."
    dmpc "You know, since this school was originally made for noble children and they would often demand their own rooms, and the school's funded by the government and nobility, so the school can afford it."
    dmpc "Oh, yeah! I tend to refer to this school as 'the school' when I'm talking. Less annoyingly long than 'The Laventhyrian Institute for Secondary Education'. Just wanted to clarify that."
    dmpc "Sooooo..."
    dmpc "Yeah! Back to the explanation!"
    dmpc "I'm guessing the common people aren't particularly happy about how the nobles get to live it up in this palace off their taxes."
    dmpc "Technically, anyone can attend nowadays, but it's pretty rare to see a commoner here.\nBasically, there's a system where the next class is chosen every year by a random wheel. Five hundred seats."
    dmpc "So in theory, you might think that everyone has an equal shot at attending, right? Well, that's where donations come in."
    dmpc "See, if someone donates sufficient money, about a hundred thousand levants, or {font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}\u20B7{/font}100,000, to the school, that grants their child or children of choice a seat. From the five hundred, of course."
    dmpc "And even then, any children that they haven't chosen still have a shot at a seat. So they say it's super exclusive and all, but really, it's a noble children's romping ground. At least, that's what the newspapers that try to rile up the commoners say."
    dmpc "Come to think of it, I think I've heard rumors about some kind of insurgence within Laventhyria. Some kind of 'Revolutionary Pirate Order' that goes around blowing stuff up that belongs to the nobility. I'm sure that would never happen here, though..."
    dmpc "Oh, whoops, I've gotten myself sidetracked again! Hey, if you feel like I'm getting sidetracked, you can tell me and I'll get back on task! Of course, if you want to listen to me yap, that's all fine and dandy too!"
    play sound "Achievement.ogg"
    show taskinator at genpos
    with dis
    $ dmp.hide(dis,True)
    "Unlocked Taskbringer!"
    "When someone goes off on a ramble, you can get them back on task with this! Be warned, though. If you use it too much, they'll think you don't care about them and like you less in turn."
    hide taskinator with dis
    $ dmp.show("idle",genpos,dis,true)
    dmpc "Hey! Hello?"
    dmpc "Ah, you're back!"
    dmpc "What even happened?"
    $ dmp.show("idle",ripos,dis,True)
    menu:
        "I saw this bright light...":
            dmpc "What a bizarre occurence..."
        "A divine intervention...?":
            $dmp.show("excited",genpos,dis,true)
            dmpc "DID YOU SEE THE GARLIC-"
            $ dmp.show("idle",genpos, dis, True)
            dmpc "I apologize for my earlier lack of composure."
        "I heard this weird sound...":
            dmpc "Is there a g-ghost around here?"
        "I got this strange item...":
            dmpc "Are you sure you're not hallucinating? I don't see anything here..."
    $ dmp.show("idle",genpos,dis,True)
    dmpc "Bizarre hauntings aside, I think I still have a bit to tell you!"
    dmpc "Since our school building is the old palace of the Skorgmiloquis monarchs, we have plenty of rooms available. At least a hundred, I think. That, along with the demands of nobles for greater attention to their kids, has led to the school having a class size of ten."
    dmpc "During break periods, however, you may wander the school as you please. This, too, was a demand from the nobles, as they felt the school needed to be more enriching for their children."
    dmpc "The rooftop's locked."
    dmpc "It's apparently because some kid decided to walk up there and lean over the balcony, and then a noble kid without a shred of sense pushed them off the railing 'as a practical joke'."
    menu:
        "Would you like to use the Taskbringer?"
        "Yes":
            $ dmpc(dmp.taskHandler())
        "No":
            dmpc "As you might expect, the noble faced no consequences whatsoever, because that kid was a commoner."
            dmpc "What a world we live in, right?"
    
    dmpc "Well, anyway, it's locked and they've put up giant wire to stop any more people from falling to their deaths. A little-known secret, however, is that the lock's so old and broken that if you poke it right it'll open up."
    dmpc "So if you wanna do something {font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}in secret{/font}, that's the place ~"
    dmpc "You didn't hear that from me, though!"
    dmpc "Well, I think that's about it for the tour, so feel free to go back to your room and sle-"
    dmpc "Wait, I just realized that you don't know the school's scheduling yet!"
    dmpc "Oh, how could I forget? Well, the school has four quarters for each year, meaning that you'll be learning over the course of four four-week periods."
    dmpc "It's a bit intense, but that's just life, huh? After all, you {font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}are{/font} at probably the most prestigious school in the nation, so it makes sense that it might be a bit on the intense side."
    dmpc "So we'll be doing that, but you do also get time to hang out with your classmates!"
    $ dmp.show("excited",genpos, dis, True)
    dmpc "Like, for exampleeeee, me!"
    $ dmp.show("idle",genpos, dis, True)
    "Not too excited, are you?"
    $ dmp.show("pout",genpos, dis, true)
    menu:
        "I am, though!":
            dmpc "Wait, really?"
            $ dmp.show("excited",genpos,dis,True)
            dmpc "Yay! I'm super excited to be in the same class as you too!"
            $ dmp.aff += 0.1
        "It's just class placement, isn't it? You're a fun person, but I'm not sure if I care too much who's in my classes as long as I can learn well.":
            dmpc "Hmph."
            $ dmp.show("idle",genpos,dis,True)
            dmpc "Well, I suppose that's only fair. Come to think of it, if I was in the same position, I'd probably say the same thing."
        "Oh, nooooo, I'm sooooooo excited that you're in my class.":
            dmpc "Rude."
            dmpc "You know, if you keep talking to me like this, maybe I just won't talk to you anymore. How about that?"
            $ dmp.aff -= 0.1
    dmpc "Come on now! Off you go! Your journey through Laventhyria awaits!"
    jump bedroom
label bedroom:
    image bg_bedroom = Placeholder("bg","Bedroom")
    scene bg_bedroom
    if (day>1):
        menu:
            "Another day has drawn to an end. What would you like to do now?"
            "Sleep":
                if (noEep >0):
                    $ noEep -= 0.5
                jump expression ("class_" + str(day)) 
                with fade
            "Stay up":
                with fade
                scene expression "/images/staying_up_late.png"
                "You stay up until the morning doing who knows what."
                "You're very tired."
                "You might make some mistakes tomorrow, but at least you got that last book in, right?"
                $ noEep += 1
                jump expression ("class_" + str(day))
                with fade
    else:
        menu:
            "The day has drawn to an end. What would you like to do now?"
            "Sleep":
                $ day += 1
                jump expression ("class_" + str(day))
                with fade
            "Stay up":
                with Fade(0.5,1.0,0.5,color="#000000")
                scene expression "/images/staying_up_late.png"
                $ day += 1
                "You stay up until the morning doing who knows what."
                "You're very tired."
                "You might make some mistakes tomorrow, but at least you got that last book in, right?"
                $ noEep += 1
                jump expression ("class_" + str(day))
                with fade
label class_1:
    image bg_classroom = Placeholder("bg","Classroom")
    scene bg_classroom
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Quarter One{/font}"
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Day One{/font}"
    $ player.show("idle",genpos,dis,True)
    p "It's the first day of school."
    p "And from what it sounds like, this one is pretty hardcore."
    if (noEep==1):
        p "I was up all night last night, and I'm not sure how well I can make it through..."
    menu:
        "I'm so excited for class, though!":
            p "That's right!"
            p "I was up all night thinking about how excited I was to meet my classmates and start my classes!"
        "I've been dreading this...":
            p "I was up all night worrying about how it'll go. Will they like me? What kind of people are they?"
            p "I mean, I guess I know that Lily'll be here."
            default word = "something."
            if (dmp.aff == 0.2):
                $ word = "comforting."
            elif (dmp.aff >= 0.11):
                $ word = "calming."
            elif (dmp.aff >= 0.01):
                $ word = "something, I guess?"
            elif (dmp.aff >= 0):
                $ word = "okay."
            elif (dmp.aff >= -0.09):
                $ word = "irritating."
            elif (dmp.aff >= -0.2):
                $ word = "annoying."
            $ renpy.say(p,"That's "+word)
    play sound "Bell.ogg"
    p "Oh, the bell's rung!"
    p "Regardless of my doubts and my worries, I should give it my all!"
    p "O-or at least the best I can..."
    p "H-hopefully that's enough..."
    $ player.hide(dis,true)
    scene bg_classroom
    t "All right, settle down now, class."
    t "I hope that we'll have a productive session today."
    t "You may call me 'Your Lordship'."
    t "Today, we'll be talking about Systems of Linear equations. Oh, and we'll also be talking about some elementary row operations. You probably don't know what that is yet, but you will."
    t "So, I'm sure you all know what linear equations are, right?"
    t "Well, if you don't, linear equations have the form a₁x₁+a₂x₂+...+aₙxₙ=b, where a₁,...,aₙ and b are coefficients, x₁,...,xₙ are variables or unknowns, and n is the dimension, or the number of variables."
    t "So, here's some examples of linear equations to help it stick a bit better in your heads."
    t "2x₁+4x₂=4 is a line in two dimensions, as the keen-eyed among you might be able to tell from how the highest subscript is 2."
    t "Now, then, how many dimensions do you think 3x₁ + 2x₂ + x₃ = 6 is in?"
    $ renpy.say(t, f"Ah, the keen-eyed looking {p1genterm} in the front!")
    default ansRight = false
    default ansExp = false
    menu: 
        "One!":
            $ ansRight = false
        "Two!":
            $ ansRight = false
        "Three!":
            $ eepNum = renpy.random.random()
            if(eepNum < 0.01*(2)**noEep and noEep != 0):
                p "3!"
                p "{i}Curses! I messed up and said it wrong!{/i}"
                t "Your answer is..."
                $ ansRight = true
                t "{size=+20}Wrong!"
            else:
                $ ansRight = true
        "3!":
            $ eepNum = renpy.random.random()
            if(eepNum < 0.01*(2)**noEep and noEep != 0):
                p "Three!"
                p "{i}Curses! I messed up and said it wrong!{/i}"
                t "Your answer is..."
                $ ansRight = true
                t "{size=+20}Correct!"
            else:
                $ ansRight = false
                t "This one was a bit of a trick question, so I must apologize."
                t "It does feel good seeing people fall for it, though."
                t "Now, this isn't quite in my job description, but I'll tell you it anyway. When you put an exclamation mark after an integer, like I did with 3!, it's called a factorial and means that you multiply the integer with all the integers that come before it."
                t "So like here, 3! = 3*2*1=6, so that's why you're wrong."
                t "Your mind was certainly in the right place, though! Heehee!"
                $ ansExp = true
        "N!":
            $ ansRight = false
    if (ansRight):
        t "Excellent work, young...?"
        $ renpy.say(p,f"{pname}, Your Lordship.")
        t "Such respect! I like that in a pupil."
    elif (ansExp):
        t "Teehee! Thanks for amusing me, young..."
        $ renpy.say(p,f"{pname}, Your Lordship.")
        t "Such respect! I like that in a pupil."
    else:
        t "That's not right, but I can see you were trying pretty hard there."
        t "The number of variables can tell you the dimension of a linear expression. For example, if there's three variables, it's going to have three dimensions, like here."
    t "Now, when you have a set of one or more linear equations, you've got a linear system of equations!"
    t "The solutions of a system of linear equations are pretty important. Now, you may be wondering how we describe those solutions, or even what they are."
    t "The set of solutions for a linear system is the set of all possible values of x₁,x₂,x₃,...,xₙ that satisfy all of the equations. Not just one, not just two, not just n-1, alllll of them."
    t "For any system of linear equations, regardless of the dimension or the number of equations, there's only three possible solution cases. There's either one unique solution, infinite solutions, or no solutions."
    t "We can use these things called Elementary Row Operations to find the solution set for a system."
    t "The first is called Replacement/Addition. In this operation, you add a multiple of one row to another. Another is Interchange, where you interchange two rows. Finally, there's Scaling, where you multiply a row by a nonzero scalar."
    t "An important thing to remember is that conducting row operations does not change the solution set."
    show image "/images/math/row_operations_1.png.png" at genpos
    t "Let's go through an example. R₁ is the linear equation x₁-2x₂+x₃=0, R₂ is 2x₂-8x₃=8, and R₃ is 5x₁-5x₃=10. We can start by adding R₂ to R₁, or R₁+R₂→R₁. This eliminates the x₂ term in R₁."
    scene bg_classroom
    show image "/images/math/row_operations_2.png.png" at genpos
    t "Next, we can divide R₂ by two, R₂/2→R₂, which makes the new value of R₂ x₂-4x₃=4. This'll make it a bit easier to deal with later. We can then subtract 5R₁ from R₃ to eliminate the x₁ term. This leaves the third row as 10x₂-10x₃=10."
    t "You may notice that R₂ and R₃ both only have x₂ and x₃ terms. This means that we can use replacement to have just one variable. Since R₃ has 10x₂ and R₂ has x₂, it's easier to eliminate x₂ by subtracting 10R₂ from R₃."
    scene bg_classroom
    show image "/images/math/row_operations_3.png.png" at genpos
    t "Subtracting 10x₂-40x₃=40 from 10x₂-10x₃=10 leaves us with 30x₃=-30, which simplifies to x₃=-1. We can now substitute this into the other equations. Substituting it into R₁ results in x₁+7=8, which means that x₁=1. Substituting it into R₂ results in x₂+4=4, so x₂=0."
    t "This means that the solution set for the system R₁: x₁-2x₂+x₃=0, R₂: 2x₂-8x₃=8, R₃: 5x₁-5x₃=10 is the point (1,0,-1)."
    scene bg_classroom
    t "It's a bit awkward to keep writing x₁, x₂, and x₃, right? Fortunately, these can be rewritten as augmented matrices. For example, {image=/images/math/lineq1.png} can be written as the augmented matrix {image=/images/math/augmatrix1.png}. The vertical line is basically a reminder that the columns before it are the coefficients to x₁, x₂, and x₃."
    t "Now, here's a couple of important terms. A linear system is consistent if it has ≥1 solution. It could have one particular solution or it could have infinitely many, but as long as it has solutions, it's consistent." 
    t "Two matrices are row equivalent if a sequence of row operations can transform one into the other. An important thing about row equivalence is that if the augmented matrices of two linear systems are row equivalent, they have the same solution set."
    t "Now, here's something to hopefully get it to stick a bit better."
    t "Suppose that "
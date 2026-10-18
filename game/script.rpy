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
default pname = ""
default p1sub = ""
default p1obj = ""
default p1adj = ""
default p1pos = ""
default p1flex = ""
default p1genterm = ""
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
    def Live2Ds(*args, charFold, fallback = Placeholder(base = "girl", text="No Live2D"),**kwargs):
        if renpy.has_live2d() and live2d_there(charFold):
            return Live2D(*args,**kwargs)
        else:
            return fallback
image bg_room = Placeholder("bg",text = "room")
#image player = Live2Ds("Live2D/dmpc", charFold = "dmpc", fallback = Placeholder(base = "girl",text = "Lily"), base=.6,aliases={"idle":"m01","avf":"bibac"})
#image playerf = Live2Ds("Live2D/Playerf", charFold = "Playerf", fallback = Placeholder(base = "girl", text = "Player"),  base=.6,aliases={"idle":"m01","avf":"bibac"})
#image playerm = Live2Ds("Live2D/Playerm", charFold = "Playerm", fallback = Placeholder(base = "boy", text = "Player"), base=.6,aliases={"idle":"m01","avf":"bibac"})
#image dmp = Live2Ds("Live2D/dmpc", charFold = "dmpc", fallback = Placeholder(base = "girl",text = "Lily"), base=.6,aliases={"idle":"m01","avf":"bibac"})
image alf = Live2Ds("Live2D/alf", charFold = "alf", fallback = Placeholder(base = "girl", text = "Alva"),  base=.6,aliases={"idle":"m01","avf":"bibac"})
image alm = Live2Ds("Live2D/alm", charFold = "alm", fallback = Placeholder(base = "boy", text = "Alva"),  base=.6,aliases={"idle":"m01","avf":"bibac"})
image gwf = Live2Ds("Live2D/gwf", charFold = "gwf", fallback = Placeholder(base = "girl", text = "Gwynedd"),  base=.6,aliases={"idle":"m01","avf":"bibac"})
image gwm = Live2Ds("Live2D/gwm", charFold = "gwm", fallback = Placeholder(base = "boy", text = "Gwynedd"),  base=.6,aliases={"idle":"m01","avf":"bibac"})
image hof = Live2Ds("Live2D/hof", charFold = "hof", fallback = Placeholder(base = "girl", text = "Hoshi"),  base=.6,aliases={"idle":"m01","avf":"bibac"})
image hom = Live2Ds("Live2D/hom", charFold = "hom", fallback = Placeholder(base = "boy", text = "Hoshi"),  base=.6,aliases={"idle":"m01","avf":"bibac"})
# Bibac means biblically accurate, aka Avatar form, and as such is only necessary for the player and dmpc
define als = renpy.random.random()*2
define gws = renpy.random.random()*2
define hos = renpy.random.random()*2
image al = ConditionSwitch("als > 1", "alf", "True", "alm")
image gw = ConditionSwitch("gws > 1", "gwf", "True", "gwm")
image ho = ConditionSwitch("hos > 1", "hof", "True", "hom")
image taskinator = "images/Taskbringer.png"
image gbr = "images/Garlic_Bread.png"
default dmpcFavor = 0.0
default r1Love = 0.0
default r2Love = 0.0
default r3Love = 0.0
default gbFavor = 0.0
init python:

    Class Char(object):
        image ima = None
        taskNum = 0
        genChooser = 0
        aff = 0.0
        def __init__(self, gen, name, filepath, folder, isL2D, isGenChangeable, canBib, bass):
            self.name = name
            self.filepath = filepath
            self.gen = gen
            # gen is a string that is "boy" or "girl"
            self.folder = folder
            self.bass = bass
            # usually .6, but can be customized
            self.alia = {"idle":"m01","scared":"m02","excited":"m03","pout":"m04"}
            self.isL2D = isL2D

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
                    self.ima = ConditionSwitch("self.genChooser > 1", "charf","True", "charm")
                else:
                    self.ima = Live2Ds(self.filepath,charFold = self.folder, fallback = Placeholder(base = self.gen,text = self.name),base=self.bass, aliases = self.alia)
                else:
                    self.ima = self.filepath
        def taskHandler() -> str:
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
                renpy.show(nam, at_list = [pos],what = self.ima)
            else:
                renpy.show(self.name, at_list = [pos],what=self.ima)
            if(hasTrans):
                renpy.with_statement(wi)
        def hide(self,wi,hasTrans):
            renpy.hide(self.name)
            if(hasTrans):
                renpy.with_statement(wi)
                
define false = False
define true = True
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
    $ dmp = Char("girl",dname,"Live2D/dmpc","dmpc",True, False,True,.6)
    $ al = Char("", "Alva", "Live2D/al","al",True, True,False,.6)
    $ gw = Char("","Gwynedd","Live2D/gw","gw",True,True,False,.6)
    $ ho = Char("","Hoshi","Live2D/ho","ho",True,True,False,.6)
    $ gb = Char("","Garlic Bread","images/Garlic_Bread.png","Garlic_Bread",False,False,False,.6)
    $ pname = renpy.input("What would you like to name your character?")
    $ p = Character(pname)
    $ playerf = Char("girl",pname,"Live2D/Playerf","Playerf",True,False,True,.6)
    $ playerm = Char("boy",pname,"Live2D/Playerm","Playerm",True,False,True,.6)
    
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
    $ playerf.show("idle",lefpos,dis,True)
    $ playerm.show("idle",ripos,dis,true)
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
    $ player.show("idle",lefpos,dis,True)
    $ dmp.show("idle",ripos,dis,True)
    
    dmpc "Hi there, [pname]!"
    dmpc "Welcome to the Laventhyrian Institute for Secondary Education! This is the leading institution for the education of the citizens of Laventhyria."
    dmpc "It is primarily attended by the Laventhyrian nobility. In some exceptional cases, those without a noble background have been admitted, but that is exceedingly rare."
    dmpc "But enough about the school! I'm [dname]. It's very nice to meet you, [pname]! "
    menu:
        "Likewise.":
            dmpc "Short and to the point, I see! I'm sure you'll fit right in here!"
        "I, too, am eager to begin my studies at this institution.":
            dmpc "Wow, a bit formal for talking to a fellow student, huh? I suppose we did just meet, though, so it's only understandable."
            dmpc "Not to worry, though! I'm sure you'll be feeling a bit more comfortable soon enough."
        "It is as nice to meet you as it is to see you, and I am sure many would agree.":
            dmpc "Quite the charmer, aren't we? Unfortunately for you, I'm aromantic and asexual, or what they would call aroace. Well, more specifically, I'm aegoromantic and black stripe asexual."
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
            jump aroaceRoute
    jump classes
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
            jump classes
label classes:
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
    $ player.hide(dis,True)
    $ player.hide(dis,True)
    "Unlocked Taskbringer!"
    "When someone goes off on a ramble, you can get them back on task with this! Be warned, though. If you use it too much, they'll think you don't care about them and like you less in turn."
    hide taskinator with dis
    $ player.show()
    if (live2d_there("Playerm") or live2d_there("Playerf")):
        show player.ima idle at lefpos
        with dis
    else:
        show player.ima at lefpos
        with dis
    if (live2d_there("dmp")):
        show dmp.ima idle at ripos
        with dis
    else:
        show dmp.ima at ripos
        with dis
    dmpc "Hey! Hello?"
    dmpc "Ah, you're back!"
    dmpc "What even happened?"
    menu:
        "I saw this bright light...":
            dmpc "What a bizarre occurence..."
        "A divine intervention...?":
            if (live2d_there("dmp")):
                show dmp.ima excited at ripos
                with dis
            dmpc "DID YOU SEE THE GARLIC-"
            if (live2d_there("dmp")):
                show dmp.ima idle at ripos
                with dis
            dmpc "I apologize for my earlier lack of composure."
        "I heard this weird sound...":
            dmpc "Is there a g-ghost around here?"
        "I got this strange item...":
            dmpc "Are you sure you're not hallucinating? I don't see anything here..."
    dmpc "Bizarre hauntings aside, I think I still have a bit to tell you!"
    dmpc "Since our school building is the old palace of the Skorgmiloquis monarchs, we have plenty of rooms available. At least a hundred, I think. That, along with the demands of nobles for greater attention to their kids, has led to the school having a class size of ten."
    dmpc "During break periods, however, you may wander the school as you please. This, too, was a demand from the nobles, as they felt the school needed to be more enriching for their children."
    dmpc "The rooftop's locked."
    dmpc "It's apparently because some kid decided to walk up there and lean over the balcony, and then a noble kid without a shred of sense pushed them off the railing 'as a practical joke'."
    menu:
        "Would you like to use the Taskbringer?"
        "Yes":
            $ taskHandler()
        "No":
            dmpc "As you might expect, the noble faced no consequences whatsoever, because that kid was a commoner."
            dmpc "What a world we live in, right?"
    
    dmpc "Well, anyway, it's locked and they've put up giant wire to stop any more people from falling to their deaths. A little-known secret, however, is that the lock's so old and broken that if you poke it right it'll open up."
    dmpc "So if you wanna do something {font=NotoSerifDisplay-Italic-VariableFont_wdth,wght.ttf}in secret{/font}, that's the place ~"
    dmpc "You didn't hear that from me, though!"
    dmpc "Well, I think that's about it for the tour, so feel free to go back to your room and sle-"
    dmpc "Wait, I just realized "
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
#image playerf = Live2D("Live2D/Playerf",base=.6,aliases={"idle":"m01":"bibac"})
#image playerm = Live2D("Live2D/playerm",base=.6,aliases={"idle":"m01":"bibac"})
#image dmp = Live2D("Live2D/dmpc",base=.6,aliases={"idle":"m01":bibac})
default dmpcFavor = 0.0
default r1Love = 0.0
default r2Love = 0.0
default r3Love = 0.0
default gbFavor = 0.0
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
    play music "audio/Main_BGM.wav"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ pname = renpy.input("What would you like to name your character?")
    $ p = Character(pname)
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
    #show playerf idle at lefpos
    #show playerm idle at ripos
    menu:
        "Which player character do you prefer?"
        "1(Left)":
            pass
            #image player = Live2D("Live2D/Playerf",base=.6,aliases={"idle":"m01":"bibac"})
            # Bibac means biblically accurate, aka Avatar form, and as such is only necessary for the player and dmpc
        "2(Right)":
            #image player = Live2D("Live2D/Playerm",base=.6,aliases={"idle":"m01":"bibac"})
            pass
    jump begin
label begin:
    scene bg_classroom
    #show player idle at lefpos
    #show dmp idle at ripos
    dmpc "Hi there, [pname]!"
    dmpc "Welcome to the Laventhyrian Institute for Secondary Education! This is the leading institution for the education of the citizens of Laventhyria."
    dmpc "It is primarily attended by the Laventhyrian nobility. In some exceptional cases, those without a noble background have been admitted, but that is exceedingly rare."
    dmpc "But enough about the school! I'm [dname]. It's very nice to meet you, [pname]! "
    menu:
        "Likewise":
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
                    dmpc "I think there're some people who're aegoromantice and feel some romantic attraction, but since I'm not one of them, I can't quite speak on their experiences."
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

        else:
            dmpc "Oh, sorry, I must be boring you with all my rambling. I can just get like that sometimes, especially when it's something that I'm super interested in or passionate about."
            menu:
                "Oh, no, it's fine."
                dmpc "No, really, you don't have to be so kind!"
                dmpcFavor += 0.01
                "Yeah, I was getting a bit bored."
                dmpc "Jeez, I know I said it, but you don't have to be that blunt about it!"
                dmpcFavor -= 0.1
                "I actually found it really interesting!"
                dmpc "Wait, really? You don't have to lie to me if you didn't!"
                dmpc "Hmm... I find that your heart aligns with these words."
                dmpc "I have to resume the tour for now, but if you want to hear about it another time, come talk to me during break time! If you want, I can tell you all about the history of aroace people here!"
                dmpcFavor += 0.1
            jump classes
label classes:
    dmpc "Anyway, this school's a boarding school"

    
    



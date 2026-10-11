# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[pname]")
default pname = ""
default p1sub = ""
default p1obj = ""
default p1adj = ""
default p1pos = ""
default p1flex = ""
#default pronoun2sub = ""
#default pronoun2obj = ""
#default pronoun2adj = ""
#default pronoun2pos = ""
#default secondarypronouns = false


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play music "Main_BGM.wav"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ pname = renpy.input("What would you like to name your character?")
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
        "An example sentence using your chosen character name and pronouns will be displayed shortly. Please select whether it correctly uses your entered pronouns and name."
        "Okay":
            pass
    menu: 
        "'[pname] was quite confident in [p1flex], as [p1sub] believed that nothing could hurt [p1obj] on account of [p1adj] powerful weaponry. Though [p1sub] knew better than to count [p1adj] chickens before they hatched, the game was all but [p1pos]. Or so [p1sub] thought...'"
        "Yes":
            jump cselect
        "No":
            jump start
label cselect:
    return
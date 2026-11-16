define fad = Fade(0.5,0.0,0.5,color = "#ffffff")
# In essence, this is to be the opposite of fade, used when something fades into white.
define dis = Dissolve(.5)
transform dying:
    linear 1.0 matrixcolor SaturationMatrix(0.0)
transform genpos:
    xalign 0.5
    yalign 0.125
transform lefpos:
    xalign 0
    yalign 0.125
transform ripos:
    xalign 1.0
    yalign 0.125
screen quicktime(choices,time,labels):
# A basic screen for quicktime events. May add to it later.
# Ensure that the number of labels is equal to the number of choices, plus one label at the end in case of failure. time must be a double.
    vbox:
        for i, choice in enumerate(choices):
            textbutton choice action Jump(labels[i]) xalign 0.5 yalign 0.5
    timer time action Jump(labels[len(labels)-1])
screen death(buttonNames,jumpLabels,deathMessage):
# A basic attempt at making a death screen. Will be debugged later.
    modal True
    vbox:
        align(0.5,0.2)
        text "Game Over":
            size 300
            color "#cc0000"
            font "NotoSerifDisplay-VariableFont_wdth,wght.ttf"
        text deathMessage xalign 0.5 yalign 0.4 size 36 # font "NotoSerifDisplay-VariableFont_wdth,wght.ttf"
    vbox:
        text "How will you continue?" size 60 yalign 0.6 font "NotoSerifDisplay-VariableFont_wdth,wght.ttf"
        align(0.5,0.7)
        for i, name in enumerate(buttonNames):
            textbutton name:
                text_color"#cc0000"
                hover_background Solid("#eec2ff")
                action Jump(jumpLabels[i]) 
                xalign 0.5 
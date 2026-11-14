label class_2:
    play music "Main_BGM.ogg"
    scene bg_classroom
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Quarter One{/font}"
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Day Two{/font}"
    $ player.show("idle",genpos,dis,True)
    p "Yesterday was pretty fun."
    p "I wonder what we're learning about today."
    p "Hold on, I can probably check my schedule."
    play sound "Bell.ogg"
    p "No time! Well, I guess the teacher'll tell us what we're studying."
    "The code for this segment has not yet been written. It will now proceed to the second day's break period."
    jump break_2
label class_5:
    play music "Main_BGM.ogg"
    scene bg_classroom
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Quarter One{/font}"
    "{font=NotoSerifDisplay-VariableFont_wdth,wght.ttf}Day Five{/font}"
    t "Today is the date of your first quiz. I hope that you have studied well."
    t "Now. On the request of one of your classmates, I have decided to hold a review session prior to said quiz. I hope that it will serve you well."
    menu:
        "Would you like to skip the review session?"
        "Yes":
            jump quiz_1
        "No":
            "This label serves as a placeholder for until the code for the days prior to day five is written. Please proceed to the quiz label."
            jump quiz_1
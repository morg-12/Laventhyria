init python:
    import math
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
    def hw():
        renpy.say(None,"Headphone warning: A loud sound will soon follow. It is advised that you remove your headphones, if you have any, and turn down your volume.")
    def qw(qt):
        if(not qt):
            renpy.say(None,"A quicktime event is coming up! Since this is your first quicktime event, there is a warning. In the future, there will be no warnings.")
            qt = true
    def listCompare(list1,list2) -> list:
        # These two lists must be the same length and contain the same type of object. 
        boolList = [false] * list1.len()
        for i in range(list1.len()):
            boolList[i]= list1[i]==list2[i]
        return boolList
    def multiChecker(correctAnswers, inCollected, receivedAnswers=list(None), recPhrases=list(None)) -> list:
        # inCollected describes whether the values to compare have already been collected.
        if (not inCollected):
            receivedAnswers = list()
            for i in range(correctAnswers.len()):
                receivedAnswers[i] = renpy.input(recPhrases[i])
        return listCompare(correctAnswers,receivedAnswers)
    def rightCounter(boolvarsList) -> list:
        j = 0.0
        fracRight = 0.0
        for bean in boolvarsList:
            if bean:
                j+=1
        fracRight = j/boolvarsList.len()
        return list(j,fracRight)
        
    class Char:
        ima  = None
        taskNum = 0
        aff = 0.0
        idNum = ""
        name = " "
        genChooser = 120983736720298382937289
        roofWith = True
        denied = False
        isIma = False
        oathBound = False
        oathBreak = False
        def __init__(self, idNum, gen, name, filepath, folder, isL2D, isGenChangeable, canBib, bass, genChooser, isIma = False, customFallback = "noFall"):
            self.name = name
            self.idNum = idNum
            # Used as a unique identification number to differentiate between models of the same name
            self.filepath = filepath
            self.gen = gen
            # gen is a string that is "boy" or "girl"
            self.folder = folder
            self.bass = bass
            self.isIma = isIma
            # usually .6, but can be customized
            self.alia = {"idle":"m01","scared":"m02","excited":"m03","pout":"m04","embarassed":"m05"}
            self.isL2D = isL2D
            self.customFallback = customFallback
            self.genChooser = genChooser
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
                    self.genChooser = renpy.random.random()*2
                    self.ima = ConditionSwitch(self.genChooser > 1, charf,True, charm)
                else:
                    self.ima = Live2Ds(self.filepath,charFold = self.folder, fallback = Placeholder(base = self.gen,text = self.name),base=self.bass, aliases = self.alia, )
            else:
                self.ima = renpy.displayable(self.filepath)
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
            elif (self.isIma):
                renpy.show(self.filepath,at_list = [pos],what = self.ima,tag = "ima_"+self.idNum)
            else:
                renpy.show(self.name, at_list = [pos],what=self.ima,tag="char_"+self.idNum)
            if(hasTrans):
                renpy.with_statement(wi)
        def hide(self,wi,hasTrans):
        # seems to be kind of broken, probably best to add a scene after every instance of this to make sure it actually does what's intended.
            renpy.hide(self.name)
            # renpy.say(p,str(self.genChooser)) 
            # Used for testing if genChooser was working properly
            if(hasTrans):
                renpy.with_statement(wi,always=True)
        def affOut(self) -> str:
            self.show("idle",genpos,dis,true)
            wor = "interesting."
            if (self.aff >= 2.0):
                wor = "irresistible."
            elif (self.aff >= 1.8):
                wor = "enchanting."
            elif (self.aff >= 1.6):
                word = "captivating."
            elif (self.aff >= 1.4):
                wor = "winsome."
            elif (self.aff >= 1.2):
                wor = "charming."
            elif (self.aff >= 1.0):
                wor = "cute."
            elif (self.aff >= 0.8):
                wor = "lovely."
            elif (self.aff >= 0.6):
                wor = "appealing."
            elif (self.aff >= 0.4):
                wor = "endearing."
            elif (self.aff >= 0.2):
                wor = "pleasing."
            elif (self.aff >= 0.1):
                wor = "intriguing."
            elif (self.aff > -0.05):
                pass
            elif (self.aff >= -0.1):
                wor = "a bit of a nuisance."
            elif (self.aff >= -0.2):
                wor = "a right nuisance."
            elif (self.aff >= -0.4):
                wor = "bothersome."
            elif (self.aff >= -0.6):
                wor = "an honourable nuisance."
            elif (self.aff >= -0.8):
                wor = "disturbing."
            elif (self.aff >= -1.0):
                wor = "annoying."
            elif (self.aff >= -1.2):
                wor = "a proper annoyance."
            elif (self.aff >= -1.4):
                wor = "contemptible."
            elif (self.aff >= -1.6):
                wor = "despicable."
            elif (self.aff >= -1.8):
                wor = "reprehensible."
            elif (self.aff >= -2.0):
                wor = "the scum of the Earth."
            else:
                wor = "The Right Honourable Lord Nuisance of the City of London (How did you even manage to get them to hate you this much???)."
            return wor
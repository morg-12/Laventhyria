default dmp = Char("001","girl",dname,"Live2D/dmpc","dmpc",True, False,True,.6,2)
default al = Char("002","", "Alva", "Live2D/al","al",True, True,False,.6,renpy.random.random()*2)
default gw = Char("003","","Gwynedd","Live2D/gw","gw",True,True,False,.6,renpy.random.random()*2)
default ho = Char("004","","Hoshi","Live2D/ho","ho",True,True,False,.6,renpy.random.random()*2)
default gb = Char("005","","Garlic Bread","images/Garlic_Bread.png","Garlic_Bread",False,False,False,.6,-1, isIma = true, customFallback = "Garlic_Bread.png")
image gIm = Transform("Garlic_Bread.png",zoom = 16.0)
$ gb.ima = gIm
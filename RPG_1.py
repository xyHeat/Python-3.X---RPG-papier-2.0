from tkinter import *
from random import *

#----- DEFINITIONS PRINCIPALES -----

def NewGame():
    CloseMainMenu()
    ResetSaveFile()
    DefinirLeNomDuJoueur()

def Quit():
    RPG_fenetre.destroy()

def Continuer():
    CloseMainMenu()

    global nomJoueur
    global niveauJoueur
    global viesJoueur
    global argentJoueur
    global savePoint
    global story_line
    global attaqueJoueur
    global defenseJoueur
    
    saveFile = open("save.txt","r")

    nomJoueur = saveFile.readline().replace("\n","")
    niveauJoueur  = eval(saveFile.readline().replace("\n",""))
    viesJoueur = eval(saveFile.readline().replace("\n",""))
    argentJoueur = eval(saveFile.readline().replace("\n",""))
    savePoint = eval(saveFile.readline().replace("\n",""))
    story_line = eval(saveFile.readline().replace("\n",""))
    attaqueJoueur = eval(saveFile.readline().replace("\n",""))
    defenseJoueur = eval(saveFile.readline().replace("\n",""))

    saveFile.close()

    ReadStory()

def Save():

    global nomJoueur
    global niveauJoueur
    global viesJoueur
    global argentJoueur
    global savePoint
    global story_line
    global attaqueJoueur
    global defenseJoueur
    
    saveFile = open("save.txt","w")

    saveFile.write(str(nomJoueur)+"\n")
    saveFile.write(str(niveauJoueur)+"\n")
    saveFile.write(str(viesJoueur)+"\n")
    saveFile.write(str(argentJoueur) + "\n")
    saveFile.write(str(savePoint)+"\n")
    saveFile.write(str(story_line) + "\n")
    saveFile.write(str(attaqueJoueur)+"\n")
    saveFile.write(str(defenseJoueur) + "\n")
    
    saveFile.close()
    

def ResetSaveFile():
    global nomJoueur
    global niveauJoueur
    global viesJoueur
    global argentJoueur
    global savePoint
    global story_line
    global attaqueJoueur
    global defenseJoueur

    nomJoueur = "_nomJoueur"
    niveauJoueur = 1
    viesJoueur = 100
    argentJoueur = 100
    savePoint = 0
    story_line = 0
    attaqueJoueur = 10
    defenseJoueur = 10

    saveFile = open("save.txt","w")

    saveFile.write(str(nomJoueur)+"\n")
    saveFile.write(str(niveauJoueur)+"\n")
    saveFile.write(str(viesJoueur)+"\n")
    saveFile.write(str(argentJoueur) + "\n")
    saveFile.write(str(savePoint)+"\n")
    saveFile.write(str(story_line) + "\n")
    saveFile.write(str(attaqueJoueur)+"\n")
    saveFile.write(str(defenseJoueur) + "\n")

    saveFile.close()

def GetAStatValue(stat):
    saveFile = open("save.txt","r")

    _nomJoueur = saveFile.readline().replace("\n","")
    _niveauJoueur  = eval(saveFile.readline().replace("\n",""))
    _viesJoueur = eval(saveFile.readline().replace("\n",""))
    _argentJoueur = eval(saveFile.readline().replace("\n",""))
    _savePoint = eval(saveFile.readline().replace("\n",""))
    _story_line = eval(saveFile.readline().replace("\n",""))
    _attaqueJoueur = eval(saveFile.readline().replace("\n",""))
    _defenseJoueur = eval(saveFile.readline().replace("\n",""))

    saveFile.close()

    if stat == "nom":
        return _nomJoueur
    elif stat == "niveau":
        return _niveauJoueur
    elif stat == "vies":
        return _viesJoueur
    elif stat == "argent":
        return _argentJoueur
    elif stat == "save":
        return _savePoint
    elif stat == "story":
        return _story_line
    elif stat == "attaque":
        return _attaqueJoueur
    elif stat == "defense":
        return _defenseJoueur


#----- DEFINITIONS NOM DU JOUEUR -----

def DefinirLeNomDuJoueur():
    global RPG_fenetre
    
    global nomLabel
    nomLabel = Label(RPG_fenetre, text ="Entrez un nom pour votre héro", bg = "black", fg = "white", font=(16), width = 40, height = 2)
    nomLabel.place(x= 240, y=180)

    global nomEntry
    nomEntry = Entry(RPG_fenetre, bg = "black", fg = "white", font=(16), width = 12)
    nomEntry.place(x= 360, y=220)
    
    global validerButton
    validerButton = Button(RPG_fenetre, text = "Valider nom", bg = "black", fg = "white", width = 12, height = 2, bd = 0, font=(16), command = ValiderNom)
    validerButton.place(x= 360, y=380)

def ValiderNom():
    global nomLabel
    global nomEntry    
    global validerButton

    nomLabel.destroy()
    
    _nom = str(nomEntry.get())
    nomEntry.destroy()

    validerButton.destroy()

    global nomJoueur
    nomJoueur = _nom

    Save()

    ReadStory()

#----- MENU PRINCIPAL -----
    # ----- Nouvelle partie / Continuer / Quitter

def OpenMainMenu():
    global RPG_fenetre
    
    global newGameButton
    newGameButton = Button(RPG_fenetre, text = "Nouvelle Partie", bg = "black", fg = "white", width = 12, height = 2, bd = 0, font=(16), command = NewGame)
    newGameButton.place(x= 340, y=180)

    global playButton
    playButton = Button(RPG_fenetre, text = "Continuer", bg = "black", fg = "white", width = 8, height = 2, bd = 0, font=(16), command = Continuer)
    playButton.place(x= 360, y=280)

    global quitButton
    quitButton = Button(RPG_fenetre, text = "Quitter", bg = "black", fg = "white", width = 6, height = 2, bd = 0, font=(16), command = Quit)
    quitButton.place(x= 370, y=380)

def CloseMainMenu():
    global newGameButton
    newGameButton.destroy()

    global playButton
    playButton.destroy()

    global quitButton
    quitButton.destroy()


# ----- LECTURE HISTOIRE -----

def PlaceStoryLabelAndButton():    
    global story_ligne1
    global story_ligne2
    global story_ligne3
    global story_ContinueButton

    story_ligne1 = Label(RPG_fenetre, text ="", bg = "black", fg = "white", font=(16), width = 50, height = 2)
    story_ligne1.place(x = 175, y = 180)

    story_ligne2 = Label(RPG_fenetre, text ="", bg = "black", fg = "white", font=(16), width = 50, height = 2)
    story_ligne2.place(x = 175, y = 240)

    story_ligne3 = Label(RPG_fenetre, text ="", bg = "black", fg = "white", font=(16), width = 50, height = 2)
    story_ligne3.place(x=175, y = 300)

    story_ContinueButton = Button(RPG_fenetre, text = "", bg = "black", fg = "white", width = 50, height = 2, bd = 0, font=(16))
    story_ContinueButton.place(x= 175, y=380)

def ReadStory():
    global story_line
    global last_story_line
    
    storyFile = open("story.txt","r")

    _str = str("")
    
    i = int(0)
    lineCount = int(0)

    PlaceStoryLabelAndButton()

    global story_ligne1
    global story_ligne2
    global story_ligne3
    global story_ContinueButton

    global nomJoueur

    continueRead = True
    while (continueRead==True):
        if i < story_line:
            storyFile.readline()
        else:
            lineCount = lineCount + 1
            ligne = storyFile.readline()
            _str = str(ligne).replace("\n","")
            _str = _str.strip()

            if _str.count("SAVE") == 1:
                Save()

            if _str.count("&playerName&") == 1:
                _str = _str.replace("&playerName&",nomJoueur)

            if _str.count("__NEXT__") == 1:
                l = str("")
                for c in _str:
                    if c.isdigit() == True:
                        l = l + c
                last_story_line = story_line
                story_line = eval(l)
                print(story_line)
                continueRead = False
                story_ContinueButton.configure(command = NextRead, text = "Suivant")
            elif _str.count("__BATTLE__") == 1:
                _str = storyFile.readline()

                ReadBattleSettings(_str)

                print(story_line)
                continueRead = False

                story_ContinueButton.configure(command = LunchBattle, text ="Combattre")

            elif _str.count("__CARTE__") == 1:
                l = str("")

                isReadingMapName = False

                global nomMapAOuvrir
                nomMapAOuvrir = str("")
                
                for c in _str:
                    if isReadingMapName == False:
                        if c.isdigit() == True:
                            l = l + c
                        elif c == "<":
                            isReadingMapName = True
                    else:
                        if c == ">":
                            isReadingMapName = False
                        else:
                            nomMapAOuvrir = nomMapAOuvrir + c
                            
                last_story_line = story_line
                story_line = eval(l)
                print(story_line)
                continueRead = False
                story_ContinueButton.configure(command = OpenAMap, text = "Ouvrir la carte")
                            
                
            else:
                if lineCount == 1:
                    story_ligne1.configure(text=_str)
                elif lineCount == 2:
                    story_ligne2.configure(text=_str)
                else:
                    story_ligne3.configure(text=_str)  
                            
        i = i + 1

    storyFile.close()

def NextRead():
    Delete_StoryLabels()
    ReadStory()

def Delete_StoryLabels():
    global story_ligne1
    global story_ligne2
    global story_ligne3
    global story_ContinueButton

    story_ligne1.destroy()
    story_ligne2.destroy()
    story_ligne3.destroy()
    story_ContinueButton.destroy()

def ReadBattleSettings(line):
    global story_line
    global last_story_line
    
    l = str("")
    
    global _mob
    global _mobType

    _mob = str("")
    _mobType = str("")

    isReading_mob = False
    isReading_mobType = False

    for c in line:
        if c == "<":
            isReading_mobType = True
            
        elif c == ">":
            isReading_mobType = False
            
        elif c == "_":
            if isReading_mob == True:
                isReading_mob = False
            else:
                isReading_mob = True

        else:
            if isReading_mob == True:
                _mob = _mob + c.lower()
            elif isReading_mobType == True:
                _mobType = _mobType + c.lower()
            else:
                if c.isdigit:
                    l = l + c                 
    last_story_line = story_line        
    story_line = eval(l)

    print("mob = " + _mob)
    print("mobType = " + _mobType)


# ----- COMBATS -----


allMobsTypes = ["bandits", "cavalde", "isle", "parmes","ouse","zag dabog", "story"]
allMobsTypesCount = len(allMobsTypes)

bandits = ["maraudeur","voleur"]
allBanditsCount = len(bandits)

soldats = ["chevalier","lancier","archer","mage", "prince","roi","épéiste"]
allSoldatsCount = len(soldats)

story = ["edward drawed injured a"]
allStoryCount = len(story)


def LunchBattle():
    Save()

    global player_willDodge
    player_willDodge = False

    global mob_willDodge
    mob_willDodge = False
    
    Delete_StoryLabels()

    global viesJoueur
    global playerCurrentLife

    playerCurrentLife = viesJoueur
    
    global _mob
    global _mobType    

    if _mobType == "random":        
        RandomMobType()
        print("Random mobType = " + _mobType)
        RandomMob()
        print("Random mob = " + _mob)
    else:
        if _mob == "null":
            RandomMob()

    print("Battle : " + _mob)
    SetupMobValues()

def RandomMobType():
    global _mobType    

    i = int(randint(0, allMobsTypesCount - 1))
    _mobType = allMobsTypes[i]
    

def RandomMob():
    global _mobType
    global _mob
    
    if _mobType == "bandits":
        i = int(randint(0, allBanditsCount - 1))
        _mob = bandits[i]
    elif _mobType == "soldats":
        i = int(randint(0, allSoldatsCount - 1))
        _mob = soldats[i]
    elif _mobType == "isle":
        i = int(randint(0, allSoldatsCount - 1))
        _mob = soldats[i]

def SetupMobValues():

    global _mob
    global _mobType

    global bMobName
    global bMobMaxLife
    global bMobCurrentLife
    global bMobLevel
    global bMobAttack
    global bMobDefense


    path = "MobFiles/" + _mobType + "/" + _mob + ".txt"
    mobFile = open(path,"r")

    bMobName = str(mobFile.readline().replace("\n",""))
    bMobMaxLife = eval(mobFile.readline().replace("\n",""))
    bMobCurrentLife = bMobMaxLife
    bMobLevel = eval(mobFile.readline().replace("\n",""))
    bMobAttack = eval(mobFile.readline().replace("\n",""))
    bMobDefense = eval(mobFile.readline().replace("\n",""))

    mobFile.close()

    print("bMobName =", bMobName)
    print("bMobMaxLife =", bMobMaxLife)
    print("bMobCurrentLife =", bMobCurrentLife)
    print("bMobLevel =", bMobLevel)
    print("bMobAttack =", bMobAttack)
    print("bMobDefense =", bMobDefense)

    SetupBattleInterface()

def SetupBattleInterface():
    global RPG_fenetre
    
    global battlePanel
    global infoPanel
    global actionPanel

    global playerIcon
    global playerLifeLabel
    global playerLevelLabel

    global mobIcon
    global mobLifeLabel
    global mobLevelLabel

    global _mob
    global _mobType
    
    battlePanel = Frame(RPG_fenetre, bg = "white", width = 404, height = 304,highlightcolor="darkgrey", highlightthickness=2, highlightbackground="darkgrey")
    battlePanel.place(x=200, y = 150)

    infoPanel = Frame(battlePanel, bg = "white", width = 400, height = 225,highlightcolor="darkgrey", highlightthickness=2, highlightbackground="darkgrey")
    infoPanel.place(x=0,y=0)

    actionPanel = Frame(battlePanel, bg = "white", width = 400, height = 75,highlightcolor="darkgrey", highlightthickness=2, highlightbackground="darkgrey")
    actionPanel.place(x= 0,y=225)


    # Icon Joueur -----
    playerIcon = Canvas(infoPanel, bg = "white",bd = 0, width = 96, height = 96)
    playerIcon.place(x=29,y=100)

    global pI
    pI = PhotoImage(file="Icons/player_Icon.png")
    playerIcon.create_image(48,48,image=pI)

    # Icon Mob -----
    mobIcon = Canvas(infoPanel, bg = "white",bd = 0, width = 96, height = 96)
    mobIcon.place(x=275,y=29)

    global mI
    _file = "Icons/" + _mobType + "_" + _mob + "_Icon.png"
    mI = PhotoImage(file= _file)
    mobIcon.create_image(48,48,image=mI)

    # Labels Joueur -----
    playerLevelLabel = Label(infoPanel, text ="Niveau Joueur", bg = "white", fg = "black")
    playerLevelLabel.place(x= 29 ,y= 70)
    
    playerLifeLabel = Label(infoPanel, text ="Vie Joueur", bg = "white", fg = "black")
    playerLifeLabel.place(x=29,y=85)

    # Labels Mob -----
    mobLevelLabel = Label(infoPanel, text ="Niveau Mob", bg = "white", fg = "black")
    mobLevelLabel.place(x= 230 ,y= 125)
    
    mobLifeLabel = Label(infoPanel, text ="Vie Mob", bg = "white", fg = "black")
    mobLifeLabel.place(x=255,y=140)

    UpdatePlayerBattleLabels()
    UpdateMobBattleLabels()

    Place_ActionResultLabelsAndButton()

    Player_Turn()

def UpdatePlayerBattleLabels():
    global nomJoueur
    global niveauJoueur
    global viesJoueur

    global playerLifeLabel
    global playerLevelLabel

    global playerCurrentLife

    _str = nomJoueur + " : " + str(niveauJoueur) + " (lvl)"
    playerLevelLabel.configure(text=_str)

    _str = "Vies : " + str(playerCurrentLife) + " | " + str(viesJoueur)
    playerLifeLabel.configure(text=_str)

def UpdateMobBattleLabels():
    global bMobName
    global bMobMaxLife
    global bMobCurrentLife
    global bMobLevel

    global mobLifeLabel
    global mobLevelLabel

    _str = bMobName + " : " + str(bMobLevel) + " (lvl)"
    mobLevelLabel.configure(text=_str)

    _str = "Vies : " + str(bMobCurrentLife) + " | " + str(bMobMaxLife)
    mobLifeLabel.configure(text=_str)

def Player_Turn():

    print("")
    print("Player Turn ------")

    Destroy_ActionResultLabelsAndButton()

    global player_willDodge
    player_willDodge = False

    Place_PlayerEntries()


def PlayerAttack(arg):
    global playerEntry
    global sendPlayerEntry
    global entryLabel
    
    global attaque
    global motPlusProche

    attaque = str(playerEntry.get().replace("\n","")).lower()
    print("Entrée du joueur =",attaque)

    motPlusProche = str("")
    nbIdentite = int(0)
    nbDifference = int(0)
    total = int(0)
    pourcentageIdentite = float(0)

    attackList = open("Attaques/Liste.txt","r")

    for ligne in attackList:
        _attaque = attaque
        nbIdentite = int(0)
        nbDifference = int(0)
        total = int(0)
        
        l = str(ligne.replace("\n","")).lower()

        # Dans le cas où l'entrée du joueur est plus longue (ou égale) que la ligne.

        if len(_attaque) >= len(l):
            nbDifference = nbDifference + (len(_attaque) - len(l))
            total = total + (len(_attaque) - len(l))
            for i in range (len(l)):
                if l[i] == _attaque[i]:
                    nbIdentite = nbIdentite + 1
                else:
                    nbDifference = nbDifference + 1
                total = total + 1

        # Dans le cas où l'entrée du joueur est moins longue que la ligne.
        if len(_attaque) < len(l):
            nbDifference = nbDifference + (len(l) - len(_attaque))
            total = total + (len(l) - len(_attaque))
            for i in range (len(_attaque)):
                if l[i] == _attaque[i]:
                    nbIdentite = nbIdentite + 1
                else:
                    nbDifference = nbDifference + 1
                total = total + 1

        _pourcentageIdentite = float((100 * nbIdentite)/(total))        
                
        if _pourcentageIdentite > pourcentageIdentite:
            pourcentageIdentite = _pourcentageIdentite
            motPlusProche = l
            
        print("Comparison avec le mot",l,":")
        print("Identité =",nbIdentite)
        print("Difference =",nbDifference)
        print("% Identité =", _pourcentageIdentite)
        

    if pourcentageIdentite == 0:
        motPlusProche = "coup d'épée"
        
    print("Le mot le plus proche est :", motPlusProche)  

    attackList.close()

    Destroy_PlayerEntries()
    Place_ActionResultLabelsAndButton()

    global resultLabel
    global damageLabel
    global endTurnButton

    _str = attaque + " ==> " + motPlusProche + " (" + str(pourcentageIdentite) + "%)"

    resultLabel.configure(text = _str)

    global succes

    if pourcentageIdentite < 100:
        _str = "Le joueur a raté son attaque, il en subit les dommages"
        succes = False
    else:
        _str = "Le joueur lance l'attaque : " + attaque
        succes = True

    damageLabel.configure(text = _str)

    endTurnButton.configure(text ="FIN DE TOUR", command = LunchAttaque)

def Place_PlayerEntries():
    global actionPanel
        
    global playerEntry
    global sendPlayerEntry
    global entryLabel

    entryLabel = Label(actionPanel, text ="Entrez une attaque", bg = "white", fg = "black")
    entryLabel.place(x=50,y=0)
    
    playerEntry = Entry(actionPanel, bg = "white", fg = "black",width = 50)
    playerEntry.place(x = 50, y = 15)

    playerEntry.bind('<Control-x>', lambda e: 'break') #disable cut
    playerEntry.bind('<Control-c>', lambda e: 'break') #disable copy
    playerEntry.bind('<Control-v>', lambda e: 'break') #disable paste
    playerEntry.bind('<Button-3>', lambda e: 'break')  #disable right-click

    playerEntry.bind('<Return>', PlayerAttack)  #enable Return

    sendPlayerEntry = Button(actionPanel, bg = "white", fg  ="black", text ="ENVOYER", command = lambda x = "button":PlayerAttack(x))
    sendPlayerEntry.place(x=175, y = 35)

def Destroy_PlayerEntries():
    global playerEntry
    global sendPlayerEntry
    global entryLabel

    playerEntry.bind('<Return>', lambda e: 'break')  #disable Return

    playerEntry.destroy()
    sendPlayerEntry.destroy()
    entryLabel.destroy()


def Place_ActionResultLabelsAndButton():
    global actionPanel
    
    global resultLabel
    global damageLabel
    global endTurnButton

    resultLabel = Label(actionPanel, text ="", bg = "white", fg = "black")
    resultLabel.place(x=50,y=0)

    damageLabel = Label(actionPanel, text ="", bg = "white", fg = "black")
    damageLabel.place(x=50,y=20)

    endTurnButton = Button(actionPanel, bg = "white", fg  ="black", text ="")
    endTurnButton.place(x=160, y = 40)
    

def Destroy_ActionResultLabelsAndButton():
    global resultLabel
    global damageLabel
    global endTurnButton    

    resultLabel.destroy()
    damageLabel.destroy()
    endTurnButton.destroy()
    
def LunchAttaque():
    global resultLabel
    global damageLabel
    global endTurnButton

    resultLabel.destroy()
    damageLabel.destroy()
    endTurnButton.destroy()
    
    global motPlusProche

    global attackType
    global boostType
    global attackEffectPoint
    
    attackType = str("")
    boostType =str("")
    attackEffectPoint = int(0)

    DefineAttack(motPlusProche)

    global turn
    turn = "player"

    UseAttack(motPlusProche,turn)    


def DamagePlayer(dmg):
    global mob_willDodge
    global turn
            
    if mob_willDodge == True:
        if turn == "player":
            Mob_Turn()
        else:
            Player_Turn()
    else : 
        global playerCurrentLife
        playerCurrentLife = playerCurrentLife - dmg
        UpdatePlayerBattleLabels()

        
        if playerCurrentLife <= 0:
            EndBattle("player dead")
        else:
            if turn == "player":
                Mob_Turn()
            else:
                Player_Turn()
            

def DamageMob(dmg):
    global mob_willDodge
    global turn

    if mob_willDodge == True:
        if turn == "player":
            Mob_Turn()
        else:
            Player_Turn()
    else :    
        global bMobCurrentLife
        bMobCurrentLife = bMobCurrentLife - dmg
        UpdateMobBattleLabels()

        if bMobCurrentLife <= 0:
            EndBattle("mob dead")
        else:
            if turn == "player":
                Mob_Turn()
            else:
                Player_Turn()
        

def BoostPlayer(effect, bType):
    global attaqueJoueur
    global defenseJoueur
    global playerCurrentLife
    global viesJoueur
    
    if bType == "attaque":
        attaqueJoueur =  attaqueJoueur + effect
    elif bType =="defense":
        defenseJoueur = defenseJoueur + effect
    elif bType =="heal":
        playerCurrentLife = playerCurrentLife + effect
        if viesJoueur < playerCurrentLife:
            playerCurrentLife = viesJoueur

    UpdatePlayerBattleLabels()

    global turn

    if turn == "player":
        Mob_Turn()
    else:
        Player_Turn()

def BoostMob(effect, bType):
    global bMobMaxLife
    global bMobCurrentLife
    global bMobAttack
    global bMobDefense
    
    if bType == "attaque":
        bMobAttack =  bMobAttack + effect
    elif bType =="defense":
        bMobDefense = bMobDefense + effect
    elif bType =="heal":
        bMobCurrentLife = bMobCurrentLife + effect
        if bMobMaxLife < playerCurrentLife:
            bMobCurrentLife = bMobMaxLife

    UpdateMobBattleLabels()

    global turn

    if turn == "player":
        Mob_Turn()
    else:
        Player_Turn()
        
def EndBattle(cause):
    RestaureStats()

    global battlePanel
    global infoPanel
    global actionPanel
    
    infoPanel.destroy()
    actionPanel.destroy()
    battlePanel.destroy()
    
    global story_ligne1
    global story_ligne2
    global story_ligne3
    global story_ContinueButton

    global story_line
    global last_story_line
    
    if cause == "mob dead":
        global bMobLevel
        global argentJoueur

        argentJoueur = argentJoueur + (bMobLevel * bMobLevel)

        Save()

        PlaceStoryLabelAndButton()

        _str = ("")

        _str = "Félicitation, vous avez vaincu le Mob !"
        story_ligne1.configure(text = _str)

        _str = "Vous gagnez " + str(bMobLevel) + " argent ("+str(argentJoueur)+")."
        story_ligne2.configure(text = _str)

        _str = "La partie est save, vous pouvez quitter maintenant ou continuer"
        story_ligne3.configure(text = _str)

        story_ContinueButton.configure(command = NextRead, text = "Suivant")

    elif cause == "fuite":
        Save()

        PlaceStoryLabelAndButton()

        _str = ("")

        _str = "Vous avez pris la fuite."
        story_ligne1.configure(text = _str)

        _str = "Vous ne gagnez rien."
        story_ligne2.configure(text = _str)

        _str = "La partie est save, vous pouvez quitter maintenant ou continuer"
        story_ligne3.configure(text = _str)

        story_ContinueButton.configure(command = NextRead, text = "Suivant")

    elif cause == "player dead":

        PlaceStoryLabelAndButton()

        story_line = last_story_line
        Save()

        _str = ("")

        _str = "Vous êtes mort."
        story_ligne1.configure(text = _str)

        _str = "Vous pouvez reprendre au dernier point de sauvegarde,"
        story_ligne2.configure(text = _str)

        _str = "ou recommencer une nouvelle partie."
        story_ligne3.configure(text = _str)

        story_ContinueButton.configure(command = DeathToMainMenu, text = "Retour au menu")    
        
        
def RestaureStats():
    global attaqueJoueur
    global defenseJoueur

    attaqueJoueur = GetAStatValue("attaque")
    defenseJoueur = GetAStatValue("defense")

    Save()

def DeathToMainMenu():
    Delete_StoryLabels()
    Close_MainWindow()
    Create_MainWindow()

def DefineAttack(a):
    global attackType
    global boostType
    global attackEffectPoint
    global esquive

    if a == "coup d'épée":
        attackType = "attaque"
        boostType = ""
        attackEffectPoint = int(20)
        
    elif a == "protection":
        attackType = "boost"
        boostType = "defense"
        attackEffectPoint = int(5)
        
    elif a == "coup de hache":
        attackType = "attaque"
        boostType = ""
        attackEffectPoint = int(25)

    elif a == "esquive":
        attackType = "esquive"
        boostType = "null"
        attackEffectPoint = int(0)

    elif a == "coup de dague":
        attackType = "attaque"
        boostType = ""
        attackEffectPoint = int(10)

    elif a == "":
        attackType = ""
        boostType = ""
        attackEffectPoint = int(0)
        
def Mob_Turn():

    print("")
    print("Mob Turn ------")

    Destroy_ActionResultLabelsAndButton()

    global mob_willDodge
    mob_willDodge = False
    
    global bMobAttackList
    bMobAttackList = []

    ReadMobAttackList()

    i = randint(0, len(bMobAttackList) - 1)

    global mobAttack
    mobAttack = bMobAttackList[i]
    print("Mob use", mobAttack)

    global turn
    turn = "mob"

    global succes
    succes = True

    DefineAttack(mobAttack)

    Place_ActionResultLabelsAndButton()    
    global resultLabel
    global damageLabel
    global endTurnButton
    
    global bMobName

    _str = bMobName + " lance l'attaque : " + mobAttack
    resultLabel.configure(text = _str)

    endTurnButton.configure(text ="FIN DE TOUR", command = Mob_Attack)
     
        
def Mob_Attack():
    Destroy_ActionResultLabelsAndButton()  
    
    global mobAttack
    global turn

    UseAttack(mobAttack, turn)

def ReadMobAttackList():
    global _mob
    global _mobType

    global bMobAttackList
    bMobAttackList.clear()

    path = "MobFiles/" + _mobType + "/" + _mob + ".txt"
    mobFile = open(path,"r")

    attackLineNb = int(5)
    attackLineString = str("")

    for i in range(6):
        l = mobFile.readline()
        if i == 5:
            attackLineString = str(l)

    mobFile.close()

    attaque = str("")
    for c in attackLineString:
        if c == "," or c == "\n":
            bMobAttackList.append(attaque)
            attaque = str("")
        else:
            attaque = attaque + c

    print(bMobAttackList)
    

def UseAttack(attaque, side):
    global succes

    global attackType
    global boostType
    global attackEffectPoint

    global player_willDodge
    global mob_willDodge

    global esquive_context

    global attaqueJoueur
    global bMobAttack

    print("attackEffectPoint =", attackEffectPoint)
    
    if side == "player":
        if attackType == "attaque":
            modif = attackEffectPoint * ( (attaqueJoueur)/((niveauJoueur * 10) + 100))
            attackEffectPoint = attackEffectPoint + int(round(modif))
        elif attackType == "boost":
            modif = attackEffectPoint * ( (defenseJoueur)/((niveauJoueur * 10) + 100))
            attackEffectPoint = attackEffectPoint + int(round(modif))
    else:
        if attackType == "attaque":
            modif = attackEffectPoint * ( (bMobAttack)/((bMobLevel * 10) + 100))
            attackEffectPoint = attackEffectPoint + int(round(modif))
        elif attackType == "boost":
            modif = attackEffectPoint * ( (bMobDefense)/((bMobLevel * 10) + 100))
            attackEffectPoint = attackEffectPoint + int(round(modif))

    print("new attackEffectPoint =", attackEffectPoint)
        

    if succes == True:
        if attackType == "attaque":
            if side == "player":
                if mob_willDodge == True:
                    esquive_context = "mob esquive player"
                    Esquive()
                else:
                    DamageMob(attackEffectPoint)
            else :
                if player_willDodge == True:
                    esquive_context = "player esquive mob"
                    Esquive()
                else:
                    DamagePlayer(attackEffectPoint)
                
        elif attackType == "boost":
            BoostPlayer(attackEffectPoint,boostType)
            
        elif attackType == "esquive":
            if side == "player":
                player_willDodge = True
                esquive_context = "player set esquive"
                SetEsquiveMode()
            else:
                mob_willDodge = True
                esquive_context = "mob set esquive"
                SetEsquiveMode()
                
                
    else:
        if attackType == "attaque":
            if player_willDodge == True:
                esquive_context = "player esquive player"
                Esquive()
            else:
                DamagePlayer(attackEffectPoint)
        else:
            BoostPlayer(0,"null")    

def SetEsquiveMode():
    Place_ActionResultLabelsAndButton()

    global esquive_context
        
    global actionPanel
    
    global resultLabel
    global damageLabel
    global endTurnButton

    global nomJoueur
    global bMobName

    if esquive_context == "player set esquive":
        resultLabel.configure(text = nomJoueur + " passe en mode esquive.")
        damageLabel.configure(text = "Il esquivera la prochaine attaque.")
        endTurnButton.configure(text = "Suivant", command = Mob_Turn)
    else:        
        resultLabel.configure(text = bMobName + " passe en mode esquive.")
        damageLabel.configure(text = "Il esquivera la prochaine attaque.")
        endTurnButton.configure(text = "Suivant", command = Player_Turn)

def EndEsquiveMode():
    Destroy_ActionResultLabelsAndButton()
    Place_ActionResultLabelsAndButton()

    global esquive_context
        
    global actionPanel
    
    global resultLabel
    global damageLabel
    global endTurnButton

    if esquive_context == "player esquive mob":
        resultLabel.configure(text = nomJoueur + " sort du mode esquive.")
        damageLabel.configure(text = "Il n'esquivera pas la prochaine attaque.")
        endTurnButton.configure(text = "Suivant", command = Player_Turn)

    elif esquive_context == "player esquive player":
        resultLabel.configure(text = nomJoueur + " sort du mode esquive.")
        damageLabel.configure(text = "Il n'esquivera pas la prochaine attaque.")
        endTurnButton.configure(text = "Suivant", command = Mob_Turn)
        
    else:        
        resultLabel.configure(text = bMobName + " sort du mode esquive.")
        damageLabel.configure(text = "Il n'esquivera pas la prochaine attaque.")
        endTurnButton.configure(text = "Suivant", command = Mob_Turn)
    
def Esquive():
    Place_ActionResultLabelsAndButton()

    global esquive_context
        
    global actionPanel
    
    global resultLabel
    global damageLabel
    global endTurnButton

    global player_willDodge
    global mob_willDodge

    if esquive_context == "player esquive player":
        player_willDodge = False
        resultLabel.configure(text = nomJoueur + " esquive l'attaque.")
        damageLabel.configure(text = "")
        endTurnButton.configure(text = "Suivant", command = EndEsquiveMode)
        
    elif esquive_context == "player esquive mob":
        player_willDodge = False
        resultLabel.configure(text = nomJoueur + " esquive l'attaque.")
        damageLabel.configure(text = "")
        endTurnButton.configure(text = "Suivant", command = EndEsquiveMode)
    else:
        mob_willDodge = False
        resultLabel.configure(text = bMobName + " esquive l'attaque.")
        damageLabel.configure(text = "")
        endTurnButton.configure(text = "Suivant", command = EndEsquiveMode)

# ----- CARTES -----

def OpenAMap():
    global nomMapAOuvrir

    print("Ouverture de la carte : " + nomMapAOuvrir)
    
    Create_MapInterface(nomMapAOuvrir)

def Create_MapInterface(name):
    global RPG_fenetre
    
    global _map
    global _mapExitButton


    _map = Canvas(RPG_fenetre, width = 600, height = 450, bg = "white",bd = 0)
    _map.place(x=100,y=75)
    
    global _mapIcon    
    _str = "Maps/"+name+".png"
    _mapIcon = PhotoImage(file=_str)
    _map.create_image(300,225,image=_mapIcon)

    _mapExitButton = Button(RPG_fenetre, text = "Sortir", command = CloseAMap)
    _mapExitButton.place(x=200,y=545)


def CloseAMap():
    Destroy_MapInterface()
    NextRead()

def Destroy_MapInterface():
    global _map
    global _mapExitButton

    _map.destroy()
    _mapExitButton.destroy()


# ----- FENETRE PRINCIPALE DU JEU -----


def Create_MainWindow():        
    global RPG_fenetre
    RPG_fenetre = Tk()
    RPG_fenetre.title("RPG - Main)")
    RPG_fenetre.configure(bg = "black", width = 800, height = 600)

    OpenMainMenu()

    RPG_fenetre.mainloop()

def Close_MainWindow():
    Quit()

Create_MainWindow()

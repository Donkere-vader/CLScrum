from tkinter import *
from os import makedirs
import os
import shutil
from datetime import *
from sys import exit
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

try:
    makedirs('boards')
except:
    pass

try:
    f = open('boards/BOARDS.txt').readlines()
except:
    file = open('boards/BOARDS.txt', 'w')
    file.close()

try:
    f = open('boards/settings.txt').readlines()
except:
    f = open('boards/settings.txt', 'w')
    f.write('background:grey\n')
    f.write('maxcards:5\n')
    f.write('textcolor:black')
    f.close()

try:
    f = open('boards/colors.txt').readlines()
except:
    file = open('boards/colors.txt', 'w')
    file.write('snow\nghost white\nwhite smoke\ngainsboro\nfloral white\nold lace\nlinen\nantique white\npapaya whip\nblanched almond\nbisque\npeach puff\nnavajo white\nlemon chiffon\nmint cream\nazure\nalice blue\nlavender\nlavender blush\nmisty rose\ndark slate gray\ndim gray\nslate gray\nlight slate gray\ngray\nlight grey\nmidnight blue\nnavy\ncornflower blue\ndark slate blue\nslate blue\nmedium slate blue\nlight slate blue\nmedium blue\nroyal blue\nblue\ndodger blue\ndeep sky blue\nsky blue\nlight sky blue\nsteel blue\nlight steel blue\nlight blue\npowder blue\npale turquoise\ndark turquoise\nmedium turquoise\nturquoise\ncyan\nlight cyan\ncadet blue\nmedium aquamarine\naquamarine\ndark green\ndark olive green\ndark sea green\nsea green\nmedium sea green\nlight sea green\npale green\nspring green\nlawn green\nmedium spring green\ngreen yellow\nlime green\nyellow green\nforest green\nolive drab\ndark khaki\nkhaki\npale goldenrod\nlight goldenrod yellow\nlight yellow\nyellow\ngold\nlight goldenrod\ngoldenrod\ndark goldenrod\nrosy brown\nindian red\nsaddle brown\nsandy brown\ndark salmon\nsalmon\nlight salmon\norange\ndark orange\ncoral\nlight coral\ntomato\norange red\nred\nhot pink\ndeep pink\npink\nlight pink\npale violet red\nmaroon\nmedium violet red\nviolet red\nmedium orchid\ndark orchid\ndark violet\nblue violet\npurple\nmedium purple\nthistle\nsnow2\nsnow3\nsnow4\nseashell2\nseashell3\nseashell4\nAntiqueWhite1\nAntiqueWhite2\nAntiqueWhite3\nAntiqueWhite4\nbisque2\nbisque3\nbisque4\nPeachPuff2\nPeachPuff3\nPeachPuff4\nNavajoWhite2\nNavajoWhite3\nNavajoWhite4\nLemonChiffon2\nLemonChiffon3\nLemonChiffon4\ncornsilk2\ncornsilk3\ncornsilk4\nivory2\nivory3\nivory4\nhoneydew2\nhoneydew3\nhoneydew4\nLavenderBlush2\nLavenderBlush3\nLavenderBlush4\nMistyRose2\nMistyRose3\nMistyRose4\nazure2\nazure3\nazure4\nSlateBlue1\nSlateBlue2\nSlateBlue3\nSlateBlue4\nRoyalBlue1\nRoyalBlue2\nRoyalBlue3\nRoyalBlue4\nblue2\nblue4\nDodgerBlue2\nDodgerBlue3\nDodgerBlue4\nSteelBlue1\nSteelBlue2\nSteelBlue3\nSteelBlue4\nDeepSkyBlue2\nDeepSkyBlue3\nDeepSkyBlue4\nSkyBlue1\nSkyBlue2\nSkyBlue3\nSkyBlue4\nLightSkyBlue1\nLightSkyBlue2\nLightSkyBlue3\nLightSkyBlue4\nSlateGray1\nSlateGray2\nSlateGray3\nSlateGray4\nLightSteelBlue1\nLightSteelBlue2\nLightSteelBlue3\nLightSteelBlue4\nLightBlue1\nLightBlue2\nLightBlue3\nLightBlue4\nLightCyan2\nLightCyan3\nLightCyan4\nPaleTurquoise1\nPaleTurquoise2\nPaleTurquoise3\nPaleTurquoise4\nCadetBlue1\nCadetBlue2\nCadetBlue3\nCadetBlue4\nturquoise1\nturquoise2\nturquoise3\nturquoise4\ncyan2\ncyan3\ncyan4\nDarkSlateGray1\nDarkSlateGray2\nDarkSlateGray3\nDarkSlateGray4\naquamarine2\naquamarine4\nDarkSeaGreen1\nDarkSeaGreen2\nDarkSeaGreen3\nDarkSeaGreen4\nSeaGreen1\nSeaGreen2\nSeaGreen3\nPaleGreen1\nPaleGreen2\nPaleGreen3\nPaleGreen4\nSpringGreen2\nSpringGreen3\nSpringGreen4\ngreen2\ngreen3\ngreen4\nchartreuse2\nchartreuse3\nchartreuse4\nOliveDrab1\nOliveDrab2\nOliveDrab4\nDarkOliveGreen1\nDarkOliveGreen2\nDarkOliveGreen3\nDarkOliveGreen4\nkhaki1\nkhaki2\nkhaki3\nkhaki4\nLightGoldenrod1\nLightGoldenrod2\nLightGoldenrod3\nLightGoldenrod4\nLightYellow2\nLightYellow3\nLightYellow4\nyellow2\nyellow3\nyellow4\ngold2\ngold3\ngold4\ngoldenrod1\ngoldenrod2\ngoldenrod3\ngoldenrod4\nDarkGoldenrod1\nDarkGoldenrod2\nDarkGoldenrod3\nDarkGoldenrod4\nRosyBrown1\nRosyBrown2\nRosyBrown3\nRosyBrown4\nIndianRed1\nIndianRed2\nIndianRed3\nIndianRed4\nsienna1\nsienna2\nsienna3\nsienna4\nburlywood1\nburlywood2\nburlywood3\nburlywood4\nwheat1\nwheat2\nwheat3\nwheat4\ntan1\ntan2\ntan4\nchocolate1\nchocolate2\nchocolate3\nfirebrick1\nfirebrick2\nfirebrick3\nfirebrick4\nbrown1\nbrown2\nbrown3\nbrown4\nsalmon1\nsalmon2\nsalmon3\nsalmon4\nLightSalmon2\nLightSalmon3\nLightSalmon4\norange2\norange3\norange4\nDarkOrange1\nDarkOrange2\nDarkOrange3\nDarkOrange4\ncoral1\ncoral2\ncoral3\ncoral4\ntomato2\ntomato3\ntomato4\nOrangeRed2\nOrangeRed3\nOrangeRed4\nred2\nred3\nred4\nDeepPink2\nDeepPink3\nDeepPink4\nHotPink1\nHotPink2\nHotPink3\nHotPink4\npink1\npink2\npink3\npink4\nLightPink1\nLightPink2\nLightPink3\nLightPink4\nPaleVioletRed1\nPaleVioletRed2\nPaleVioletRed3\nPaleVioletRed4\nmaroon1\nmaroon2\nmaroon3\nmaroon4\nVioletRed1\nVioletRed2\nVioletRed3\nVioletRed4\nmagenta2\nmagenta3\nmagenta4\norchid1\norchid2\norchid3\norchid4\nplum1\nplum2\nplum3\nplum4\nMediumOrchid1\nMediumOrchid2\nMediumOrchid3\nMediumOrchid4\nDarkOrchid1\nDarkOrchid2\nDarkOrchid3\nDarkOrchid4\npurple1\npurple2\npurple3\npurple4\nMediumPurple1\nMediumPurple2\nMediumPurple3\nMediumPurple4\nthistle1\nthistle2\nthistle3\nthistle4\ngray1\ngray2\ngray3\ngray4\ngray5\ngray6\ngray7\ngray8\ngray9\ngray10\ngray11\ngray12\ngray13\ngray14\ngray15\ngray16\ngray17\ngray18\ngray19\ngray20\ngray21\ngray22\ngray23\ngray24\ngray25\ngray26\ngray27\ngray28\ngray29\ngray30\ngray31\ngray32\ngray33\ngray34\ngray35\ngray36\ngray37\ngray38\ngray39\ngray40\ngray42\ngray43\ngray44\ngray45\ngray46\ngray47\ngray48\ngray49\ngray50\ngray51\ngray52\ngray53\ngray54\ngray55\ngray56\ngray57\ngray58\ngray59\ngray60\ngray61\ngray62\ngray63\ngray64\ngray65\ngray66\ngray67\ngray68\ngray69\ngray70\ngray71\ngray72\ngray73\ngray74\ngray75\ngray76\ngray77\ngray78\ngray79\ngray80\ngray81\ngray82\ngray83\ngray84\ngray85\ngray86\ngray87\ngray88\ngray89\ngray90\ngray91\ngray92\ngray93\ngray94\ngray95\ngray97\ngray98\ngray99\nwhite')
    file.close()

def checkUpdate():
    url = 'http://clscrum.000webhostapp.com/downloads.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,features="html5lib")
    newestVersionInformationLoc = str(soup).index('<!-- Newest Version:V')
    newestVersion = str(soup)[newestVersionInformationLoc+len('<!-- Newest Version:V'):].split('-')[0]
    if newestVersion != '1.5':
        messagebox.showinfo('New version available','A new version of CL Scrum is available at clscrum.cf\nFor the optimal CL Scrum experience please upgrade.\n\nNew Version: '+newestVersion)
        return
    else:
        return

global startWindowScrolled
startWindowScrolled = 0

def settings(board):
    def settingsWindowKeyPressed(key):
        if key.char == '\x1b':
            settingsWindow.destroy()

    try:
        global settingsWindow
        for i in settingsWindow.winfo_children():
            i.destroy()
    except:
        global settingsWIndow
        settingsWindow = Tk()
        settingsWindow.iconbitmap(r'clScrumIcon.ico')
        settingsWindow.title('Settings')

    def checkNewLists():
        f = open(board[:-9]+'lists.txt').readlines()
        file = open(board[:-9]+'lists.txt','w')
        for line in f:
            if line != 'newList;0\n':
                file.write(line)
        file.close()
        settingsWindow.destroy()

    settingsWindow.bind('<Key>',settingsWindowKeyPressed)
    settingsWindow.config(bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n',''))
    settingsWindow.protocol("WM_DELETE_WINDOW",checkNewLists)
    settingsWindow.focus_force()

    #BACKGROUND COLOR:
    def setBgColor(color):
        f = open('boards/settings.txt').readlines()
        file = open('boards/settings.txt','w')
        for line in f:
            if line != '\n':
                line = line.replace('\n', '')
                line = line.split(':')
                if line[0] == 'background':
                    line[1] = color
                elif line[0] == 'textcolor':
                    line[1] = 'black'
                    if 'gray' in color:
                        try:
                            if int(color[4:]) < 40:
                                line[1] = 'white'
                        except ValueError:
                            pass
                    elif color in ['blue4', 'blue2', 'blue', 'dark slate gray', 'dark green', 'dark sleet blue', 'forest green', 'black', 'maroon', 'medium blue', 'midnight blue', 'navy', 'red4']:
                        line[1] = 'white'
                line = line[0]+':'+line[1] + '\n'
                file.write(line)
        file.close()
        updateScreen()
        settings(board)
        global colorSelectWindow
        colorSelectWindow.focus_force()

    #Set the maximum amount of cards
    def setMaxCards(entry):
        maxCards = entry.get()
        error = False
        try:
            maxCards = int(maxCards)
            if maxCards < 1:
                error = True
            elif maxCards > 30:
                error = True
        except:
            error = True

        if error:
            messagebox.showerror('ERROR','Please fill in a whole number in the range 1-30.')
            settingsWindow.focus_force()
            return

        f = open('boards/settings.txt').readlines()
        file = open('boards/settings.txt','w')
        for line in f:
            if line != '\n':
                line = line.replace('\n','')
                line = line.split(':')
                if line[0] == 'maxcards':
                    line[1] = maxCards
                file.write(line[0]+':'+str(line[1])+ '\n')
        file.close()
        updateScreen()
        settingsWindow.focus_force()

    def newList(listEntrys):
        if setLists(listsEntrys):
            f = open(board[:-9] + 'lists.txt').readlines()
            file = open(board[:-9] + 'lists.txt','w')
            f.append('newList;0\n')
            for line in f:
                file.write(line)
            file.close()
            settings(board)

    def setLists(listsEntrys):
        givenLists = []
        for entry in listsEntrys:
            if givenLists.count(entry.get()) != 0:
                messagebox.showerror('ERROR', 'No duplicate list names alowed.')
                settingsWindow.focus_force()
                return False
            elif entry.get().replace('\n','') == '':
                continue
            givenLists.append(entry.get())
        if 'newList' in givenLists:
            messagebox.showerror('ERROR','Give the new list a name first.')
            settingsWindow.focus_force()
            return False
        for listName in givenLists:
            if len(listName) > 21:
                messagebox.showerror('ERROR', 'List name '+listName[:21]+'...\nis too long.')
                settingsWindow.focus_force()
                return False
        f1 = open(board[:-9]+'lists.txt').readlines()
        f = open(board).readlines()
        if len(f1) > len(givenLists):
            file = open(board,'w')
            for line in f:
                line = line.split(';')
                if int(line[0]) >= len(givenLists):
                    line[0] = 0
                file.write(str(line[0])+';'+line[1]+';'+line[2])
        file = open(board[:-9]+'lists.txt','w')
        for lstName in givenLists:
            file.write(lstName.replace('\n','')+';0\n')
        file.close()
        settings(board)
        updateScreen()
        settingsWindow.focus_force()
        return True


    textcolor = 'black'
    if ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','') in ['black','grey22','blue']:
        textcolor = 'white'

    def colorScreen():
        global colorSelectWindow
        colorSelectWindow = Tk()
        colorSelectWindow.iconbitmap(r'clScrumIcon.ico')
        colorSelectWindow.title('Color Selection Window')

        colorButtons = []
        colors = open('boards/colors.txt').readlines()
        x = 0
        y = 0
        for color in colors:
            color = color.replace('\n', '')
            textcolor = 'black'
            if 'gray' in color:
                try:
                    if int(color[4:]) < 40:
                        textcolor = 'white'
                except ValueError:
                    pass
            elif color in ['blue4', 'blue2', 'blue', 'dark slate gray', 'dark green', 'dark sleet blue', 'forest green', 'black', 'maroon', 'medium blue', 'midnight blue', 'navy', 'red4']:
                textcolor = 'white'
            colorButtons.append(Button(master=colorSelectWindow,bg=color,fg=textcolor,width=10,text=color,border=0,command= lambda color=color: setBgColor(color)))
            colorButtons[x].grid(row=x-y*30,column=y)
            x += 1
            if x % 30 == 0:
                y += 1

    textcolor = 'black'
    if 'gray' in ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', ''):
        try:
            if int(((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')[4:]) < 40:
                textcolor = 'white'
        except ValueError:
            pass
    elif ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '') in ['blue4', 'blue2', 'blue', 'dark slate gray', 'dark green', 'dark sleet blue', 'forest green', 'black', 'maroon', 'medium blue', 'midnight blue', 'navy', 'red4']:
        textcolor = 'white'

    lbl = Label(master=settingsWindow,text='Backgroundcolor:',fg=textcolor,font=('Arial',20),bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','')).grid(row=0,columnspan=1000)
    changeColorBtn = Button(master=settingsWindow,text='Select color',bg='lightgrey',border=0,command=colorScreen)
    changeColorBtn.grid(row=1,column=0,columnspan=2)

    lbl2 = Label(master=settingsWindow, text='Max cards:', fg=textcolor, font=('Arial', 20),bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')).grid(row=2,columnspan=2)
    entry = Entry(master=settingsWindow,bg='lightgrey',border=0,width=5)
    entry.insert(0,((open('boards/settings.txt').readlines())[1].split(':'))[1].replace('\n', ''))
    entry.grid(row=3,column=0,columnspan=2)

    confirmButton = Button(master=settingsWindow,text='Ok',command=lambda entry=entry: setMaxCards(entry),border=0)
    confirmButton.grid(row=3,column=1)

    listsLabel = Label(master=settingsWindow, text='Lists:', fg=textcolor, font=('Arial', 20),bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')).grid(row=4,columnspan=1000)

    listsEntrys = []
    lists = open(board[:-9]+'lists.txt').readlines()
    x = 0
    for line in lists:
        lists[x] = line.split(';')[0]
        x += 1
    x = 0
    for lst in lists:
        listsEntrys.append(Entry(master=settingsWindow,font=('arial',15),bd=1,bg='lightgrey'))
        listsEntrys[x].grid(row=x+5,columnspan=2)
        listsEntrys[x].insert(0,lst)
        x += 1
    listsConfirmButton = Button(master=settingsWindow,text='Ok',command=lambda listEntrys=listsEntrys: setLists(listsEntrys),border=0)
    listsConfirmButton.grid(row=x+5,column=0)
    newListButton = Button(master=settingsWindow,text='New List',command=lambda listEntrys=listsEntrys: newList(listsEntrys),border=0)
    newListButton.grid(row=x+5,column=1)

    for btn in [confirmButton,listsConfirmButton,newListButton]:
        btn.bind('<Enter>', lambda event,btn=btn: btn.config(bg='white'))
        btn.bind('<Leave>', lambda event, btn=btn: btn.config(bg='lightgrey'))

def openAgenda():
    def agendaWindowKeyPressed(key):
        if key.char == 'n' or key.char == 'N':
            global newActivity
            newActivity()
        elif key.char == '\x1b':
            agendaWindow.destroy()
    # Destroy any possible already existing agendaWindows
    global date, agendaWindow
    date = datetime.now()
    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','')

    try:
        agendaWindow.destroy()
    except:
        agendaWindow = Tk()
        agendaWindow.iconbitmap(r'clScrumIcon.ico')
        agendaWindow.title('Calendar')
        agendaWindow.config(bg=bgColor)
        agendaWindow.bind('<Key>',agendaWindowKeyPressed)
        agendaWindow.focus_force()

    updateAgenda()

def updateAgenda():
    # Import the needed variables/ windows
    global date, agendaWindow
    # Script for new activty
    global newActivity
    def newActivity():
        def newActivityKeyPressed(key):
            if key.char == '\r':
                addNewActivity()
            elif key.char == '\x1b':
                newActivityWindow.destroy()
                updateAgenda()
        def addNewActivity():
            global newActivityTitleEntry, newActivityDayEntry, newActivityMonthEntry, newActivityYearEntry
            if newActivityTitleEntry.get() == '':
                return

            activityTitle = newActivityTitleEntry.get()
            activityDay = newActivityDayEntry.get()
            activityMonth = newActivityMonthEntry.get()
            activityYear = newActivityYearEntry.get()
            if activityDay == '':
                activityDay = datetime.now().day
            if activityMonth == '':
                activityMonth = datetime.now().month
            if activityYear == '':
                activityYear = datetime.now().year

            f = open(board[:-9] + 'agenda.txt').readlines()
            file = open(board[:-9] + 'agenda.txt', 'w')
            for line in f:
                file.write(line)
            file.write(str(int(activityDay)) + ';' + str(int(activityMonth)) + ';' + str((activityYear)) + ';' + activityTitle + '\n')
            file.close()
            newActivityWindow.destroy()
            updateAgenda()

        bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','')
        textColor = ((open('boards/settings.txt').readlines())[2].split(':'))[1].replace('\n','')

        newActivityWindow = Tk()
        newActivityWindow.iconbitmap(r'clScrumIcon.ico')
        newActivityWindow.title('New activity')
        newActivityWindow.config(bg=bgColor)
        newActivityWindow.bind('<Key>',newActivityKeyPressed)

        newActivityLabel = Label(master=newActivityWindow, text='New activity',bg=bgColor,fg=textColor)
        newActivityLabel.grid(columnspan=3)

        global newActivityTitleEntry, newActivityDayEntry, newActivityMonthEntry, newActivityYearEntry
        newActivityTitleEntry = Entry(master=newActivityWindow, width=15,bg='lightgrey',fg='black',border=0)
        newActivityTitleEntry.grid(row=1, column=0, columnspan=3)
        newActivityTitleEntry.focus_force()

        newActivityDayEntry = Entry(master=newActivityWindow, width=4,bg='lightgrey',fg='black',border=0)
        newActivityDayEntry.grid(row=2, column=0)

        newActivityMonthEntry = Entry(master=newActivityWindow, width=4,bg='lightgrey',fg='black',border=0)
        newActivityMonthEntry.grid(row=2, column=1)

        newActivityYearEntry = Entry(master=newActivityWindow, width=4,bg='lightgrey',fg='black',border=0)
        newActivityYearEntry.grid(row=2, column=2)

        newActivityButton = Button(text='Done', master=newActivityWindow, command=addNewActivity,border=0)
        newActivityButton.grid(row=2, column=3)


    def viewDay(day, vandaagInfo):
        def viewDayKeyPressed(key):
            if key.char == '\x1b':
                viewDayWindow.destroy()
        def deleteActivity(activity):
            f = open(board[:-9] + 'agenda.txt').readlines()
            x = 0
            for line in f:
                line = line.split(';')
                if line[0] == '\n':
                    pass
                elif line[3].replace('\n','') == activity:
                    f[x] = ''
                    break
                x += 1
            f.remove('')
            file = open(board[:-9] + 'agenda.txt','w')
            for line in f:
                file.write(line)
            file.close()
            viewDayWindow.destroy()
            updateAgenda()

        global viewDayWindow
        try:
            for i in viewDayWindow.winfo_children():
                i.destroy()
        except NameError:
            viewDayWindow = Tk()
            viewDayWindow.iconbitmap(r'clScrumIcon.ico')
        viewDayWindow.title(day)
        viewDayWindow.focus_force()
        viewDayWindow.config(bg=bgColor)
        viewDayWindow.bind('<Key>',viewDayKeyPressed)

        dateLabel = Label(master=viewDayWindow,text=day,font=('arial',20),bg=bgColor,fg=textColor,width=20)
        dateLabel.grid(row=0,column=0,columnspan=2)

        activityLabels = []
        activityButtons = []
        x = 0
        vandaagInfo = vandaagInfo.split('\n')
        vandaagInfo.remove('')
        for activity in vandaagInfo:
            activityLabels.append(Label(master=viewDayWindow,text=activity,font=('arial',13),bg=bgColor,fg=textColor))
            activityLabels[x].config(anchor='nw',justify='left',width=30)
            activityLabels[x].grid(row=x+1,column=1)

            activityButtons.append(Button(master=viewDayWindow,text='X',command= lambda activity=activity: deleteActivity(activity),border=0))
            activityButtons[x].grid(row=x+1,column=0)
            x += 1


    # Function that sets the date information back to the current date
    def ftoday():
        global date
        date = datetime.now()
        updateAgenda()

    def nextWeek():
        global date
        date += timedelta(days=7)
        updateAgenda()

    def pastWeek():
        global date
        date -= timedelta(days=7)
        updateAgenda()

    # Clear agenda window
    try:
        for i in agendaWindow.winfo_children():
            i.destroy()
    except:
        pass

    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','')
    textColor = ((open('boards/settings.txt').readlines())[0].split(':'))[2].replace('\n', '')

    agendaWindow.config(bg=bgColor)

    dagenLabels = []
    x = 0
    for dag in ['Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo']:
        dagenLabels.append(Label(master=agendaWindow, text=dag,bg=bgColor,fg=textColor))
        dagenLabels[x].grid(row=1, column=x)
        x += 1
    #year label
    yearLabel = Label(master=agendaWindow,text=str(date.year),bg=bgColor,fg=textColor,font=('arial',20))
    yearLabel.grid(row=0,column=2,columnspan=3)

    days = []
    # Set the dates
    monday = datetime(date.year, date.month, date.day)+timedelta(days=-(datetime.now().weekday()))

    for i in range(0,7):
        days.append((str(monday+timedelta(days=i))+'\n'))

    # get dagInfo
    dagInfo = ['', '', '', '', '', '', '']
    try:
        f = open(board[:-9] + 'agenda.txt').readlines()
    except:
        f = open(board[:-9] + 'agenda.txt','w')
        f.close()
        f = open(board[:-9] + 'agenda.txt').readlines()
    for line in f:
        if line[0] == '\n' or line[0] == '#':
            continue
        line = line.split(';')
        activityDate = datetime(int(line[2]),int(line[1]),int(line[0]))

        for i in range(0,7):
            if str(activityDate) == (days[i])[:-1]:
                line[3] = line[3].replace('\n','')
                dagInfo[i] = dagInfo[i] + '\n' + line[3]

    x = 0
    for day in dagInfo:
        day = day.split('\n')
        day = sorted(day)
        day.remove('')
        dagInfo[x] = ''
        for item in day:
            dagInfo[x] = dagInfo[x] + '\n' + item
        x += 1

    dayBgColor = 'lightgreen'
    if bgColor == 'lightgreen':
        dayBgColor = 'green2'

    # Build up the window
    dayButtons = []
    for i in range(0,7):
        dayButtons.append(Button(master=agendaWindow,text=((str(days[i])[8:])[:2]+' - '+(str(days[i])[5:])[:2]+str(dagInfo[i])),command= lambda day=((str(days[i])[8:])[:2]+' - '+(str(days[i])[5:])[:2]), vandaagInfo=dagInfo[i]:viewDay(day,vandaagInfo)))
        if str(days[i])[:10] == str(datetime.now())[:10]:
            dayButtons[i].config(width=20,height=25,font=("arial",10),border=0,anchor='nw',justify='left',background=dayBgColor)
            dayButtons[i].bind('<Enter>', lambda event, btn=dayButtons[i]: btn.config(bg='white', fg=bgColor))
            dayButtons[i].bind('<Leave>', lambda event, btn=dayButtons[i]: btn.config(bg=dayBgColor, fg=textColor))
        else:
            dayButtons[i].config(width=20,height=25,font=("arial",10),border=0,anchor='nw',justify='left',bg=bgColor,fg=textColor)
            dayButtons[i].bind('<Enter>', lambda event, btn=dayButtons[i]: btn.config(bg='white', fg=bgColor))
            dayButtons[i].bind('<Leave>', lambda event, btn=dayButtons[i]: btn.config(bg=bgColor, fg=textColor))
        dayButtons[i].grid(row=2,column=i)

    # Next week button
    nextWeekButton = Button(master=agendaWindow,text='Next week',command=nextWeek,border=0)
    nextWeekButton.grid(row=3,column=6)

    # Past week button
    pastWeekButton = Button(master=agendaWindow,text='Past week', command=pastWeek,border=0)
    pastWeekButton.grid(row=3, column=0)

    # Today week button
    todayButton = Button(master=agendaWindow,text='Today',command=ftoday,border=0)
    todayButton.grid(row=3,column=3)

    # New activity Button
    newActivityButton = Button(master=agendaWindow,text='New activity',command=newActivity,border=0)
    newActivityButton.grid(row=0,column=0)


def deleteBoardWindow():
    def deleteBoard(brd):
        f = open('boards/BOARDS.txt').readlines()
        # delete from list
        f.remove((str(brd) + '\n'))
        # delete from computer
        shutil.rmtree('boards/' + str(brd))
        file = open('boards/BOARDS.txt', 'w')
        for line in f:
            file.write(line)
        file.close()
        root.destroy()
        start()

    global root
    try:
        for i in root.winfo_children():
            i.destroy()
    except:
        pass
    root.title('delete Board')

    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')
    textColor = ((open('boards/settings.txt').readlines())[2].split(':'))[1].replace('\n','')
    Label1 = Label(text='Delete board:', font=("Arial", 20),background=bgColor,fg=textColor)
    Label1.grid(row=0,column=1,columnspan=1000)

    buttons = []

    boards = open('boards/BOARDS.txt').readlines()
    x = 0
    for brd in boards:
        brd = brd[:len(brd) - 1]
        buttons.append(Button(text=brd, width=20, height=2, font=("Arial", 20), command=lambda brd=brd: deleteBoard(brd),background=bgColor,fg=textColor,border=0))
        buttons[x].bind('<Enter>', lambda event, btn=buttons[x]: btn.config(bg='white', fg='black'))
        buttons[x].bind('<Leave>', lambda event,btn=buttons[x]: btn.config(bg=bgColor, fg=textColor))
        buttons[x].grid(row=x + 1,columnspan=1000)
        x += 1

    def back():
        start()
    backBtn = Button(text='<', font=('arial', 12), background=bgColor, fg=textColor, anchor='nw', justify='left',border=0, command=back)
    backBtn.bind('<Enter>', lambda event: backBtn.config(bg='white', fg='black'))
    backBtn.bind('<Leave>', lambda event: backBtn.config(bg=bgColor, fg=textColor))
    backBtn.grid(row=0,column=0)


def newBoard():
    def createNewBoard(Entry1):
        if len(Entry1.get()) > 50:
            messagebox.showerror('ERROR','Board name to long.')
            return
        global board
        board = 'boards/' + str(Entry1.get()) + '/board.txt'
        makedirs('boards/' + str(Entry1.get()))
        x = open(board, 'w')
        x.close()
        f = open('boards/BOARDS.txt').readlines()
        f.append(str(Entry1.get()) + '\n')
        file = open('boards/BOARDS.txt', 'w')
        for line in f:
            file.write(line)
        file.close()
        boardSelect(str(Entry1.get()))

    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')
    textColor = ((open('boards/settings.txt').readlines())[2].split(':'))[1].replace('\n','')
    print(textColor)

    global root
    for i in root.winfo_children():
        i.destroy()
    root.title('New Board')
    root.config(bg=bgColor)

    Label1 = Label(text="New board",bg=bgColor,fg=textColor,font=('arial',20))
    Label1.grid(row=0, column=1)

    Entry1 = Entry(font=('arial',20),bg=bgColor,fg=textColor)
    Entry1.grid(row=1, column=0,columnspan=2)

    Button1 = Button(text='Done',font=('arial',15), command=lambda Entry1=Entry1: createNewBoard(Entry1),border=0)
    Button1.grid(row=1, column=2)

    def back():
        start()

    backBtn = Button(text='<', font=('arial', 12), background=bgColor, fg=textColor, anchor='nw', justify='left',border=0, command=back)
    backBtn.bind('<Enter>', lambda event: backBtn.config(bg='white', fg='black'))
    backBtn.bind('<Leave>', lambda event: backBtn.config(bg=bgColor, fg=textColor))
    backBtn.grid(row=0, column=0)


def boardSelect(brd):
    global board
    board = 'boards/' + brd + '/board.txt'
    global root
    for i in root.winfo_children():
        i.destroy()

    try:
        f = open('boards/'+brd+'/todoScrolled.txt').readlines()
        messagebox.showwarning('WARNING','You need to run the "Update.exe" first.\n\nIt will update all the files so that they are compatible with this version of CL Scrum')
        root.destroy()
        return
    except:
        pass

    try:
        f = open('boards/'+brd+'/agenda.txt').readlines()
    except:
        f = open('boards/'+brd+'/agenda.txt','w')

    try:
        f = open(board).readlines()
    except:
        f = open(board,'w')

    try:
        f = open(board[:-9]+'lists.txt').readlines()
    except:
        f = open(board[:-9]+'lists.txt','w')
        f.write('list1;0\nlist2;0\nlist3;0\n')
        f.close()
    f = open(board[:-9] + 'lists.txt').readlines()
    file = open(board[:-9] + 'lists.txt', 'w')
    for line in f:
        line = line.split(';')
        file.write(line[0]+';'+'0\n')
    file.close()

    updateScreen()

def startWindowKeyPressed(key):
    pass

def start():
    global root
    try:
        for i in root.winfo_children():
            i.destroy()
    except:
        root = Tk()
        root.iconbitmap(r'clScrumIcon.ico')
    root.bind('<Key>', startWindowKeyPressed)
    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')
    root.config(background=bgColor)
    root.title('Select board')
    textcolor = ((open('boards/settings.txt').readlines())[2].split(':'))[1].replace('\n','')

    Label1 = Label(text="Available boards", font=("Arial", 20),fg=textcolor,bg=bgColor)
    Label1.grid(row=0, column=0, columnspan=2)

    def startWindowScroll(direction):
        global startWindowScrolled
        startWindowScrolled += direction
        start()

    boards = open('boards/BOARDS.txt').readlines()
    buttons = []
    x = 0
    count = 0
    for brd in boards:
        if count == startWindowScrolled and startWindowScrolled == 0:
            buttons.append(Button(text=' ', font=('arial', 10), bg=bgColor,border=0))
            buttons[x].grid(row=x + 1, column=0, columnspan=2)
            x += 1
        if count >= startWindowScrolled:
            brd = str(brd)
            brd = brd[:len(brd) - 1]
            buttons.append(Button(text=brd, width=20, height=2, font=("Arial", 20), bg='lightgrey',border=0,command=lambda brd=brd: boardSelect(brd)))
            buttons[x].grid(row=x + 1, column=0, columnspan=2)
            buttons[x].bind('<Enter>', lambda event, btn=buttons[x]: btn.config(bg='white'))
            buttons[x].bind('<Leave>', lambda event, btn=buttons[x]: btn.config(bg='lightgrey'))
            x += 1
        elif count == 0:
            buttons.append(Button(text='/\\', width=40, height=1, font=("Arial", 10), bg='grey',border=0,command= lambda : startWindowScroll(-1)))
            buttons[x].grid(row=x+1,column=0,columnspan=2)
            buttons[x].bind('<Enter>', lambda event, btn=buttons[x]: btn.config(bg='white'))
            buttons[x].bind('<Leave>', lambda event, btn=buttons[x]: btn.config(bg='grey'))
            x += 1
        if (count == 4 and startWindowScrolled == 0 and len(boards) > 5) or (x == 6 and startWindowScrolled >= 1 and count != x-1):
            buttons.append(Button(text='\\/', width=40, height=1, font=("Arial", 10), bg='grey',border=0,command= lambda : startWindowScroll(1)))
            buttons[x].grid(row=x+1,column=0,columnspan=2)
            buttons[x].bind('<Enter>', lambda event, btn=buttons[x]: btn.config(bg='white'))
            buttons[x].bind('<Leave>', lambda event, btn=buttons[x]: btn.config(bg='grey'))
            x += 1
            break
        if x == 6 and not((count == 4 and startWindowScrolled == 0) or (x == 6 and startWindowScrolled >= 1 and count != x-1)):
            buttons.append(Button(text=' ', font=('arial', 10), bg=bgColor,border=0))
            buttons[x].grid(row=x + 1, column=0, columnspan=2)
            x += 1
        count += 1

    buttons.append(Button(text='New board', width=18, height=1, font=("Arial", 10), bg='lightgrey',command=newBoard,border=0))
    buttons[x].grid(row=x + 1, column=0)
    buttons[x].bind('<Enter>', lambda event, btn=buttons[x]: btn.config(bg='white'))
    buttons[x].bind('<Leave>', lambda event, btn=buttons[x]: btn.config(bg='lightgrey'))

    buttons.append(Button(text='Delete board', width=21, height=1, font=("Arial", 10), bg='lightgrey',border=0,command=deleteBoardWindow))
    buttons[x + 1].grid(row=x + 1, column=1)
    buttons[x+1].bind('<Enter>', lambda event, btn=buttons[x+1]: btn.config(bg='white'))
    buttons[x+1].bind('<Leave>', lambda event, btn=buttons[x+1]: btn.config(bg='lightgrey'))

    versionLabel = Label(text='(CL Scrum V 1.5) ©CasLinders',width=40,font=('arial',10), fg=textcolor, bg=bgColor,anchor='nw',justify='left').grid(row=x+2,column=0,columnspan=2)
    checkUpdate()

def updateText(textBox,task,lst,entry):
    f = open(board).readlines()
    tasks = []
    for line in f:
        tasks.append(line.split(';')[1])
    if entry.get() in tasks and entry.get() != task.fullName.split(';')[1]:
        messagebox.showerror('Warning','Task already exists')
        return
    f = open(board).readlines()
    file = open(board,'w')
    for line in f:
        if line.split(';')[1] == task.fullName.split(';')[1]:
            line = line.split(';')
            file.write(line[0]+';'+entry.get()+';'+line[2])
            os.remove(board[:-9] + 'tasks/' + task.fullName.split(';')[1] + ';' + (task.fullName.split(';')[2].replace('\n', '')).replace(':', '-')+'.txt')
        else:
            file.write(line)
    file.close()
    text = textBox.get(1.0, END)
    f = open(board[:-9] + 'tasks/' + entry.get() + ';' + (task.fullName.split(';')[2].replace('\n', '')).replace(':', '-') + '.txt', 'w')
    text = text.split('\n')
    for line in text:
        if line != '':
            f.write(line + '\n')
    task.fullName = task.fullName.split(';')[0] + ';' + entry.get() + ';' + task.fullName.split(';')[2]
    f.close()
    return

def viewTask(task,lst):
    def close(textBox, textTask, lst, entry):
        updateText(textBox,task,lst,entry)
        viewTaskWindow.destroy()
        updateScreen()
    def viewTaskWindowKeyPressed(key):
        if key.char == '\x1b':
            updateText(textBox,task,lst,entry)
            viewTaskWindow.destroy()
            updateScreen()

    #Get the correct task and task
    textTask = task.fullName.split(';')
    global viewTaskWindow
    try:
        for i in viewTaskWindow.winfo_children():
            i.destroy()
    except:
        viewTaskWindow = Tk()

    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')
    textColor = ((open('boards/settings.txt').readlines())[2].split(':'))[1].replace('\n','')

    viewTaskWindow.title(lst.name.upper()+': '+textTask[1])
    viewTaskWindow.iconbitmap(r'clScrumIcon.ico')
    viewTaskWindow.bind('<Key>',viewTaskWindowKeyPressed)
    viewTaskWindow.focus_force()
    viewTaskWindow.config(bg=bgColor)

    lbl1 = Label(master=viewTaskWindow,text=lst.name+': ',font=('arial',15),background=bgColor,fg=textColor)
    lbl1.grid(column=0)
    entry = Entry(master=viewTaskWindow,font=('arial',15),background=bgColor,fg=textColor,border=0)
    entry.insert(0,textTask[1])
    entry.grid(row=0,column=1)
    f = open(board[:-9]+'tasks/'+textTask[1] + ';' + (textTask[2].replace('\n','')).replace(':','-') +'.txt','r').readlines()
    x = ''
    for line in f:
        x = x + line

    textBox = Text(master=viewTaskWindow,width=40,height=10,background=bgColor,fg=textColor,border=0,font=('arial',12))
    textBox.grid(columnspan=3)
    textBox.insert(END,x)

    viewTaskWindow.protocol("WM_DELETE_WINDOW", lambda textBox=textBox, entry=entry, textTask=textTask, task=task, lst=lst: close(textBox, textTask, lst, entry))

    deleteButton = Button(master=viewTaskWindow,border=0,bg=bgColor,fg=textColor, text='Delete',command= lambda textTask=textTask,lst=lst: fDelete(textTask,lst))
    deleteButton.grid(column=1,row=2)

    moveButton = Button(master=viewTaskWindow, border=0,bg=bgColor,fg=textColor, text='Move',command= lambda lst=lst,task=task,textBox=textBox,entry=entry: moveTask(task,lst,textBox,entry))
    moveButton.grid(column=2,row=2)

    for btn in [deleteButton,moveButton]:
        btn.bind('<Enter>', lambda event, btn=btn: btn.config(bg='white',fg='black'))
        btn.bind('<Leave>', lambda event, btn=btn: btn.config(bg=bgColor, fg=textColor))

def updateScreen():
    global root
    try:
        for i in root.winfo_children():
            i.destroy()
    except:
        pass

    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','')
    textColor = ((open('boards/settings.txt').readlines())[2].split(':'))[1].replace('\n','')

    def close():
        f = open(board[:-9]+'lists.txt').readlines()
        file = open(board[:-9] + 'lists.txt','w')
        for line in f:
            if line.split(';')[0] != 'newList':
                file.write(line)
        file.close()
        exit()

    # create screen:
    root.title(board[:-10][7:])
    root.config(background=bgColor)
    root.bind('<Key>',rootKeyPressed)
    root.focus_force()
    root.protocol("WM_DELETE_WINDOW", close)

    def back():
        start()
    backBtn = Button(text='<',font=('arial',12),background=bgColor,fg=textColor,anchor='nw',justify='left',border=0,command=back)
    greyLBL = Label(text=' ',width=35,bg=bgColor).grid(row=0,column=1) # This label is to push the back btn to the left
    backBtn.bind('<Enter>', lambda event: backBtn.config(bg='white',fg='black'))
    backBtn.bind('<Leave>', lambda event: backBtn.config(bg=bgColor,fg=textColor))
    #backBtn.grid(row=0,column=0,columnspan=1)

    class Task():
        def __init__(self, task):
            self.fullName = task
            task = task.split(';')
            self.listNum = task[0]
            self.name = task[1]
            self.identifier = task[2]

    #List and task class
    class List():
        def __init__(self,name,scrolled):
            self.name = name
            self.index = len(lists)
            items = []
            f = open(board).readlines()
            for line in f:
                if int(line.split(';')[0]) == self.index:
                    items.append(Task(line))
            self.items = items
            self.scrolled = scrolled

        def scroll(self,direction):
            f = open(board[:-9]+'lists.txt').readlines()
            file = open(board[:-9]+'lists.txt','w')
            for line in f:
                if line.split(';')[0] == self.name:
                    line = line.split(';')
                    line[1] = str(int(line[1].replace('\n','')) + direction)
                    file.write(line[0]+';'+line[1]+'\n')
                else:
                    file.write(line)
            file.close()
            updateScreen()

    # the lists
    global delete,lists
    delete = []
    lists = []

    try:
        scrolled = 0
        listsF = open(board[:-9] + 'lists.txt').readlines()
        for i in range(0, len(listsF)):
            listsF[i] = listsF[i].replace('\n', '')
            scrolled = int(listsF[i].split(';')[1].replace('\n', ''))
            lists.append(List(listsF[i].split(';')[0],scrolled))

    except IndexError:
        listsF = open(board[:-9] + 'lists.txt', 'w')
        listsF.close()
        listsF = open(board[:-9] + 'lists.txt').readlines()
        for i in range(0, len(listsF)):
            listsF[i] = listsF[i].replace('\n', '')
            scrolled = int(listsF[i].split(';')[1].replace('\n', ''))
            lists.append(List(listsF[i].split(';')[0],scrolled))

    # other variables
    space = 30  # width for the buttons and labels

    # labels to screen:
    labels = []
    x = 0

    for listType in lists:
        labels.append(Label(text=listType.name, font=('arial', 15),fg=textColor))
        labels[x].config(background=bgColor,highlightbackground=bgColor)
        labels[x].grid(row=0, column=x)
        x += 1

    # Add tasks to screen
    cards = []
    x = 0

    height = 0
    count = 0
    maxCards = int(open('boards/settings.txt').readlines()[1].split(':')[1].replace('\n',''))
    listIndexNum = 0

    for currentList in lists:
        y = 1
        height = 0
        count = 0
        for fullTask in currentList.items:
            task = fullTask.fullName.split(';')[1].replace('\n','')
            if count >= currentList.scrolled:
                if currentList.scrolled != 0 and count == currentList.scrolled:
                    cards.append(Button(text='/\\', width=space, height=1, border=0,font=('arial', 12), pady=0, background='grey',command=lambda lst=currentList, direction=-1: lst.scroll(direction)))
                    cards[x].bind('<Enter>', lambda event,btn=cards[x]: btn.config(bg='white'))
                    cards[x].bind('<Leave>', lambda event, btn=cards[x]: btn.config(bg='grey'))
                    cards[x].grid(row=y, column=currentList.index)
                    x += 1
                elif count == 0:
                    nothingNess = Label(text=' ',bg=bgColor,height=1,font=('arial',16)).grid(row=y,column=currentList.index)
                y += 1
                for i in range(1,round(len(task)/30)):
                    texttask = task[:i*30] + '\n' + task[30:]
                else:
                    texttask = task
                cards.append(Button(anchor='w',justify=LEFT, text=texttask, border=0,width=space, height=2+texttask.count('\n'), font=('arial', 12), pady=0,command=lambda lst=currentList, task=fullTask: viewTask(task,lst)))
                cards[x].config(background='lightgrey',highlightbackground='lightgrey')
                cards[x].bind('<Enter>', lambda event, btn=cards[x]: btn.config(bg='white'))
                cards[x].bind('<Leave>', lambda event, btn=cards[x]: btn.config(bg='lightgrey'))
                cards[x].grid(row=y, column=currentList.index)
                x += 1
                y += 1
                height += 1
            if height == maxCards and count != len(currentList.items)-1:
                cards.append(Button(text='\/',border=0,width=space,height=1,font=('arial',12),pady=0,background='grey',command= lambda lst=currentList,direction=1: lst.scroll(direction)))
                cards[x].bind('<Enter>', lambda event, btn=cards[x]: btn.config(bg='white'))
                cards[x].bind('<Leave>', lambda event, btn=cards[x]: btn.config(bg='grey'))
                cards[x].grid(row=y,column=currentList.index)
                x += 1
                break
            elif height == maxCards and count == len(currentList.items)-1:
                nothingNess = Label(text=' ', bg=bgColor, height=1, font=('arial', 16)).grid(row=y, column=currentList.index)
            count += 1
        listIndexNum += 1


    # some white space
    whiteLabels = []
    for x in range(0,len(lists)):
        whiteLabels.append(Label(text=' '))
        whiteLabels[x].config(background=bgColor,highlightbackground=bgColor,width=31,font=('arial',10))
        whiteLabels[x].grid(row=999,column=x)

    # Ui Buttons
    newButton = Button(text='New task', command=newTask,border=0)
    newButton.grid(row=1000,column=0)

    agendaButton = Button(text='Calendar',border=0, command=openAgenda)
    agendaButton.grid(row=1000,column=1)

    settingsButton = Button(text='Settings',border=0,command= lambda board=board: settings(board))
    settingsButton.grid(row=1000,column=2)

    for btn in [newButton,agendaButton,settingsButton]:
        btn.bind('<Enter>', lambda event,btn=btn: btn.config(bg='lightgreen'))
        btn.bind('<Leave>', lambda event, btn=btn: btn.config(bg='lightgrey'))




def moveTask(task,lst,textBox,entry):
    updateText(textBox,task,lst,entry)
    f = open(board).readlines()

    x = -1
    for line in f:
        global lists
        x += 1
        if line[0] == '#':
            continue
        line = line.split(';')
        line[0] = int(line[0])
        if line[1] == task.fullName.split(';')[1]:
            if line[0] >= len(lists)-1:
                line[0] = -1
            line[0] += 1
            f[x] = str(line[0]) + ';' + line[1] + ';' + line[2]
            file = open(board, 'w')
            for line in f:
                file.write(line)
            file.close()
            break
    updateScreen()
    x = 0
    for xlst in lists:
        if xlst.name == lst.name:
            break
        x += 1
    if x >= len(lists):
        x = 0
    lst = lists[x]
    viewTask(task,lst)


def fDelete(textTask,lst):
    f = open(board).readlines()
    for line in f:
        if line == '\n':
            continue
        linex = line.split(';')
        if linex[1] == textTask[1]:
            f.remove(line)
            lst.scroll(-1)
            os.remove(board[:-9] + 'tasks/' + textTask[1] + ';' + (str(textTask[2]).replace('\n','')).replace(':','-') +'.txt')
            agendaF = open(board[:-9]+'agenda.txt').readlines()
            for line1 in agendaF:
                if line1 == '\n':
                    continue
                line1x = line1.split(';')
                if line1x[3] == textTask[1]:
                    agendaF.remove(line1)
                    break
            agendaFile = open(board[:-9]+'agenda.txt','w')
            for line1 in agendaF:
                if line1 != '\n':
                    agendaFile.write(line1)

            break
    file = open(board,'w')
    for line in f:
        if line != '\n':
            file.write(line)
    file.close()
    #Zorg dat scroll 1 omlaag gaat (indien nodig)
    updateScreen()
    global viewTaskWindow, agendaWindow
    try:
        for i in agendaWindow.winfo_children():
            i.destroy
        updateAgenda()
    except:
        pass
    viewTaskWindow.destroy()

def rootKeyPressed(key):
    if key.char == 'n' or key.char == 'N':
        newTask()
    elif key.char == 'c' or key.char == 'C':
        openAgenda()
    elif key.char == 's' or key.char == 'S':
        global board
        settings(board)
    elif key.char == 'B' or key.char == 'b':
        start()

def newTask():
    def newTaskKeyPressed(key):
        if key.char == '\r':
            done(entry, popUpWindow,dayEntry,monthEntry,yearEntry)
        elif key.char == '\x1b':
            popUpWindow.destroy()
    def done(entry, popUpWindow,dayEntry,monthEntry,yearEntry):
        timeStamp = datetime.now()
        task = entry.get()
        f = open(board).readlines()
        for line in f:
            line = line.split(';')
            if task == line[1]:
                def close():
                    extraWindow.destroy()
                extraWindow = Tk()
                extraWindow.title('ERROR')
                label = Label(master=extraWindow,text='That task already exists')
                label.grid()
                button = Button(master=extraWindow,text='Ok',command=close)
                button.grid()
                return
        if ';' in task or '?' in task or ':' in task or '/' in task or '\\' in task or '*' in task or '<' in task or '>' in task or '|' in task:
            extraWindow = Tk()
            extraWindow.title('ERROR')
            label = Label(master=extraWindow, text='Task name can not include a ; : ? * / \\ < > or | ', font=('Arial', 13))
            label.grid()
        elif task.lower() == 'cas is gay':
            extraWindow = Tk()
            extraWindow.title('8===>')
            label = Label(master=extraWindow,text='JE BENT ZELF GAY!',font=('Arial',30))
            label.grid()
        elif len(task) > 100:
            messagebox.showerror('ERROR','Task name too long.\nMax 100 characters.')
            popUpWindow.focus_force()
            return
        elif task != '':
            f = open(board).readlines()
            f.append(('0' + ';' + task + ';' + str(timeStamp)+'\n'))
            file = open(board, 'w')
            for line in f:
                file.write(line)
            file.close()
            taskDay = dayEntry.get()
            taskMonth = monthEntry.get()
            taskYear = yearEntry.get()
            if taskDay != '' or taskMonth != '' or taskYear != '':
                try:
                    f = open(board[:-9] + 'agenda.txt').readlines()
                except:
                    f = open(board[:-9] + 'agenda.txt','w')
                    f.close()
                    f = open(board[:-9] + 'agenda.txt').readlines()
                file = open(board[:-9] + 'agenda.txt','w')
                for line in f:
                    file.write(line)
                if taskDay == '':
                    taskDay = datetime.now().day
                if taskMonth == '':
                    taskMonth = datetime.now().month
                if taskYear == '':
                    taskYear = datetime.now().year

                try:
                    datetime(int(taskYear),int(taskMonth),int(taskDay))
                    file.write(str(taskDay) + ';' + str(taskMonth) + ';' + str(taskYear) + ';' + task + ';' + str(timeStamp) + '\n')
                    file.close()
                except:
                    def done():
                        extraWindow.destroy()
                    extraWindow = Tk()
                    extraWindow.title('ERROR')

                    label = Label(master=extraWindow,text='Date fromat should be DD MM YYYY, your entered date is not possible\n The task is added, how ever not in the calendar...').grid()
                    button = Button(master=extraWindow,text='OK',command=done).grid()
                    updateScreen()

            try:
                f = open(board[:-9]+'tasks/' + task + ';' + str(timeStamp).replace(':','-') + '.txt','w+')
            except:
                makedirs(board[:-9] + 'tasks/')
                f = open(board[:-9] + 'tasks/' + task + ';' + str(timeStamp).replace(':','-') + '.txt', 'w+')

            global agendaWindow
            try:
                for i in agendaWindow.winfo_children():
                    i.destroy
                updateAgenda()
            except:
                pass
            popUpWindow.destroy()
            updateScreen()
            return ''

    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','')
    textColor = ((open('boards/settings.txt').readlines())[2].split(':'))[1].replace('\n','')

    popUpWindow = Tk()
    popUpWindow.config(bg=bgColor)
    popUpWindow.iconbitmap(r'clScrumIcon.ico')

    lbl = Label(master=popUpWindow, text='New Task:',bg=bgColor,fg=textColor)
    lbl.grid(columnspan=10)
    entry = Entry(master=popUpWindow,bg='lightgrey',border=0)
    entry.focus_force()
    entry.grid(row=1,columnspan=10)

    lbl2 = Label(master=popUpWindow,text='Include in calendar:',bg=bgColor,fg=textColor)
    lbl2.grid(row=2,column=0,columnspan=4)

    dayEntry = Entry(master=popUpWindow,width=4,bg='lightgrey',border=0)
    dayEntry.grid(row=3,column=0)
    monthEntry = Entry(master=popUpWindow,width=4,bg='lightgrey',border=0)
    monthEntry.grid(row=3,column=1)
    yearEntry = Entry(master=popUpWindow,width=6,bg='lightgrey',border=0)
    yearEntry.grid(row=3,column=2)

    btn = Button(master=popUpWindow, border=0, text='Done',command=lambda dayEntryday=dayEntry, monthEntry=monthEntry, yearEntry=yearEntry, entry=entry, popUpWindow=popUpWindow: done(entry, popUpWindow,dayEntry,monthEntry,yearEntry))
    btn.grid(row=1, column=11)

    popUpWindow.bind('<Key>',newTaskKeyPressed)

start()
root.mainloop()
from tkinter import *
from os import makedirs
import os
import shutil
from datetime import *
from sys import exit
from tkinter import messagebox

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
    f.write('background:white\n')
    f.write('maxcards:5')
    f.close()

def settings():
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
        settingsWindow.title('Settings')

    def checkNewLists():
        f = open(board[:-9]+'lists.txt').readlines()
        file = open(board[:-9]+'lists.txt','w')
        for line in f:
            if line != 'newList;0\n':
                file.write(line)
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
                line = line[0]+':'+line[1] + '\n'
                file.write(line)
        file.close()
        updateScreen()
        settings()

    #Set the maximum amount of cards
    def setMaxCards(entry):
        maxCards = entry.get()
        error = False
        try:
            maxCards = int(maxCards)
        except:
            error = True
        if maxCards < 0:
            error = True

        if error:
            alertWindow = Tk()
            alertWindow.title('ERROR')
            alertWindowLabel = Label(master=alertWindow,text='Please fill in a (positive) number').grid(row=0)
            btn = Button(master=alertWindow,text='Ok',command=lambda : alertWindow.destroy()).grid(row=1)
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
            settings()

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
        file = open(board[:-9]+'lists.txt','w')
        for lstName in givenLists:
            file.write(lstName.replace('\n','')+';0\n')
        file.close()
        settings()
        updateScreen()
        settingsWindow.focus_force()
        return True


    textcolor = 'black'
    if ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','') in ['black','grey22','blue']:
        textcolor = 'white'

    lbl = Label(master=settingsWindow,text='Backgroundcolor:',fg=textcolor,font=('Arial',20),bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','')).grid(row=0,columnspan=1000)
    colorButtons = []
    colors = ['black','white','red','grey22','lightgreen','orange','blue','orangered','VioletRed1','turquoise1','green2']
    for color in colors:
        textcolor = 'black'
        if color == 'black' or color == 'grey22':
            textcolor = 'white'
        colorButtons.append(Button(master=settingsWindow,text=color,bg=color,fg=textcolor,command= lambda color=color: setBgColor(color)).grid(column=colors.index(color),row=1))

    textcolor = 'black'
    if ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '') in ['black', 'grey22', 'blue']:
        textcolor = 'white'
    lbl2 = Label(master=settingsWindow, text='Max cards:', fg=textcolor, font=('Arial', 20),bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')).grid(row=2,columnspan=1000)
    entry = Entry(master=settingsWindow,fg=textcolor,bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', ''))
    entry.insert(0,((open('boards/settings.txt').readlines())[1].split(':'))[1].replace('\n', ''))
    entry.grid(row=3,column=0,columnspan=1000)

    confirmButton = Button(master=settingsWindow,text='Ok',command=lambda entry=entry: setMaxCards(entry))
    confirmButton.grid(row=3,column=4,columnspan=1000)

    listsLabel = Label(master=settingsWindow, text='Lists:', fg=textcolor, font=('Arial', 20),bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')).grid(row=4,columnspan=1000)

    listsEntrys = []
    lists = open(board[:-9]+'lists.txt').readlines()
    x = 0
    for line in lists:
        lists[x] = line.split(';')[0]
        x += 1
    x = 0
    for lst in lists:
        listsEntrys.append(Entry(master=settingsWindow,font=('arial',15),bg=((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', ''),fg=textcolor))
        listsEntrys[x].grid(row=x+5,columnspan=1000)
        listsEntrys[x].insert(0,lst)
        x += 1
    listsConfirmButton = Button(master=settingsWindow,text='Ok',command=lambda listEntrys=listsEntrys: setLists(listsEntrys))
    listsConfirmButton.grid(row=x+5,column=0,columnspan=1000)
    newListButton = Button(master=settingsWindow,text='New List',command=lambda listEntrys=listsEntrys: newList(listsEntrys))
    newListButton.grid(row=x+5,column=3,columnspan=1000)

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
        if bgColor in ['black','grey22','blue']:
            textColor = 'white'
        else:
            textColor = 'black'

        newActivityWindow = Tk()
        newActivityWindow.title('New activity')
        newActivityWindow.config(bg=bgColor)
        newActivityWindow.bind('<Key>',newActivityKeyPressed)

        newActivityLabel = Label(master=newActivityWindow, text='New activity',bg=bgColor,fg=textColor)
        newActivityLabel.grid(columnspan=3)

        global newActivityTitleEntry, newActivityDayEntry, newActivityMonthEntry, newActivityYearEntry
        newActivityTitleEntry = Entry(master=newActivityWindow, width=15,bg=bgColor,fg=textColor)
        newActivityTitleEntry.grid(row=1, column=0, columnspan=3)
        newActivityTitleEntry.focus_force()

        newActivityDayEntry = Entry(master=newActivityWindow, width=4,bg=bgColor,fg=textColor)
        newActivityDayEntry.grid(row=2, column=0)

        newActivityMonthEntry = Entry(master=newActivityWindow, width=4,bg=bgColor,fg=textColor)
        newActivityMonthEntry.grid(row=2, column=1)

        newActivityYearEntry = Entry(master=newActivityWindow, width=4,bg=bgColor,fg=textColor)
        newActivityYearEntry.grid(row=2, column=2)

        newActivityButton = Button(text='Done', master=newActivityWindow, command=addNewActivity)
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


        viewDayWindow = Tk()
        viewDayWindow.title(day)
        viewDayWindow.focus_force()
        viewDayWindow.config(bg=bgColor)
        viewDayWindow.bind('<Key>',viewDayKeyPressed)

        dateLabel = Label(master=viewDayWindow,text=day,font=('arial',20),bg=bgColor,fg=textColor)
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

            activityButtons.append(Button(master=viewDayWindow,text='X',command= lambda activity=activity: deleteActivity(activity)))
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
    if bgColor in ['black','grey22','blue']:
        textColor = 'white'
    else:
        textColor = 'black'

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

    dayBgColor = 'lightgreen'
    if bgColor == 'lightgreen':
        dayBgColor = 'green2'

    # Build up the window
    dayButtons = []
    for i in range(0,7):
        dayButtons.append(Button(master=agendaWindow,text=((str(days[i])[8:])[:2]+' - '+(str(days[i])[5:])[:2]+str(dagInfo[i])),command= lambda day=((str(days[i])[8:])[:2]+' - '+(str(days[i])[5:])[:2]), vandaagInfo=dagInfo[i]:viewDay(day,vandaagInfo)))
        if str(days[i])[:10] == str(datetime.now())[:10]:
            dayButtons[i].config(width=20,height=25,font=("arial",10),anchor='nw',justify='left',background=dayBgColor)
        else:
            dayButtons[i].config(width=20,height=25,font=("arial",10),anchor='nw',justify='left',bg=bgColor,fg=textColor)
        dayButtons[i].grid(row=2,column=i)

    # Next week button
    nextWeekButton = Button(master=agendaWindow,text='Next week',command=nextWeek)
    nextWeekButton.grid(row=3,column=6)

    # Past week button
    pastWeekButton = Button(master=agendaWindow,text='Past week', command=pastWeek)
    pastWeekButton.grid(row=3, column=0)

    # Today week button
    todayButton = Button(master=agendaWindow,text='Today',command=ftoday)
    todayButton.grid(row=3,column=3)

    # New activity Button
    newActivityButton = Button(master=agendaWindow,text='New activity',command=newActivity)
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

    Label1 = Label(text='Delete board:', font=("Arial", 20),background='white')
    Label1.grid()

    buttons = []

    boards = open('boards/BOARDS.txt').readlines()
    x = 0
    for brd in boards:
        brd = brd[:len(brd) - 1]
        buttons.append(
            Button(text=brd, width=20, height=2, font=("Arial", 20), command=lambda brd=brd: deleteBoard(brd)))
        buttons[x].grid(row=x + 1)
        x += 1


def newBoard():
    def createNewBoard(Entry1):
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
    if bgColor in ['black','grey22','blue']:
        textColor = 'white'
    else:
        textColor = 'black'

    global root
    root.destroy()
    root = Tk()
    root.title('New Board')
    root.config(bg=bgColor)

    Label1 = Label(text="New board",bg=bgColor,fg=textColor)
    Label1.grid(row=0, column=0)

    Entry1 = Entry(bg=bgColor,fg=textColor)
    Entry1.grid(row=1, column=0)

    Button1 = Button(text='Done', command=lambda Entry1=Entry1: createNewBoard(Entry1))
    Button1.grid(row=1, column=1)


def boardSelect(brd):
    global board
    board = 'boards/' + brd + '/board.txt'
    global root
    root.destroy()

    try:
        f = open('boards/'+brd+'/todoScrolled.txt').readlines()
        messagebox.showwarning('WARNING','You need to run the "Update.exe" first.\n\nIt will update all the files so that they are compatible with this version of CL Scrum')
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

    root = Tk()
    updateScreen()



def start():
    global root
    root = Tk()
    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n', '')
    root.config(background=bgColor)
    root.title('Select board')
    textcolor = 'black'
    if bgColor in ['black','grey22','blue']:
        textcolor = 'white'

    Label1 = Label(text="Available boards", font=("Arial", 20),fg=textcolor,bg=bgColor)
    Label1.grid(row=0, column=0, columnspan=2)

    boards = open('boards/BOARDS.txt').readlines()
    buttons = []
    x = 0
    for brd in boards:
        brd = str(brd)
        brd = brd[:len(brd) - 1]
        buttons.append(Button(text=brd, width=20, height=2, font=("Arial", 20), fg=textcolor, bg=bgColor,command=lambda brd=brd: boardSelect(brd)))
        buttons[x].grid(row=x + 1, column=0, columnspan=2)
        x += 1

    buttons.append(Button(text='New board', width=18, height=1, font=("Arial", 10), fg=textcolor, bg=bgColor,command=newBoard))
    buttons[x].grid(row=x + 1, column=0)

    buttons.append(Button(text='delete board', width=21, height=1, font=("Arial", 10), fg=textcolor, bg=bgColor,command=deleteBoardWindow))
    buttons[x + 1].grid(row=x + 1, column=1)

    versionLabel = Label(text='(CL Scrum V 1.4) ©CasLinders',width=40,font=('arial',10), fg=textcolor, bg=bgColor,anchor='nw',justify='left').grid(row=x+2,column=0,columnspan=2)

def viewTask(task,lst):
    def viewTaskWindowKeyPressed(key):
        if key.char == 'd' or key.char == 'D':
            fDelete(task,lst)
        elif key.char == 'm' or key.char == 'M':
            moveTask(task,lst)
        elif key.char == '\x1b':
            updateText(textBox,task,lst)
    def updateText(textBox,task,lst,entry):
        f = open(board).readlines()
        tasks = []
        for line in f:
            tasks.append(line.split(';')[1])
        if entry.get() in tasks and entry.get() != task[1]:
            messagebox.showerror('Warning','Task already exists')
            return
        f = open(board).readlines()
        file = open(board,'w')
        for line in f:
            if line.split(';')[1] == task[1]:
                line = line.split(';')
                file.write(line[0]+';'+entry.get()+';'+line[2])
                os.remove(board[:-9] + 'tasks/' + task[1] + ';' + (task[2].replace('\n', '')).replace(':', '-')+'.txt')
            else:
                file.write(line)
        file.close()
        text = textBox.get(1.0, END)
        f = open(board[:-9] + 'tasks/' + entry.get() + ';' + (task[2].replace('\n', '')).replace(':', '-') + '.txt', 'w')
        text = text.split('\n')
        for line in text:
            if line != '':
                f.write(line + '\n')
        f.close()
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
    if bgColor in ['black', 'grey22', 'blue']:
        textColor = 'white'
    else:
        textColor = 'black'

    viewTaskWindow.title(lst.name.upper()+': '+textTask[1])
    viewTaskWindow.bind('<Key>',viewTaskWindowKeyPressed)
    viewTaskWindow.focus_force()
    viewTaskWindow.config(bg=bgColor)

    lbl1 = Label(master=viewTaskWindow,text=lst.name+': ',font=('arial',15),background=bgColor,fg=textColor)
    lbl1.grid(column=0)
    entry = Entry(master=viewTaskWindow,font=('arial',15),background=bgColor,fg=textColor)
    entry.insert(0,textTask[1])
    entry.grid(row=0,column=1)
    f = open(board[:-9]+'tasks/'+textTask[1] + ';' + (textTask[2].replace('\n','')).replace(':','-') +'.txt','r').readlines()
    x = ''
    for line in f:
        x = x + line

    textBox = Text(master=viewTaskWindow,width=50,height=10,background=bgColor,fg=textColor)
    textBox.grid(columnspan=3)
    textBox.insert(END,x)

    viewTaskWindow.protocol("WM_DELETE_WINDOW", lambda textBox=textBox, entry=entry, textTask=textTask, task=task, lst=lst: updateText(textBox, textTask, lst, entry))

    deleteButton = Button(master=viewTaskWindow,text='Delete',command= lambda textTask=textTask,lst=lst: fDelete(textTask,lst))
    deleteButton.grid(column=1,row=2)

    moveButton = Button(master=viewTaskWindow, text='Move',command= lambda lst=lst,task=task: moveTask(task,lst))
    moveButton.grid(column=2,row=2)
 

def updateScreen():
    global root
    try:
        for i in root.winfo_children():
            i.destroy()
    except:
        pass

    bgColor = ((open('boards/settings.txt').readlines())[0].split(':'))[1].replace('\n','')
    if bgColor in ['black','grey22','blue']:
        textColor = 'white'
    else:
        textColor = 'black'

    def close():
        exit()

    # create screen:
    root.title(board[:-10][7:])
    root.config(background=bgColor)
    root.bind('<Key>',rootKeyPressed)
    root.focus_force()
    root.protocol("WM_DELETE_WINDOW", close)

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
        labels.append(Label(text=listType.name, font=('arial', 15), width=25,fg=textColor))
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
                    cards.append(Button(text='/\\', width=space, height=1, font=('arial', 12), pady=0, background='grey',command=lambda lst=currentList, direction=-1: lst.scroll(direction)))
                    cards[x].grid(row=y, column=currentList.index)
                    x += 1
                elif count == 0:
                    nothingNess = Label(text=' ',bg=bgColor,height=1,font=('arial',16)).grid(row=y,column=currentList.index)
                y += 1
                for i in range(1,round(len(task)/30)):
                    texttask = task[:i*30] + '\n' + task[30:]
                else:
                    texttask = task
                cards.append(Button(anchor='w',justify=LEFT, text=texttask, width=space, height=2+texttask.count('\n'), font=('arial', 12), pady=0,command=lambda lst=currentList, task=fullTask: viewTask(task,lst)))
                cards[x].config(background='lightgrey',highlightbackground='lightgrey')
                cards[x].grid(row=y, column=currentList.index)
                x += 1
                y += 1
                height += 1
            if height == maxCards and count != len(currentList.items)-1:
                cards.append(Button(text='\/',width=space,height=1,font=('arial',12),pady=0,background='grey',command= lambda lst=currentList,direction=1: lst.scroll(direction)))
                cards[x].grid(row=y+1,column=currentList.index)
                x += 1
                break
            elif height == maxCards and count == len(currentList.items)-1:
                nothingNess = Label(text=' ', bg=bgColor, height=1, font=('arial', 16)).grid(row=y, column=currentList.index)
            count += 1
        listIndexNum += 1


    # some white space
    whiteLabels = []
    whiteLabels.append(Label(text=' '))
    whiteLabels[0].config(background=bgColor,highlightbackground=bgColor)
    whiteLabels[0].grid()

    # Ui Buttons
    newButton = Button(text='New task', command=newTask)
    newButton.grid(row=1000)

    agendaButton = Button(text='Calendar', command=openAgenda)
    agendaButton.grid(row=1000,column=1)

    settingsButton = Button(text='Settings',command=settings)
    settingsButton.grid(row=1000,column=2)




def moveTask(task,lst):
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
        settings()

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
    textColor = 'black'
    if bgColor in ['black','grey22','blue']:
        textColor = 'white'

    popUpWindow = Tk()
    popUpWindow.config(bg=bgColor)

    lbl = Label(master=popUpWindow, text='New Task:',bg=bgColor,fg=textColor)
    lbl.grid(columnspan=10)
    entry = Entry(master=popUpWindow,bg=bgColor,fg=textColor)
    entry.focus_force()
    entry.grid(row=1,columnspan=10)

    lbl2 = Label(master=popUpWindow,text='Include in calendar:',bg=bgColor,fg=textColor)
    lbl2.grid(row=2,column=0,columnspan=4)

    dayEntry = Entry(master=popUpWindow,width=4,bg=bgColor,fg=textColor)
    dayEntry.grid(row=3,column=0)
    monthEntry = Entry(master=popUpWindow,width=4,bg=bgColor,fg=textColor)
    monthEntry.grid(row=3,column=1)
    yearEntry = Entry(master=popUpWindow,width=6,bg=bgColor,fg=textColor)
    yearEntry.grid(row=3,column=2)

    btn = Button(master=popUpWindow, text='Done',command=lambda dayEntryday=dayEntry, monthEntry=monthEntry, yearEntry=yearEntry, entry=entry, popUpWindow=popUpWindow: done(entry, popUpWindow,dayEntry,monthEntry,yearEntry))
    btn.grid(row=1, column=11)

    popUpWindow.bind('<Key>',newTaskKeyPressed)

start()
root.mainloop()
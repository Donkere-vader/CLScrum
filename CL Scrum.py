from tkinter import *
from os import makedirs
import shutil
from datetime import *

# to make sure there is a BOARDS.txt file, in the boards directory
try:
    makedirs('boards')
except:
    pass

try:
    f = open('boards/BOARDS.txt').readlines()
except:
    file = open('boards/BOARDS.txt', 'w')
    file.close()


def openAgenda():
    # Destroy any possible already existing agendaWindows
    global date, agendaWindow
    date = datetime.now()

    try:
        agendaWindow.destroy()
    except:
        agendaWindow = Tk()
        agendaWindow.title('Agenda')

    updateAgenda()

def updateAgenda():
    # Import the needed variables/ windows
    global date, agendaWindow
    # Script for new activty
    def newActivity():
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

        newActivityWindow = Tk()
        newActivityWindow.title('Nieuwe activiteit')

        newActivityLabel = Label(master=newActivityWindow, text='Nieuwe activiteit:')
        newActivityLabel.grid(columnspan=3)

        global newActivityTitleEntry, newActivityDayEntry, newActivityMonthEntry, newActivityYearEntry
        newActivityTitleEntry = Entry(master=newActivityWindow, width=15)
        newActivityTitleEntry.grid(row=1, column=0, columnspan=3)

        newActivityDayEntry = Entry(master=newActivityWindow, width=4)
        newActivityDayEntry.grid(row=2, column=0)

        newActivityMonthEntry = Entry(master=newActivityWindow, width=4)
        newActivityMonthEntry.grid(row=2, column=1)

        newActivityYearEntry = Entry(master=newActivityWindow, width=4)
        newActivityYearEntry.grid(row=2, column=2)

        newActivityButton = Button(text='Done', master=newActivityWindow, command=addNewActivity)
        newActivityButton.grid(row=2, column=3)

    def viewDay(day, vandaagInfo):
        def deleteActivity(activity):
            print(activity)
            f = open(board[:-9] + 'agenda.txt').readlines()
            x = 0
            for line in f:
                line = line.split(';')
                if (line[3])[:-1] == activity:
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

        dateLabel = Label(master=viewDayWindow,text=day,font=('arial',20))
        dateLabel.grid(row=0,column=0,columnspan=2)

        activityLabels = []
        activityButtons = []
        x = 0
        vandaagInfo = vandaagInfo.split('\n')
        vandaagInfo.remove('')
        for activity in vandaagInfo:
            print(activity)
            activityLabels.append(Label(master=viewDayWindow,text=activity,font=('arial',13)))
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

    dagenLabels = []
    x = 0
    for dag in ['Ma', 'Di', 'Wo', 'Do', 'Vr', 'Za', 'Zo']:
        dagenLabels.append(Label(master=agendaWindow, text=dag))
        dagenLabels[x].grid(row=1, column=x)
        x += 1
    #year label
    yearLabel = Label(master=agendaWindow,text=str(date.year),font=('arial',20))
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

    # Build up the window
    dayButtons = []
    for i in range(0,7):
        dayButtons.append(Button(master=agendaWindow,text=((str(days[i])[8:])[:2]+' - '+(str(days[i])[5:])[:2]+str(dagInfo[i])),command= lambda day=((str(days[i])[8:])[:2]+' - '+(str(days[i])[5:])[:2]), vandaagInfo=dagInfo[i]:viewDay(day,vandaagInfo)))
        if str(days[i])[:10] == str(datetime.now())[:10]:
            dayButtons[i].config(width=20,height=25,font=("arial",10),anchor='nw',justify='left',background='lightgreen')
        else:
            dayButtons[i].config(width=20,height=25,font=("arial",10),anchor='nw',justify='left')
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
        updateScreen()

    global root
    root.destroy()
    root = Tk()
    root.title('New Board')

    Label1 = Label(text="New board")
    Label1.grid(row=0, column=0)

    Entry1 = Entry()
    Entry1.grid(row=1, column=0)

    Button1 = Button(text='Done', command=lambda Entry1=Entry1: createNewBoard(Entry1))
    Button1.grid(row=1, column=1)


def boardSelect(brd):
    global board
    board = 'boards/' + brd + '/board.txt'
    global root
    root.destroy()
    try:
        f = open('boards/'+brd+'agenda.txt').readlines()
    except:
        f = open('boards/'+brd+'agenda.txt','w')

    try:
        f = open(board).readlines()
    except:
        f = open(board,'w')
    root = Tk()
    updateScreen()


def start():
    global root
    root = Tk()
    root.config(background='white')
    root.title('Select board')

    Label1 = Label(text="Available boards", font=("Arial", 20))
    Label1.config(background='white',highlightbackground='white')
    Label1.grid(row=0, column=0, columnspan=2)

    boards = open('boards/BOARDS.txt').readlines()
    buttons = []
    x = 0
    for brd in boards:
        brd = str(brd)
        brd = brd[:len(brd) - 1]
        buttons.append(Button(text=brd, width=20, height=2, font=("Arial", 20), command=lambda brd=brd: boardSelect(brd)))
        buttons[x].grid(row=x + 1, column=0, columnspan=2)
        x += 1

    buttons.append(Button(text='New board', width=18, height=1, font=("Arial", 10), command=newBoard))
    buttons[x].grid(row=x + 1, column=0)

    buttons.append(Button(text='delete board', width=21, height=1, font=("Arial", 10), command=deleteBoardWindow))
    buttons[x + 1].grid(row=x + 1, column=1)
 

def updateScreen():
    global root
    try:
        for i in root.winfo_children():
            i.destroy()
    except:
        pass

    bgColor = 'grey'

    # create screen:
    root.title(board[:-10][7:])
    root.config(background=bgColor)

    # the lists
    todo = []
    busy = []
    done = []
    global delete
    delete = []

    # other variables
    space = 30  # width for the buttons and labels

    # create lists from the file
    f = open(board).readlines()

    for line in f:
        if line[0] == '#':
            continue
        line = line.split(';')
        line[0] = int(line[0])
        if line[0] == 1:
            todo.append((line[1])[:len(line[1]) - 1])
        if line[0] == 2:
            busy.append((line[1])[:len(line[1]) - 1])
        if line[0] == 3:
            done.append((line[1])[:len(line[1]) - 1])
        if line[0] == 4:
            delete.append((line[1])[:len(line[1]) - 1])

    # labels to screen:
    labels = []
    x = 0
    for listType in ['To Do', 'Busy', 'Done']:
        labels.append(Label(text=listType, font=('arial', 15), width=25))
        labels[x].config(background=bgColor,highlightbackground=bgColor)
        labels[x].grid(row=0, column=x)
        x += 1

    deleteBool = False
    if len(delete) != 0:
        deleteBool = True
        labels.append(Label(text='delete', font=('arial', 15)))
        labels[3].config(background=bgColor,highlightbackground=bgColor)
        labels[3].grid(row=0, column=3)

    # Add tasks to screen
    cards = []
    x = 0
    y = 1

    height = 0
    for task in todo:
        if len(task) > 30:
            texttask = task[:30] + '\n' + task[30:]
        else:
            texttask = task
        cards.append(Button(anchor='w',justify=LEFT, text=texttask, width=space, height=2, font=('arial', 12), pady=0,command=lambda task=task: moveTask(task)))
        cards[x].config(background='lightgrey',highlightbackground='lightgrey')
        cards[x].grid(row=y, column=0)
        x += 1
        y += 1
        height += 1
    y = 1
    for task in busy:
        if len(task) > 30:
            texttask = task[:30] + '\n' + task[30:]
        else:
            texttask = task
        cards.append(Button(anchor='w',justify=LEFT, text=texttask, width=space, height=2, font=('arial', 12), pady=0,command=lambda task=task: moveTask(task)))
        cards[x].config(background='lightgrey',highlightbackground='lightgrey')
        cards[x].grid(row=y, column=1)
        x += 1
        y += 1
        if y == height:
            height += 1
    y = 1
    for task in done:
        if len(task) > 30:
            texttask = task[:30] + '\n' + task[30:]
        else:
            texttask = task
        cards.append(Button(anchor='w',justify=LEFT, text=texttask, width=space, height=2, font=('arial', 12), pady=0,command=lambda task=task: moveTask(task)))
        cards[x].config(background='lightgrey',highlightbackground='lightgrey')
        cards[x].grid(row=y, column=2)
        x += 1
        y += 1
        if y == height:
            height += 1
    y = 1
    for task in delete:
        if len(task) > 30:
            texttask = task[:30] + '\n' + task[30:]
        else:
            texttask = task
        cards.append(Button(anchor='w',justify=LEFT, text=texttask, width=space, height=2, font=('arial', 12), pady=0,command=lambda task=task: moveTask(task)))
        cards[x].config(background='red',highlightbackground='red')
        cards[x].grid(row=y, column=3)
        x += 1
        y += 1
        if y == height:
            height += 1

    # some white space
    whiteLabels = []
    whiteLabels.append(Label(text=' '))
    whiteLabels[0].config(background=bgColor,highlightbackground=bgColor)
    whiteLabels[0].grid()

    # Ui Buttons
    newButton = Button(text='New task', command=newTask)
    newButton.grid(row=1000)

    agendaButton = Button(text='Agenda', command=openAgenda)
    agendaButton.grid(row=1000,column=1)

    if deleteBool:
        deleteButton = Button(text='delete', command=fDelete)
        deleteButton.config(background=bgColor,highlightbackground=bgColor)
        deleteButton.grid(row=100, column=3)


def moveTask(task):
    f = open(board).readlines()

    x = -1
    for line in f:
        x += 1
        if line[0] == '#':
            continue
        line = line.split(';')
        line[0] = int(line[0])
        if (line[1])[:len(line[1]) - 1] == task:
            if line[0] > 3:
                line[0] = 0
            line[0] += 1
            f[x] = str(line[0]) + ';' + line[1]
            file = open(board, 'w')
            for line in f:
                file.write(line)
            file.close()
            break
    updateScreen()


def fDelete():
    f = open(board).readlines()
    while len(delete) > 0:
        if len(f) == 0:
            break
        for line in f:
            if line[0] == '#':
                continue
            line = line.split(';')
            line[0] = int(line[0])
            if line[0] == 4:
                delete.remove(str(line[1])[:len(line[1]) - 1])
                line = str(line[0]) + ';' + line[1]
                f.remove(line)
                break
    file = open(board, 'w')
    for line in f:
        file.write(line)
    file.close()

    updateScreen()


def newTask(dayEntry=None):
    def done(entry, popUpWindow,dayEntry,monthEntry,yearEntry):
        task = entry.get()
        if task.lower() == 'cas is gay':
            extraWindow = Tk()
            extraWindow.title('8===>')
            label = Label(master=extraWindow,text='JE BENT ZELF GAY!',font=('Arial',30))
            label.grid()
        elif task != '':
            f = open(board).readlines()
            f.append(('1' + ';' + task + '\n'))
            file = open(board, 'w')
            for line in f:
                file.write(line)
            file.close()
            print(checkBoxValue)
            if checkBoxValue == 0:
                f = open(board[:-9] + 'agenda.txt').readlines()
                file = open(board[:-9] + 'agenda.txt','w')
                for line in f:
                    file.write(line)
                taskDay = dayEntry.get()
                taskMonth = monthEntry.get()
                taskYear = yearEntry.get()
                if taskDay == '':
                    taskDay = datetime.now().day
                if taskMonth == '':
                    taskMonth = datetime.now().month
                if taskYear == '':
                    taskYear = datetime.now().year

                file.write('\n'+str(taskDay)+';'+str(taskMonth)+';'+str(taskYear)+';'+task)
                file.close()
            popUpWindow.destroy()
            updateScreen()
            return ''

    popUpWindow = Tk()
    lbl = Label(master=popUpWindow, text='New Task:')
    lbl.grid(columnspan=10)
    entry = Entry(master=popUpWindow)
    entry.grid(row=1,columnspan=10)

    checkBoxValue = 0
    checkBox = Checkbutton(master=popUpWindow,text='Include in calander',variable=checkBoxValue)
    checkBox.grid(row=2,columnspan=10)

    dayEntry = Entry(master=popUpWindow,width=4)
    dayEntry.grid(row=3,column=0)
    monthEntry = Entry(master=popUpWindow,width=4)
    monthEntry.grid(row=3,column=1)
    yearEntry = Entry(master=popUpWindow,width=4)
    yearEntry.grid(row=3,column=2)

    btn = Button(master=popUpWindow, text='Done',command=lambda dayEntryday=dayEntry, monthEntry=monthEntry, yearEntry=yearEntry, entry=entry, popUpWindow=popUpWindow: done(entry, popUpWindow,dayEntry,monthEntry,yearEntry))
    btn.grid(row=1, column=11)

start()
root.mainloop()
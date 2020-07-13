import random as rm
from tkinter import *
from tkinter import messagebox

tk = Tk()
line = 0
comline = 0
MainList = []
CheckList = []
ComCheckList = []
turn = "User"


def checkTurn(turns):
    global turn
    turn = turns
    return turn


PeloList = [1, 2, 3, 4, 5, 6, 8, 9, 7, 10, 11, 12, 13,
            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
MainList = rm.sample(PeloList, k=25)
CommainList = rm.sample(PeloList, k=25)
SelectComList = CommainList.copy()

MainCheckList = [[0, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9],
                 [10, 11, 12, 13, 14],
                 [15, 16, 17, 18, 19],
                 [20, 21, 22, 23, 24],
                 [0, 5, 10, 15, 20],
                 [1, 6, 11, 16, 21],
                 [2, 7, 12, 17, 22],
                 [3, 8, 13, 18, 23],
                 [4, 9, 14, 19, 24],
                 [0, 6, 12, 18, 24],
                 [4, 8, 12, 16, 20],
                 ]
ComMainCheckList = [[0, 1, 2, 3, 4],
                 [5, 6, 7, 8, 9],
                 [10, 11, 12, 13, 14],
                 [15, 16, 17, 18, 19],
                 [20, 21, 22, 23, 24],
                 [0, 5, 10, 15, 20],
                 [1, 6, 11, 16, 21],
                 [2, 7, 12, 17, 22],
                 [3, 8, 13, 18, 23],
                 [4, 9, 14, 19, 24],
                 [0, 6, 12, 18, 24],
                 [4, 8, 12, 16, 20],
                 ]


def ResetArrangement():
    MainList = rm.sample(PeloList, k=25)


def disableButton(buttons):
    buttons.configure(state=DISABLED)


def CheckLine(ListCheck):
    global line
    for i in MainCheckList:
        if 1 in ListCheck and 2 in ListCheck and 3 in ListCheck and 4 in ListCheck and 5 in ListCheck:
            if [0, 1, 2, 3, 4] in MainCheckList:
                MainCheckList.remove([0, 1, 2, 3, 4])
                line = line + 1
        if 6 in ListCheck and 7 in ListCheck and 8 in ListCheck and 9 in ListCheck and 10 in ListCheck:
            if [5, 6, 7, 8, 9] in MainCheckList:
                MainCheckList.remove([5, 6, 7, 8, 9])
                line = line + 1
        if 11 in ListCheck and 12 in ListCheck and 13 in ListCheck and 14 in ListCheck and 15 in ListCheck:
            if [10, 11, 12, 13, 14] in MainCheckList:
                MainCheckList.remove([10, 11, 12, 13, 14])
                line = line + 1
        if 16 in ListCheck and 17 in ListCheck and 18 in ListCheck and 19 in ListCheck and 20 in ListCheck:
            if [15, 16, 17, 18, 19] in MainCheckList:
                MainCheckList.remove([15, 16, 17, 18, 19])
                line = line + 1
        if 21 in ListCheck and 22 in ListCheck and 23 in ListCheck and 24 in ListCheck and 25 in ListCheck:
            if [20, 21, 22, 23, 24] in MainCheckList:
                MainCheckList.remove([20, 21, 22, 23, 24])
                line = line + 1
        if 1 in ListCheck and 6 in ListCheck and 11 in ListCheck and 16 in ListCheck and 21 in ListCheck:
            if [0, 5, 10, 15, 20] in MainCheckList:
                MainCheckList.remove([0, 5, 10, 15, 20])
                line = line + 1
        if 2 in ListCheck and 7 in ListCheck and 12 in ListCheck and 17 in ListCheck and 22 in ListCheck:
            if [1, 6, 11, 16, 21] in MainCheckList:
                MainCheckList.remove([1, 6, 11, 16, 21])
                line = line + 1
        if 3 in ListCheck and 8 in ListCheck and 13 in ListCheck and 18 in ListCheck and 23 in ListCheck:
            if [2, 7, 12, 17, 22] in MainCheckList:
                MainCheckList.remove([2, 7, 12, 17, 22])
                line = line + 1
        if 4 in ListCheck and 9 in ListCheck and 14 in ListCheck and 19 in ListCheck and 24 in ListCheck:
            if [3, 8, 13, 18, 2, 3] in MainCheckList:
                MainCheckList.remove([3, 8, 13, 18, 23])
                line = line + 1
        if 5 in ListCheck and 10 in ListCheck and 15 in ListCheck and 20 in ListCheck and 25 in ListCheck:
            if [4, 9, 14, 19, 24] in MainCheckList:
                MainCheckList.remove([4, 9, 14, 19, 24])
                line = line + 1
        if 1 in ListCheck and 7 in ListCheck and 13 in ListCheck and 19 in ListCheck and 25 in ListCheck:
            if [0, 6, 12, 18, 24] in MainCheckList:
                MainCheckList.remove([0, 6, 12, 18, 24])
                line = line + 1
        if 5 in ListCheck and 9 in ListCheck and 13 in ListCheck and 17 in ListCheck and 21 in ListCheck:
            if [4, 8, 12, 16, 20] in MainCheckList:
                MainCheckList.remove([4, 8, 12, 16, 20])
                line = line + 1

    print('User Line',line)


def ComCheckLine(ListCheck):
    global comline
    print(ListCheck)
    for i in ComMainCheckList:
        if 1 in ListCheck and 2 in ListCheck and 3 in ListCheck and 4 in ListCheck and 5 in ListCheck:
            if [0, 1, 2, 3, 4] in ComMainCheckList:
                ComMainCheckList.remove([0, 1, 2, 3, 4])
                comline = comline + 1
        if 6 in ListCheck and 7 in ListCheck and 8 in ListCheck and 9 in ListCheck and 10 in ListCheck:
            if [5, 6, 7, 8, 9] in ComMainCheckList:
                ComMainCheckList.remove([5, 6, 7, 8, 9])
                comline = comline + 1
        if 11 in ListCheck and 12 in ListCheck and 13 in ListCheck and 14 in ListCheck and 15 in ListCheck:
            if [10, 11, 12, 13, 14] in ComMainCheckList:
                ComMainCheckList.remove([10, 11, 12, 13, 14])
                comline = comline + 1
        if 16 in ListCheck and 17 in ListCheck and 18 in ListCheck and 19 in ListCheck and 20 in ListCheck:
            if [15, 16, 17, 18, 19] in ComMainCheckList:
                ComMainCheckList.remove([15, 16, 17, 18, 19])
                comline = comline + 1
        if 21 in ListCheck and 22 in ListCheck and 23 in ListCheck and 24 in ListCheck and 25 in ListCheck:
            if [20, 21, 22, 23, 24] in ComMainCheckList:
                ComMainCheckList.remove([20, 21, 22, 23, 24])
                comline = comline + 1
        if 1 in ListCheck and 6 in ListCheck and 11 in ListCheck and 16 in ListCheck and 21 in ListCheck:
            if [0, 5, 10, 15, 20] in ComMainCheckList:
                ComMainCheckList.remove([0, 5, 10, 15, 20])
                comline = comline + 1
        if 2 in ListCheck and 7 in ListCheck and 12 in ListCheck and 17 in ListCheck and 22 in ListCheck:
            if [1, 6, 11, 16, 21] in ComMainCheckList:
                ComMainCheckList.remove([1, 6, 11, 16, 21])
                comline = comline + 1
        if 3 in ListCheck and 8 in ListCheck and 13 in ListCheck and 18 in ListCheck and 23 in ListCheck:
            if [2, 7, 12, 17, 22] in ComMainCheckList:
                ComMainCheckList.remove([2, 7, 12, 17, 22])
                comline = comline + 1
        if 4 in ListCheck and 9 in ListCheck and 14 in ListCheck and 19 in ListCheck and 24 in ListCheck:
            if [3, 8, 13, 18, 2, 3] in ComMainCheckList:
                ComMainCheckList.remove([3, 8, 13, 18, 23])
                comline = comline + 1
        if 5 in ListCheck and 10 in ListCheck and 15 in ListCheck and 20 in ListCheck and 25 in ListCheck:
            if [4, 9, 14, 19, 24] in ComMainCheckList:
                ComMainCheckList.remove([4, 9, 14, 19, 24])
                comline = comline + 1
        if 1 in ListCheck and 7 in ListCheck and 13 in ListCheck and 19 in ListCheck and 25 in ListCheck:
            if [0, 6, 12, 18, 24] in ComMainCheckList:
                ComMainCheckList.remove([0, 6, 12, 18, 24])
                comline = comline + 1
        if 5 in ListCheck and 9 in ListCheck and 13 in ListCheck and 17 in ListCheck and 21 in ListCheck:
            if [4, 8, 12, 16, 20] in ComMainCheckList:
                ComMainCheckList.remove([4, 8, 12, 16, 20])
                comline = comline + 1

    print('Computer Line :',comline)



def Computerclick():
    valucom = rm.choice(SelectComList)
    global comline
    indexvalue = CommainList.index(valucom)
    SelectComList.remove(valucom)
    ComCheckList.append(indexvalue)
    ComCheckLine(ComCheckList)
    if(comline>=5):
        CheckWin()
    combtnClick(valucom)

def UserComclick(UserValue):
    global comline
    print('value from user',UserValue)
    indexvalue = CommainList.index(UserValue)
    SelectComList.remove(UserValue)
    ComCheckList.append(indexvalue)
    ComCheckLine(ComCheckList)
    if(comline>=5):
        CheckWin()
    else:
        Computerclick()



def btnClick(buttons):
        disableButton(buttons)
        val = MainList.index(int(buttons['text']))
        CheckList.append(val+1)
        CheckLine(CheckList)
        buttons.configure(background="#fd0f2b", fg="white")
        UserComclick(int(buttons['text']))
        CheckWin()



def combtnClick(comnum):
    val = MainList.index(comnum)
    CheckList.append(val+1)
    CheckLine(CheckList)
    if(val < 5):
        button2 = Button(tk, text=comnum, font='Times 20 bold', bg='gray',
                         fg='white', height=4, width=8)
        button2.grid(row=3, column=val+0)
        button2.configure(background="#fd0f2b", fg="white",state=DISABLED)
    if(val >= 5 and val < 10):
        button2 = Button(tk, text=comnum, font='Times 20 bold', bg='gray',
                         fg='white', height=4, width=8)
        button2.grid(row=4, column=val-5)
        button2.configure(background="#fd0f2b", fg="white",state=DISABLED)
    if(val >= 10 and val < 15):
        button2 = Button(tk, text=comnum, font='Times 20 bold', bg='gray',
                         fg='white', height=4, width=8)
        button2.grid(row=5, column=val-10)
        button2.configure(background="#fd0f2b", fg="white",state=DISABLED)
    if(val >= 15 and val < 20):
        button2 = Button(tk, text=comnum, font='Times 20 bold', bg='gray',
                         fg='white', height=4, width=8)
        button2.grid(row=6, column=val-15)
        button2.configure(background="#fd0f2b", fg="white",state=DISABLED)
    if(val >= 20 and val < 25):
        button2 = Button(tk, text=comnum, font='Times 20 bold', bg='gray',
                         fg='white', height=4, width=8)
        button2.grid(row=7, column=val-20)
        button2.configure(background="#fd0f2b", fg="white",state=DISABLED)
    CheckWin()

    
def CheckWin():
    if(line >= 5):
        messagebox.showinfo("Win or Lose","User Win !!!!!")
        tk.quit()
        pass
    elif(comline >= 5):
        messagebox.showinfo("Win or Lose","Computer Win !!!!!")
        tk.quit()
        pass
    else:
        pass

def GUI():
    tk.title("Play Bingo With Computer")
    RandomSelect = Button(tk, text="Reset", font='Times 20 bold', bg='gray',
                          fg='white', height=3, width=8, command=lambda: ResetArrangement())
    RandomSelect.grid(row=2, column=2)

    label = Label(tk, text="Lines : ", font='Times 20 bold',
                  bg='white', fg='black', height=1, width=9)
    label.grid(row=1, column=0)

    button1 = Button(tk, text=MainList[0], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=MainList[1], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=MainList[2], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=MainList[3], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button4))
    button4.grid(row=3, column=3)

    button5 = Button(tk, text=MainList[4], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button5))
    button5.grid(row=3, column=4)

    button6 = Button(tk, text=MainList[5], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button6))
    button6.grid(row=4, column=0)

    button7 = Button(tk, text=MainList[6], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button7))
    button7.grid(row=4, column=1)

    button8 = Button(tk, text=MainList[7], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button8))
    button8.grid(row=4, column=2)

    button9 = Button(tk, text=MainList[8], font='Times 20 bold', bg='gray',
                     fg='white', height=4, width=8, command=lambda: btnClick(button9))
    button9.grid(row=4, column=3)

    button10 = Button(tk, text=MainList[9], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button10))
    button10.grid(row=4, column=4)

    button11 = Button(tk, text=MainList[10], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button11))
    button11.grid(row=5, column=0)

    button12 = Button(tk, text=MainList[11], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button12))
    button12.grid(row=5, column=1)

    button13 = Button(tk, text=MainList[12], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button13))
    button13.grid(row=5, column=2)

    button14 = Button(tk, text=MainList[13], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button14))
    button14.grid(row=5, column=3)

    button15 = Button(tk, text=MainList[14], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button15))
    button15.grid(row=5, column=4)

    button16 = Button(tk, text=MainList[15], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button16))
    button16.grid(row=6, column=0)

    button17 = Button(tk, text=MainList[16], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button17))
    button17.grid(row=6, column=1)

    button18 = Button(tk, text=MainList[17], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button18))
    button18.grid(row=6, column=2)

    button19 = Button(tk, text=MainList[18], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button19))
    button19.grid(row=6, column=3)

    button20 = Button(tk, text=MainList[19], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button20))
    button20.grid(row=6, column=4)

    button21 = Button(tk, text=MainList[20], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button21))
    button21.grid(row=7, column=0)

    button22 = Button(tk, text=MainList[21], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button22))
    button22.grid(row=7, column=1)

    button23 = Button(tk, text=MainList[22], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button23))
    button23.grid(row=7, column=2)

    button24 = Button(tk, text=MainList[23], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button24))
    button24.grid(row=7, column=3)

    button25 = Button(tk, text=MainList[24], font='Times 20 bold', bg='gray',
                      fg='white', height=4, width=8, command=lambda: btnClick(button25))
    button25.grid(row=7, column=4)


GUI()

tk.mainloop()

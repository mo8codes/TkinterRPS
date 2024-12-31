import tkinter
from tkinter import *
import random

mainframe = tkinter.Tk()

#Classes
class MyLabel(Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, font=("TrebuchetMS", 20), padx=10, pady=10, bg="#0088FF", fg="white",  **kwargs)

class MyButton(Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, font=("TrebuchetMS", 20), padx=10, pady=10, bg="#0050FF", fg="white",bd=3, **kwargs)  

#RPS
def rps():
    destroyMainMenu()
    options = ["Rock", "Paper", "Scissors"]
    global randomChosenRPS
    global userChosenRPS
    randomChosenRPS = random.choice(options)

    global RockButton
    global PaperButton
    global ScissorsButton

    RockButton = MyButton(master=mainmenu, text="Rock", command=rock)
    PaperButton = MyButton(master=mainmenu, text="Paper", command=paper)
    ScissorsButton = MyButton(master=mainmenu, text="Scissors", command=scissors)

    RockButton.pack()
    PaperButton.pack()
    ScissorsButton.pack()

def rock():
    global userChosenRPS
    userChosenRPS = "Rock"
    rpsWinCondition()

def paper():
    global userChosenRPS
    userChosenRPS = "Paper"
    rpsWinCondition()
    
def scissors():
    global userChosenRPS
    userChosenRPS = "Scissors"
    rpsWinCondition()

def rpsWinCondition():
    global RockButton
    global PaperButton
    global ScissorsButton

    RockButton.destroy()
    PaperButton.destroy()
    ScissorsButton.destroy()

    global outcomeLabel

    if userChosenRPS == randomChosenRPS:
        outcomeLabel = MyLabel(master=mainmenu, text="Draw, try again?")
        outcomeLabel.pack()

    # If user chose rock and computer chose scissors
    elif (userChosenRPS == "Rock" and randomChosenRPS == "Scissors") or (userChosenRPS == "Paper" and randomChosenRPS == "Rock") or (userChosenRPS == "Scissors" and randomChosenRPS == "Paper"):
        outcomeLabel = MyLabel(master=mainmenu, text="Congratulations, you win!")
        outcomeLabel.pack()


    else:
        # User Loses
        outcomeLabel = MyLabel(master=mainmenu, text="You lose, try again?")
        outcomeLabel.pack()
    
    global TryAgainButton
    global MainMenuButton
    TryAgainButton = MyButton(master=mainmenu, text="Try Again", command=tryagainRPS)
    TryAgainButton.pack()
    MainMenuButton = MyButton(master=mainmenu, text="Main Menu", command=mainmenuRPS)
    MainMenuButton.pack()
    

def tryagainRPS():
    global TryAgainButton
    global MainMenuButton
    global outcomeLabel

    TryAgainButton.destroy()
    MainMenuButton.destroy()
    outcomeLabel.destroy()
    rps()
    

def mainmenuRPS():
    global TryAgainButton
    global MainMenuButton
    global outcomeLabel
    TryAgainButton.destroy()
    MainMenuButton.destroy()
    outcomeLabel.destroy()

    packMainMenu()

#Main Menu
def packMainMenu():
    global TitleLabel
    global RPSButton

    TitleLabel = MyLabel(master=mainmenu, text="TkinterRPS")
    TitleLabel.pack()

    RPSButton = MyButton(master=mainmenu, text="Rock-Paper-Scissors", command=rps)
    RPSButton.pack()

def destroyMainMenu():
    TitleLabel.destroy()
    RPSButton.destroy()


#Initial Window
mainmenu = Frame(master=mainframe, height=400, width=400, bg="#0088FF")
mainmenu.pack(fill=tkinter.BOTH, expand=True)
packMainMenu()
mainframe.geometry("400x400")
mainframe.mainloop()

import random
import tkinter as tk
from tkinter.font import Font
window=tk.Tk()
window.state("zoomed")
window.title("Rock Paper Scissor")
UserScore=0
CompScore=0
UserChoice=""
CompChoice=""
rockI = tk.PhotoImage(file = "rock.png")
paperI = tk.PhotoImage(file = "paper.png")
scissorI = tk.PhotoImage(file = "scissors.png")
myFont = Font(family="Times New Roman,", size=16)

def RCompChoice():
    return random.choice(["rock","paper","scissor"])
def result(x,y):
    global UserScore
    global CompScore
    if (UserChoice==CompChoice):
        print("tie")
    elif(UserChoice=="rock" and CompChoice=="scissor"):
        print("You win")
        UserScore=UserScore+1
    elif(UserChoice=="paper" and CompChoice=="rock"):
        print("You win")
        UserScore=UserScore+1
    elif(UserChoice=="scissor" and CompChoice=="paper"):
        print("You win")
        UserScore=UserScore+1   
    else:
        print("Computer wins")
        CompScore=CompScore+1
    TextArea=tk.Text(master=window,height=8,width=24,bg="moccasin")
    TextArea.configure(font=myFont)
    TextArea.place(x=200,y=200)
    answer="Your Choice:  {UC} \n\nComputer's Choice: {CC}\n\nYour Score: {US} \n\nComputer's Score: {CS}".format(UC=UserChoice,CC=CompChoice,US=UserScore,CS=CompScore)
    TextArea.insert(tk.END,answer)
def rock():
    global UserChoice
    global CompChoice
    UserChoice="rock"
    CompChoice=RCompChoice()
    result(UserChoice,CompChoice)
def scissor():
    global UserChoice
    global CompChoice
    UserChoice="scissor"
    CompChoice=RCompChoice()
    result(UserChoice,CompChoice)
def paper():
    global UserChoice
    global CompChoice
    UserChoice="paper"
    CompChoice=RCompChoice()
    result(UserChoice,CompChoice)

tk.Label(window,text="Challenge the computer in a game of Rock Paper Scissors!!",fg="coral",font="Algerian 20 bold").pack()
tk.Label(window,text="GAMEPLAY:",fg="RosyBrown",font="Helvetica 12 bold").place(x=60,y=20)
tk.Label(window,text="The person that plays the 'strongest object' is the winner of the game. It's that easy! ",fg="IndianRed",font="Helvetica 11 bold").place(x=70,y=50)
tk.Label(window,text="Rock crushes scissor",fg="IndianRed",font="Helvetica 10 bold").place(x=90,y=70)
tk.Label(window,text="Scissor cuts paper",fg="IndianRed",font="Helvetica 10 bold").place(x=90,y=90)
tk.Label(window,text="Paper covers rock",fg="IndianRed",font="Helvetica 10 bold").place(x=90,y=110)


button1=tk.Button(text="       Rock       ",image=rockI,bg="skyblue",command=rock,padx=15)
button1.place(x=50,y=190)
button2 = tk.Button(text="       Paper      ",image=paperI,bg="pink",command=paper,padx=15)
button2.place(x=50,y=280)
button3 = tk.Button(text="      Scissor     ",image=scissorI,bg="lightgreen",command=scissor,padx=15)
button3.place(x=50,y=370)
window.mainloop()

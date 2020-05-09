### MyAlphabet.py ###
# Project by Johnathan Manasco
# Started on April 16, 2020
########## Explanation ############
"""
'My Alphabet' is a simple game that uses letter number generation to create a fun game for young children.
 The purpose of the game is to teach children the Alphabet by randomizing the letters. 
 This game will be a match game where you will match the capital and lower case letters by inputting the correct answer. 
 The app will randomly provide an upper or lower case letter and you must match with the latter.
 Example: 'A' must be matched with 'a' and 'f' must be matched with 'F'
 Answers will be provided through user input.
""" 
########## End Explanation #############
import random, time
import tkinter as tk
from tkinter import *

class QA:
    def __init__(self, question, correctAnswer):
        self.question = question
        self.corrAns = correctAnswer


quest_list = [QA("A","a"), QA("B","b"), QA("C","c"), QA("D","d"), QA("E","e"), QA("F","f"), QA("G","g"), QA("H","h"), QA("I","i"), QA("J","j"), QA("K","k"), QA("L","l"), 
            QA("M","m"), QA("N","n"), QA("O","o"), QA("P","p"), QA("Q","q"), QA("R","r"), QA("S","s"), QA("T","t"), QA("U","u"), QA("V","v"), QA("W","w"), QA("X","x"), QA("Y","y"), QA("Z","z"), 
            QA("a","A"), QA("b","B"), QA("c","C"), QA("d","D"),("e","E"), QA("f","F"), QA("g","G"), QA("h","H"), QA("i","I"), QA("j","J"), QA("k","K"), QA("l","L"), QA("m","M"), QA("n","N"), 
            QA("o","O"), QA("p","P"), QA("q","Q"), QA("r","R"), QA("s","S"), QA("t","T"), QA("u","U"), QA("v","V"), QA("w","W"), QA("x","X"), QA("y","Y"), QA("z","Z")]

random.shuffle(quest_list)  #Shuffle questions in list to get random questions.

corrCount = 0
ans_count = 0  
x = ans_count 

def play_again():
    again = input("Play again? Y / N: ").upper()
    if again == "Y":
        new_game()
    elif again == "N":
        print("See Ya!")

def Game_Loop():
    for qaitem in quest_list:
        print(qaitem.question)
        userAns = input()
        if userAns == qaitem.corrAns:
            print("Great Job!!")
            time.sleep(1)
            corrCount += 1
            ans_count += 1
        else:
            print("No :(")
            ans_count += 1
        if ans_count == 10:
            break

def New_Game():
        
    while ans_count < 10:
        Game_Loop()
            
        if ans_count == 10:
            print("Great Work!")
            print("You got ", corrCount," correct!")
            play_again()

        

## GUI ##
root = tk.Tk()
root.iconbitmap('MA_Icon.ico')
root.title("My Alphabet")
root.configure(background="black")

logo = PhotoImage(file="MA_Logo.gif")
Label (root, image=logo, bg="black") .grid(row=0, column=0, sticky=W)

Start_Button = Button(text="Play", command= New_Game, bg="cyan", fg= "magenta") .grid(row=2, column=0, sticky=W)

Quit_Button = Button(text="Quit", command= root.destroy, bg="magenta", fg= "yellow") .grid(row=2, column=0, sticky=E)

Answer_input = Entry(root, width=10, bg="black", fg="red") .grid(row=4, column=0)
    



root.geometry("305x200")

root.mainloop()

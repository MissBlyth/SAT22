#import the tkinter library
from tkinter import *

#create a main window
window = Tk()
#change the title of the main window
window.title("Bruno+ Health")
#change the size of the main window
window.minsize(300,500)

##font declarations
#main heading
fontHeading = ("Calibri", 24, "bold")
#sub heading
fontSub = ("Calibri", 18)
#body text
fontBody = ("Calibri", 12)

##interface functions - screen switching
'''
Show the menu screen
'''
def GoMenu():
    ClearScreen()
    menuFrame.grid(row=1)
    print("show main menu")

'''
Show the add dog screen
'''
def GoAddDog():
    ClearScreen()
    addDogFrame.grid(row=1)
    buttonGoMenu.grid()
    print("go to add dog page")

'''
Clear screen function - this function removes every frame so that the interface becomes blank. Except for permanently displayed things like the app header/logo.
'''
def ClearScreen():
    menuFrame.grid_remove()
    addDogFrame.grid_remove()
    buttonGoMenu.grid_remove()
    print("clear all interface elements ")

#common interface objects
#logo pic
logo=PhotoImage(file="brunoLogo.png")
#application title label
mainHeading = Label(window, image=logo, font=fontHeading).grid(row=0, column=0, columnspan=3)

#return to menu button
buttonGoMenu= Button(window, text="Main Menu >>>", command=GoMenu)
buttonGoMenu.grid(row=3,column=0,columnspan=5)

###create menu screen
#frame - container for the interface elements
menuFrame = Frame()
menuFrame.grid()
##menu buttons
menuAddDogDetails = Button(menuFrame, text="Add Dog", command=GoAddDog).grid(row=1,column=0)
menuViewDogDetails = Button(menuFrame, text="View Dog").grid(row=1,column=1)
menuEditDogDetails = Button(menuFrame, text="Edit Dog").grid(row=1, column=2)

###create add dog screen
#frame
addDogFrame = Frame()
addDogFrame.grid(row=1)

#screen head
addDogHeaderLabel = Label(addDogFrame, text="Add your dog details").grid(row=0, column=0)



###create  view dog screen


###create  edit dog screen


GoMenu()

##############################################################
#DO NOT CODE BELOW THIS LINE
#create the event loop for the interface
mainloop()

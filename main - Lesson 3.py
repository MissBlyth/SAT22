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
#screen header
addDogHeaderLabel = Label(addDogFrame, text="Add your dog details", font=fontSub).grid(row=0, column=0, columnspan=2)

#create tk variable wrapper for dog name
dogTKName = StringVar()
#create the label
Label(addDogFrame, text="Name:").grid(row=1, column=0)
#create text input
inputDogName = Entry(addDogFrame)
inputDogName.grid(row=1, column=1)

#gender
dogTKGender = StringVar()
Radiobutton(addDogFrame, text="Male", variable="dogTKGender", value="Male").grid(row=2, column=0)
Radiobutton(addDogFrame, text="Female", variable="dogTKGender", value="Female").grid(row=2, column=1)
Radiobutton(addDogFrame, text="Unknown", variable="dogTKGender", value="Unknown").grid(row=2, column=2)
dogTKGender.set("Unknown")

#dropdown
##add a drop down box
#create the label
Label(addDogFrame, text="Breed:").grid(row=3, column=0)
#items in the drop down
dogBreeds=["Unknown", "Shih Tzu", "Maltese", "German Shepherd"] #items for dropdown
#container for dropdown selection
dogBreedSelect = StringVar()
dogBreedSelect.set("Unknown")
breedDropDown=OptionMenu(addDogFrame, dogBreedSelect, *dogBreeds)
breedDropDown.grid(row=3, column=1) #pack into frame

#save button
Button(addDogFrame, text="Save").grid(row=4, column=2)



###create  view dog screen


###create  edit dog screen


GoMenu()

##############################################################
#DO NOT CODE BELOW THIS LINE
#create the event loop for the interface
mainloop()

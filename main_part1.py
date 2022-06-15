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

#common interface objects
#application title
mainHeading = Label(window, text="Bruno+", font=fontHeading).grid(row=0, column=0)

###create menu page
#frame - container for the interface elements
menuFrame = Frame(window).grid(row=1,column=0)
##menu buttons
menuAddDogDetails = Button(menuFrame, text="Add Dog").grid(row=1,column=0)
menuEditDogDetails = Button(menuFrame, text="Edit Dog").grid(row=1, column=1)


##############################################################
#DO NOT CODE BELOW THIS LINE
#create the event loop for the interface
mainloop()

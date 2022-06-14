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



###create menu page
#frame - container for the interface elements
menuFrame = Frame().pack()
#heading
menuLabelHeading = Label(menuFrame, text="Bruno+", font=fontHeading).pack()






##############################################################
#DO NOT CODE BELOW THIS LINE
#create the event loop for the interface
mainloop()

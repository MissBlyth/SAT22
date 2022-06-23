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
Show the menu screen
'''
def GoViewDog():
    ClearScreen()
    viewDogFrame.grid(row=1)
    print("show dog details")
    buttonGoMenu.grid()

    #get the details from the file
    dogFile=open("dog_data.txt", "r")

    #add the details to the label
    dogTKDetails.set(dogFile.read())

    #close the dog file
    dogFile.close()

'''
Show the add dog screen
'''
def GoAddDog():
    ClearScreen()
    addDogFrame.grid(row=1)
    buttonGoMenu.grid()
    #display defaults
    dogTKName.set("")
    dogTKGender.set("Unknown")
    dogTKBreed.set("Unknown")
    print("go to add dog page")

'''
Clear screen function - this function removes every frame so that the interface becomes blank. Except for permanently displayed things like the app header/logo.
'''
def ClearScreen():
    menuFrame.grid_remove()
    addDogFrame.grid_remove()
    buttonGoMenu.grid_remove()
    viewDogFrame.grid_remove()
    print("clear all interface elements ")

'''
Save dog function
'''
def SaveDog():
    print("Saving dog")
    print(dogTKName.get())
    print(dogTKGender.get())
    print(dogTKBreed.get())

    #open the dog file for writing - deletes existing file contents
    dogFile=open("dog_data.txt", "w")

    dogFile.write(dogTKName.get() + "\n")
    dogFile.write(dogTKGender.get() + "\n")
    dogFile.write(dogTKBreed.get() + "\n")

    #close the dog file
    dogFile.close()

    GoMenu()


'''
Edit dog details functon
'''
def EditDog():
    #load the add dog screen
    ClearScreen()
    addDogFrame.grid(row=1)
    buttonGoMenu.grid()

    #get the details from the file
    dogFile=open("dog_data.txt", "r")

    #display them in the interface
    dogTKName.set(dogFile.readline().strip("\n"))
    dogTKGender.set(dogFile.readline().strip("\n"))
    dogTKBreed.set(dogFile.readline().strip("\n"))

    #close the dog file
    dogFile.close()


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
menuViewDogDetails = Button(menuFrame, text="View Dog", command=GoViewDog).grid(row=1,column=1)
menuEditDogDetails = Button(menuFrame, text="Edit Dog", command=EditDog).grid(row=1, column=2)

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
inputDogName = Entry(addDogFrame, textvariable=dogTKName)
inputDogName.grid(row=1, column=1)

#gender
dogTKGender = StringVar()
dogTKGender.set("Unknown")
Radiobutton(addDogFrame, text="Male", variable=dogTKGender, value="Male").grid(row=2, column=0)
Radiobutton(addDogFrame, text="Female", variable=dogTKGender, value="Female").grid(row=2, column=1)
Radiobutton(addDogFrame, text="Unknown", variable=dogTKGender, value="Unknown").grid(row=2, column=2)

#dropdown
##add a drop down box
#create the label
Label(addDogFrame, text="Breed:").grid(row=3, column=0)
#items in the drop down
dogBreeds=["Unknown", "Shih Tzu", "Maltese", "German Shepherd"] #items for dropdown
#container for dropdown selection
dogTKBreed = StringVar()
dogTKBreed.set("Unknown")
breedDropDown=OptionMenu(addDogFrame, dogTKBreed, *dogBreeds)
breedDropDown.grid(row=3, column=1) #pack into frame

#save button
Button(addDogFrame, text="Save", command=SaveDog).grid(row=4, column=2)

####  view Dog detaiks screen
#frame - container for the interface elements
viewDogFrame = Frame()
viewDogFrame.grid()
##heading label
Label(viewDogFrame, text="Your Dog Details").grid(row=1)
#Dog detail label
dogTKDetails = StringVar()
Label(viewDogFrame, width=25, height=5, textvariable=dogTKDetails).grid(row=2)



GoMenu()

##############################################################
#DO NOT CODE BELOW THIS LINE
#create the event loop for the interface
mainloop()

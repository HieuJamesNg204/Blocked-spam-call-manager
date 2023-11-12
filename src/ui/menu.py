# This is the main menu of the call blocking manager application

from tkinter import *

from ui.infoForm import *
from ui.fontConfig import *
from ui.checkNumber import *
from ui.updateForm import *

def startApplication():
    window = Tk()
    window.title("Spam call manager")
    window.geometry("700x250")

    # Create a label
    label = Label(window, text="Select one of buttons below to manage spam numbers", font=titleLabel)
    label.pack(side="top", pady=50)

    frame = Frame(window)
    frame.pack(expand=True, pady=0)

    def createInfoForm(mainWindow):
        infoForm(mainWindow)

    def createDisplay(mainWindow):
        infoDisplay(mainWindow)

    def createUpdateForm(mainWindow):
        updateForm(mainWindow)

    # Create three buttons
    addNumberButton = Button(frame, text="Add a number", font=textLabel, command=lambda: createInfoForm(window))
    checkNumberButton = Button(frame, text="Check number", font=textLabel, command=lambda: createDisplay(window))
    updateNumberButton = Button(frame, text="Update number", font=textLabel, command=lambda: createUpdateForm(window))

    addNumberButton.pack(side="left", padx=20)
    checkNumberButton.pack(side="left", padx=20)
    updateNumberButton.pack(side="left", padx=20)

    window.mainloop()
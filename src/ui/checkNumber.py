# This module creates a UI window to manage all blocked number, this allows searching for a certain number.

from app.spam_number import *
from app.database_library import *
from ui.fontConfig import *

from tkinter import *
from tkinter import messagebox

def infoDisplay(mainWindow):
    form = Toplevel(mainWindow)
    form.title("Spam list")

    blockedNumberFrame = LabelFrame(form, text="Blocked Numbers", font=textLabel)
    blockedNumberFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    blockedNumberListbox = Listbox(blockedNumberFrame, font=textLabel)
    blockedNumberListbox.pack(fill="both", expand=True)

    def clearList():
        blockedNumberListbox.delete(0, END)

    def listAllNumbers():
        clearList()
        for instance in listAll():
            blockedNumberListbox.insert("end", instance)
    
    def listAllNumbersByDate():
        dateInput = promptDateEntry.get()
        if dateInput:
            clearList()
            for instance in listByDate(dateInput):
                blockedNumberListbox.insert("end", instance)
        else:
            listAllNumbers()

    def displayInfo():
        numberId = searchEntry.get()
        if numberId.isdigit():
            try:
                number = SpamNumber(int(numberId))
                info = f"\n - Block date: {number.getBlockDate()} \n - Address: {number.getAddress()}"
                
                numberLabel.configure(text="Number: "+number.getNumber())
                infoLabel.configure(text="Info:"+info)
            except IndexError:
                messagebox.showerror("Error", f"Phone number with ID {numberId} could not be found")
        else:
            messagebox.showerror("Error", f"Phone number ID is not valid")

    searchLabel = Label(form, text="Search for a number with id:", font=textLabel)
    searchLabel.grid(row=1, column=0, padx=10, pady=(0, 5))

    searchEntry = Entry(form, font=textLabel)
    searchEntry.grid(row=2, column=0, padx=10, pady=(0, 10))

    searchButton = Button(form, text="Search", font=textLabel, command=displayInfo)
    searchButton.grid(row=3, column=0, padx=10, pady=(0, 10))

    promptDateLabel = Label(form, text="Enter date to list numbers (yyyy-mm-dd):", font=textLabel)
    promptDateLabel.grid(row=1, column=1, padx=10, pady=(0, 5))

    promptDateEntry = Entry(form, font=textLabel)
    promptDateEntry.grid(row=2, column=1, padx=10, pady=(0, 10))

    listAllButton = Button(form, text="List All", font=textLabel, command=listAllNumbersByDate)
    listAllButton.grid(row=3, column=1, padx=10, pady=(0, 10))

    numberInfoFrame = LabelFrame(form, text="Number Information", font=textLabel)
    numberInfoFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    numberLabel = Label(numberInfoFrame, text="Number:", font=textLabel)
    numberLabel.grid(row=0, column=0, padx=10, pady=5)

    infoLabel = Label(numberInfoFrame, text="Info:", font=textLabel)
    infoLabel.grid(row=1, column=0, padx=10, pady=5)
# This module creates a form to fill in new information to update an existing number

from app.spam_number import SpamNumber
from ui.fontConfig import *
from tkinter import *
from tkinter import messagebox

def updateForm(mainWindow):
    form = Toplevel(mainWindow)
    form.title("Update spam number")
    form.geometry("550x250")

    frame = Frame(form)
    frame.pack(expand=True)

    def updateProcess():
        numberId_str = idEntry.get()
        if not numberId_str:
            messagebox.showerror("Error", f"Please fill in the compulsory field: ID")
        else:
            numberId = int(numberId_str)
            try:
                number = SpamNumber(numberId)

                newNumber = newNumberEntry.get()
                newBlockDate = newDateEntry.get()
                newAddress = newAddressEntry.get()

                if not newNumber and not newBlockDate and not newAddress:
                    messagebox.showerror("Error", f"Please enter at least one field to update!")
                else:
                    if newNumber:
                        number.setNumber(newNumber)
                    if newBlockDate:
                        number.setBlockDate(newBlockDate)
                    if newAddress:
                        number.setAddress(newAddress)
                    
                    messagebox.showinfo("Success", "Number information has been updated!")
                    form.destroy()
            except Exception:
                messagebox.showerror("Error", f"Number with ID {numberId} could not be found")

    # Prompt the id
    idLabel = Label(frame, text="id:", font=textLabel)
    idLabel.grid(row=0, column=0)
    idEntry = Entry(frame, font=textLabel)
    idEntry.grid(row=0, column=1)

    # Prompt the new number
    newNumberLabel = Label(frame, text="Number:", font=textLabel)
    newNumberLabel.grid(row=1, column=0)
    newNumberEntry = Entry(frame, font=textLabel)
    newNumberEntry.grid(row=1, column=1)

    # Prompt the new call date
    newDateLabel = Label(frame, text="Block date (yyyy-mm-dd):", font=textLabel)
    newDateLabel.grid(row=2, column=0)
    newDateEntry = Entry(frame, font=textLabel)
    newDateEntry.grid(row=2, column=1)

    # Prompt the new address
    newAddressLabel = Label(frame, text="Address:", font=textLabel)
    newAddressLabel.grid(row=3, column=0)
    newAddressEntry = Entry(frame, font=textLabel)
    newAddressEntry.grid(row=3, column=1)
    
    # Update button
    updateButton = Button(frame, text="Update", font=textLabel, command=updateProcess)
    updateButton.grid(row=4, columnspan=2)
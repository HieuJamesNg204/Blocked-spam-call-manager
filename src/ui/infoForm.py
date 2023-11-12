# This module creates a form to fill in information of new spam number that is blocked.

from app.pgUtil import DatabaseUtil as dbutil
from ui.fontConfig import *
from tkinter import *
from tkinter import messagebox

def infoForm(mainWindow):
    def submitProcess():
        number = numberEntry.get()
        blockDate = dateEntry.get()
        address = addressEntry.get()

        db = dbutil()

        if not number or not blockDate or not address:
            messagebox.showerror("Error", "Please fill in all the fields.")
        else:
            db.addNumber(number, blockDate, address)
            messagebox.showinfo("Success", "The number has been added to spam list")
            form.destroy()

    form = Toplevel(mainWindow)
    form.title("Add new number")
    form.geometry("550x250")

    frame = Frame(form)
    frame.pack(expand=True)

    # Prompt phone number to add to spam list
    numberLabel = Label(frame, text="Phone number:", font=textLabel)
    numberLabel.grid(row=0, column=0)
    numberEntry = Entry(frame, font=textLabel)
    numberEntry.grid(row=0, column=1)

    # Prompt call date
    dateLabel = Label(frame, text="Block date (yyyy-mm-dd):", font=textLabel)
    dateLabel.grid(row=1, column=0)
    dateEntry = Entry(frame, font=textLabel)
    dateEntry.grid(row=1, column=1)

    # Prompt number of addresss from which the spam number has called
    addressLabel = Label(frame, text="Address:", font=textLabel)
    addressLabel.grid(row=2, column=0)
    addressEntry = Entry(frame, font=textLabel)
    addressEntry.grid(row=2, column=1)

    # Submit button
    submitButton = Button(frame, text="Submit", command=submitProcess, font=textLabel)
    submitButton.grid(row=3, columnspan=2)
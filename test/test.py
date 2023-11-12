import tkinter as tk

def clear_listbox():
    listbox.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Listbox Example")

# Create a Listbox and add some items
listbox = tk.Listbox(window)
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Create a Clear button
clear_button = tk.Button(window, text="Clear", command=clear_listbox)

# Pack the Listbox and Clear button into the window
listbox.pack(pady=10)
clear_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
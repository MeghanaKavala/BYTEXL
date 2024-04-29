import tkinter as tk

def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        status_label.config(text=f"Selected Item: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox widget
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.insert(4, "Item 4")
listbox.insert(5,"II-CSE")

# Bind the on_select function to the Listbox selection event
listbox.bind("<<ListboxSelect>>", on_select)

# Create a label to display the selected item
status_label = tk.Label(root, text="Selected Item: None")

# Pack the widgets into the window
listbox.pack(pady=10)
status_label.pack(pady=10)

# Start the main loop
root.mainloop()
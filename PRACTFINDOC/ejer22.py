from tkinter import *

# Define a function to add a person to the listbox
def add_person():
    # Get the name, surname and age from the entries
    name = name_entry.get()
    surname = surname_entry.get()
    age = age_entry.get()
    # Check if they are not empty
    if name and surname and age:
        # Create a string with the person's information
        person = f"{name} {surname} ({age})"
        # Insert it at the end of the listbox
        listbox.insert(END, person)
        # Clear the entries
        name_entry.delete(0, END)
        surname_entry.delete(0, END)
        age_entry.delete(0, END)

# Define a function to delete a person from the listbox
def delete_person():
    # Get the index of the selected item
    index = listbox.curselection()
    # Check if there is an item selected
    if index:
        # Delete it from the listbox
        listbox.delete(index)

# Define a function to show the details of a person
def show_details(event):
    # Get the index of the selected item
    index = listbox.curselection()
    # Check if there is an item selected
    if index:
        # Get the item text
        person = listbox.get(index)
        # Split it by spaces and parentheses
        name, surname, age = person.split(" ")
        age = age.strip("()")
        # Display the details in a label below the listbox
        details_label.config(text=f"Name: {name}\nSurname: {surname}\nAge: {age}")

# Create a root window
root = Tk()
# Set the title and size
root.title("Add people")
root.geometry("300x400")

# Create a frame for the entries and labels
entry_frame = Frame(root)
entry_frame.pack()

# Create a label and entry for name
name_label = Label(entry_frame, text="Name:")
name_label.grid(row=0, column=0)
name_entry = Entry(entry_frame)
name_entry.grid(row=0, column=1)

# Create a label and entry for surname
surname_label = Label(entry_frame, text="Surname:")
surname_label.grid(row=1, column=0)
surname_entry = Entry(entry_frame)
surname_entry.grid(row=1, column=1)

# Create a label and entry for age
age_label = Label(entry_frame, text="Age:")
age_label.grid(row=2, column=0)
age_entry = Entry(entry_frame)
age_entry.grid(row=2, column=1)

# Create a frame for the buttons
button_frame = Frame(root)
button_frame.pack()

# Create an add button that calls the add_person function
add_button = Button(button_frame, text="Add", command=add_person)
add_button.grid(row=0, column=0)

# Create a delete button that calls the delete_person function
delete_button = Button(button_frame, text="Delete", command=delete_person)
delete_button.grid(row=0, column=1)

# Create a listbox to display the added people
listbox = Listbox(root)
listbox.pack()

# Bind a double-click event to the listbox that calls the show_details function
listbox.bind("<Double-Button-1>", show_details)

# Create a label to display the details of a person
details_label = Label(root, text="")
details_label.pack()

# Start the main loop of the window
root.mainloop()
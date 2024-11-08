import tkinter as tk
from tkinter import messagebox

# Initialize main application window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.config(bg="#f0f0f0")

# Task list to store tasks
tasks = []

# Function to update the task display
def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove a selected task
def remove_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Create the interface elements
frame = tk.Frame(root)
frame.pack(pady=10)

# Entry field for task input
task_entry = tk.Entry(frame, width=30, font=("Arial", 14))
task_entry.pack(side=tk.LEFT, padx=10)

# Add task button
add_button = tk.Button(frame, text="Add Task", command=add_task, font=("Arial", 12), bg="#4CAF50", fg="white")
add_button.pack(side=tk.LEFT)

# Listbox for displaying tasks
listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=20)

# Remove task button
remove_button = tk.Button(root, text="Remove Selected Task", command=remove_task, font=("Arial", 12), bg="#ff4c4c", fg="white")
remove_button.pack()

# Run the application
root.mainloop()

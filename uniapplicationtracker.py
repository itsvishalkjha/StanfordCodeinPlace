import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar  
import random

class UniversityAppTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Vishal's Application Tracker")
        self.root.geometry("800x600")

        self.applications = []
        self.populate_data()

        self.create_widgets()

    def populate_data(self):
        universities = ["Harvard University", "Stanford University", "MIT", "Caltech", "Yale University", "Princeton University", "Columbia University", "University of Chicago"]
        statuses = ["Submitted", "Under Review", "Accepted", "Rejected"]

        for i in range(10):
            application = {
                "name": random.choice(universities),
                "deadline": f"{random.randint(1, 28)}/{random.randint(1, 12)}/2024",
                "status": random.choice(statuses)
            }
            self.applications.append(application)

    def create_widgets(self):
        self.heading_label = tk.Label(self.root, text="Vishal's Application Tracker", font=("Arial", 24, "bold"), fg="blue")
        self.heading_label.pack(pady=20)

        self.listbox = tk.Listbox(self.root, width=80, height=15, font=("Arial", 12))
        self.listbox.pack(padx=10, pady=10)

        for app in self.applications:
            self.listbox.insert(tk.END, app['name'])

        self.view_button = tk.Button(self.root, text="View Details", command=self.view_details, font=("Arial", 12), bg="green", fg="white")
        self.view_button.pack(padx=10, pady=5)

        self.calendar_label = tk.Label(self.root, text="Select a Deadline Date:", font=("Arial", 12))
        self.calendar_label.pack()

        self.calendar = Calendar(self.root, selectmode='day', date_pattern='dd/mm/yyyy', font=("Arial", 12))
        self.calendar.pack(padx=10, pady=5)

    def view_details(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            application = self.applications[index]
            messagebox.showinfo("Application Details", f"University Name: {application['name']}\nDeadline: {application['deadline']}\nStatus: {application['status']}")
        else:
            messagebox.showwarning("No Selection", "Please select a university to view details.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversityAppTracker(root)
    root.mainloop()

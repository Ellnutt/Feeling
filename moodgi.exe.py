import tkinter as tk
from tkinter import ttk
import datetime

# Define a dictionary to store mood data for each day of the week
moods = {}

# Define a list of mood options
mood_options = ['Happy', 'Sad', 'Sad', 'Scared', 'Excited', 'Nervous', 'Angry', 'Calm']

# Function to save the user's mood for the current day
def save_mood():
    mood = mood_var.get()
    current_day = datetime.datetime.now().strftime("%A")
    moods[current_day] = mood
    mood_dropdown.set("")  # Clear the selected mood in the dropdown
    update_display()


# Function to update the mood display
def update_display():
    display_text.config(state=tk.NORMAL)
    display_text.delete(1.0, tk.END)  # Clear the display
    display_text.insert(tk.END, "Here's how you've been feeling this week:\n\n")
    for day, mood in moods.items():
        display_text.insert(tk.END, f"{day}: {mood}\n")
    display_text.insert(tk.END, f"\nYour predominant feeling for the week is: {get_predominant_mood()}")
    display_text.config(state=tk.DISABLED)

# Function to find the predominant mood
def get_predominant_mood():
    if not moods:
        return "No data yet"
    
    mood_counts = {}
    for mood in moods.values():
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
    return max(mood_counts, key=mood_counts.get)

# Create the main application window
root = tk.Tk()
root.title("Mood Tracker")

# Create a mood selection label and dropdown menu
mood_label = ttk.Label(root, text=f"How do you feel on {datetime.datetime.now().strftime('%A')}?")
mood_label.pack()
mood_var = tk.StringVar()
mood_dropdown = ttk.Combobox(root, textvariable=mood_var, values=mood_options)
mood_dropdown.pack()

# Create a button to save the mood
save_button = ttk.Button(root, text="Save Mood", command=save_mood)
save_button.pack()

# Create a text display area for mood data
display_text = tk.Text(root, height=10, width=40, wrap=tk.WORD, state=tk.DISABLED)
display_text.pack()

# Update the display with existing mood data
update_display()

root.mainloop()

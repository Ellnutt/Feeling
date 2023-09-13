import datetime

# Define a dictionary to store mood data for each day of the week
moods = {}

# Define a list of mood options
mood_options = ['Happy', 'Sad', 'Excited', 'Angry', 'Calm']

# Get the current day of the week
current_day = datetime.datetime.now().strftime("%A")

# Prompt the user to enter their mood for the current day
while True:
    print(f"How do you feel on {current_day}? (Choose from {', '.join(mood_options)}): ")
    mood = input()

    # Validate user input
    if mood in mood_options:
        moods[current_day] = mood
        break
    else:
        print("Invalid mood. Please choose from the available options.")

# Display the results to the user
print("\nHere's how you've been feeling this week:")
for day, mood in moods.items():
    print(f"{day}: {mood}")

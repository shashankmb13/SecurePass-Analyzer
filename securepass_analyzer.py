import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to measure password strength
def measure_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    strength_score = 0

    # Scoring the password
    if length >= 12:
        strength_score += 2
    elif length >= 8:
        strength_score += 1

    if has_upper:
        strength_score += 1
    if has_lower:
        strength_score += 1
    if has_digit:
        strength_score += 1
    if has_special:
        strength_score += 1

    # Determine password strength based on score
    if strength_score >= 5:
        return "Strong"
    elif strength_score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Function to estimate the time to crack the password
def estimate_time_to_crack(password):
    length = len(password)

    # Determine character pool size
    character_pool = 0
    if any(c.islower() for c in password):
        character_pool += 26  # Lowercase letters
    if any(c.isupper() for c in password):
        character_pool += 26  # Uppercase letters
    if any(c.isdigit() for c in password):
        character_pool += 10  # Digits
    if any(c in string.punctuation for c in password):
        character_pool += len(string.punctuation)  # Special characters

    # Total combinations
    total_combinations = character_pool ** length

    # Assuming 1 billion attempts per second (10^9 attempts/second)
    attempts_per_second = 1_000_000_000

    # Calculate time in seconds
    seconds_to_crack = total_combinations / attempts_per_second

    # Convert seconds to hours, days, or years
    minutes = seconds_to_crack / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if years > 1:
        return f"{years:.2f} years"
    elif days > 1:
        return f"{days:.2f} days"
    elif hours > 1:
        return f"{hours:.2f} hours"
    else:
        return f"{seconds_to_crack:.2f} seconds"

# Function to generate the password, measure strength, and estimate cracking time
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8 or length > 16:
            raise ValueError("Length must be between 8 and 16 characters")

        include_upper = upper_var.get()
        include_numbers = numbers_var.get()
        include_special = special_var.get()

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase if include_upper else ''
        numbers = string.digits if include_numbers else ''
        special = string.punctuation if include_special else ''

        all_characters = lower + upper + numbers + special

        if not all_characters:
            raise ValueError("At least one character type must be selected")

        password = ''.join(random.choice(all_characters) for _ in range(length))
        password_entry.delete(0, tk.END)  # Clear previous password
        password_entry.insert(0, password)  # Insert new password

        # Measure and display the strength of the password
        strength = measure_strength(password)
        strength_label.config(text=f"Password Strength: {strength}")

        # Estimate and display time to crack the password
        time_to_crack = estimate_time_to_crack(password)
        crack_time_label.config(text=f"Time to Crack: {time_to_crack}")

    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

# Creating the GUI
root = tk.Tk()
root.title("Password Generator")

# Password length label and entry
length_label = tk.Label(root, text="Enter password length (8-16):")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkbox options
upper_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
special_var = tk.BooleanVar()

upper_check = tk.Checkbutton(root, text="Include Uppercase", variable=upper_var)
upper_check.pack()
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_check.pack()
special_check = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Entry box to show the result (generated password)
password_label = tk.Label(root, text="Generated Password:")
password_label.pack()
password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Label to show the password strength
strength_label = tk.Label(root, text="Password Strength: ")
strength_label.pack()

# Label to show the estimated time to crack the password
crack_time_label = tk.Label(root, text="Time to Crack: ")
crack_time_label.pack()

# Run the GUI loop
root.mainloop()
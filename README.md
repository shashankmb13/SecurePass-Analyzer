# SecurePass-Analyzer
SecurePass Analyzer is a Python GUI tool that creates secure passwords &amp; checks their strength. Users can choose to include uppercase letters, numbers &amp; special characters. It estimates how long it would take to crack  password with brute-force attack. Built with tkinter, this helps users generate strong passwords &amp; learn about password security.

# 🔐 SecurePass Analyzer

A simple yet powerful Python-based GUI application to generate secure passwords, evaluate their strength, and estimate how long they would take to crack using brute-force methods.

## 💡 Features

- Generate passwords of custom length (8–16 characters)
- Choose to include:
  - Uppercase letters
  - Numbers
  - Special characters
- Instantly see:
  - Password strength (Weak / Moderate / Strong)
  - Estimated time to crack the password
- Easy-to-use graphical interface using `tkinter`

## 🛠️ Tech Stack

- Python 3.x
- tkinter (for GUI)
- string (for character set handling)
- random (for password generation)

## 📦 Installation

1. Make sure you have Python installed (version 3.6 or above recommended).
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/SecurePass-Analyzer.git
   cd SecurePass-Analyzer


Run the application:

*python securepass_analyzer.py*

🚀 How It Works
Enter desired password length (between 8 and 16 characters).

Select the character types to include (uppercase, numbers, special characters).

Click "Generate Password".

The application:

Displays a randomly generated password.

Evaluates and shows its strength.

Calculates and displays the estimated time to crack it based on character complexity.

🔐 Password Strength Evaluation
The strength score is based on:

Length of the password

Presence of:

Uppercase letters

Lowercase letters

Numbers

Special characters

🧮 Time to Crack Estimation
Estimation is done assuming a brute-force attack with:

1 billion guesses per second

Character pool based on selected options

📋 License
This project is open-source and available under the MIT License.

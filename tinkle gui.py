import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk  # Import from Pillow to handle images

# Function to determine the winner
def determine_winner(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Function to handle user selection
def user_choice(choice):
    determine_winner(choice)

# Set up the main application window
abc = tk.Tk()
abc.title("Rock-Paper-Scissors Game")
abc.geometry("500x400")  # Set window size
abc.attributes('-fullscreen', True)

# Load background image (Ensure the path is correct)
bg_image = Image.open(r"C:\Users\hp\OneDrive\Pictures\my photos\YUTUBE.jpg")  # Replace with your image path
bg_image = bg_image.resize((120, 160), Image.LANCZOS)  # Resize to fit window
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to hold the background image
canvas = tk.Canvas(abc, width=500, height=400)
canvas.pack(fill="both", expand=True)

# Set the background image on the canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")  # Changed to "nw"

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(abc, text="Rock", command=lambda: user_choice("Rock"), width=20, height=2)
paper_button = tk.Button(abc, text="Paper", command=lambda: user_choice("Paper"), width=20, height=2)
scissors_button = tk.Button(abc, text="Scissors", command=lambda: user_choice("Scissors"), width=20, height=2)

# Place buttons on the canvas
canvas.create_window(250, 100, window=rock_button)  # Adjust button positions
canvas.create_window(250, 170, window=paper_button)
canvas.create_window(250, 240, window=scissors_button)

# Run the application
abc.mainloop()

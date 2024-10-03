import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

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

def user_choice(choice):
    determine_winner(choice)

# Set up the main application window
abc = tk.Tk()
abc.title("Rock-Paper-Scissors Game")

# Set the window to full-screen
abc.attributes('-fullscreen', True)

# Load and resize background image
try:
    bg_image = Image.open(r"C:\Users\hp\OneDrive\Pictures\my photos\YUTUBE.jpg")  # Use a landscape image
except FileNotFoundError:
    messagebox.showerror("Error", "Background image not found!")
    abc.quit()

# Resize the image to fit the full screen
screen_width = abc.winfo_screenwidth()
screen_height = abc.winfo_screenheight()
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to hold the background image
canvas = tk.Canvas(abc, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(abc, text="Rock", command=lambda: user_choice("Rock"), width=20, height=2)
paper_button = tk.Button(abc, text="Paper", command=lambda: user_choice("Paper"), width=20, height=2)
scissors_button = tk.Button(abc, text="Scissors", command=lambda: user_choice("Scissors"), width=20, height=2)

# Place buttons on the canvas
canvas.create_window(screen_width // 2, 150, window=rock_button)
canvas.create_window(screen_width // 2, 220, window=paper_button)
canvas.create_window(screen_width // 2, 290, window=scissors_button)

# Run the application
abc.mainloop()

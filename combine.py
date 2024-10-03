import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import random
import pygame  # For Media Player
# You would use `requests` for Weather App, but we’ll mock this for now


# Calculator Function
def open_calculator():
    def calculate():
        try:
            result = eval(entry.get())
            result_label.config(text="Result: " + str(result))
        except Exception as e:
            result_label.config(text="Error")

    calc_window = tk.Toplevel(root)
    calc_window.title("Calculator")

    entry = tk.Entry(calc_window)
    entry.pack()

    result_label = tk.Label(calc_window, text="Result:")
    result_label.pack()

    calc_button = tk.Button(calc_window, text="Calculate", command=calculate)
    calc_button.pack()


# Text Editor Function
def open_text_editor():
    editor_window = tk.Toplevel(root)
    editor_window.title("Text Editor")

    text_area = scrolledtext.ScrolledText(editor_window, width=40, height=10)
    text_area.pack()

    def save_file():
        file_content = text_area.get("1.0", tk.END)
        with open("text_editor_output.txt", "w") as file:
            file.write(file_content)
        messagebox.showinfo("File Saved", "Your file has been saved successfully!")

    save_button = tk.Button(editor_window, text="Save", command=save_file)
    save_button.pack()


# Tic-Tac-Toe Function
def open_tic_tac_toe():
    game_window = tk.Toplevel(root)
    game_window.title("Tic-Tac-Toe")

    buttons = []
    current_player = "X"

    def check_winner():
        for i in range(3):
            if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
                return True
            if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
                return True
        if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            return True
        if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            return True
        return False

    def on_click(r, c):
        nonlocal current_player
        if buttons[r][c]["text"] == "" and not check_winner():
            buttons[r][c]["text"] = current_player
            if check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            current_player = "O" if current_player == "X" else "X"

    for row in range(3):
        button_row = []
        for col in range(3):
            button = tk.Button(game_window, text="", width=10, height=3,
                               command=lambda r=row, c=col: on_click(r, c))
            button.grid(row=row, column=col)
            button_row.append(button)
        buttons.append(button_row)


# Weather App Function
def open_weather_app():
    weather_window = tk.Toplevel(root)
    weather_window.title("Weather App")

    label = tk.Label(weather_window, text="Enter City:")
    label.pack()

    city_entry = tk.Entry(weather_window)
    city_entry.pack()

    result_label = tk.Label(weather_window, text="")
    result_label.pack()

    def fetch_weather():
        city = city_entry.get()
        # Here, you would fetch weather using an API like OpenWeatherMap
        # Mock-up weather info
        weather_info = f"Weather in {city}: 25°C, Sunny"
        result_label.config(text=weather_info)

    fetch_button = tk.Button(weather_window, text="Get Weather", command=fetch_weather)
    fetch_button.pack()


# Password Generator Function
def open_password_generator():
    pw_window = tk.Toplevel(root)
    pw_window.title("Password Generator")

    label = tk.Label(pw_window, text="Enter Password Length:")
    label.pack()

    length_entry = tk.Entry(pw_window)
    length_entry.pack()

    result_label = tk.Label(pw_window, text="")
    result_label.pack()

    def generate_password():
        length = int(length_entry.get())
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        password = "".join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password)

    generate_button = tk.Button(pw_window, text="Generate Password", command=generate_password)
    generate_button.pack()


# Media Player Function
def open_media_player():
    player_window = tk.Toplevel(root)
    player_window.title("Media Player")

    pygame.mixer.init()  # Initialize the mixer

    def load_file():
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            status_label.config(text="Playing: " + file_path.split("/")[-1])

    def stop_music():
        pygame.mixer.music.stop()
        status_label.config(text="Music Stopped")

    status_label = tk.Label(player_window, text="No music loaded")
    status_label.pack()

    load_button = tk.Button(player_window, text="Load Music", command=load_file)
    load_button.pack()

    stop_button = tk.Button(player_window, text="Stop Music", command=stop_music)
    stop_button.pack()


# Main Menu
def main_menu():
    global root
    root = tk.Tk()
    root.title("Multi-Tool Application")

    main_frame = tk.Frame(root)
    main_frame.pack()

    # Buttons for different tools
    calc_button = tk.Button(main_frame, text="Open Calculator", command=open_calculator)
    calc_button.pack(pady=10)

    editor_button = tk.Button(main_frame, text="Open Text Editor", command=open_text_editor)
    editor_button.pack(pady=10)

    tic_tac_toe_button = tk.Button(main_frame, text="Open Tic-Tac-Toe", command=open_tic_tac_toe)
    tic_tac_toe_button.pack(pady=10)

    weather_button = tk.Button(main_frame, text="Open Weather App", command=open_weather_app)
    weather_button.pack(pady=10)

    password_button = tk.Button(main_frame, text="Open Password Generator", command=open_password_generator)
    password_button.pack(pady=10)

    media_button = tk.Button(main_frame, text="Open Media Player", command=open_media_player)
    media_button.pack(pady=10)

    root.mainloop()


# Run the main menu
if __name__ == "__main__":
    main_menu()

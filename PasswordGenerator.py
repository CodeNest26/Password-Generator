import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get().strip())
        if length <= 0:
            result_label.config(text="Length should be a positive integer.")
            return
        password = generate_password(length)
        result_label.config(text="Generated password: " + password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid integer for the length.")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Set window size
window_width = 500
window_height = 150
root.geometry(f"{window_width}x{window_height}")

# Set background color
root.config(bg="#f0f0f0")

# Create input field for password length
length_label = tk.Label(root, text="Enter the length of the password:", bg="#f0f0f0", fg="#333333")
length_label.pack()
length_entry = tk.Entry(root, width=50, bg="#ffffff", fg="#333333")
length_entry.pack()

# Create button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password, bg="#4caf50", fg="#ffffff")
generate_button.pack()

# Create label to display generated password
result_label = tk.Label(root, text="", bg="#f0f0f0", fg="#333333")
result_label.pack()

# Start GUI event loop
root.mainloop()



import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        global img
        height = int(root.winfo_width() * 0.5) 
        width = int(root.winfo_width() * 0.8)

        img = Image.open(file_path)
        img = img.resize((width, height), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk, width=width, height=height)
        image_label.image = img_tk

def remove_image():
    image_label.config(image='')
    image_label.config(width=80, height=20)
    image_label.image = None

# Create the main application window
root = tk.Tk()
root.title("Image Viewer")
root.geometry("800x600")  # Set window size
root.configure(bg="#eeeeee")

# Create a label to display the image
image_label = tk.Label(root, width=80, height=20, bg="#f7f7f7", relief="solid")
image_label.pack(pady=50)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#eeeeee")
button_frame.pack(pady=20)

# Create Open button with blue color
open_button = tk.Button(button_frame, text="Open", command=open_image, bg="#2864ff", fg="white", font=("Helvetica", 12), borderwidth=0)
open_button.pack(side=tk.LEFT, padx=10)

# Create Remove button with dark grey color
remove_button = tk.Button(button_frame, text="Remove", command=remove_image, bg="#9b9b9b", fg="white", font=("Helvetica", 12), borderwidth=0)
remove_button.pack(side=tk.LEFT, padx=10)

# Start the main loop
root.mainloop()


import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        global img
        img = Image.open(file_path)
        img = img.resize((600, 400), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

def remove_image():
    image_label.config(image='')
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

# Configure ttk style to change button background
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), borderwidth=0)
style.map('Open.TButton',
          background=[('active', '#2864ff'), ('!disabled', '#2864ff')],
          foreground=[('active', 'white'), ('!disabled', 'white')])

style.map('Remove.TButton',
          background=[('active', '#9b9b9b'), ('!disabled', '#9b9b9b')],
          foreground=[('active', 'white'), ('!disabled', 'white')])

# Create Open button with blue color
open_button = ttk.Button(button_frame, text="Open", command=open_image, style='Open.TButton')
open_button.pack(side=tk.LEFT, padx=10)

# Create Remove button with dark grey color
remove_button = ttk.Button(button_frame, text="Remove", command=remove_image, style='Remove.TButton')
remove_button.pack(side=tk.LEFT, padx=10)

# Start the main loop
root.mainloop()

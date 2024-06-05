import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from io import BytesIO

# Function to fetch image from URL
def fetch_image(url):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    return img

# Function to handle menu item selection
def menu_callback(menu_item):
    print(f"Selected: {menu_item}")

# Function to toggle the visibility of menu items
def toggle_menu():
    global menu_items_frame
    if menu_items_frame.winfo_ismapped():  # Check if menu is already open
        menu_items_frame.pack_forget()  # Close the menu
    else:
        menu_items_frame.pack(side=tk.TOP)  # Open the menu

# Create the main window
root = tk.Tk()
root.title("mercedes Me")

# Set window size to match a common mobile screen resolution
window_width = 400
window_height = 640
root.geometry(f"{window_width}x{window_height}")

# Fetch the image from URL
img_url = "https://c4.wallpaperflare.com/wallpaper/931/875/651/car-mercedes-benz-mercedes-amg-mercedes-amg-gt-wallpaper-preview.jpg"
background_img = fetch_image(img_url)

# Resize the image to fit the window using LANCZOS resampling
background_img = background_img.resize((window_width, window_height), Image.LANCZOS)

# Convert image to Tkinter-compatible format
background_img_tk = ImageTk.PhotoImage(background_img)

# Create a label with the background image
background_label = tk.Label(root, image=background_img_tk)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the frame for the menu button
menu_button_frame = tk.Frame(root, bg='white')
menu_button_frame.pack(side=tk.TOP, anchor="nw")

# Create the themed button with the menu symbol
menu_button = ttk.Button(menu_button_frame, text="☰", command=toggle_menu, style='TButton', width=5)
menu_button.pack(side=tk.TOP)

# Create a frame for menu items
menu_items_frame = tk.Frame(menu_button_frame, bg='white')

# Create menu items
menu_items = ["Energie", "Service", "Maps", "Contact"]
for item in menu_items:
    ttk.Button(menu_items_frame, text=item, command=lambda i=item: menu_callback(i), 
              style='TButton', cursor="hand2", takefocus=False).pack(side=tk.TOP, fill=tk.X)

# Pack the menu items frame below the menu button
menu_items_frame.pack(side=tk.TOP)

# Center buttons horizontally and align vertically to the middle-left
button_frame = tk.Frame(root, bg=root['background'])
button_frame.place(relx=0, rely=0.5, anchor=tk.W)

# Create the first row of buttons
button_vehicle_status = ttk.Button(button_frame, text="⛽ Vehicle Status", command=lambda: menu_callback("⛽ Vehicle Status"), style='TButton')
button_vehicle_status.grid(row=0, column=0, padx=5)

button_lock_status = ttk.Button(button_frame, text="🔒 Lock Status", command=lambda: menu_callback("🔒 Lock Status"), style='TButton')
button_lock_status.grid(row=0, column=1, padx=5)

button_tire_pressure = ttk.Button(button_frame, text="🌡 Tire Pressure", command=lambda: menu_callback("🌡 Tire Pressure"), style='TButton')
button_tire_pressure.grid(row=0, column=2, padx=5)

# Create the second row of buttons
button_trip_data = ttk.Button(button_frame, text="📍 Trip Data", command=lambda: menu_callback("📍 Trip Data"), style='TButton')
button_trip_data.grid(row=1, column=0, padx=5, pady=10)

button_vehicle_search = ttk.Button(button_frame, text="⛐ Vehicle Search", command=lambda: menu_callback("⛐ Vehicle Search"), style='TButton')
button_vehicle_search.grid(row=1, column=1, padx=5, pady=10)

button_more = ttk.Button(button_frame, text="✜ More", command=lambda: menu_callback("✜ More"), style='TButton')
button_more.grid(row=1, column=2, padx=5, pady=10)

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from io import BytesIO
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def get_phone_info():
    mobileNo = entry.get()
    if is_valid_phone_number(mobileNo):
        mobileNo = phonenumbers.parse(mobileNo)
        region_info = ', '.join(timezone.time_zones_for_number(mobileNo))
        provider_info = carrier.name_for_number(mobileNo, "en")
        country_info = geocoder.description_for_number(mobileNo, "en")
        messagebox.showinfo("Phone Number Info", f"Phone Number belongs to region: {region_info}\n"
                                                  f"Service Provider: {provider_info}\n"
                                                  f"Phone number belongs to country: {country_info}")
    else:
        messagebox.showerror("Error", "Please enter a valid mobile number")

def is_valid_phone_number(phone_number):
    try:
        # Parse the input as a phone number
        parsed_number = phonenumbers.parse(phone_number)
        # Check if the parsed number is valid
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

# Create the main window
window = tk.Tk()
window.title("Phone Number Info")

# Set window size to 872x872 pixels
window.geometry("375x500")

# Load background image from URL
response = requests.get("https://img.freepik.com/photos-gratuite/telephone-contact-icone-signe-symbole-bouton-bulle-bleue-fond-blanc-rendu-3d_56104-1186.jpg?w=740&t=st=1707005533~exp=1707006133~hmac=7b1f2da039b114e2241d1862fd36240decba43a2cdb14dd5b10d2a68a184fa5c")
image_data = response.content
image = Image.open(BytesIO(image_data))
background_image = ImageTk.PhotoImage(image)

# Set window background to the loaded image
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create and place entry field with custom styling
entry = tk.Entry(window, font=('Helvetica', 14), bd=3, relief=tk.SOLID)
entry.pack(pady=10, padx=20, ipady=5, fill=tk.X)

# Create and place button with custom styling
button = tk.Button(window, text="Get Info", command=get_phone_info, font=('Helvetica', 14), bd=3, relief=tk.RAISED, bg='#0A71F4', fg='white', activebackground='#0A71F4')
button.pack(pady=5, padx=20, ipadx=10, ipady=5, fill=tk.X)

# Run the GUI
window.mainloop()

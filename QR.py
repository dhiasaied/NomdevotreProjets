import qrcode
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def generate_code():
    try:
        qr = qrcode.QRCode(version=int(size.get()), box_size=10, border=5)
        qr.add_data(text.get())
        qr.make(fit=True)
        img = qr.make_image()

        file_directory = filedialog.askdirectory()
        if not file_directory:
            return  # User canceled file dialog

        file_path = f'{file_directory}/{name.get()}.png'
        img.save(file_path)

        messagebox.showinfo("QR Code Generator", f"QR Code saved successfully at {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_entry_frame(parent_frame, label_text, row):
    frame = Frame(parent_frame, bg="SteelBlue3")
    frame.place(relx=0.1, rely=0.15 + row * 0.2, relwidth=0.7, relheight=0.2)

    label = Label(frame, text=label_text, bg="SteelBlue3", fg='azure', font=('Courier', 13, 'bold'))
    label.place(relx=0.05, rely=0.2, relheight=0.08)

    entry = Entry(frame, font=('Century 12'))
    entry.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

    return entry

wn = Tk()
wn.title('QR Code Generator')
wn.geometry('800x800')
wn.config(bg='SteelBlue3')

heading_frame = Frame(wn, bg="azure", bd=5)
heading_frame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
heading_label = Label(heading_frame, text="Generate QR Code", bg='azure', font=('Times', 20, 'bold'))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

text = create_entry_frame(wn, "Enter the text/URL: ", 0)
loc = create_entry_frame(wn, "Enter the name of the QR Code: ", 1)
name = create_entry_frame(wn, "Enter the location to save the QR Code: ", 2)
size = create_entry_frame(wn, "Enter the size from 1 to 40 with 1 being 21x21: ", 3)

button = Button(wn, text='Generate Code', font=('Courier', 15, 'normal'), command=generate_code)
button.place(relx=0.35, rely=0.9, relwidth=0.30, relheight=0.05)

wn.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

class LoanCalculator:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("Loan Calculator")  # Set title
        window.geometry("350x300")  # Set width and height

        # Load the background image from URL
        # Load the background image from URL
        url = "https://img.freepik.com/psd-gratuit/element-argent-realiste_23-2150396386.jpg?w=740&t=st=1706306926~exp=1706307526~hmac=62728d08aa201afe227ec018eaffcf771e96db46c45cfc298f0fc37248844c1d"
        response = requests.get(url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((350, 300), Image.LANCZOS)  # Resize the image to fit the window

        # Convert the image to Tkinter format
        tk_img = ImageTk.PhotoImage(img)

        # Create a label to display the background image
        background_label = Label(window, image=tk_img)
        background_label.image = tk_img  # Keep a reference to avoid garbage collection
        background_label.place(relwidth=1, relheight=1)

        # Set the window as not resizable
        window.resizable(width=False, height=False)

        # create the input boxes.
        Label(window, text="Annual Interest Rate").grid(row=1, column=1, sticky=W, padx=10, pady=5)
        Label(window, text="Number of Years").grid(row=2, column=1, sticky=W, padx=10, pady=5)
        Label(window, text="Loan Amount").grid(row=3, column=1, sticky=W, padx=10, pady=5)
        Label(window, text="Monthly Payment").grid(row=4, column=1, sticky=W, padx=10, pady=5)
        Label(window, text="Total Payment").grid(row=5, column=1, sticky=W, padx=10, pady=5)

        # for taking inputs
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2, padx=10, pady=5)
        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2, padx=10, pady=5)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2, padx=10, pady=5)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E, padx=10, pady=5)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E, padx=10, pady=5)

        # create the button
        btComputePayment = Button(window, text="Compute Payment", command=self.computePayment).grid(row=6, column=2, sticky=E, padx=10, pady=10)

        window.mainloop()  # Create an event loop

    # compute the total payment.
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment.
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

# call the class to run the program.
LoanCalculator()

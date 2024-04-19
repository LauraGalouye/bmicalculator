import string
from tkinter import *

def bmicalculator():
    print("Welcome to BMI Calculator")

    weight = float(entry_weight.get())
    height = float(entry_height.get())

    bmi = weight / ((height / 100) ** 2)

    result_label.config (text="Your BMI is: {:.2f}".format(bmi))

    if bmi < 18.5:
        bmi_category_label.config(text="You are underweight")

    elif 18.5<= bmi < 24.9:
        bmi_category_label.config(text="You are normal weight")
    elif 25<= bmi < 29.9:
        bmi_category_label.config(text="You are overweight")


fenetre = Tk()
fenetre.geometry("600x600")
fenetre.title("BMI Calculator")
fenetre.resizable(width=True, height=True)

label = Label(fenetre, text="Welcome to BMI Calculator", font=("Arial", 20))
label.pack()

label_weight = Label(fenetre, text="Enter your weight in kg: ")
label_weight.pack() 
entry_weight = Entry(fenetre)
entry_weight.pack()

label_height = Label(fenetre, text="Enter your height in cm: ")
label_height.pack()
entry_height = Entry(fenetre)
entry_height.pack()

label_result = Label(fenetre, text = "Your BMI is: ")
label_result.pack()

generate_button = Button(fenetre, text="Calcul", command=bmicalculator)
generate_button.pack()

result_label = Label(fenetre, text="")
result_label.pack()

bmi_category_label = Label(fenetre, text="")
bmi_category_label.pack()

fenetre.mainloop()
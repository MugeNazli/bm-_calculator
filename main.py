import tkinter
from tkinter import *

window =Tk()
window.minsize(height=500,width=500)
window.title("height and weight index")
window.config(padx=10,pady=10)
def click_button() :
    user_input = my_entry.get()
    user_input2 = my_entry2.get()
    if my_entry == "" or my_entry2 == "" :
        my_label.config(text = "enter both weight and height.")
    else :
        try :
            bmi = float(user_input)/((float(user_input2)/100)**2)
            result_string = write_result(bmi)
            my_label3.config(text=result_string)
        except:
            my_label3.config(text="Enter a valid number!")


my_label= tkinter.Label(text="please enter your weight")
my_label.config(fg="black",font=("Arial",15,"italic"))
my_label.pack()
my_label.config(padx=30,pady=30)


my_entry = tkinter.Entry()
my_entry.pack()




my_label2= tkinter.Label(text="please enter your height")
my_label2.config(fg="black",font=("Arial",15,"italic"))
my_label2.pack()
my_label2.config(padx=30,pady=30)

my_entry2 = tkinter.Entry()
my_entry2.pack()


my_button = tkinter.Button(text="entry",command = click_button)
my_button.pack()

my_label3= tkinter.Label(text="")
my_label3.config(fg="black",font=("Arial",15,"italic"))
my_label3.pack()
my_label3.config(padx=30,pady=30)

def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
            result_string += "severely thin!"
    elif 16 < bmi <= 17:
            result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
            result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
            result_string += "normal weight"
    elif 25 < bmi <= 30:
            result_string += "overweight"
    elif 30 < bmi <= 35:
            result_string += "obese class 1"
    elif 35 < bmi <= 40:
            result_string += "obese class 2"
    else:
            result_string += "obese class 3"
    return result_string



window.mainloop()
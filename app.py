import tkinter as tk
from tkinter import *
from tkinter import messagebox
from weather import weather2


def output_weather():
    city_id = int(input_city.get())
    conditions, temp, temp_min, temp_max, city_name = weather2(city_id)
    allinfo = f'city:{city_name} ,conditions:{conditions}, temp:{temp}, temp_mn:{temp_min}, temp_mx:{temp_max}'
    messagebox.showinfo('погода', allinfo)


window = Tk()
window.title('Weather')
window.geometry('900x500')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)
waeather_city = Label(
    frame,
    text='input city'
)
waeather_city.grid(row=3, column=1)

input_city = Entry(
    frame,
)
input_city.grid(row=3, column=2)


waeather_button = Button(
    frame,
    text='Узнать погоду',
    command=output_weather
)
waeather_button.grid(row=4, column=2)

window.mainloop()

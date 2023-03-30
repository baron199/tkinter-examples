from tkinter import *
from tkinter import messagebox


Window = Tk()  #Создаём окно приложения.
Window.title("Калькулятор индекса массы тела (ИМТ)")  #Добавляем название приложения.
Window.geometry("700x400")

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
 
    if bmi < 18.5:
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi < 24.9):
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi < 29.9):
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
       messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')  


frame = Frame(Window,  #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10,  #Задаём отступ по горизонтали.
   pady = 10  #Задаём отступ по вертикали.
)
frame.pack(expand=True)  #Не забываем позиционировать виджет в окне. Здесь используется метод pack. С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, созданный для него.
height_lb = Label(
   frame,
   text="Введите свой рост (в см)  ",
)
height_lb.grid(row=3, column=1)
 
weight_lb = Label(
   frame,
   text="Введите свой вес (в кг)  ",
)
weight_lb.grid(row=4, column=1)
 
height_tf = Entry(
   frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
   frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
   frame,
   text='Рассчитать ИМТ',
   command=calculate_bmi
)
cal_btn.grid(row=5, column=2)
Window.mainloop()
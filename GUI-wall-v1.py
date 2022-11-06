# GUI-wall-v1.py

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('โปรแกรมคำนวณ v.1')
GUI.geometry('1000x700')

FONT1 = ('Angsana New',20)
FONT2 = ('Angsana New',30,'bold')
# Frame 1

F1 = Frame(GUI,width=300)
F1.place(x=50,y=50)

#####WIDTH######

image = PhotoImage(file='wall.png').subsample(8) #.subsample ใช้ย่อกี่เท่า?

L0 = Label(F1,image=image)
L0.pack()


L1 = Label(F1,text='ความกว้างผนัง (ม.)',font=FONT1)
L1.pack()

v_width = StringVar()
E1 = ttk.Entry(F1, textvariable= v_width, font=FONT1)
E1.pack()

#####HIGHT######
L2 = Label(F1,text='ความสูงผนัง (ม.)',font=FONT1)
L2.pack()

v_height = StringVar()
E2 = ttk.Entry(F1, textvariable= v_height, font=FONT1)
E2.pack()

#####BUTTON######
total = 0

def Calculate():
    global total
    width = float(v_width.get())
    height = float(v_height.get())
    cal = width * height
    price = float(v_price.get()) * cal

    total = total + price
    
    text = 'ผนังกว้าง {:.1f} ม. x {:.1f} ม. ({:.2f} ตร.ม.) ราคา {:.2f} บาท'.format(width,height,cal,price)
    v_result.set(text)

    result2 = v_result2.get() + text + '\n'
    v_result2.set(result2)

    v_result3.set('รวมทั้งหมด: {:,.2f} บาท'.format(total))
    


B1 = ttk.Button(F1,text='คำนวณ',command=Calculate)
B1.pack(ipadx=30,ipady=20, pady=20)

v_result = StringVar()
v_result.set('--------------ผลลัพธ์---------------')
R1 = Label(F1,textvariable=v_result,font=FONT1)
R1.pack()

# Frame 2
F2 = Frame(GUI)
F2.place(x=550,y=50)

L3 = Label(F2,text='รวมค่าใช้จ่ายทั้งหมด',font=FONT2,fg='green')
L3.pack()

text = '--------รายการ---------\n'

v_result2 = StringVar()
v_result2.set(text)
R2 = Label(F2,textvariable=v_result2,font=FONT1)
R2.pack()

v_result3 = StringVar()
v_result3.set('รวมทั้งหมด: 0 บาท')
R3 = Label(F2,textvariable=v_result3,font=FONT2)
R3.pack()
# Frame 3
F3 = Frame(GUI)
F3.place(x=500,y=550)

L3 = Label(F3,text='ราคาต่อหน่วย (บาท/ตร.ม.)',font=FONT1)
L3.grid(row=0,column=0)

v_price = StringVar()
v_price.set('100')
E3 = ttk.Entry(F3, textvariable= v_price, font=FONT1, width=5)
E3.grid(row=0,column=1)

def Reset():
    global total
    total = 0
    v_result.set('--------------ผลลัพธ์---------------')
    text = '--------รายการ---------\n'
    v_result2.set(text)
    v_result3.set('รวมทั้งหมด: {:,.2f} บาท'.format(total))
    


FB = Frame(GUI)
FB.place(x=600,y=600)
B1 = ttk.Button(FB,text='reset')
B1.pack(ipadx=30,ipady=20, pady=20)

GUI.mainloop()

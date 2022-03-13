from guizero import App, Text, Combo, TextBox, Window, PushButton, CheckBox, Picture, Waffle
from io import BytesIO
from time import sleep


def fetch_response():
    user = submits.value
    if user == "4362":
        sleep(1)
        app.hide()
        sleep(1/10)
        module2.show()
def Keypad__1():
    submits.append('1')
def Keypad__2():
    submits.append('2')
def Keypad__3():
    submits.append('3')
def Keypad__4():
    submits.append('4')
def Keypad__5():
    submits.append('5')
def Keypad__6():
    submits.append('6')
def Keypad__7():
    submits.append('7')
def Keypad__8():
    submits.append('8')
def Keypad__9():
    submits.append('9')
def Keypad__0():
    submits.append('0')
def Clearapp():
    submits.clear()
def counter():
    text.value = int(text.value) - 1
def counter1():
    sequence.append('1')
    Sequence = Text(module2, text = sequence, size = 10, grid=[400, 250])
def counter2():
    sequence.append('2')
    Sequence = Text(module2, text = sequence, size = 10, grid=[400, 250])
def counter3():
    sequence.append('3')
    Sequence = Text(module2, text = sequence, size = 10, grid=[400, 250])
def counter4():
    sequence.append('4')
    Sequence = Text(module2, text = sequence, size = 10, grid=[400, 250])
def counter5():
    sequence.append('5')
    Sequence = Text(module2, text = sequence, size = 10, grid=[400, 250])
def counter6():
    sequence.append('6')
    Sequence = Text(module2, text = sequence, size = 10, grid=[400, 250])
def Clear():
    length = len(sequence)
    sequence.clear()
    Sequence = Text(module2, text = sequence, size = 10, grid=[400, 250])
    butt = ['0']*length
    Butt = Text(module2, text = butt, size = 10, grid=[400, 250])
def Define():
    Correct = '0'
def close_module2():
    if sequence == Msequence:
        sleep(1)
        module2.hide()
        module3.show()
def counter_2():
    timer_3.value = int(timer_3.value) - 1
def counter_1():
    timer.value = int(timer.value) - 1
def GreenCheck():
    Made = Text(module3, text="0", size = 20, font="Times New Roman", color="Green", grid = [550, 0])
    Correct.value = int(Correct.value) + 1
    if Correct.value == Correct1.value:
        module3.hide()
def YellowCheck():
    Made = Text(module3, text="0", size = 20, font="Times New Roman", color="Green", grid = [550, 80])
    Correct.value = int(Correct.value) + 1
    if Correct.value == Correct1.value:
        sleep(2)
        module3.hide()
def RedCheck():
    timer_3.value = int(timer_3.value) - 30
    MadeW = Text(module3, text="1", size = 20, font="Times New Roman", color="Green", grid = [550, 40])
def Clear_B():
    WireInput.clear()
app = App(title="Module 1", width=800, height=480, layout="grid")
text = Text(app, text="360", size=10, grid=[300, 280])
text.repeat(1000, counter)

module1_message = Text(app, text="What is the code?",  size=20, font="Times New Roman", color="black", grid = [400, 0])
submits = TextBox(app, grid=[400, 300])
submit = PushButton(app, fetch_response, text="Submit", grid=[410, 300])
Clear_app = PushButton(app, Clearapp, text="Clear", grid=[410, 325])

waffle = Waffle(app, grid=[0,0])


Keypad_1 = PushButton(app, Keypad__1, text="1", grid=[0, 400])
Keypad_1.width = 8
Keypad_1.height = 4
Keypad_2 = PushButton(app, Keypad__2, text="2", grid=[50, 400])
Keypad_2.width = 8
Keypad_2.height = 4
Keypad_3 = PushButton(app, Keypad__3, text="3", grid=[100, 400])
Keypad_3.width = 8
Keypad_3.height = 4
Keypad_4 = PushButton(app, Keypad__4, text="4", grid=[0, 450])
Keypad_4.width = 8
Keypad_4.height = 4
Keypad_5 = PushButton(app, Keypad__5, text="5", grid=[50, 450])
Keypad_5.width = 8
Keypad_5.height = 4
Keypad_6 = PushButton(app, Keypad__6, text="6", grid=[100, 450])
Keypad_6.width = 8
Keypad_6.height = 4
Keypad_7 = PushButton(app, Keypad__7, text="7", grid=[0, 500])
Keypad_7.width = 8
Keypad_7.height = 4
Keypad_8 = PushButton(app, Keypad__8, text="8", grid=[50, 500])
Keypad_8.width = 8
Keypad_8.height = 4
Keypad_9 = PushButton(app, Keypad__9, text="9", grid=[100, 500])
Keypad_9.width = 8
Keypad_9.height = 4
Keypad_0 = PushButton(app, Keypad__0, text="0", grid=[50, 550])
Keypad_0.width = 8
Keypad_0.height = 4

module2 = Window(app, "Module 2", width=800, height=480, layout="grid")
module2.hide()
module3 = Window(app, "Module 3", width=800, height=480, layout="grid")
module3.hide()
Correct = Text(module3, text="0", size = 1, font="Times New Roman", color="black", grid = [400, 480]) 

waffle_2 = Waffle(module2, grid=[300,0])
waffle_3 = Waffle(module3, grid=[600,0])
waffle_2.set_pixel(0, 0, "green")
waffle_3.set_pixel(0, 0, "blue")
waffle_2.set_pixel(2, 1, "black")
waffle_3.set_pixel(2, 0, "green")
#Module 2 coding
Msequence = ['2', '1', '5', '4', '3', '6']
sequence = []*6

timer = Text(module2, text= text.value, size=10, grid=[0, 0])
timer.repeat(1000, counter_1)
title2 = Text(module2, text="What is the sequence?", size=20, font="Times New Roman", color="black", grid=[200, 0])#Change for different versions
button1 = PushButton(module2, command=counter1, image="C:/Users/Bryan/Desktop/guizero/Weird1A.jpg", grid=[0,1])
button1.width = 80
button1.height = 80
button2 = PushButton(module2, command=counter2, image="C:/Users/Bryan/Desktop/guizero/Weird2A.png", grid=[1,1])
button2.width = 80
button2.height = 80
button3  = PushButton(module2, command=counter3, image="C:/Users/Bryan/Desktop/guizero/Weird3A.png", grid=[2,2])
button3.width = 80
button3.height = 80
button4  = PushButton(module2, command=counter4, image="C:/Users/Bryan/Desktop/guizero/Weird4A.jpg", grid=[0,2])
button4.width = 80
button4.height = 80
button5  = PushButton(module2, command=counter5, image="C:/Users/Bryan/Desktop/guizero/Weird5A.png", grid=[1,3])
button5.width = 80
button5.height = 80
button6  = PushButton(module2, command=counter6, image="C:/Users/Bryan/Desktop/guizero/Weird6A.jpg", grid=[2,3])
button6.width = 80
button6.height = 80
button7 = PushButton(module2, command=Clear, text= "Clear", grid=[200, 50])
submit_2 = PushButton(module2, command=close_module2, text="Submit", grid=[200, 30])

#Module 3 coding
timer_3 = Text(module3, text=text.value, size=10, grid=[0, 0])
timer_3.repeat(1000, counter_2)
GreenPic = PushButton(module3,command=GreenCheck, image="C:/Users/Bryan/Desktop/guizero/GreenWire.jpg", grid=[550, 0])
GreenPic.width = 150
GreenPic.height = 40
RedPic = PushButton(module3, command=RedCheck, image="C:/Users/Bryan/Desktop/guizero/RedWire.jpg", grid=[550, 40])
RedPic.width = 150
RedPic.height = 40

YellowPic = PushButton(module3, command=YellowCheck, image="C:/Users/Bryan/Desktop/guizero/YellowWire.jpg", grid=[550, 80])
YellowPic.width = 150
YellowPic.height = 40
Correct1 = Text(module3, text = "2", size = 1, font = "Times New Roman", grid=[500, 480])


app.display()

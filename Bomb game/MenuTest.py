from guizero import App, Text, Combo, TextBox, Window, PushButton, CheckBox, Picture 
from io import BytesIO
from time import sleep

def call1A():
    import Version1A
    app1.hide()
def call1B():
    import Version1B
    app1.hide()
def call1C():
    import Version1C
    app1.hide()
def call1D():
    import Version1D
    app1.hide()
def call1E():
    import Version1E
    app1.hide()
def call1F():
    import Version1F
    app1.hide()
def call1G():
    import Version1G
    app1.hide()
def call1H():
    import Version1H
    app1.hide()

app1 = App(title="Module 1", width=800, height=480, layout="grid")
Module1 = PushButton(app1, call1A, text="Play Version 1A", grid=[410, 325])
Module1 = PushButton(app1, call1A, text="Play Version 1B", grid=[410, 350])

Module1 = PushButton(app1, call1A, text="Play Version 1C", grid=[410, 375])

Module1 = PushButton(app1, call1A, text="Play Version 1D", grid=[410, 400])

Module1 = PushButton(app1, call1A, text="Play Version 1E", grid=[410, 425])

Module1 = PushButton(app1, call1A, text="Play Version 1F", grid=[410, 450])
Module1 = PushButton(app1, call1A, text="Play Version 1G", grid=[410, 475])

Module1 = PushButton(app1, call1A, text="Play Version 1H", grid=[410, 500])


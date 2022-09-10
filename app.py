import pyautogui
from tkinter import *

window = Tk()
window.title('ScreenShot')
window.geometry('200x100')

def scrShot():
    im = pyautogui.screenshot()
    im.save(r'E:\\mohamed\\coding\\python\\screenShot\\myScreenShot.png')

tit = Label(window, text='Screen Shot').pack()
btn = Button(window, text='Take screen shot', bg='blue', fg='white', command=scrShot).pack()

mainloop()
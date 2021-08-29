import pyautogui
import tkinter as tk

x = 100
y = 100
speed = 5
pyautogui.FAILSAFE = False
def move(left, up, x, y, speed):
    print('cmere')
    if left == True:
        face.configure(text = "Ow O")
        ax = 0
        we = "w"
        x -= speed
    elif left == False:
        face.configure(text = "O wO")
        ax = 1
        we = "e"
        x += speed
    else:
        ax = 0.5
        face.configure(text = "O w O")
        we = ""
    if up == True:
        ay = 0
        ns = "n"
        y -= speed
    elif up == False:
        ay = 1
        ns = "s"
        y += speed
    else:
        ay = 0.5
        ns = ""
    face.place(relx = ax, rely = ay, anchor = ns+we)
    root.geometry("50x50+"+str(x-25)+"+"+str(y-25))
    root.after(10, update, x, y, speed)

def snatch(x, y, speed):
    w, h = pyautogui.size()
    if x < w + 10:
        x += speed
    else:
        root.after(5000, lambda: root.destroy())
    root.geometry("50x50+"+str(x-25)+"+"+str(y-25))
    pyautogui.moveTo(x+25, y+25, duration = 0, _pause=False)
    root.after(10, snatch, x, y, speed)

def update(x, y, speed):
    mx, my = pyautogui.position()
    if x-20<mx<x+20:
        left = None
    elif x > mx:
        left = True
    else:
        left = False
    
    if y-20<my<y+20:
        up = None
    elif y > my:
        up = True
    else:
        up = False
    if x-25<mx<x+25 and y-25<my<y+25:
        face.configure(text = "U wU")
        face.place(relx = 1, rely = 0.5, anchor = "e")
        root.after(10, snatch, x, y, speed)
        print("gotcha")
        return
    root.after(10, move, left, up, x, y, speed)

root = tk.Tk()
root.geometry("50x50+75+75")
root.overrideredirect(True)
root.wm_attributes('-topmost', 'true')
face = tk.Label(text="O w O")
face.place(relx =0.5, rely = 0.5, anchor = "center")
root.after(1000, update, x, y, speed)
root.mainloop()
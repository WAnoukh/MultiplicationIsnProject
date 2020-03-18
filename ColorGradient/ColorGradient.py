from tkinter import Tk, Label, Button,Scale,HORIZONTAL,Canvas,Toplevel


from sys import path
from pathlib import Path
pth = Path(__file__).parent.parent
path.append(str(pth)+"/Methodes")
from DrawingMethodes import ColorLerp

c2,c1 = (255,0,0),(0,255,255)
lastScale = 50
interColor = (0,0,0)

def SetMaster(Master,Update):
    global master,dLUpdate
    master = Master
    dLUpdate = Update

def StartInterface():
    global master,grad
    grad = Toplevel(master)
    my_gui = ColorGraduitGui(grad)
    grad.grid()
    grad.mainloop()

def StopInterface():
    global grad
    grad.destroy()

def SetInterColor():
    global interColor
    interColor = ColorLerp(c1,c2,0.5)

def GetColorInGradient(at):
    global c1,c2,lastScale,interColor
    if(at< lastScale ):
        newColor = ColorLerp(interColor,c1,at/lastScale)
    elif(at> lastScale):
        newColor = ColorLerp(c2,interColor,(at-lastScale)/(100-(lastScale)))
    else:
        newColor = interColor
    return newColor

class ColorGraduitGui:
    def __init__(self,master):
        self.mainLabel = Label(master,text="GradientEditor",bg = "#DDDDDD")
        self.mainLabel.grid()



        self.canvas = Canvas(master, width=150, height=20, background='white')
        self.canvas.grid()

        self.mainScale = Scale(master,from_=0, to=100,length=150, orient=HORIZONTAL,showvalue = 0,cursor = "tcross")
        self.mainScale.grid()
        self.mainScale.set(50)
        global lastScale
        self.mainScale.set(lastScale)
        self.lines = []
        self.DrawGradient()
        self.Update()

    def Update(self):
        global lastScale, interColor,SetInterColor,dLUpdate
        if not (self.mainScale.get() ==lastScale ):
            for line in self.lines:
                self.canvas.delete(line)
            self.lines = []
            lastScale = self.mainScale.get()
            self.DrawGradient()
            dLUpdate()
        self.canvas.after(1,self.Update)

    def DrawGradient(self):
        SetInterColor()
        global c1,c2,lastScale
        scaleValue = int((lastScale/100)*150)
        for i in range(150):
            newColor = GetColorInGradient(float(i)/150*100)
            self.lines.append(self.canvas.create_line(i,0,i,20,fill = "#{:02x}{:02x}{:02x}".format(newColor[0],newColor[1],newColor[2])))



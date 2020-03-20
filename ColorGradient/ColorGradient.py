from tkinter import Tk, Label, Button,Scale,HORIZONTAL,Canvas,Toplevel


from sys import path
from pathlib import Path
pth = Path(__file__).parent.parent
path.append(str(pth)+"/Methodes")
from DrawingMethodes import ColorLerp
from ColorGradient.ColorPicker import picker

c2,c1 = (255,0,0),(0,255,255)
lastScale = 50
interColor = (0,0,0)

def SetMaster(Master,Update):
    global master,dLUpdate
    master = Master
    dLUpdate = Update

def StartInterface():
    global master,grad, my_gui
    grad = Toplevel(master)
    my_gui = ColorGraduitGui(grad)
    grad.grid()
    grad.mainloop()

def StopInterface():
    global grad, my_gui
    del my_gui
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

class ColorSelector:
    pick = None
    def __init__(self,master,gridpos,var,cmdUpdate,sticky="w"):
        self.color = "#{:02x}{:02x}{:02x}".format(var[0],var[1],var[2])
        self.canvas = Canvas(master, width=20, height=20, background=self.color)
        self.canvas.grid(column = gridpos[0],row = gridpos[1],sticky = sticky)
        self.canvas.bind("<Button-1>", self.click)
        self.CallUpdate = cmdUpdate
    
    def click(self,event):
        if(self.pick is None):
            global grad
            self.pick = picker(grad,self.color,self.DelPicker,self.UpdateColor)

    def UpdateCanvas(self):
        self.canvas.config(background=self.color)

    def UpdateColor(self,color):
        self.color = color
        self.UpdateCanvas()
        self.CallUpdate()


    def DelPicker(self):
        del self.pick
        self.pick = None

class ColorGraduitGui:
    def __init__(self,master):
        self.mainLabel = Label(master,text="GradientEditor",bg = "#DDDDDD")
        self.mainLabel.grid(columnspan=2)

        
        self.colorS1 = ColorSelector(master,(0,2),c1,self.UpdateColorInGrad)
        self.colorS2 = ColorSelector(master,(1,2),c2,self.UpdateColorInGrad, sticky="e")
        self.canvas = Canvas(master, width=150, height=20, background='white')
        self.canvas.grid(columnspan=2,sticky ="we")

        self.mainScale = Scale(master,from_=0, to=100,length=150, orient=HORIZONTAL,showvalue = 0,cursor = "tcross")
        self.mainScale.grid(columnspan=2)
        self.mainScale.set(50)
        global lastScale
        self.mainScale.set(lastScale)
        self.lines = []
        self.DrawGradient()
        self.Update()

    def UpdateColorInGrad(self):
        print(self.colorS1.color,self.colorS2.color)
        nc1 = self.colorS1.color
        nc2 = self.colorS2.color
        global c1,c2,dLUpdate
        c1 = (int(nc1[1:3],16),int(nc1[3:5],16),int(nc1[5:7],16))
        c2 = (int(nc2[1:3],16),int(nc2[3:5],16),int(nc2[5:7],16))
        self.DrawGradient()
        dLUpdate()
        

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



from tkinter import Tk, Label, Button,Scale,HORIZONTAL,Canvas


from sys import path
from pathlib import Path
pth = Path(__file__).parent.parent
path.append(str(pth)+"/Methodes")
from DrawingMethodes import ColorLerp



class ColorGraduitGui:
    def __init__(self,master):
        self.mainLabel = Label(master,text="GradientEditor",bg = "#DDDDDD")
        self.mainLabel.grid()

        self.c1,self.c2 = (255,0,0),(0,255,255)

        self.canvas = Canvas(master, width=150, height=20, background='white')
        self.canvas.grid()

        self.mainScale = Scale(master,from_=0, to=100,length=150, orient=HORIZONTAL,showvalue = 0,cursor = "tcross")
        self.mainScale.grid()
        self.mainScale.set(50)
        self.lastScale = self.mainScale.get()

        self.lines = []
        self.DrawGradient()
        self.Update()

    def Update(self):
        if not (self.mainScale.get() ==self.lastScale ):
            for line in self.lines:
                self.canvas.delete(line)
            self.lines = []
            self.DrawGradient()
            self.lastScale = self.mainScale.get()
        self.canvas.after(5,self.Update)

    def GetColorInGradient(self,at):
        pass

    def DrawGradient(self):
        scaleValue = int((self.mainScale.get()/100)*150)
        interColor = ColorLerp(self.c1,self.c2,0.5)
        for i in range(150):
            if(i< scaleValue ):
                newColor = ColorLerp(interColor,self.c1,i/(scaleValue))
            else:
                newColor = ColorLerp(self.c2,interColor,(i-scaleValue)/(150-(scaleValue)))
            self.lines.append(self.canvas.create_line(i,0,i,20,fill = "#{:02x}{:02x}{:02x}".format(newColor[0],newColor[1],newColor[2])))


grad = Tk()
grad.title("Gr")
my_gui = ColorGraduitGui(grad)
grad.mainloop()
from tkinter import Toplevel, Canvas,PhotoImage
from math import sqrt,acos,pi,cos,sin
from ColorGradient.cols import hsv_to_rgb,rgb_to_hsv
from Methodes.DrawingMethodes import DrawCircleAt

def GetColorFromCoord(x,y,dist,ray,val):
    if(x==0 and y == 0):
        return (255*val,255*val,255*val)
    else:
        saturation = (dist/ray)
        angle = abs(acos((x)/(dist)))
        if(y<0):
            angle = 2*pi - angle
        angle /= 2 * pi
        col = hsv_to_rgb(angle,saturation,val)
        color = "#{:02x}{:02x}{:02x}".format(int(col[0]*255),int(col[1]*255),int(col[2]*255))
        return color

class picker:
    cSize = 160
    border = 5
    pos = (0,0)
    cValue = 1
    previewColor = (0,0,0)
    def __init__(self,master,baseColor,closeMeth,updateMeth):
        self.baseColor = baseColor
        self.window = Toplevel(master)
        self.closeMeth = closeMeth
        self.updateMeth = updateMeth
        self.window.protocol("WM_DELETE_WINDOW", self.OnClosing)

        self.canvas = Canvas(self.window, width=self.cSize, height=self.cSize, background="#{:02x}{:02x}{:02x}".format(240,240,237))
        self.canvas.bind("<Button-1>", self.ChangePos)
        self.canvas.grid()
        self.initCanvasCircle()
        pos = self.rgbToCoord(self.baseColor)
        self.pos = pos
        self.DrawCursor()
        self.lumCanvas = Canvas(self.window, width=20, height=self.cSize, background="black")
        self.lumCanvas.bind("<Button-1>", self.ChangeLum)
        self.lumCanvas.grid(row = 0,column = 1)

        self.InitLumCanvas()
        self.previewCanvas = Canvas(self.window, width=self.cSize, height=20, background="black")
        self.previewCanvas.grid()
        self.UpdatePreview()

    def DrawCursor(self):
        pos = self.pos
        newPos = (pos[0]+self.cSize//2,self.cSize//2-pos[1])
        self.circle = DrawCircleAt(newPos[0],newPos[1],3,self.canvas)

    def ChangePos(self,event):
        newX=event.x-160//2
        newY=-(event.y-160//2)
        if(sqrt(newX**2 + newY**2)<150//2):
            self.pos = (newX,newY)
            self.UpdatePreview()
        self.canvas.delete(self.circle)
        self.DrawCursor()

    def ChangeLum(self,event):
        self.cValue = (self.cSize-event.y)/self.cSize
        self.UpdatePreview()

    def UpdatePreview(self):
        dist = sqrt(self.pos[0]**2 + self.pos[1]**2)
        color = GetColorFromCoord(self.pos[0],self.pos[1],dist,self.cSize//2-self.border,self.cValue)
        self.prewiewColor = (int(color[1:3],16),int(color[3:5],16),int(color[5:7],16))
        self.previewCanvas.configure(background=color)
        self.updateMeth(color)

    def rgbToCoord(self,color):
        if(isinstance(color, str)):
            color = (int(color[1:3],16),int(color[3:5],16),int(color[5:7],16))
        hsv = rgb_to_hsv(color[0]/255,color[1]/255,color[2]/255)
        angle = hsv[0]*2*pi
        if(hsv[1] ==0):
            dist = 0
        else:
            dist = (self.cSize//2-self.border)*(hsv[1])
        x = cos(angle) * dist
        y= sin(angle) * dist
        print(hsv,color,x,y)
        return x,y,hsv[2]

    def InitLumCanvas(self):
        for y in range(self.cSize):
            color = 255-int( y/self.cSize *255)
            color = "#{:02x}{:02x}{:02x}".format(color,color,color)
            self.lumCanvas.create_line(0,y,20,y,fill = color)

    def initCanvasCircle(self):

        cRange = range(self.cSize)
        self.img = PhotoImage(width=self.cSize, height=self.cSize)
        midSize = self.cSize//2
        s = 0.5
        l = 0.5
        for x in cRange:
            for y in cRange:
                color = "#{:02x}{:02x}{:02x}".format(240,240,237)
                relx = x-midSize
                rely = midSize-y
                pixelDFromCenter = sqrt((relx)**2+(rely)**2)
                if(pixelDFromCenter< midSize-self.border and not(x==midSize and y ==midSize)):
                    color = GetColorFromCoord(relx,rely,pixelDFromCenter,midSize-self.border,self.cValue)

                self.img.put(color, (x, y))
        self.canvas.create_image((midSize, midSize), image=self.img, state="normal")


    def OnClosing(self):
        self.closeMeth()
        self.window.destroy()

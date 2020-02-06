from tkinter import Canvas
import Methodes.DrawingMethodes as drawMeth
import Dictionnaire as Dic

CansColl = Dic.GridColumn.Canvas

def InitCanvas(w,h,fenetre):
    global canvas
    canvas = Canvas(fenetre, width=w, height=h)
    canvas.grid(column = CansColl,row=1,rowspan=60)
    print("hey")
    InitBackground()

def SetCanvasBackgroundColor(color = "#DDDDDD"):
    canvas.configure(bg=color)

def InitCircle():
    canvasSize = Dic.GetCanvasSize()
    if (canvasSize[0]<canvasSize[1]):
        lowestSize = canvasSize[0]
    else :
        lowestSize = canvasSize[1]
    
    r = (lowestSize*Dic.Settings["CircleSize"])/2

    drawMeth.DrawCircleAt(canvasSize[0]/2,canvasSize[1]/2,r,canvas)

def InitBackground():
    SetCanvasBackgroundColor()
    InitCircle()
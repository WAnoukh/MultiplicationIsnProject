from tkinter import Canvas
import Methodes.DrawingMethodes as drawMeth
import Dictionnaire as Dic
import CanvasScript.PointManager as PntMan
from math import pi

CansColl = Dic.GridColumn.Canvas

def InitCanvas(w,h,fenetre):
    global canvas
    canvas = Canvas(fenetre, width=w, height=h)
    canvas.grid(column = CansColl,row=1,rowspan=60)
    InitBackground()

def SetCanvasBackgroundColor(color = "#DDDDDD"):
    canvas.configure(bg=color)

def GetCanvas():
    return canvas

##CircleDrawing
def InitCircle():
    global circleRay
    canvasSize = Dic.GetCanvasSize()
    if (canvasSize[0]<canvasSize[1]):
        lowestSize = canvasSize[0]
    else :
        lowestSize = canvasSize[1]
    
    r = (lowestSize*Dic.Settings["CircleSize"])/2
    circleRay = r
    drawMeth.DrawCircleAt(canvasSize[0]/2,canvasSize[1]/2,r,canvas)

def InitBackground():
    SetCanvasBackgroundColor()
    InitCircle()

##PointDrawing
def DrawPoint(modulo):
    canvasSize = Dic.GetCanvasSize()
    r = circleRay
    poses = PntMan.GeneratePointPos(modulo)
    coords = PntMan.GenerateCoordFromPntPos(poses)
    return PntMan.DrawPointsFromTrigoCoord(canvasSize[0]/2,canvasSize[1]/2,r,coords,canvas)

##LineDrawing
def DrawLine(modulo,coef):
    canvasSize = Dic.GetCanvasSize()
    r = circleRay
    poses1 = PntMan.GeneratePointPos(modulo)
    print(poses1)
    poses2=[]
    for pos in poses1 :
        poses2.append(((pos+0.5*pi)*coef)-0.5*pi)
    print(poses2)
    coords1 = PntMan.GenerateCoordFromPntPos(poses1)
    coords2 = PntMan.GenerateCoordFromPntPos(poses2)
    return PntMan.DrawLinesFromTrigoCoords(canvasSize[0]/2,canvasSize[1]/2,r,coords1,coords2,canvas)


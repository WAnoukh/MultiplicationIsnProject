import CanvasManager as cM
from math import sqrt
from Dictionnaire import GetCanvasSize,Settings
from Methodes.DrawingMethodes import ColorLerp
drawDot= True
colorMode = False
lineColor = ((255,0,0),(0,255,255))
def SwitchColorMode(mode,c1=(255,0,0),c2 = (0,255,255)):
    global colorMode,lineColor
    colorMode = mode
    if(mode):
        lineColor=(c1,c2)
        ColorLines()
    else:
        resetColorLine()

def SwitchDotDrawing(state):
    global Entry_modulo
    if(state):
        Entry_modulo.needDrawingUpdate = True
    global drawDot
    drawDot=state

def resetColorLine():
    list = GiveLines()
    canvas = cM.GetCanvas()
    for line in list:
        canvas.itemconfig(line,fill="#000000")

def ColorLines():
    global lineColor
    list = GiveLines()
    canvas = cM.GetCanvas()
    for line in list:
        coords = canvas.coords(line)
        distance = int(sqrt((coords[0]-coords[2])**2 + (coords[1]-coords[3])**2))
        size = GetCanvasSize()
        if(size[0]<size[1]):
            minsize = size[0]
        else:
            minsize = size[1]
        maxColorSize = minsize * Settings["CircleSize"]
        colorCoef = (distance/maxColorSize)
        newColor = ColorLerp(lineColor[0],lineColor[1],colorCoef)
        canvas.itemconfig(line,fill='#{:02x}{:02x}{:02x}'.format( newColor[0], newColor[1] , newColor[2] ))


def StartLooping(modulo,coef,TScale,window,canvas):
    global Entry_modulo,Entry_Coef,Entry_TimeScale,win,can
    global ToDeletes,PointsList,LineList
    PointsList=[]
    LineList=[]
    ToDeletes = []
    win = window
    can=canvas
    Entry_modulo= modulo
    Entry_Coef= coef
    Entry_TimeScale = TScale
    Update()

def newTick():
    global ToDeletes,PointsList
    for obj in ToDeletes:
        can.delete(obj)
    ToDeletes=[]
    Update()
    

def Update():
    global ToDeletes,PointsList,LineList,colorMode

    if(Entry_modulo.isOnClock):
        Entry_modulo.IncrementEntryValue(Entry_TimeScale.lastValidEntry)
        Entry_modulo.needDrawingUpdate = True
    if(Entry_Coef.isOnClock):
        Entry_Coef.IncrementEntryValue(Entry_TimeScale.lastValidEntry)
        Entry_Coef.needDrawingUpdate = True

    if(Entry_modulo.needDrawingUpdate == True or Entry_Coef.needDrawingUpdate):
        ToDeletes+=LineList
        LineList = cM.DrawLine(float(Entry_modulo.lastValidEntry),float(Entry_Coef.lastValidEntry))
        Entry_Coef.needDrawingUpdate = False
        if(colorMode):
            ColorLines()

    if(drawDot):
        if(Entry_modulo.needDrawingUpdate == True):
            ToDeletes+=PointsList
            PointsList = cM.DrawPoint(int(Entry_modulo.lastValidEntry))
            Entry_modulo.needDrawingUpdate = False
    else:
        ToDeletes+=PointsList
        PointsList = []

    win.after(2,newTick)

def GiveLines():
    return LineList
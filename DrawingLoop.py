import CanvasManager as cM

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
    global ToDeletes,PointsList,LineList

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

    if(Entry_modulo.needDrawingUpdate == True):
        ToDeletes+=PointsList
        PointsList = cM.DrawPoint(int(Entry_modulo.lastValidEntry))
        Entry_modulo.needDrawingUpdate = False

    win.after(2,newTick)

def GiveLines():
    return LineList
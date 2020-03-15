from tkinter import Tk,Label,Scale,Entry,PhotoImage
import Dictionnaire as Dic
import CanvasManager as cM
import Methodes.UICreator as UIC
import DrawingLoop as dLoop
dxfWorking = True
try :
    import DxfExport.DxfDrawing as DXFDraw
except:
    dxfWorking = False

def TakeImage(path,coef = 4):
    photo = PhotoImage(file = r"Img/{}".format(path))
    photoPlus = photo.subsample(coef, coef)  
    return photoPlus

def ExportScreenToDXF():
    DXFDraw.DrawScreen('Screen.dxf',dLoop.GiveLines(),cM.GetCanvas())

def PerspectiveSwitch(state):
    print("perpective switched")
    pass

def ColorSwitch(state):
    print("color switched")
    dLoop.SwitchColorMode(state)
    pass

def DotDrawing(state):
    dLoop.SwitchDotDrawing(state)

CansColl, UIColl = Dic.GridColumn.Canvas,Dic.GridColumn.UI
UiCellH = Dic.SoftInfo["UICell_Height"]
#Create the window
window = Tk()

#Set the title
window.title(Dic.SoftInfo["Title"])

#Create the canvas
canvasSize = Dic.GetCanvasSize()

cansLabel = Label(window, text="Drawer",bg="#AAAAAA",width = int((85*canvasSize[0])/600))
cansLabel.grid(column=CansColl,row=0)
cM.InitCanvas(canvasSize[0],canvasSize[1],window)

#Create UI
UILabel = Label(window, text="Parameters",bg="#AAAAAA",width = 27)
UILabel.grid(column=UIColl,row=0,columnspan = 4)

####Set image to ui
i1=TakeImage("Plus.png")
i2=TakeImage("Minus.png")
i3=TakeImage("Valid.png")
i4=TakeImage("Clock.png",coef = 11)
i5=TakeImage("Clock23.png",coef = 11)
UIC.SetImg(i1,i2,i3,i4,i5)

####SetEntries
Entry_modulo = UIC.NewUIEntry(UIColl,200,window,"Modulo :",defaultValue=5)
Entry_Coef= UIC.NewUIEntry(UIColl,250,window,"Multiplicande :")

####Set Time Scale
Entry_TimeScale = UIC.NewUITimeScale(UIColl,300,window,"TimeScale :",defaultValue=0.01)

if(dxfWorking):
    ####Set DXF Button
    button_DXF = UIC.NewButton(UIColl,1000,window,"Export to Dxf :",ExportScreenToDXF)
else : 
    errorLabel = Label(window,text = "ezdxf not installed on this computer",bg = "#DD2222",fg = "#FFFFFF")
    errorLabel.grid(column = 1 , row = 1000, sticky = "W",columnspan=4)

###Set 3D switcher 
##DisableForTheMoment
'''perspectiveSwitch = UIC.NewSwitchBut(UIColl,1100,window,"Switch perspective :",PerspectiveSwitch,
enableT = "3D with complex numbers",disableT = "2D with real numbers")'''

###Set Color button
colorSwitch = UIC.NewSwitchBut(UIColl,1100,window,"Switch color mode",ColorSwitch,
enableT = "Colored by length")

###Set dot switcher
colorSwitch = UIC.NewSwitchBut(UIColl,900,window,"Draw Dots",DotDrawing,defaultSwitch=True)

###DrawPoint
dLoop.StartLooping(Entry_modulo,Entry_Coef,Entry_TimeScale,window,cM.GetCanvas())

window.mainloop()


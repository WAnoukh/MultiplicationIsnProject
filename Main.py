from tkinter import Tk,Label,Scale,Entry,PhotoImage
import Dictionnaire as Dic
import CanvasManager as cM
import Methodes.UICreator as UIC
import DrawingLoop as dLoop

def TakeImage(path,coef = 4):
    photo = PhotoImage(file = r"Img\{}".format(path))
    photoPlus = photo.subsample(coef, coef)  
    return photoPlus

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

###DrawPoint
dLoop.StartLooping(Entry_modulo,Entry_Coef,window,cM.GetCanvas())

window.mainloop()


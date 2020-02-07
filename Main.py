from tkinter import Tk,Label,Scale,Entry
import Dictionnaire as Dic
import CanvasManager as cM
import Methodes.UICreator as UIC
import DrawingLoop as dLoop

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
UILabel = Label(window, text="Parameters",bg="#AAAAAA",width = 30)
UILabel.grid(column=UIColl,row=0,columnspan = 4)

####SetEntries
Entry_modulo = UIC.NewUIEntry(UIColl,1,window,"Modulo :",defaultValue=5)
Entry_Coef= UIC.NewUIEntry(UIColl,3,window,"Coef :")

###DrawPoint
dLoop.StartLooping(Entry_modulo,Entry_Coef,window,cM.GetCanvas())

window.mainloop()
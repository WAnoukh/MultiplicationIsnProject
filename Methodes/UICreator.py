from tkinter import Tk,Label,Scale,Entry,Button ,END,DoubleVar,PhotoImage

def SetImg(plus,minus,valid,clock,clock2):
    global image_plus,image_minus,image_valid,image_clock,image_clock2
    image_plus,image_minus,image_valid,image_clock,image_clock2=plus,minus,valid,clock,clock2

class TScaleObj:
    needDrawingUpdate = True
    def __init__(self,cellx,celly,window,title,defaultValue):
        self.InitEntry(defaultValue)
        #Label init
        self.label = Label(window, text=title)
        self.label.grid(column=cellx,row=celly, sticky = "W" )
        #Entry init
        self.entry = Entry(window,textvariable=self.EntryValue)
        self.entry.grid(column=cellx,row=celly+1, sticky = "W" )
        #Buttons init
        self.buttSub = Button(window,text = "Sub" ,command= self.Sub,image = image_minus)
        self.buttSub.grid(column=cellx+3,row=celly+1, sticky = "W")
        self.buttAdd = Button(window,text = "Add",command=self.Add,image = image_plus )
        self.buttAdd.grid(column=cellx+2,row=celly+1, sticky = "W")
        self.buttValidate = Button(window,text = "<-",command=self.setNewEntry,image = image_valid )
        self.buttValidate.grid(column=cellx+1,row=celly+1, sticky = "W")

    def UpdateValidEntry(self,value):
        self.lastValidEntry = value
        self.RefreshDisplayedValue()
        self.needDrawingUpdate = True

    def setNewEntry(self):
        newValue = self.EntryValue.get()

        if(self.CheckForValidEntry(newValue)):
            self.UpdateValidEntry(float(newValue))
        else :
            self.RefreshDisplayedValue()

    def CheckForValidEntry(self,value):
        try:
            v = float(value)
            if v <0:
                floatable = False
            else : 
                floatable = True
        except:
            floatable = False
        return floatable
            
    def RefreshDisplayedValue(self):
        self.EntryValue.set(self.lastValidEntry)

    def IncrementEntryValue(self,inc):
        newValue = self.lastValidEntry + inc
        if self.CheckForValidEntry(newValue):
            self.UpdateValidEntry(newValue)

    def Add(self):
        self.IncrementEntryValue(0.001)
    def Sub(self):
        self.IncrementEntryValue(-0.001)

    def InitEntry (self,defaultValue):
        self.EntryValue = DoubleVar()
        self.EntryValue.set(defaultValue)
        self.lastValidEntry = defaultValue


class EntryObj :
    needDrawingUpdate = True
    isOnClock = False
    def __init__(self,cellx,celly,window,title,defaultValue):
        self.InitEntry(defaultValue)
        self.clock1 = image_clock
        self.clock2 = image_clock2
        self.cImg = self.clock1
        #Label init
        self.label = Label(window, text=title)
        self.label.grid(column=cellx,row=celly, sticky = "W" )
        #Entry init
        self.entry = Entry(window,textvariable=self.EntryValue)
        self.entry.grid(column=cellx,row=celly+1, sticky = "W" )
        #Buttons init
        self.buttSub = Button(window,text = "Sub" ,command= self.Sub,image = image_minus)
        self.buttSub.grid(column=cellx+3,row=celly+1, sticky = "W")
        self.buttAdd = Button(window,text = "Add",command=self.Add,image = image_plus )
        self.buttAdd.grid(column=cellx+2,row=celly+1, sticky = "W")
        self.buttValidate = Button(window,text = "<-",command=self.setNewEntry,image = image_valid )
        self.buttValidate.grid(column=cellx+1,row=celly+1, sticky = "W")
        self.buttClock = Button(window,text = "<-",image = self.cImg,command = self.ToogleClock )
        self.buttClock.grid(column=cellx,row=celly+2, sticky = "W")

    def UpdateClockImg(self):
        if not self.isOnClock:
            self.cImg = self.clock1
        else :
            self.cImg = self.clock2
        self.buttClock.configure(image = self.cImg)

    def ToogleClock(self):
        self.isOnClock = not self.isOnClock
        self.UpdateClockImg()
        

    def UpdateValidEntry(self,value):
        self.lastValidEntry = value
        self.RefreshDisplayedValue()
        self.needDrawingUpdate = True

    def setNewEntry(self):
        newValue = self.EntryValue.get()
        if(self.CheckForValidEntry(newValue)):
            self.UpdateValidEntry(float(newValue))
        else :
            self.RefreshDisplayedValue()

    def CheckForValidEntry(self,value):
        try:
            v = float(value)
            if v <0:
                floatable = False
            else : 
                floatable = True
        except:
            floatable = False
        return floatable
            
    def RefreshDisplayedValue(self):
        self.EntryValue.set(self.lastValidEntry)

    def IncrementEntryValue(self,inc):
        newValue = self.lastValidEntry + inc
        print(float(self.lastValidEntry) , inc, "give" , float(self.lastValidEntry)+0.01)
        if self.CheckForValidEntry(newValue):
            self.UpdateValidEntry(newValue)

    def Add(self):
        self.IncrementEntryValue(1)
    def Sub(self):
        self.IncrementEntryValue(-1)

    def InitEntry (self,defaultValue):
        self.EntryValue = DoubleVar()
        self.EntryValue.set(defaultValue)
        self.lastValidEntry = defaultValue
        
        
def NewUIEntry(cellx,celly,window,title,defaultValue= 0):
    obj = EntryObj(cellx,celly,window,title,defaultValue)
    return obj

def NewUITimeScale (cellx,celly,window,title,defaultValue= 0):
    obj = TScaleObj(cellx,celly,window,title,defaultValue)
    return obj
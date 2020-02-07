from tkinter import Tk,Label,Scale,Entry,Button ,END,StringVar



class EntryObj :
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
        self.buttSub = Button(window,text = "Sub" ,command= self.Sub)
        self.buttSub.grid(column=cellx+2,row=celly+1, sticky = "W")
        self.buttAdd = Button(window,text = "Add",command=self.Add )
        self.buttAdd.grid(column=cellx+1,row=celly+1, sticky = "W")
        self.buttValidate = Button(window,text = "<-",command=self.setNewEntry )
        self.buttValidate.grid(column=cellx+3,row=celly+1, sticky = "W")

    def UpdateValidEntry(self,value):
        self.lastValidEntry = value
        self.RefreshDisplayedValue()
        self.needDrawingUpdate = True

    def setNewEntry(self):
        newValue = self.EntryValue.get()
        if(self.CheckForValidEntry(newValue)):
            self.UpdateValidEntry(int(newValue))
        else :
            self.RefreshDisplayedValue()

    def CheckForValidEntry(self,value):
        try:
            v = int(value)
            if v <0:
                intable = False
            else : 
                intable = True
        except:
            intable = False
        return intable
            
    def RefreshDisplayedValue(self):
        self.EntryValue.set(self.lastValidEntry)

    def IncrementEntryValue(self,inc):
        newValue = self.lastValidEntry + inc
        if self.CheckForValidEntry(newValue):
            self.UpdateValidEntry(newValue)

    def Add(self):
        self.IncrementEntryValue(1)
    def Sub(self):
        self.IncrementEntryValue(-1)

    def InitEntry (self,defaultValue):
        self.EntryValue = StringVar()
        self.EntryValue.set(defaultValue)
        self.lastValidEntry = defaultValue
        
        
def NewUIEntry(cellx,celly,window,title,defaultValue= 0):
    obj = EntryObj(cellx,celly,window,title,defaultValue)
    return obj
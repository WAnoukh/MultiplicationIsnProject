from tkinter import Tk,Label,Scale,Entry,Button ,END,StringVar



class EntryObj :
    def __init__(self,cellx,celly,window,title):
        self.InitEntry()
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

    def CheckForValidEntry(self):
        try:
            int(self.EntryValue.get())
        except:
            self.EntryValue.set(self.lastValidEntry)

    def IncrementEntryValue(self,inc):
        self.CheckForValidEntry()
        newValue = int(self.EntryValue.get()) + inc
        self.EntryValue.set(newValue)
        self.lastValidEntry = newValue

    def Add(self):
        self.IncrementEntryValue(1)
    def Sub(self):
        self.IncrementEntryValue(-1)

    def InitEntry (self):
        self.EntryValue = StringVar()
        self.EntryValue.set(0)
        self.lastValidEntry = 0
        
        
def NewUIEntry(cellx,celly,window,title):
    obj = EntryObj(cellx,celly,window,title)
    return obj
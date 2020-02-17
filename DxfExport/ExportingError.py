from tkinter import Tk,Label,Button

def Close():
    global window
    window.destroy()

def ReturnError(errorTxt):
    global window
    #Create the window
    window = Tk()

    #Set the title
    window.title("Exporting Error")

    label = Label(window,text="The script encounter the following error :")
    label.grid(sticky = "W" )

    label = Label(window,text=errorTxt)
    label.grid(sticky = "W" )

    button = Button(window,text = "Ok",command = Close)
    button.grid(sticky = "W")

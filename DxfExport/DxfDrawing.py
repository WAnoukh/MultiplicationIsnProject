
from tkinter import Tk,Label,Entry,Button,END
import Dictionnaire
import os.path as ospath
import DxfExport.ExportingError as expError

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append(ospath.dirname(ospath.realpath(__file__))+'/libs')
import ezdxf

CircleRay = 100

def ConvertPointOperation(point,axis):
    size = Dictionnaire.GetCanvasSize()
    if(size[0]<size[1]):
        lowerSize = size[0]
    else:
        lowerSize= size[1]
    if(axis == 'x'):
        newPoint = point - size[0]/2
    else :
        newPoint = -(point -size[1]/2)
    newPoint/=(lowerSize*Dictionnaire.Settings["CircleSize"])
    newPoint*=CircleRay*2
    return newPoint

def ConvertCoordToDxfCoord(coord):
    pnt1 = ConvertPointOperation(coord[0],'x')
    pnt2 = ConvertPointOperation(coord[1],'y')
    pnt3 = ConvertPointOperation(coord[2],'x')
    pnt4 = ConvertPointOperation(coord[3],'y')
    return (pnt1,pnt2,pnt3,pnt4)

def StarExport():
    global name,lines,canvas,entry,window
    name = entry.get() + ".dxf"
    if(ospath.isfile(name)):
        expError.ReturnError("There is already a dxf file named : " + name)
    else:
        doc = ezdxf.new('R2004')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'

        msp = doc.modelspace()  # add new entities to the modelspace
        msp.add_circle((0,0),CircleRay)
        for line in lines :
            coord = canvas.coords(line)
            color = canvas.itemconfigure(line,"fill")
            color =color[4]
            if(color == "black"):
                decColor = "000"    
            else :
                decColor = "{:03d}{:03d}{:03d}".format(int(color[1:3],16),int(color[3:5],16),int(color[5:7],16))
            decColor="255255255"
            print(decColor)
            newcoord = ConvertCoordToDxfCoord(coord)
            line =msp.add_line((newcoord[0], newcoord[1]), (newcoord[2], newcoord[3]),dxfattribs={'true_color': ezdxf.rgb2int((int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)))})

        doc.saveas(name)
        window.destroy()

def DrawScreen(n,l,c):
    global name,lines,canvas,entry,window
    name,lines,canvas= n,l,c
    filename = "NewVector"
    i=2
    while(ospath.isfile(filename+".dxf")):
        filename = "NewVector" +"("+ str(i)+")"
        i+=1

    #Create the window
    window = Tk()

    #Set the title
    window.title("Exporting panel")

    label = Label(window,text="FileName")
    label.grid(sticky = "W" )

    entry = Entry(window)
    entry.grid()
    entry.insert(END, filename)

    label = Label(window,text=".dxf")
    label.grid(row=1,column=1,sticky = "W")

    button = Button(window,text = "Export",command = StarExport)
    button.grid(sticky = "W",row=1,column=2)
    window.mainloop()
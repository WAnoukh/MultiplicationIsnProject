import ezdxf
import tkinter
import Dictionnaire

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

def DrawScreen(name,lines,canvas):
    doc = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'

    msp = doc.modelspace()  # add new entities to the modelspace
    msp.add_circle((0,0),CircleRay)
    for line in lines :
        coord = canvas.coords(line)
        newcoord = ConvertCoordToDxfCoord(coord)
        msp.add_line((newcoord[0], newcoord[1]), (newcoord[2], newcoord[3]))  # add a LINE entity

    doc.saveas(name)
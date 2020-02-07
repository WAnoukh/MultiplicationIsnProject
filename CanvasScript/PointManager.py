from math import pi,cos,sin
import Methodes.DrawingMethodes as drawMeth
def GeneratePointPos(nb):
    '''
    Generate Points To 0 to 2*pi from the origin

    :param int nb: number of point to generate
    return position on x axis
        (Need to be converted in x/y axis in a circle perimeter.)
    '''
    positions = []
    if nb<0:
        nb=1
    try:
        gap = (2*pi)/(nb)
    except:
        nb=1
        gap = (2*pi)/(nb)

    for i in range(nb):
        positions.append(i*gap-(pi/2))
    return positions

def GenerateCoordFromPntPos(positions):
    coords = []
    for pos in positions:
        coord = cos(pos),sin(pos)
        coords.append(coord)
    return coords

def DrawPointsFromTrigoCoord(circleX,circleY,circleRay,coords,canvas):
    points = []
    for coord in coords:
        point = drawMeth.DrawCircleAt(circleX+(coord[0]*circleRay),circleY+(coord[1]*circleRay),3,canvas,fillColor="Red",outlineColor='')
        points.append(point)
    return points

def DrawLinesFromTrigoCoords(circleX,circleY,circleRay,coords1,coords2,canvas):
    lines =[]
    for i in range(len(coords1)):
        readCoord1 = coords1[i]
        newCoord1 = circleX+(readCoord1[0]*circleRay),circleY+(readCoord1[1]*circleRay)
        readCoord2 = coords2[i]
        newCoord2 = circleX+(readCoord2[0]*circleRay),circleY+(readCoord2[1]*circleRay)
        line = canvas.create_line(newCoord1[0],newCoord1[1],newCoord2[0],newCoord2[1])
        lines.append(line)
    return lines


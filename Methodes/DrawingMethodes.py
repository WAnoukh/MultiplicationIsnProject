def DrawCircleAt(x,y,ray,canvas,fillColor= '',outlineColor = '#000000'):
    x0 = x - ray
    y0 = y - ray
    x1 = x + ray
    y1 = y + ray
    return canvas.create_oval(x0, y0, x1, y1,fill = fillColor,outline= outlineColor )

def Lerp(a,b,lerp):
    return int((lerp * a) + ((1-lerp) * b))

def ColorLerp(c1,c2,lerp):
    return (Lerp(c1[0],c2[0],lerp),Lerp(c1[1],c2[1],lerp),Lerp(c1[2],c2[2],lerp))

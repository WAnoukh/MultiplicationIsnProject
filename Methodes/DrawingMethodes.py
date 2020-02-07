def DrawCircleAt(x,y,ray,canvas,fillColor= '',outlineColor = '#000000'):
    x0 = x - ray
    y0 = y - ray
    x1 = x + ray
    y1 = y + ray
    return canvas.create_oval(x0, y0, x1, y1,fill = fillColor,outline= outlineColor )
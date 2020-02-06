from enum import auto

SoftInfo = {
    "Title" : "Multiplication Viewer",
    "UICell_Height":10
}

Settings = {
    "Canvas_width": 600,
    "Canvas_height": 600,
    "CircleSize": 0.9
}

class GridColumn(auto):
    Canvas = 0
    UI = 1

def GetCanvasSize():
    return Settings["Canvas_width"],Settings["Canvas_height"]
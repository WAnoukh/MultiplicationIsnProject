# Copyright (c) 2015-2019 Manfred Moitzi
# License: MIT License
import os.path as ospath
import sys
sys.path.append(ospath.dirname(ospath.realpath(__file__))+'/DxfExport/libs')
import ezdxf

# Another way to set true color values for DXF entities: Property DXFEntity.rgb
def lines_with_true_color():
    doc = ezdxf.new('AC1018')  # for true color and transparency is DXF version AC1018 (ACAD R2004) or newer necessary
    msp = doc.modelspace()
    for y in range(10):
        line = msp.add_line((0, y * 10), (100, y * 10),dxfattribs={'color': 3,'true_color': ezdxf.rgb2int((255, 0, 0))})
        print(line.dxf.color) # set true color as RGB tuple
        # IMPORTANT: as you see it is not in the line.dxf namespace!
    # getting RGB values by r, g, b = line.rgb also works
    doc.saveas("true_color_lines.dxf")






lines_with_true_color()

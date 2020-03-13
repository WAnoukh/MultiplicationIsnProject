# Created: 17.02.2019
# Copyright (c) 2019, Manfred Moitzi
# License: MIT License
from typing import TYPE_CHECKING
import logging
from ezdxf.math import Vector
from ezdxf.lldxf.attributes import DXFAttr, DXFAttributes, DefSubclass, XType
from ezdxf.lldxf.const import DXF12, SUBCLASS_MARKER, DXF2000, DXF2007
from ezdxf.entities.dxfentity import base_class, SubclassProcessor, DXFEntity
from ezdxf.entities.layer import acdb_symbol_table_record
from .factory import register_entity

logger = logging.getLogger('ezdxf')

if TYPE_CHECKING:
    from ezdxf.eztypes import TagWriter, DXFNamespace

__all__ = ['VPort']

acdb_vport = DefSubclass('AcDbViewportTableRecord', {
    'name': DXFAttr(2),
    'flags': DXFAttr(70, default=0),
    'lower_left': DXFAttr(10, xtype=XType.point2d, default=(0, 0)),
    'upper_right': DXFAttr(11, xtype=XType.point2d, default=(1, 1)),
    'center': DXFAttr(12, xtype=XType.point2d, default=(70, 50)),
    'snap_base': DXFAttr(13, xtype=XType.point2d, default=(0, 0)),
    'snap_spacing': DXFAttr(14, xtype=XType.point2d, default=(.5, .5)),
    'grid_spacing': DXFAttr(15, xtype=XType.point2d, default=(.5, .5)),
    'direction': DXFAttr(16, xtype=XType.point3d, default=Vector(0, 0, 1)),
    'target': DXFAttr(17, xtype=XType.point3d, default=Vector(0, 0, 0)),
    'height': DXFAttr(40, default=1),  # DXF reference error: listed as group code 45
    'aspect_ratio': DXFAttr(41, default=1.34),
    'focal_length': DXFAttr(42, default=50),
    'front_clipping': DXFAttr(43, default=0),
    'back_clipping': DXFAttr(44, default=0),
    'snap_rotation': DXFAttr(50, default=0),
    'view_twist': DXFAttr(51, default=0),
    'view_mode': DXFAttr(71, default=0),

    'circle_sides': DXFAttr(72, default=1000),
    'fast_zoom': DXFAttr(73, default=1),  # removed in R2007
    'ucs_icon': DXFAttr(74, default=3),
    'snap_on': DXFAttr(75, default=0),  # removed in R2007
    'grid_on': DXFAttr(76, default=0),  # removed in R2007
    'snap_style': DXFAttr(77, default=0),  # removed in R2007
    'snap_isopair': DXFAttr(78, default=0),  # removed in R2007
    # R2000: 331 or 441 (optional) - ignored by ezdxf
    # Soft or hard-pointer ID/handle to frozen layer objects; repeats for each frozen layers
    # 70: Bit flags and perspective mode

    'plot_style_sheet': DXFAttr(1, dxfversion=DXF2007),
    'render_mode': DXFAttr(281, default=0, dxfversion=DXF2000),
    # 0 = 2D Optimized (classic 2D)
    # 1 = Wireframe
    # 2 = Hidden line
    # 3 = Flat shaded
    # 4 = Gouraud shaded
    # 5 = Flat shaded with wireframe
    # 6 = Gouraud shaded with wireframe
    # All rendering modes other than 2D Optimized engage the new 3D graphics pipeline. These values directly correspond
    # to the SHADEMODE command and the AcDbAbstractViewTableRecord::RenderMode enum

    # Value of UCSVP for this viewport. If set to 1, then viewport stores its
    # own UCS which will become the current UCS whenever the viewport is
    # activated. If set to 0, UCS will not change when this viewport is
    # activated
    'ucs_vp': DXFAttr(65, dxfversion=DXF2000, default=0),
    'ucs_origin': DXFAttr(110, xtype=XType.point3d, dxfversion=DXF2000),
    'ucs_xaxis': DXFAttr(111, xtype=XType.point3d, dxfversion=DXF2000),
    'ucs_yaxis': DXFAttr(112, xtype=XType.point3d, dxfversion=DXF2000),
    # handle of AcDbUCSTableRecord if UCS is a named UCS. If not present, then UCS is unnamed
    'ucs_handle': DXFAttr(345, dxfversion=DXF2000),
    # handle of AcDbUCSTableRecord of base UCS if UCS is orthographic (79 code is non-zero). If not present and 79 code
    # is non-zero, then base UCS is taken to be WORLD
    'base_ucs_handle': DXFAttr(346, dxfversion=DXF2000),
    'ucs_ortho_type': DXFAttr(79, dxfversion=DXF2000),
    # 0 = UCS is not orthographic
    # 1 = Top
    # 2 = Bottom
    # 3 = Front
    # 4 = Back
    # 5 = Left
    # 6 = Right
    'elevation': DXFAttr(146, dxfversion=DXF2000, default=0),
    'unknown1': DXFAttr(60, dxfversion=DXF2000),

    'shade_plot_setting': DXFAttr(170, dxfversion=DXF2007),
    'major_grid_lines': DXFAttr(61, dxfversion=DXF2007),

    # Soft-pointer handle to background object
    'background_handle': DXFAttr(332, dxfversion=DXF2007, optional=True),
    # Soft-pointer handle to shade plot object
    'shade_plot_handle': DXFAttr(333, dxfversion=DXF2007, optional=True),
    # Hard-pointer handle to visual style object
    'visual_style_handle': DXFAttr(348, dxfversion=DXF2007, optional=True),

    'default_lighting_on': DXFAttr(292, dxfversion=DXF2007),
    'default_lighting_type': DXFAttr(282, dxfversion=DXF2007),
    # 0 = One distant light
    # 1 = Two distant lights
    'brightness': DXFAttr(141, dxfversion=DXF2000),
    'contrast': DXFAttr(142, dxfversion=DXF2000),
    'ambient_color_aci': DXFAttr(63, dxfversion=DXF2000, optional=True),
    'ambient_true_color': DXFAttr(421, dxfversion=DXF2000, optional=True),
    'ambient_color_name': DXFAttr(431, dxfversion=DXF2000, optional=True),
    # Hard-pointer handle to sun object
    'sun_handle': DXFAttr(361, dxfversion=DXF2007, optional=True),

})


@register_entity
class VPort(DXFEntity):
    """ DXF VIEW entity """
    DXFTYPE = 'VPORT'
    DXFATTRIBS = DXFAttributes(base_class, acdb_symbol_table_record, acdb_vport)

    def load_dxf_attribs(self, processor: SubclassProcessor = None) -> 'DXFNamespace':
        dxf = super().load_dxf_attribs(processor)
        if processor:
            tags = processor.load_dxfattribs_into_namespace(dxf, acdb_vport)
            if len(tags) and not processor.r12:
                processor.log_unprocessed_tags(tags, subclass=acdb_vport.name)
        return dxf

    def export_entity(self, tagwriter: 'TagWriter') -> None:
        super().export_entity(tagwriter)
        # AcDbEntity export is done by parent class
        dxfversion = tagwriter.dxfversion
        if dxfversion > DXF12:
            tagwriter.write_tag2(SUBCLASS_MARKER, acdb_symbol_table_record.name)
            tagwriter.write_tag2(SUBCLASS_MARKER, acdb_vport.name)
        self.dxf.export_dxf_attribs(tagwriter, [
            'name', 'flags', 'lower_left', 'upper_right', 'center', 'snap_base', 'snap_spacing', 'grid_spacing',
            'direction', 'target', 'height', 'aspect_ratio', 'focal_length', 'front_clipping', 'back_clipping',
            'snap_rotation', 'view_twist', 'view_mode', 'circle_sides', 'fast_zoom', 'ucs_icon', 'snap_on', 'grid_on',
            'snap_style', 'snap_isopair', 'plot_style_sheet', 'render_mode', 'ucs_vp', 'ucs_origin', 'ucs_xaxis',
            'ucs_yaxis', 'ucs_handle', 'base_ucs_handle', 'ucs_ortho_type', 'elevation', 'unknown1',
            'shade_plot_setting', 'major_grid_lines', 'background_handle', 'shade_plot_handle', 'visual_style_handle',
            'default_lighting_on', 'default_lighting_type', 'brightness', 'contrast', 'ambient_color_aci',
            'ambient_true_color', 'ambient_color_name'
        ])

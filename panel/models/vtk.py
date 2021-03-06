# coding: utf-8
"""
Defines custom VTKPlot bokeh model to render VTK objects.
"""
from bokeh.core.properties import (String, Bool, Dict, Any, Override,
                                   Instance, Int, Float, PositiveInt, Enum)
from bokeh.core.enums import enumeration
from bokeh.models import HTMLBox, Model

vtk_cdn = "https://unpkg.com/vtk.js"


class VTKAxes(Model):
    """
    A Bokeh model for axes
    """

    xticker = Dict(String, Any)

    yticker = Dict(String, Any)

    zticker = Dict(String, Any)

    origin = Any()

    digits = Int(default=1)

    show_grid = Bool(default=True)

    grid_opacity = Float(default=0.1)

    axes_opacity = Float(default=1)

    fontsize = PositiveInt(default=12)


class VTKPlot(HTMLBox):
    """
    A Bokeh model that wraps around a vtk-js library and renders it inside
    a Bokeh plot.
    """

    __javascript__ = [vtk_cdn]

    __js_skip__ = {'vtk': [vtk_cdn]}

    __js_require__ = {
        "paths": {"vtk": vtk_cdn[:-3]},
        "exports": {"vtk": None},
        "shim": {
            "vtk": {"exports": "vtk"}
        }
    }

    append = Bool(default=False)

    data = String(help="""The serialized vtk.js data""")

    camera = Dict(String, Any)

    axes = Instance(VTKAxes)

    enable_keybindings = Bool(default=False)

    orientation_widget = Bool(default=False)

    renderer_el = Any(readonly=True)

    height = Override(default=300)

    width = Override(default=300)


class VTKVolumePlot(HTMLBox):
    """
    A Bokeh model that wraps around a vtk-js library and renders it inside
    a Bokeh plot.
    """

    __javascript__ = [vtk_cdn]

    __js_skip__ = {'vtk': [vtk_cdn]}

    __js_require__ = {
        "paths": {"vtk": vtk_cdn[:-3]},
        "exports": {"vtk": None},
        "shim": {
            "vtk": {"exports": "vtk"}
        }
    }

    data = Dict(String, Any)

    colormap = String(help="Colormap Name")

    rescale = Bool(default=False)

    shadow = Bool(default=True)

    sampling = Float(default=0.4)

    edge_gradient = Float(default=0.2)

    ambient = Float(default=0.2)

    diffuse = Float(default=0.7)

    specular = Float(default=0.3)

    specular_power = Float(default=8.)

    slice_i = Int(default=0)

    slice_j = Int(default=0)

    slice_k = Int(default=0)

    display_volume = Bool(default=True)

    display_slices = Bool(default=False)

    render_background = String(default='#52576e')

    interpolation = Enum(enumeration('fast_linear','linear','nearest'))

    height = Override(default=300)

    width = Override(default=300)

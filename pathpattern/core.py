# -*- coding: utf-8 -*-

from igraph import Graph
from pyx import *

g = Graph(directed=True)
g.add_vertices(11)
g.add_edges([(0,1), (1,2), (1,3), (2,4), (2,5), (3,5), (3,6), (4,7), (4,8), (5,8), (5,9), (6,9), (6,10)])


def get_hmm():
    return 'hmmm...'

def degree_glyph(indegree, outdegree):
    """Return an igraph canvas glyph image based on indegree, outdegree."""
    canvas_ = canvas.canvas();
    dg_box = path.path(path.moveto(0, 0),
                       path.lineto(0, 1),
                       path.lineto(1, 1),
                       path.lineto(1, 0),
                       path.lineto(0, 0),
                       path.closepath()
                       )
    canvas_.stroke(dg_box, [color.rgb.green]) # manual bounding box
    node_dot = path.circle(.5, .5, .15)
    canvas_.fill(node_dot)
    in1 = path.path(path.moveto(.5, .5),
                    path.lineto(.5, 1)
                    )
    in2 = path.path(path.moveto(0, 1),
                    path.lineto(0, .75),
                    path.lineto(1, .75),
                    path.lineto(1, 1),
                    path.moveto(.5, .5),
                    path.lineto(.5, .75)
                    )
    out1 = path.path(path.moveto(.5, .5),
                    path.lineto(.5, 0)
                    )
    out2 = path.path(path.moveto(0, 0),
                    path.lineto(0, .25),
                    path.lineto(1, .25),
                    path.lineto(1, 0),
                    path.moveto(.5, .5),
                    path.lineto(.5, .25)
                    )
    inplus = path.path(path.moveto(1.25, .75),
                        path.lineto(1.25, 1),
                        path.moveto(1.1, .875),
                        path.lineto(1.4, .875),
                    )
    outplus = path.path(path.moveto(1.25, 0),
                        path.lineto(1.25, .25),
                        path.moveto(1.1, .125),
                        path.lineto(1.4, .125),
                    )
    if indegree == 1:
        canvas_.stroke(in1, [style.linewidth(.1)])
    if indegree == 2:
        canvas_.stroke(in2, [style.linewidth(.1)])
    if indegree == 3:
        canvas_.stroke(in1, [style.linewidth(.1)])
        canvas_.stroke(in2, [style.linewidth(.1)])
        # canvas_.stroke(inplus, [style.linewidth(.1)])
    if outdegree == 1:
        canvas_.stroke(out1, [style.linewidth(.1)])
    if outdegree == 2:
        canvas_.stroke(out2, [style.linewidth(.1)])
    if outdegree == 3:
        canvas_.stroke(out1, [style.linewidth(.1)])
        canvas_.stroke(out2, [style.linewidth(.1)])
        # canvas_.stroke(outplus, [style.linewidth(.1)])
    return canvas_


def batch_degree_glyph(indegree, outdegree):
    """"""
    return True
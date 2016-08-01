# -*- coding: utf-8 -*-

## svgwrite:
## 
##  -  [svgwrite 1.1.6 documentation](https://svgwrite.readthedocs.io/en/latest/#)
## -  ... and: [svgwrite 1.1.8](https://bitbucket.org/mozman/svgwrite)
## -  NOTE that the documentation is a bit behind the latest version, and pip / bitbucket aren't quite in sync -- pip links to an old version ~1.1.2

## Notes:
##
## -  [Creating Simple SVG from Python](http://florian-berger.de/en/articles/creating-simple-svg-from-python/)
##
## Regarding conditionally importing graphics functions (e.g. from pyx, turtle, svgwrite, pycairo, etc:).
## 
## -   http://stackoverflow.com/questions/16192448/conditional-definition-of-a-function-in-a-module
##
## The easiest way seems to be a conditional on either function definition (e.g. all def versions in one render.py, separated by an if statement):
##     
##  
## ...or a conditional import statement with 'as' to create a function that can be referred to as 'glyph' e.g.:
##     if mode=='svg':
##         from render_svgwrite import svg_glyph as glyph
##     if mode=='png':
##         from render_pyx import png_glyph as glyph
##
## Of future interest -- using a plugin library, and setting up the different renderers and parsers etc. as plugins.

## -  [Yapsy: Yet Another Plugin SYstem](http://yapsy.sourceforge.net/)  -- simple
## -  https://pypi.python.org/pypi/Plugins/0.5a1dev
## -  https://pypi.python.org/pypi/pluginmanager  -- in development
## -  http://pluginbase.pocoo.org/  -- very technical
##
## ...and rolling your own plugin management:
## 
## -  [Building a minimal plugin architecture in python](http://stackoverflow.com/questions/932069/building-a-minimal-plugin-architecture-in-python)
## -  [Writing a python plugin API](https://lkubuntu.wordpress.com/2012/10/02/writing-a-python-plugin-api/)


import svgwrite

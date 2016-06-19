# -*- coding: utf-8 -*-

from .context import pathpattern

import unittest


class RenderTestSuite(unittest.TestCase):
    """Rendering test cases."""

    def test_degree_glyph_set(self):
        ins  = 4
        outs = 4
        top = 4
        scale = 1.5

        for i in range(ins):
        	for o in range(outs):
        		imgfilename = '../output/pyx_glyphs/' + 'pyx_glyph_' + str(i) + str(o) + '.png'
        		c = pathpattern.degree_glyph(i,o); c.writeGSfile(filename=imgfilename)

        assert True

#    def test_degree_glyph_grid(self):
#        ins  = 4
#        outs = 4
#        top = 4
#        scale = 1.5
#
#        grid = canvas.canvas()
#        for i in range(ins):
#        	for o in range(outs):
#        		grid.insert(c, [trafo.translate(i*scale, (top-o)*scale)])
#        		# grid.text(i*scale, (top-o)*scale+.5, str(i)+'x'+str(o), [text.size(-3)]) ## print label
#        grid.writeGSfile(filename='pyx_grid.png')
#
#        mypage = document.page(grid, margin=1)
#        mydocument = document.document(mypage)
#        mydocument.writeSVGfile(filename='pyx_doc.svg')
#
#        assert True


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def placeholder(self):
        return True


if __name__ == '__main__':
    unittest.main()


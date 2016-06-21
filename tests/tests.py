# -*- coding: utf-8 -*-

from .context import pathpattern
from pathpattern import *

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


class UtilsTestSuite(unittest.TestCase):
    """ """
    
    def test_tgf_to_list(self):
        # t = utils.tgf_to_list("../super_mario_bros/super_mario_bros-levels.tgf")
        # print t
        return True

    def test_readgraph(self):
        # t = Graph.Read_Edgelist("../super_mario_bros/super_mario_bros-levels.el")
        filename = '../super_mario_bros/super_mario_bros-levels.el'
        li = []
        try:
            with open(filename, 'r') as inputfile:
                for line in inputfile:
                    term = line.strip().replace(" ", "").split('\t')
                    for a in term:
                        li.append(a)
        except OSError:
            print "File did not load."
        print 'list: ...'
        print li
        s = set(li)
        
        print 'set: ...'
        print s
        t = Graph.Read_Ncol(filename, directed=True)
        print 'graph ncol: ...'
        print t
        print t.degree
        print t.degree()
        print t.indegree
        print t.indegree()
        print t.outdegree
        print t.outdegree()
        print t.degree_distribution(mode = 'ALL')
        print t.degree_distribution(mode = 'IN')
        print t.degree_distribution(mode = 'OUT')
        degrees = zip(t.indegree(), t.outdegree())
        print degrees
        from collections import Counter
        degrees_counter = Counter(degrees)
        print degrees_counter

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def placeholder(self):
        return True


if __name__ == '__main__':
    unittest.main()





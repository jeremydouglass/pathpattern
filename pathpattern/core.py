# -*- coding: utf-8 -*-

from igraph import Graph
from pyx import *
from collections import Counter
from bs4 import BeautifulSoup
import tempfile
import utils
import regex as re

# g = Graph(directed=True)
# g.add_vertices(11)
# g.add_edges([(0,1), (1,2), (1,3), (2,4), (2,5), (3,5), (3,6), (4,7), (4,8), (5,8), (5,9), (6,9), (6,10)])



## set pyx unit scale (default 1cm, ~43 pixels) to 1 inch
## http://pyx.sourceforge.net/manual/unit.html
## http://nullege.com/codes/search/pyx.unit.set
## https://github.com/mjg/PyX/blob/master/test/unit/test_unit.py
unit.set(uscale=3, defaultunit="inch")


class GlyphSet():
    """ """
    def __init__(self, **kwargs):
        ##  http://stackoverflow.com/questions/1098549/proper-way-to-use-kwargs-in-python
        # self.inrange = kwargs.get('inrange')    # e.g. inrange = (1,2)
        # self.outrange = kwargs.get('outrange')
        
        # self.glist = kwargs.get('list',[(0,0),(0,1),(1,1),(1,2),(2,1),(1,3),(1,0)])
        self.glist = []
        self.id = 0
        self.width = kwargs.get('width', 4)
        self.outdir = kwargs.get('outdir', './')
        self.prefix = kwargs.get('prefix', 'glyph_')
        self.mincount = 0
        self.maxcount = 3
        
        ## http://stackoverflow.com/questions/5501725/python-iterate-a-specific-range-in-a-list
        if ('graph' in kwargs and 'range' not in kwargs and 'list' not in kwargs):
            self.graph = kwargs.get('graph')
            degrees = set(zip(self.graph.indegree(), self.graph.outdegree())) # a set -- no dups, no counts
            # print '\n    degree list:    ' + str(degrees)
            degrees_counter = Counter(zip(self.graph.indegree(), self.graph.outdegree())) # count dups
            print '* degrees_counter: '
            print degrees_counter
            self.mincount = degrees_counter[min(degrees_counter, key=degrees_counter.get)] # http://stackoverflow.com/questions/1661621/finding-the-highest-key/1747244#1747244
            self.maxcount = degrees_counter[max(degrees_counter, key=degrees_counter.get)]
            print '* self.mincount: '
            print self.mincount
            print '* self.maxcount: '
            print self.maxcount
            print degrees_counter
            # http://stackoverflow.com/questions/11055902/how-to-convert-a-counter-object-into-a-usable-list-of-pairs
            # print '\n    degree counter: ' + str(degrees_counter)
            degrees_counter_list = list(degrees_counter.items())
            # print '\n    degree counter list: '
            # print degrees_counter_list
            degrees_counter_sorted = []
            for key in sorted(degrees_counter.iterkeys()): degrees_counter_sorted.append((key, degrees_counter[key]))
            print degrees_counter_sorted
            # for i in degrees:
            #    self.glist.append(i)
            for i in degrees_counter_sorted:
                self.glist.append((i[0][0],i[0][1],i[1]))
        elif ('list' in kwargs and 'range' not in kwargs):
            self.glist = kwargs.get('list')
        # elif ('clist' in kwargs):
        #     temp_clist = kwargs.get('clist') # {(1, 0): 20, (1, 2): 12, (0, 1): 8, (1, 1): 3}
        #     for i in temp_clist:
        #         self.glist.append( i[0][0], i[0][1]), i[1] )
        elif ('range' in kwargs and 'list' not in kwargs):
            self.inrange = kwargs.get('range')[0]
            self.outrange = kwargs.get('range')[1]
            for i in range(self.inrange[0],self.inrange[1]):
                for o in range(self.outrange[0],self.outrange[1]):
                    self.glist.append( (int(i),int(o),1) ) # append tuple
                    ## consider 'slice' function as per http://stackoverflow.com/questions/28652976/passing-array-range-as-argument-to-a-function
        else:
            raise ValueError('invalid argument: provide one of the following:\n  range = ((xmin,xmax),(ymin,ymax))\n  list = [(ax,ay),(bx,by),(cx,cy)...]\n  graph = <igraph canvas.canvas object>')

        self.glist.sort(key = lambda x: (x[0], x[1])) # http://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        ## sorted -- any reason that custom list input order might matter? index lookup?

        ## id string -- this isn't unique or unambiguous, but perhaps use different separators and/or do a hash later.
        flatlist = [str(element) for tupl in self.glist for element in tupl] # http://stackoverflow.com/questions/3204245/how-do-i-convert-a-tuple-of-tuples-to-a-one-dimensional-list-using-list-comprehe
        self.id = ''.join(flatlist)
        
        # unused
        tlist = tuple(tuple(x) for x in self.glist)
        self.gcounts = Counter(tlist)
            

    # def __repr__(self):
    #     return "GlyphSet()"

    def __str__(self):
        string = 'GlyphSet:\n'
        # string += str(self.glist)
        widecount = 0
        for i in self.glist:
            if widecount >= self.width:
                string += '\n'
                widecount = 0
            string += '  ' + str(i)
            widecount += 1
        return string

    def __len__(self):
        return len(self.glist)

    def nocounts(self):
        ## replace all glist counts with 1
        newlist = []
        for i in self.glist:
            # print 'i:'
            # print i
            newlist.append((i[0], i[1], 1))
        self.glist = newlist

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

    def glyph(self, index):
        """ For a degree pair (in, out), render a glyph. """
        grid = canvas.canvas() ## left in error - comment out?
        # c = degree_glyph(index[0],index[1])
        if len(index)>2:
          c = degree_glyph(index[0],index[1],index[2], (self.mincount,self.maxcount))
        else:
          c = degree_glyph(index[0],index[1], 1, (self.mincount,self.maxcount))
        return c
        
    def glyphs(self):
        """ For a list of degree pairs, render all glyphs and append to a list of glyphs. """
        clist = []
        for i in self.glist:
            clist.append(self.glyph(i))
        #    clist.append(degree_glyph(i[0],i[1]))
        return clist
    
    def write_glyph(self, index):
        """ For a degree pair (in, out), save a glyph as a PNG file. """
        c = self.glyph(index)
        imgfilename = self.outdir + self.prefix + str(index[0]) + str(index[1]) + '.png'
        c.writeGSfile(filename=imgfilename)
        return imgfilename
    
    def write_glyphs(self):
        """ For a list of degree pairs, save all glyphs as PNG files. """
        for i in self.glist:
            self.write_glyph(i)
        return

    def signature(self):
        sig = canvas.canvas()
        ### top = 4
        # top = max(self.glist, key=lambda x: x[1]) ## http://stackoverflow.com/questions/4800419/sorting-or-finding-max-value-by-the-second-element-in-a-nested-list-python
        scale = 1.5
        # gl = self.glyphs()
        # print gl
        # for i in gl:
        #     sig.insert(i, [trafo.translate(i[0]*scale, (i[1])*scale)])
        
        # for i in self.glist:
        #     c = degree_glyph(*i); # http://stackoverflow.com/questions/1993727/expanding-tuples-into-arguments
        #     ### sig.insert(c, [trafo.translate(i[0]*scale, (top-i[1])*scale)])
        #     sig.insert(c, [trafo.translate(i[0]*scale, (i[1])*scale)])
        #   # print str(i) + str(o) + '.png'
        #   # imgfilename = '../output/pyx_glyphs/' + 'pyx_glyph_' + str(i[0]) + str(o[1]) + '.png'

        for index in self.glist:
          if len(index)>2:
            c = degree_glyph(index[0],index[1],index[2], (self.mincount,self.maxcount))
          else:
            c = degree_glyph(index[0],index[1], 1, (self.mincount,self.maxcount))
          sig.insert(c, [trafo.translate(index[0]*scale, (index[1])*scale)])
                
        return sig

    def write_signature(self, **kwargs):
        c = self.signature()
        imgfilename = self.outdir + self.prefix + 'signature_' + self.id + '.png'
        c.writeGSfile(filename=imgfilename)
        return imgfilename

class tgfFile():
    """ """

    def __init__(self, filename, **kwargs):
        self.nodelist = []
        self.nodeset  = set()
        self.nodedict = {}
        self.edgelist = []
        self.filename = filename
        if not filename:
            raise ValueError('No tgf filename given.')
        self.elfilename = kwargs.get('elfilename', '')

        try:
            with open(self.filename, 'r') as inputfile:
                phase = 'nodes'

                lines = (line.strip() for line in inputfile) # all lines including the blank ones http://stackoverflow.com/questions/4842057/python-easiest-way-to-ignore-blank-lines-when-reading-a-file
                lines = (line for line in lines if line) # non-blank lines

                for line in lines:
                    lt = line.strip().split('\t')  # line tuple
                    if '#' in line:
                        phase = 'edges'
                        continue
                    if phase == 'nodes':
                        self.nodeset.add(lt[0])
                        # self.nodedict.update({lt[0], ''}) # ADDING NODES TO DICT IS BROKEN
                        # self.nodedict.update({lt[0], lt[1:]})
                    if phase == 'edges':
                        self.edgelist.append(lt)
                        # tgf may have nodes which are only listed in edges
                        self.nodeset.add(lt[0]); self.nodeset.add(lt[1])
                        # only add keys-without-values if the values don't already exist
                        if not self.nodedict.get(lt[0]): # no key or empty value
                            self.nodedict[lt[0]] = ''  
                        if not self.nodedict.get(lt[1]): 
                            self.nodedict[lt[1]] = ''  
            self.nodelist = list(self.nodeset)
        except OSError:
            print "File not read."

    def __str__(self):
        string = 'tgfFile:\n'
        string += 'nodes:  ' + str(self.nodelist) + '\n'
        string += 'edges:  ' + str(self.edgelist) + '\n'
        return string

    def __len__(self):
        return (len(self.edgelist))
        
    def write_edgefile(self):
        if self.elfilename == '':
            self.elfilename = self.filename + '.el'
        try:
            with open(self.elfilename, "w") as outputfile:
                for line in self.edgelist:
                    outputfile.write('\t'.join(line[:2])  + '\n') # slice out edge labels to avoid igraph NCOL error, tab-delimit the tuples
            return self.elfilename
        except OSError:
            print "File not written."

    def to_graph(self):
        """ TGF file to igraph graph. Writes an edgefile and passes the filename in for a graph object, as igraph's Read_Ncol can only load from a file."""
        # results = edgelistfile_to_graph(elfilename)
        return Graph.Read_Ncol(self.write_edgefile(), directed=True)
    

def tgffile_to_edgelist(tgffilename, elfilename=''):
    """ """
    results = []
    if not tgffilename: raise ValueError('No tgf filename given.')
    if elfilename == '':
        elfilename = filename + '.el'
    try:
        with open(tgffilename, 'r') as inputfile:
            with open(elfilename, "w") as outputfile:
                phase = 'nodes'
                for line in inputfile:
                    if '#' in line.strip():
                        phase = 'edges'
                        continue
                    if phase == 'nodes':
                        continue
                    if phase == 'edges':
                        outputfile.write(line)
    except OSError:
        print "File not copied."
    results = elfilename
    
def edgelistfile_to_graph(elfilename):
    """ """
    return Graph.Read_Ncol(elfilename, directed=True)

def tgffile_to_graph(tgffilename, elfilename=''):
    """ TGF file to igraph graph. Wrapper for intermediate edgelist. """
    results = []
    if not tgffilename: raise ValueError('No tgf filename given.')
    if elfilename == '':
        elfilename = filename + '.el'
    try:
        elfilename = tgffile_to_edgelist(tgffilename, elfilename)
        results = edgelistfile_to_graph(elfilename)
    except OSError:
        print "File not copied."
    return results


def degree_glyph(indegree, outdegree, degreecount = 1, degreerange = (1,3)):
    """Return an igraph canvas glyph image based on indegree, outdegree."""
    canvas_ = canvas.canvas();

    ## temp manual flag - turn border off 0, variable 1, solid 2
    boxcolorflag=2
    ## temp manual flag - turn color background off and on
    fillcolorflag=1

    #### COLOR COUNT MAPPING
    # ## pyx color gradients
    # http://pyx.sourceforge.net/manual/color.html
    # http://pyx.sourceforge.net/manual/gradientname.html#gradientname
    # http://pydoc.net/Python/PyX/0.12/pyx.color/
    # ...hatching and fill patterns:
    # 
    # see pyx 2.x pattern.py
    # http://nullege.com/codes/show/src@p@y@pyfeyn-0.3.4@pyfeyn@feynml.py/481/pyx.pattern.hatched

    # ## python normalizing
    # ## http://stackoverflow.com/questions/26785354/normalizing-a-list-of-numbers-in-python/26785464
    # ## http://stackoverflow.com/questions/16514443/how-to-normalize-a-list-of-positive-and-negative-decimal-number-to-a-specific-ra
    #      old_min = min(input)
    #      old_range = max(input) - old_min
    # ## Here's the tricky part. You can multiply by the new range and divide by the old range, but that almost guarantees that the top bucket will only get one value in it. You need to expand your output range so that the top bucket is the same size as all the other buckets.
    #      new_min = -5
    #      new_range = 5 + 0.9999999999 - new_min
    #      output = [int((n - old_min) / old_range * new_range + new_min) for n in input]

    # norm = [float(i)/sum(raw) for i in raw]

    cmin = max([degreerange[0],1]) 
    cmax = degreerange[1]
    cnorm = float(0)
    try:
        cnorm = float(degreecount - cmin) / float(cmax-cmin) # norm = x[i]−min(x) / (max(x)−min(x))
    except ZeroDivisionError:
        cnorm = float(0);

    if fillcolorflag == 1:
        if cnorm > 0:
            print 'cmin/cmax: ' + str(cmin) + ' ' + str(cmax) + '    cnorm: ' + str(cnorm)
            canvas_.fill(path.rect(0, 0, 1, 1), [color.gradient.WhiteRed.getcolor(cnorm)])

    # # if outdegree == 1:
    # #     canvas_.fill(path.rect(0, 0, 1, 1), [color.rgb.red])
    # if outdegree == 1:
    #     canvas_.fill(path.rect(0, 0, 1, 1), [color.gradient.WhiteRed.getcolor(0.33)])
    # if outdegree == 2:
    #     canvas_.fill(path.rect(0, 0, 1, 1), [color.gradient.WhiteRed.getcolor(0.66)])
    # if outdegree == 3:
    #     canvas_.fill(path.rect(0, 0, 1, 1), [color.gradient.WhiteRed.getcolor(1.00)])

    dg_box = path.path(path.moveto(0, 0),
                       path.lineto(0, 1),
                       path.lineto(1, 1),
                       path.lineto(1, 0),
                       path.lineto(0, 0),
                       path.closepath()
                       )
    
    # boxcolor = color.cmyk(0, 0, 0, 0.25)
    # if (indegree == 0) and (outdegree == 0):
    #     boxcolor = color.cmyk.White
    # elif indegree == 0:
    #     boxcolor = color.cmyk.YellowGreen
    # elif outdegree == 0:
    #     boxcolor = color.cmyk.RedOrange
    
    if boxcolorflag == 1:     
        boxcolor = color.cmyk(0, 0, 0, 0.25)
        if (indegree == 0) and (outdegree == 0):
            boxcolor = color.cmyk.White
        elif indegree == 0:
            boxcolor = color.cmyk.YellowGreen
        elif outdegree == 0:
            boxcolor = color.cmyk.RedOrange   
        ## sort of works, but ugly
        ## https://sourceforge.net/p/pyx/mailman/message/3223332/
        # canvas_.stroke(path.rect(0, 0, 1, 1), [style.linewidth.Thick,
        #                              color.rgb.red,
        #                              deco.filled([pattern.hatched(.2 ,45)])])
        ## ugh
        # canvas_.stroke(dg_box, [boxcolor, style.linewidth(.1), pattern.hatched(.1,45)])
        
        ## manual bounding box
        canvas_.stroke(dg_box, [boxcolor, style.linewidth(.1)]) # manual bounding box
    elif boxcolorflag == 2:
        boxcolor = color.cmyk.Black
        ## reset box wider for cutter
        dg_box = path.path(path.moveto(-0.2, -0.2),
                           path.lineto(-0.2,  1.2),
                           path.lineto( 1.2,  1.2),
                           path.lineto( 1.2, -0.2),
                           path.lineto(-0.2, -0.2),
                           path.closepath()
                           )
        canvas_.stroke(dg_box, [boxcolor, style.linewidth(.05)]) # manual bounding box


    node_dot = path.circle(.5, .5, .15)
    canvas_.fill(node_dot)

    if indegree > 0:        
        gp = path.path(path.moveto( 0.5, 0.5  ),
                                path.lineto( 0.5, 0.75 )  # stub
                                )
        canvas_.stroke(gp, [style.linewidth(.1)])
        if indegree == 1:                
            gp = path.path(     path.moveto( 0.5, 0.5  ),
                                path.lineto( 0.5, 1    )   # indegree 1
                                )
            canvas_.stroke(gp, [style.linewidth(.1)])
        else:
            gp = path.path(     path.moveto( 0.5, 0.75 ),
                                path.lineto( 0,   0.75 ),  # crossbar
                                path.lineto( 1,   0.75 )
                                )
            canvas_.stroke(gp, [style.linewidth(.1)])
        if indegree > 1:
            # print range(0,indegree)
            for line in range(0,indegree):
                linef = float(line)
                indegreef = float(indegree-1)
                # print linef, indegreef, linef/indegreef
                gp = path.path( path.moveto( linef/indegreef, 1   ),
                                path.lineto( linef/indegreef, 0.75   ),  # line for each indegree
                                path.lineto( .5 , 0.75 )                 # round off the corner
                                )
                canvas_.stroke(gp, [style.linewidth(.1)])

    if outdegree > 0:        
        gp = path.path(path.moveto( 0.5, 0.5  ),
                                path.lineto( 0.5, 0.25 )  # stub
                                )
        canvas_.stroke(gp, [style.linewidth(.1)])
        if outdegree == 1:                
            gp = path.path(     path.moveto( 0.5, 0.5  ),
                                path.lineto( 0.5, 0    )   # outdegree 1
                                )
            canvas_.stroke(gp, [style.linewidth(.1)])
        else:
            gp = path.path(     path.moveto( 0.5, 0.25 ),
                                path.lineto( 0,   0.25 ),  # crossbar
                                path.lineto( 1,   0.25 )
                                )
            canvas_.stroke(gp, [style.linewidth(.1)])
        if outdegree > 1:
            # print range(0,outdegree)
            for line in range(0,outdegree):
                linef = float(line)
                outdegreef = float(outdegree-1)
                # print linef, outdegreef, linef/outdegreef
                gp = path.path( path.moveto( linef/outdegreef, 0    ),
                                path.lineto( linef/outdegreef, 0.25 ),  # line for each outdegree
                                path.lineto( .5 , 0.25 )                # round off the corner
                                )
                canvas_.stroke(gp, [style.linewidth(.1)])

    return canvas_


# def degree_glyph_old(indegree, outdegree): #2016-06-23 5:20p
#     """Return an igraph canvas glyph image based on indegree, outdegree."""
#     canvas_ = canvas.canvas();
#     dg_box = path.path(path.moveto(0, 0),
#                        path.lineto(0, 1),
#                        path.lineto(1, 1),
#                        path.lineto(1, 0),
#                        path.lineto(0, 0),
#                        path.closepath()
#                        )
#     canvas_.stroke(dg_box, [color.rgb.green]) # manual bounding box
#     node_dot = path.circle(.5, .5, .15)
#     canvas_.fill(node_dot)
#     in1 = path.path(path.moveto(.5, .5),
#                     path.lineto(.5, 1)
#                     )
#     in2 = path.path(path.moveto(0, 1),
#                     path.lineto(0, .75),
#                     path.lineto(1, .75),
#                     path.lineto(1, 1),
#                     path.moveto(.5, .5),
#                     path.lineto(.5, .75)
#                     )
#     out1 = path.path(path.moveto(.5, .5),
#                     path.lineto(.5, 0)
#                     )
#     out2 = path.path(path.moveto(0, 0),
#                     path.lineto(0, .25),
#                     path.lineto(1, .25),
#                     path.lineto(1, 0),
#                     path.moveto(.5, .5),
#                     path.lineto(.5, .25)
#                     )
###   inplus = path.path(path.moveto(1.25, .75),
###                       path.lineto(1.25, 1),
###                       path.moveto(1.1, .875),
###                       path.lineto(1.4, .875),
###                   )
###   outplus = path.path(path.moveto(1.25, 0),
###                       path.lineto(1.25, .25),
###                       path.moveto(1.1, .125),
###                       path.lineto(1.4, .125),
#                     )
#     if indegree == 1:
#         canvas_.stroke(in1, [style.linewidth(.1)])
#     if indegree == 2:
#         canvas_.stroke(in2, [style.linewidth(.1)])
#     if indegree == 3:
#         canvas_.stroke(in1, [style.linewidth(.1)])
#         canvas_.stroke(in2, [style.linewidth(.1)])
#         # canvas_.stroke(inplus, [style.linewidth(.1)])
#     if outdegree == 1:
#         canvas_.stroke(out1, [style.linewidth(.1)])
#     if outdegree == 2:
#         canvas_.stroke(out2, [style.linewidth(.1)])
#     if outdegree == 3:
#         canvas_.stroke(out1, [style.linewidth(.1)])
#         canvas_.stroke(out2, [style.linewidth(.1)])
#         # canvas_.stroke(outplus, [style.linewidth(.1)])
#     return canvas_


def pp_graph_stats(graph):
    print '\ngraph stats:'
    print '\n    degree:         ' + str(graph.degree())
    print '\n    indegree:       ' + str(graph.indegree())
    print '\n    outdegree:      ' + str(graph.outdegree())
    degrees = zip(graph.indegree(), graph.outdegree())
    print '\n    degree list:    ' + str(degrees)
    degrees_counter = Counter(degrees)
    # http://stackoverflow.com/questions/11055902/how-to-convert-a-counter-object-into-a-usable-list-of-pairs
    print '\n    degree counter: ' + str(degrees_counter)
    degrees_counter_list = list(degrees_counter.items())
    print '\n    degree counter list: '
    print degrees_counter_list
    degrees_counter_sorted = []
    for key in sorted(degrees_counter.iterkeys()): degrees_counter_sorted.append((key, degrees_counter[key]))
    print '\n    degree counter sorted: '
    print degrees_counter_sorted
    print '\n    distribution:   \n\n' + str(graph.degree_distribution(mode = 'ALL')) + '\n'
    print '\n        in-dist:        \n\n' + str(graph.degree_distribution(mode = 'IN')) + '\n'
    print '\n        out-dist:       \n\n' + str(graph.degree_distribution(mode = 'OUT')) + '\n'
    return degrees_counter_list, degrees_counter_sorted


# def signature():
#         ins  = 4
#         outs = 4
#         top = 4
#         scale = 1.5
#         
#         for i in range(ins):
#         	for o in range(outs):
#         		imgfilename = '../output/pyx_glyphs/' + 'pyx_glyph_' + str(i) + str(o) + '.png'
#         		c = degree_glyph(i,o); c.writeGSfile(filename=imgfilename)
#         
#         assert True



def batch_degree_glyph(indegree, outdegree):
    """"""
    return True



#### TWINE ANALYSIS

class twineFile():
    """ """

    def __init__(self, filename, **kwargs):
        self.filename = filename
        if not filename:
            raise ValueError('No tgf filename given.')

        self.format = kwargs.get('format', '')
        print 'FORMAT'
        print self.format

        self.elfilename = kwargs.get('elfilename', '')

        self.html_doc = ""
        self.html_doc = utils.txtfile_to_string(filename)
        self.html_doc = self.html_doc.replace('-', '')
        # stripping all hyphens because of bs4 voodoo http://stackoverflow.com/questions/25375351/beautifulsoup-unable-to-find-classes-with-hyphens-in-their-name
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        
        # print self.html_doc
        soup = BeautifulSoup(self.html_doc, 'html.parser')

        self.nodelist = []

        self.edgelist = []
        ## fake data
        # for i in [x for x in range(10)]:
        #     self.edgelist.append((i,i+1))
        # for i in [x for x in range(10)]:
        #     self.edgelist.append((i,i+2))
        # for i in [x for x in range(10)]:
        #     self.edgelist.append((i,i*2))

        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        # <tw-passagedata pid="1" name="node 1" tags="" position="575.5,480">[[node 2]]</tw-passagedata>

        ## THIS WORKS on an archive file exported from Twine 2 webmin -- could be extended to work with multiple stories in a file using:
        ##    passages = soup.twstorydata.twpassagedata

        if self.format == 'published':
            ## THIS WORKS on porpentine's howling dogs
            # view-source:view-source:http://slimedaughter.com/games/twine/howlingdogs/
            # view-source:https://commondatastorage.googleapis.com/itchio/html/226733-2206/index.html
            passages = soup.select('div[tiddler]')
            for psg in passages:
                pname = psg['tiddler']
                pid = ''

                self.nodelist.append((pname, pid)) # backwards because we are defining edges by names
                ## check passage contents for links
                ## regex match double-brackets:
                ## \[\[.*?\]\]
                ## https://regex101.com/r/qZ3fA1/2
                ## http://stackoverflow.com/questions/36442542/having-some-trouble-with-regex-and-double-brackets
                pat = re.compile(ur'\[\[.*?\]\]')
                # test_str = u"[[1,2,3],[3,5,3],[9,8,9]] aoeu [5,6,9] aoeu [[4,5,5]]"
                # print(re.findall(pat, test_str))
                for match in (re.findall(pat, psg.get_text())):
                    if "|" in match:
                        match = match.split('|')[1]
                    self.edgelist.append( ( pname.replace(' ','_') , match.replace('[','').replace(']','').replace(' ','_') ) ) # tuple: ( 'passage name' , matched '[[link 1]]' returned as 'link_1' )
                    ## broken somehow -- tried to add utils cleaning to make The Temple of No work
                    # self.edgelist.append( ( utils.tlabel(pname) , utils.tlabel(match.replace('[','').replace(']','')) ) ) # tuple: ( 'passage name' , matched '[[link 1]]' returned as 'link_1' )

        elif self.format == 'archive':
            passages = soup.find_all('twpassagedata')
            for psg in passages:
                pname = psg['name']
                pid = psg['pid']

                self.nodelist.append((pname, pid)) # backwards because we are defining edges by names
                ## check passage contents for links
                ## regex match double-brackets:
                ## \[\[.*?\]\]
                ## https://regex101.com/r/qZ3fA1/2
                ## http://stackoverflow.com/questions/36442542/having-some-trouble-with-regex-and-double-brackets
                pat = re.compile(ur'\[\[.*?\]\]')
                # test_str = u"[[1,2,3],[3,5,3],[9,8,9]] aoeu [5,6,9] aoeu [[4,5,5]]"
                # print(re.findall(pat, test_str))
                for match in (re.findall(pat, psg.get_text())):
                    self.edgelist.append( ( pname.replace(' ','_') , match.replace('[','').replace(']','').replace(' ','_') ) ) # tuple: ( 'passage name' , matched '[[link 1]]' returned as 'link_1' )

        print self.nodelist
        print self.edgelist
        
        
        
    def __str__(self):
        return "twineFile()"

    def __len__(self):    ##### not working for some reason ??
        return len(self.edgelist)
        
    def clean_nodes_edges(self):
        self.nodelist.sort()
        # rename any existing node names
        # in either node or edge references
        # to avoid id collisions
        change = '_'
        for idx, node in enumerate(self.nodelist):
            # if node[0][0].isdigit():
            self.nodelist[idx] = (change + node[0], node[1])
        for idx, edge in enumerate(self.edgelist):
            self.edgelist[idx] = (change + edge[0], edge[1])
        for idx, edge in enumerate(self.edgelist):
            self.edgelist[idx] = (edge[0], change + edge[1])

        # give ids to nodes missing ids (all of them for TwineFile)
        for idx, node in enumerate(self.nodelist):
            self.nodelist[idx] = (node[0], idx)

        for idx, node in enumerate(self.nodelist):
            node_name = node[0]
            node_id = node[1]
            # replace matching name based edges with id based edges
            for idx2, edge in enumerate(self.edgelist):
                e0 = edge[0]
                e1 = edge[1]
                if e0 == node_name:
                    e0 = str(node_id)
                if e1 == node_name:
                    e1 = str(node_id)
                self.edgelist[idx2] = (e0, e1)

        # extract edge names not found in node list
        id_counter = len(self.nodelist)
        for idx, edge in enumerate(self.edgelist):
            e0 = edge[0]
            e1 = edge[1]
            if not e0.isdigit():
                e0 = str(id_counter)
                self.nodelist.append((edge[0],e0))
                id_counter += 1
            if not e1.isdigit():
                e1 = str(id_counter)
                self.nodelist.append((edge[1],e1))
                id_counter += 1
            self.edgelist[idx] = (e0, e1)

        # clean node names -- no names in edge list anymore
        for idx, node in enumerate(self.nodelist):
            node_name = re.sub('[\W_]', '_', node[0], flags=re.UNICODE)
            self.nodelist[idx] = (node_name, node[1])
        
        # all strings
        for idx, node in enumerate(self.nodelist):
            self.nodelist[idx] = (str(node[0]), str(node[1]))
        for idx, edge in enumerate(self.edgelist):
            self.edgelist[idx] = (str(edge[0]), str(edge[1]))

        # # strip leading _ from node names
        for idx, node in enumerate(self.nodelist):
            self.nodelist[idx] = (str(node[0][1:]), node[1])

    def edge_duplicate_max(self, dupemax=0):
        if dupemax==0:
            # remove all duplicate edges
            self.edgelist = list(set(self.edgelist))
        else:
            countmax = dupemax + 1
            # prune high duplicate edge counts to max
            edgecounts = Counter(self.edgelist)
            for key in edgecounts:
                if edgecounts[key] > countmax:
                    edgecounts[key] = countmax
            self.edgelist = list(edgecounts.elements())

    def edge_remover(self, fun):
        # remove http links
        mylist = list(self.edgelist)
        for edge in self.edgelist:
            if fun(edge[0]) or fun(edge[1]):
                mylist.remove(edge)
        self.edgelist = mylist

    def node_name_shorten(self, length):
        # crop node names
        for idx, node in enumerate(self.nodelist):
            if len(node[0])>length:
                if length > 9:
                    self.nodelist[idx] = (node[0][:length-3] + '...', node[1])
                else:
                    self.nodelist[idx] = (node[0][:length], node[1])

    def node_orphans_remove(self):
        # remove orphan nodes
        mylist = list(self.nodelist)
        for node in self.nodelist:
            used = False
            for edge in self.edgelist:
                if node[1] == edge[0]:
                    used = True
                if node[1] == edge[1]:
                    used = True
            if not used:
                mylist.remove(node)
        self.nodelist = mylist


    def write_edgefile(self, temp=True):
        if self.elfilename == '':
            self.elfilename = self.filename + '.el'
        if temp:
            with tempfile.NamedTemporaryFile(delete=False) as fp:
                for line in self.edgelist:
                    fp.write('\t'.join(unicode(v).encode('ascii', 'ignore') for v in line)  + '\n')
            return fp.name
        else:
            try:
                with open(self.elfilename, "w") as outputfile:
                    for line in self.edgelist:
                        # print(line)
                        outputfile.write('\t'.join(unicode(v).encode('ascii', 'ignore') for v in line)  + '\n') # tab-delimit the tuples
                        ## UnicodeEncodeError: 'ascii' codec can't encode character u'\u2026' in position 7: ordinal not in range(128)
                        ## http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
                        ## .encode('utf-8').strip()
                        ## http://stackoverflow.com/questions/10880813/typeerror-sequence-item-0-expected-string-int-found
                        ## '\t'.join(str(v) for v in value_list)
                return self.elfilename
            except OSError:
                print "File not written."

    def write_sparse_edgefile(self):
        if self.elfilename == '':
            self.elfilename = self.filename + '.el'
        try:
            with open(self.elfilename, "w") as outputfile:
                outputfile.write('# Nodes\n')
                for nline in self.nodelist:
                    outputfile.write(str(nline[1]) + '\t\t' + str(nline[0]) + '\n')
                outputfile.write('\n# Edges\n')
                for eline in self.edgelist:
                    outputfile.write('\t'.join(unicode(v).encode('ascii', 'ignore') for v in eline)  + '\n')
            return self.elfilename
        except OSError:
            print "File not written."

    def to_graph(self, temp=False):
        """ TGF file to igraph graph. Writes an edgefile and passes the filename in for a graph object, as igraph's Read_Ncol can only load from a file."""
        # results = edgelistfile_to_graph(elfilename)
        return Graph.Read_Ncol(self.write_edgefile(temp), directed=True)




#### CURRENTLY UNUSED


def build_graph(edgelist):
    g = Graph(directed=True)
    e = [(a[0],a[1]) for a in edgelist[1]]
    # print e
    g.add_vertices(len(e))
    g.add_edges(e)
    return g
    
    #def test_build_graph(self):
    #    t = utils.tgf_to_list("../super_mario_bros/super_mario_bros-levels.tgf")
    #    g = build_graph(t)
    #    print g


def edgelistfile_to_edgelist(filename):
    results = []
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'r') as inputfile:
            for line in inputfile:
                results.append
    except OSError:
        print "File not copied."
    results = Graph.Read_Ncol(elfilename, directed=True)


def my__tgffile_to_graph(filename):
    """ """
    results = []
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'r') as inputfile:
            elfilename = filename + '.el'
            with open(elfilename, "w") as outputfile:
                phase = 'nodes'
                for line in inputfile:
                    if '#' in line.strip():
                        phase = 'edges'
                        continue
                    if phase == 'nodes':
                        continue
                    if phase == 'edges':
                        outputfile.write(line)
    except OSError:
        print "File not copied."
    results = Graph.Read_Ncol(elfilename, directed=True)
    # try:
    #     with open(elfilename, 'r') as elfile:
    #         # data = inputfile.read() # http://stackoverflow.com/questions/8240647/fast-data-move-from-file-to-some-stringio
    #         # data = data.split('#\n')
    #         # stream = StringIO.StringIO(str(data[1]))
    #         # print stream
    #         results = Graph.Read_Ncol(elfile, directed=True)
    # except OSError:
    #     print "File not loaded."

    # print results
    return results

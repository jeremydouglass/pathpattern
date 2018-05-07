# -*- coding: utf-8 -*-
"""Pathpattern core

Methods for converting branching structures
and visualizing them as glyphs and glyph set signatures.

Includes methods for extracting Twine data structures,
as well as converting, importing and outputting TGF format,
edge lists, and Edger-compatible 'sparse edge lists' for
later visualization using Edger.

"""

import logging
import tempfile
from collections import Counter
import regex as re
from bs4 import BeautifulSoup
from igraph import Graph
from pyx import canvas, color, path, style, trafo, unit

import pathpattern.utils as utils

logging.basicConfig(level=logging.WARNING)


class GlyphSet(object):
    """Glyph set for generating glyphs and signatures from edge lists."""
    def __init__(self, **kwargs):
        self.glist = []
        self.id = 0
        self.width = kwargs.get('width', 4)
        self.outdir = kwargs.get('outdir', './')
        self.prefix = kwargs.get('prefix', 'glyph_')
        self.uscale = kwargs.get('uscale', 1)
        self.mincount = 0
        self.maxcount = 3

        if 'graph' in kwargs and 'range' not in kwargs and 'list' not in kwargs:
            self.graph = kwargs.get('graph')

            degrees = set(zip(self.graph.indegree(), self.graph.outdegree()))  # a set -- no dups, no counts
            logging.debug('\n    degree list:    %s', str(degrees))

            degrees_counter = Counter(zip(self.graph.indegree(), self.graph.outdegree()))  # count dups
            logging.debug('* degrees_counter: ')
            logging.debug(degrees_counter)

            self.mincount = degrees_counter[min(degrees_counter, key=degrees_counter.get)]
            self.maxcount = degrees_counter[max(degrees_counter, key=degrees_counter.get)]
            logging.debug('* self.mincount: ')
            logging.debug(self.mincount)
            logging.debug('* self.maxcount: ')
            logging.debug(self.maxcount)
            logging.debug(degrees_counter)
            logging.debug('\n    degree counter: %s', str(degrees_counter))

            degrees_counter_list = list(degrees_counter.items())
            logging.debug('\n    degree counter list: ')
            logging.debug(degrees_counter_list)

            degrees_counter_sorted = []
            for key in sorted(degrees_counter.iterkeys()):
                degrees_counter_sorted.append((key, degrees_counter[key]))
            logging.debug(degrees_counter_sorted)

            for i in degrees_counter_sorted:
                self.glist.append((i[0][0], i[0][1], i[1]))

        elif 'list' in kwargs and 'range' not in kwargs:
            self.glist = kwargs.get('list')
        elif 'range' in kwargs and 'list' not in kwargs:
            self.inrange = kwargs.get('range')[0]
            self.outrange = kwargs.get('range')[1]
            for i in range(self.inrange[0], self.inrange[1]):
                for o in range(self.outrange[0], self.outrange[1]):
                    self.glist.append((int(i), int(o), 1))
        else:
            raise ValueError('invalid argument: provide one of the following:\n  range = ((xmin, xmax), (ymin, ymax))\n  list = [(ax, ay),(bx, by),(cx, cy)...]\n  graph = <igraph canvas.canvas object>')

        self.glist.sort(key=lambda x: (x[0], x[1]))  # http://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        # sorted -- any reason that custom list input order might matter? index lookup?

        # id string -- this isn't unique or unambiguous, but perhaps use different separators and/or do a hash later.
        flatlist = [str(element) for tupl in self.glist for element in tupl]  # http://stackoverflow.com/questions/3204245/how-do-i-convert-a-tuple-of-tuples-to-a-one-dimensional-list-using-list-comprehe
        self.id = ''.join(flatlist)

    def __str__(self):
        string = 'GlyphSet:\n'
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
        """replace all glist counts with 1"""
        newlist = []
        for i in self.glist:
            newlist.append((i[0], i[1], 1))
        self.glist = newlist

    def glyph(self, index):
        """ For a degree pair (in, out), render a glyph. """
        self.scale()
        if len(index) > 2:
            c = degree_glyph(index[0], index[1], index[2], (self.mincount, self.maxcount))
        else:
            c = degree_glyph(index[0], index[1], 1, (self.mincount, self.maxcount))
        return c

    def glyphs(self):
        """ For a list of degree pairs, render all glyphs and append to a list of glyphs. """
        clist = []
        for i in self.glist:
            clist.append(self.glyph(i))
        return clist

    def scale(self, val=0):
        """Interface to the global pyx scale: unit.set(uscale=val)
        Either sets scale directly or uses the instance variable default.
        0.25 scales to 25%, 3.0 scales to 300%.
        -  http://pyx.sourceforge.net/manual/unit.html
        -  http://nullege.com/codes/search/pyx.unit.set
        -  https://github.com/mjg/PyX/blob/master/test/unit/test_unit.py
        """

        if val == 0:
            val = self.uscale
        unit.set(uscale=val, defaultunit="inch")

    def write_glyph(self, index, overwrite=False):
        """ For a degree pair (in, out), save a glyph as a PNG file. """
        c = self.glyph(index)
        index_str = '_'.join(str(x).zfill(3) for x in index)
        imgfilepath = self.outdir + index_str + '.png'
        if not overwrite and utils.path.exists(imgfilepath):
            logging.debug(imgfilepath, " : exists (skip write)")
            return ''
        c.writeGSfile(filename=imgfilepath)
        return imgfilepath

    def write_glyphs(self):
        """ For a list of degree pairs, save all glyphs as PNG files. """
        for i in self.glist:
            self.write_glyph(i)
        return

    def signature(self, deg_max=6, padded=False, has_border=False):
        """ For a visualization of glyphs, lay out in a 2D grid PNG file. """
        self.scale()
        sig = canvas.canvas([trafo.rotate(90), trafo.mirror(0)])
        scale = 1.5
        if padded or has_border:
            sig_margin = 0.2
            x = (deg_max + 1) * scale + (1.5 * sig_margin)
            border_path = path.path(path.moveto(0, 0),
                                    path.lineto(0, x),
                                    path.lineto(x, x),
                                    path.lineto(x, 0),
                                    path.closepath())
            if padded:
                border_color = color.cmyk.White
            if has_border:
                border_color = color.cmyk.Gray
            sig.stroke(border_path, [border_color, trafo.translate(-sig_margin*2, -sig_margin*2), style.linewidth(.025)])

        for index in self.glist:
            if len(index) > 2:
                c = degree_glyph(index[0], index[1], index[2], (self.mincount, self.maxcount))
            else:
                c = degree_glyph(index[0], index[1], 1, (self.mincount, self.maxcount))
            sig.insert(c, [trafo.translate(index[0]*scale, (index[1])*scale)])  # text writing requires full latex
        return sig

    def write_signature(self, **kwargs):
        "Write signature to image file."
        c = self.signature(**kwargs)
        imgfilename = self.outdir + self.prefix + '_signature' + '.png'
        c.writeGSfile(filename=imgfilename)
        return imgfilename


class tgfFile(object):
    """TGF file for writing edges and nodes in the TGF format."""

    def __init__(self, filename, **kwargs):
        self.nodelist = []
        self.nodeset = set()
        self.nodedict = {}
        self.edgelist = []
        self.filename = filename
        if not filename:
            raise ValueError('No tgf filename given.')
        self.elfilename = kwargs.get('elfilename', '')

        try:
            with open(self.filename, 'r') as inputfile:
                phase = 'nodes'

                lines = (line.strip() for line in inputfile)  # all lines including the blank ones http://stackoverflow.com/questions/4842057/python-easiest-way-to-ignore-blank-lines-when-reading-a-file
                lines = (line for line in lines if line)  # non-blank lines

                for line in lines:
                    lt = line.strip().split('\t')  # line tuple
                    if '#' in line:
                        phase = 'edges'
                        continue
                    if phase == 'nodes':
                        self.nodeset.add(lt[0])
                        # self.nodedict.update({lt[0], ''})
                        # ADDING NODES TO DICT IS BROKEN
                        # self.nodedict.update({lt[0], lt[1:]})
                    if phase == 'edges':
                        self.edgelist.append(lt)
                        # tgf may have nodes which are only listed in edges
                        self.nodeset.add(lt[0])
                        self.nodeset.add(lt[1])
                        # only add keys-without-values if the values don't already exist
                        if not self.nodedict.get(lt[0]):  # no key or empty value
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
        return len(self.edgelist)

    def write_edgefile(self):
        """Write edge list to text file."""
        if self.elfilename == '':
            self.elfilename = self.filename + '.el'
        try:
            with open(self.elfilename, "w") as outputfile:
                for line in self.edgelist:
                    outputfile.write('\t'.join(line[:2]) + '\n')  # slice out edge labels to avoid igraph NCOL error, tab-delimit the tuples
            return self.elfilename
        except OSError:
            print "File not written."

    def to_graph(self):
        """ TGF file to igraph graph. Writes an edgefile and passes the filename in for a graph object, as igraph's Read_Ncol can only load from a file."""
        # results = edgelistfile_to_graph(elfilename)
        return Graph.Read_Ncol(self.write_edgefile(), directed=True)


def tgffile_to_edgelist(tgffilename, elfilename=''):
    """ TGF file to edgelist converter. """
    results = []
    if not tgffilename:
        raise ValueError('No tgf filename given.')
    if elfilename == '':
        elfilename = tgffilename + '.el'
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
    return results


def edgelistfile_to_graph(elfilename):
    """Stub passing an edgelist to igraph, returns an ncol graph object."""
    return Graph.Read_Ncol(elfilename, directed=True)


def tgffile_to_graph(tgffilename, elfilename=''):
    """TGF file to igraph graph. Wrapper for intermediate edgelist."""
    results = []
    if not tgffilename:
        raise ValueError('No tgf filename given.')
    if elfilename == '':
        elfilename = tgffilename + '.el'
    try:
        elfilename = tgffile_to_edgelist(tgffilename, elfilename)
        results = edgelistfile_to_graph(elfilename)
    except OSError:
        print "File not copied."
    return results


def degree_glyph(indegree, outdegree, degreecount=1, degreerange=(1, 3)):
    """Return an igraph canvas glyph image based on indegree, outdegree."""
    canvas_ = canvas.canvas()
    # box color - turn border off and on
    #   off, variable 1, solid 2, type colors 3
    boxcolorflag = 3
    # fill color - turn color background off and on
    #   background off 0, variable red 1, type colors 2
    fillcolorflag = 2

    cmin = max([degreerange[0], 1])
    cmax = degreerange[1]
    cnorm = float(0)
    try:
        # norm = x[i]−min(x) / (max(x)−min(x))
        cnorm = float(degreecount - cmin) / float(cmax-cmin)
    except ZeroDivisionError:
        cnorm = float(0)

    if fillcolorflag == 1:
        if cnorm > 0:
            logging.debug('cmin/cmax: %s %s    cnorm: %s', str(cmin), str(cmax), str(cnorm))
            canvas_.fill(path.rect(0, 0, 1, 1), [color.gradient.WhiteRed.getcolor(cnorm)])
    elif fillcolorflag == 2:
        if (indegree == 0) and (outdegree == 0):
            fillcolor = color.cmyk.White
        elif indegree == 0:
            fillcolor = color.cmyk.Green
        elif indegree == 1 and outdegree == 1:
            fillcolor = color.cmyk.Yellow
        elif outdegree == 0:
            fillcolor = color.cmyk.Red
        elif indegree == 1 and outdegree > 1:
            fillcolor = color.cmyk.ProcessBlue
        elif indegree > 1 and outdegree == 1:
            fillcolor = color.cmyk.Orange
        elif indegree > 1 and outdegree > 1:
            fillcolor = color.cmyk.Orchid
        else:
            fillcolor = color.cmyk.Black
        canvas_.fill(path.rect(0, 0, 1, 1), [fillcolor])

    dg_box = path.path(path.moveto(0, 0),
                       path.lineto(0, 1),
                       path.lineto(1, 1),
                       path.lineto(1, 0),
                       path.lineto(0, 0),
                       path.closepath())

    if boxcolorflag == 1:
        boxcolor = color.cmyk(0, 0, 0, 0.25)
        if (indegree == 0) and (outdegree == 0):
            boxcolor = color.cmyk.White
        elif indegree == 0:
            boxcolor = color.cmyk.YellowGreen
        elif outdegree == 0:
            boxcolor = color.cmyk.RedOrange
        # draw manual bounding box
        canvas_.stroke(dg_box, [boxcolor, style.linewidth(.1)])

    elif boxcolorflag == 2:
        boxcolor = color.cmyk.Gray  # Black
    elif boxcolorflag == 3:
        if (indegree == 0) and (outdegree == 0):
            boxcolor = color.cmyk.White
        elif indegree == 0:
            boxcolor = color.cmyk.Green
        elif indegree == 1 and outdegree == 1:
            boxcolor = color.cmyk.Yellow
        elif outdegree == 0:
            boxcolor = color.cmyk.Red
        elif indegree == 1 and outdegree > 1:
            boxcolor = color.cmyk.ProcessBlue
        elif indegree > 1 and outdegree == 1:
            boxcolor = color.cmyk.Orange
        elif indegree > 1 and outdegree > 1:
            boxcolor = color.cmyk.Orchid
        else:
            boxcolor = color.cmyk.Black
    if boxcolorflag == 2 or boxcolorflag == 3:
        # reset box wider for cutter
        dg_box = path.path(path.moveto(-0.2, -0.2),
                           path.lineto(-0.2, 1.2),
                           path.lineto(1.2, 1.2),
                           path.lineto(1.2, -0.2),
                           path.lineto(-0.2, -0.2),
                           path.closepath())
        # draw manual bounding box
        canvas_.stroke(dg_box, [boxcolor, style.linewidth(.05)])

    node_dot = path.circle(.5, .5, .15)
    canvas_.fill(node_dot)

    if indegree > 0:
        gp = path.path(path.moveto(0.5, 0.5),
                       path.lineto(0.5, 0.75))  # stub
        canvas_.stroke(gp, [style.linewidth(.1)])
        if indegree == 1:
            gp = path.path(path.moveto(0.5, 0.5),
                           path.lineto(0.5, 1.0))  # indegree 1
            canvas_.stroke(gp, [style.linewidth(0.1)])
        else:
            gp = path.path(path.moveto(0.5, 0.75),
                           path.lineto(0.0, 0.75),  # crossbar
                           path.lineto(1.0, 0.75))
            canvas_.stroke(gp, [style.linewidth(.1)])
        if indegree > 1:
            logging.debug(range(0, indegree))
            for line in range(0, indegree):
                linef = float(line)
                indegreef = float(indegree-1)
                logging.debug(linef, indegreef, linef/indegreef)
                gp = path.path(path.moveto(linef/indegreef, 1.00),
                               path.lineto(linef/indegreef, 0.75),  # line for each indegree
                               path.lineto(0.50, 0.75))  # round off the corner
                canvas_.stroke(gp, [style.linewidth(.1)])

    if outdegree > 0:
        gp = path.path(path.moveto(0.50, 0.50),
                       path.lineto(0.50, 0.25))  # stub
        canvas_.stroke(gp, [style.linewidth(.1)])
        if outdegree == 1:
            gp = path.path(path.moveto(0.50, 0.50),
                           path.lineto(0.50, 0.00))  # outdegree 1
            canvas_.stroke(gp, [style.linewidth(.1)])
        else:
            gp = path.path(path.moveto(0.50, 0.25),
                           path.lineto(0.00, 0.25),  # crossbar
                           path.lineto(1.00, 0.25))
            canvas_.stroke(gp, [style.linewidth(0.10)])
        if outdegree > 1:
            logging.debug(range(0, outdegree))
            for line in range(0, outdegree):
                linef = float(line)
                outdegreef = float(outdegree-1)
                logging.debug(linef, outdegreef, linef/outdegreef)
                gp = path.path(path.moveto(linef/outdegreef, 0.00),
                               path.lineto(linef/outdegreef, 0.25),  # line for each outdegree
                               path.lineto(0.50, 0.25))  # round off the corner
                canvas_.stroke(gp, [style.linewidth(0.10)])

    return canvas_


def pp_graph_stats(graph):
    """Log and return statistical discriptions of graph."""
    logging.info('\ngraph stats:')
    logging.info('\n    degree:         %s', str(graph.degree()))
    logging.info('\n    indegree:       %s', str(graph.indegree()))
    logging.info('\n    outdegree:      %s', str(graph.outdegree()))

    degrees = zip(graph.indegree(), graph.outdegree())
    logging.info('\n    degree list:    %s', str(degrees))

    degrees_counter = Counter(degrees)  # http://stackoverflow.com/questions/11055902/how-to-convert-a-counter-object-into-a-usable-list-of-pairs
    logging.info('\n    degree counter: %s', str(degrees_counter))

    degrees_counter_list = list(degrees_counter.items())
    logging.info('\n    degree counter list: ')
    logging.info(degrees_counter_list)

    degrees_counter_sorted = []
    for key in sorted(degrees_counter.iterkeys()):
        degrees_counter_sorted.append((key, degrees_counter[key]))

    logging.info('\n    degree counter sorted: ')
    logging.info(degrees_counter_sorted)
    logging.info('\n    distribution:\n\n%s', str(graph.degree_distribution(mode='ALL')) + '\n')
    logging.info('\n        in-dist: \n\n%s', str(graph.degree_distribution(mode='IN')) + '\n')
    logging.info('\n        out-dist:\n\n%s', str(graph.degree_distribution(mode='OUT')) + '\n')

    return degrees_counter_list, degrees_counter_sorted


class twineFile(object):
    """Twine analysis."""

    def __init__(self, filename, **kwargs):
        self.filename = filename
        if not filename:
            raise ValueError('No tgf filename given.')

        self.format = kwargs.get('format', '')
        logging.debug('format: %s', self.format)

        self.elfilename = kwargs.get('elfilename', '')

        self.html_doc = ""
        self.html_doc = utils.txtfile_to_string(filename)
        self.html_doc = self.html_doc.replace('-', '')
        # stripping all hyphens because of bs4 voodoo http://stackoverflow.com/questions/25375351/beautifulsoup-unable-to-find-classes-with-hyphens-in-their-name
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/

        logging.debug(self.html_doc)
        soup = BeautifulSoup(self.html_doc, 'html.parser')

        self.nodelist = []

        self.edgelist = []
        # fake data
        # for i in [x for x in range(10)]:
        #     self.edgelist.append((i,i+1))
        # for i in [x for x in range(10)]:
        #     self.edgelist.append((i,i+2))
        # for i in [x for x in range(10)]:
        #     self.edgelist.append((i,i*2))
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        # <tw-passagedata pid="1" name="node 1" tags="" position="575.5,480">[[node 2]]</tw-passagedata>

        # THIS WORKS on an archive file exported from Twine 2 webmin -- could be extended to work with multiple stories in a file using:
        #    passages = soup.twstorydata.twpassagedata

        if self.format == 'published':
            # THIS WORKS on porpentine's howling dogs
            # view-source:view-source:http://slimedaughter.com/games/twine/howlingdogs/
            # view-source:https://commondatastorage.googleapis.com/itchio/html/226733-2206/index.html
            passages = soup.select('div[tiddler]')
            for psg in passages:
                pname = psg['tiddler']
                pid = ''

                self.nodelist.append((pname.replace(' ', '_'), pid))
                # backwards because we are defining edges by names
                # check passage contents for links
                pat = re.compile(ur'\[\[.*?\]\]')
                for match in re.findall(pat, psg.get_text()):
                    if "|" in match:
                        match = match.split('|')[1]
                    self.edgelist.append((pname.replace(' ', '_'), match.replace('[', '').replace(']', '').replace(' ', '_')))
                    # tuple: ( 'passage name' , matched '[[link 1]]' returned as 'link_1' )
                    # broken somehow -- tried to add utils cleaning to make The Temple of No work
                    # self.edgelist.append( ( utils.tlabel(pname) , utils.tlabel(match.replace('[','').replace(']','')) ) )
                    # tuple: ( 'passage name' , matched '[[link 1]]' returned as 'link_1' )

        elif self.format == 'archive':
            passages = soup.find_all('twpassagedata')
            for psg in passages:
                pname = psg['name']
                pid = psg['pid']

                self.nodelist.append((pname, pid))
                # backwards because we are defining edges by names
                # check passage contents for links
                pat = re.compile(ur'\[\[.*?\]\]')
                for match in re.findall(pat, psg.get_text()):
                    self.edgelist.append((pname.replace(' ', '_'), match.replace('[', '').replace(']', ' ').replace(' ', '_')))
                    # tuple: ( 'passage name' , matched '[[link 1]]' returned as 'link_1' )

        logging.debug(self.nodelist)
        logging.debug(self.edgelist)

    def __str__(self):
        return "twineFile()"

    def __len__(self):  # not working for some reason ?
        return len(self.edgelist)

    def clean_nodes_edges_bak(self):
        """Draft Twine edge cleaning code."""
        self.nodelist.sort()
        for idx, node in enumerate(self.nodelist):
            tmpnode = '_' + str(idx) + '_' + re.sub(r'[\W_]', '_', node[0], flags=re.UNICODE)
            if tmpnode != node[0]:
                newnode = (tmpnode, node[1])
                self.nodelist[idx] = newnode
                for idx2, edge in enumerate(self.edgelist):
                    if edge[0] == node[0]:
                        self.edgelist[idx2] = (tmpnode, edge[1])
                for idx2, edge in enumerate(self.edgelist):
                    if edge[1] == node[0]:
                        self.edgelist[idx2] = (edge[0], tmpnode)
        for idx, edge in enumerate(self.edgelist):
            self.edgelist[idx] = (
                re.sub(r'[\W_]', '_', edge[0], flags=re.UNICODE),
                re.sub(r'[\W_]', '_', edge[1], flags=re.UNICODE)
                )

    def clean_nodes_edges(self):
        """Clean Twine edge list and node list data after initial import.

        Migrates name-based edges into a nodelist and creates unique ID numbers
        for all nodes and edges.

        Also reformats node names for compatability with further processing
        and for visualization -- e.g. join node names with _; crop long names.

        """
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
                self.nodelist.append((edge[0], e0))
                id_counter += 1
            if not e1.isdigit():
                e1 = str(id_counter)
                self.nodelist.append((edge[1], e1))
                id_counter += 1
            self.edgelist[idx] = (e0, e1)

        # clean node names -- no names in edge list anymore
        for idx, node in enumerate(self.nodelist):
            node_name = re.sub(r'[\W_]', '_', node[0], flags=re.UNICODE)
            self.nodelist[idx] = (node_name, node[1])

        # all strings
        for idx, node in enumerate(self.nodelist):
            self.nodelist[idx] = (str(node[0]), str(node[1]))
        for idx, edge in enumerate(self.edgelist):
            self.edgelist[idx] = (str(edge[0]), str(edge[1]))

        # strip leading _ from node names
        for idx, node in enumerate(self.nodelist):
            self.nodelist[idx] = (str(node[0][1:]), node[1])

    def edge_duplicate_max(self, dupemax=0):
        """Reduce duplicate edges if the duplicate count is greater than max.

        This is useful for visualizations in which large duplicate edge counts
        (e.g. 20, 50, 100) visually obscure other aspects of the graph.

        """
        if dupemax == 0:
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
        """Remove edges based on a function.

        Example: a lambda returning true if either edge name begins 'http'

        """
        mylist = list(self.edgelist)
        for edge in self.edgelist:
            if fun(edge[0]) or fun(edge[1]):
                mylist.remove(edge)
        self.edgelist = mylist

    def node_name_shorten(self, length):
        """Crop node names.

        Long cropped names are marked with an ellipsis.

        """
        for idx, node in enumerate(self.nodelist):
            if len(node[0]) > length:
                if length > 9:
                    self.nodelist[idx] = (node[0][:length-3] + '...', node[1])
                else:
                    self.nodelist[idx] = (node[0][:length], node[1])

    def node_orphans_remove(self):
        """Remove orphan nodes from node list.

        These are nodes not appearing in the edge list.
        In addition to cleaning up messy extracted data,
        This is useful after edge pruning -- for example,
        pruning http edges and then removing the orphaned
        nodes.

        """
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
        """Write simple edge list to file.

        By default returns a temporary file.

        This functionality is necessary because igraph's Graph.Read_Ncol
        cannot accept an in-memory object or stream, only a filename
        or file handle.

        """
        if self.elfilename == '':
            self.elfilename = self.filename + '.el'
        if temp:
            with tempfile.NamedTemporaryFile(delete=False) as fp:
                for line in self.edgelist:
                    fp.write('\t'.join(unicode(v).encode('ascii', 'ignore') for v in line) + '\n')
            return fp.name
        else:
            try:
                with open(self.elfilename, "w") as outputfile:
                    for line in self.edgelist:
                        # print(line)
                        outputfile.write('\t'.join(unicode(v).encode('ascii', 'ignore') for v in line) + '\n')  # tab-delimit the tuples
                        # UnicodeEncodeError: 'ascii' codec can't encode character u'\u2026' in position 7: ordinal not in range(128)
                        # http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
                        # .encode('utf-8').strip()
                        # http://stackoverflow.com/questions/10880813/typeerror-sequence-item-0-expected-string-int-found
                        # '\t'.join(str(v) for v in value_list)
                return self.elfilename
            except OSError:
                print "File not written."

    def write_sparse_edgefile(self):
        """Write edges and nodes to Edger-compatible sparse edge file."""
        if self.elfilename == '':
            self.elfilename = self.filename + '.el'
        try:
            with open(self.elfilename, "w") as outputfile:
                outputfile.write('# Nodes\n')
                for nline in self.nodelist:
                    outputfile.write(str(nline[1]) + '\t\t' + str(nline[0]) + '\n')
                outputfile.write('\n# Edges\n')
                for eline in self.edgelist:
                    outputfile.write('\t'.join(unicode(v).encode('ascii', 'ignore') for v in eline) + '\n')
            return self.elfilename
        except OSError:
            print "File not written."

    def to_graph(self, temp=False):
        """TGF file to igraph graph.

        Writes an edgefile and passes the filename in for a graph object,
        as igraph's Read_Ncol can only load from a file.

        """
        # results = edgelistfile_to_graph(elfilename)
        return Graph.Read_Ncol(self.write_edgefile(temp), directed=True)


# CURRENTLY UNUSED


# def batch_degree_glyph(indegree, outdegree):
#     """"""
#     return True


def build_graph(edgelist):
    """Builds a graph from an edgelist.

    To use on a TGF:
       g = build_graph(utils.tgf_to_list('edges.tgf'))

    """
    g = Graph(directed=True)
    e = [(a[0], a[1]) for a in edgelist[1]]
    g.add_vertices(len(e))
    g.add_edges(e)
    return g


def edgelistfile_to_edgelist(filename):
    """DRAFT: Load an edgelist file -- possibly not working."""
    results = []
    if not filename:
        raise ValueError('No filename given.')
    try:
        with open(filename, 'r') as inputfile:
            for line in inputfile:
                results.append
    except OSError:
        print "File not copied."
    results = Graph.Read_Ncol(elfilename, directed=True)
    return results


def my__tgffile_to_graph(filename):
    """DRAFT: Load a TGF file into a graph -- possibly not working."""
    results = []
    if not filename:
        raise ValueError('No filename given.')
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
    return results

# pathpattern DEV NOTES
2016-06-17 v1
2016-06-18 v2
2016-06-19 v3 ...

## MISC MESS

Hive plots:

-  hiveplot.net
-  https://bost.ocks.org/mike/hive/
-  https://bl.ocks.org/mbostock/2066421

Tabs

-  **** igraph metrics and viz: [Basic graph analytics using igraph](http://horicky.blogspot.com/2012/04/basic-graph-analytics-using-igraph.html)

Twine-Undum-like hypertext authoring frameworks

-  Twine https://emshort.wordpress.com/2012/11/10/choice-based-narrative-tools-twine/
-  Undum
   -  http://undum.com/games/tutorial.en.html
   -  https://github.com/idmillington/undum/blob/master/games/media/games/tutorial/tutorial.game.en.js
   -  http://sequitur.github.io/raconteur/
-  ChoiceScript
-  Ink Inklescript Inklewriter 
   -  Ink example The Intercept https://github.com/inkle/the-intercept/blob/master/Assets/Ink/TheIntercept.ink
   -  Inklewriter http://www.inklestudios.com/inklewriter/
      -  https://emshort.wordpress.com/2012/09/11/choice-based-narrative-tools-inklewriter/
-  http://ifwiki.org/index.php/Textallion
-  http://dendry.org/
-  varytale (dead)
   -  https://emshort.wordpress.com/2012/06/10/writing-for-varytale/
   -  http://www.intfiction.org/forum/viewtopic.php?f=22&t=19543 (dead)
   -  see http://pyramidifblog.blogspot.com/2015/07/alas-storynexus.html
-  StoryNexus (dead) http://storynexus.com/ 
-  StorySpace 3 https://emshort.wordpress.com/2016/04/28/mark-bernstein-on-hypertext-narrative/#more-20064
-  Wunderverse https://emshort.wordpress.com/2015/11/26/wunderverse/
-  ...gamebook format http://www.intfiction.org/forum/viewtopic.php?f=38&t=11641&start=0
-  

## python module project setup

#### install python module template

```bash

	cd /Users/jeremydouglass/Dropbox/journals/journal-dropbox-eaglefiler/Files/Pathpattern/pathpattern-master
	git clone https://github.com/kennethreitz/samplemod.git
	# ... now move contents into new folder, sans .git, then ...
	git init
	git add .
	git commit -m "Samplemod template"
```

#### setup python virtualenv

```bash

	source ~/.profile
	mkvirtualenv pathpattern
	workon pathpattern
```

#### customize template

```bash

	git mv sample pathpattern
	git rm tests/test_advanced.py 
	git mv tests/test_basic.py tests/tests.py
	git status
	git add LICENSE Makefile README.rst docs/ pathpattern/__init__.py requirements.txt setup.py tests/tests.py 
	git status
	git commit -m "customized template for pathpattern"
	git status
	git add docs/DEV-NOTES.md 
	git commit -m "tracking DEV-NOTES.md"
```

#### install python igraph

```bash

	pip install python-igraph
	pip install pyx
	pip install sphinx
	pip freeze > requirements.txt
	cat requirements.txt 
			python-igraph==0.7.1.post6
```

Note that `pip install igraph` is *not* correct -- and it came with a ton of unwanted dependencies.

> DeprecationWarning: To avoid name collision with the igraph project, this visualization library has been renamed to 'jgraph'. Please upgrade when convenient.

In order to uninstall and clean up the mess before starting over:

```bash

	deactivate
	rmvirtualenv pathpattern
```

##  igraph testing


Docs:

-  http://igraph.org/python/#docs
   -  motifs: http://igraph.org/python/doc/igraph.datatypes.TriadCensus-class.html
   -  motifs - "motifs_randesu": http://igraph.org/python/doc/igraph.GraphBase-class.html#motifs_randesu
      -  get_subisomorphisms_lad
	  -  is_dag()
   -  more on motifs from the igraph python documentation pdf: http://igraph.org/python/doc/python-igraph.pdf
   -  more on motifs from the c manual: http://igraph.org/c/doc/igraph-Motifs.html


Simple sample graph for all testing below:

	from igraph import Graph
	g = Graph(directed=True)
	g.add_vertices(11)
	g.add_edges([(0,1), (1,2), (1,3), (2,4), (2,5), (3,5), (3,6), (4,7), (4,8), (5,8), (5,9), (6,9), (6,10)])




### degree

Degree:
http://igraph.org/python/doc/tutorial/tutorial.html

List degrees

	g.degree()
	# or g.degree(type="all")
		[1, 3, 3, 3, 3, 4, 3, 1, 2, 2, 1]

	g.indegree()
	# or g.degree(type="in")
		[0, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1]

	g.outdegree()
	# or g.degree(type="out")
		[1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0]
	
	g.degree(8)
	# for a specific node
	2

	g.degree([2,3,4])
	# for a list of nodes
	[3, 3, 3]

Degree distribution:

http://igraph.org/python/doc/igraph.Graph-class.html#degree_distribution
http://igraph.org/python/doc/igraph.GraphBase-class.html#degree

	>>> print g.degree_distribution(mode = 'ALL')
	N = 11, mean +- sd: 2.3636 +- 1.0269
	[1, 2): *** (3)
	[2, 3): ** (2)
	[3, 4): ***** (5)
	[4, 5): * (1)
	>>> print g.degree_distribution(mode = 'IN')
	N = 11, mean +- sd: 1.1818 +- 0.6030
	[0, 1): * (1)
	[1, 2): ******* (7)
	[2, 3): *** (3)
	>>> print g.degree_distribution(mode = 'OUT')
	N = 11, mean +- sd: 1.1818 +- 0.9816
	[0, 1): **** (4)
	[1, 2): * (1)
	[2, 3): ****** (6)
	>>> 



	>>> g.indegree()
	[0, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1]
	>>> g.outdegree
	<bound method Graph.outdegree of <igraph.Graph object at 0x102a6d430>>
	>>> g.outdegree()
	[1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0]
	>>> degrees = zip(g.indegree(), g.outdegree())
	>>> print degrees
	[(0, 1), (1, 2), (1, 2), (1, 2), (1, 2), (2, 2), (1, 2), (1, 0), (2, 0), (2, 0), (1, 0)]

http://stackoverflow.com/questions/16013485/counting-the-amount-of-occurences-in-a-list-of-tuples

	>>> from collections import Counter
	>>> degrees_counter = Counter(degrees)
	>>> degrees_counter
	Counter({(1, 2): 5, (1, 0): 2, (2, 0): 2, (0, 1): 1, (2, 2): 1})

http://stackoverflow.com/questions/20950650/how-to-sort-counter-by-value-python
http://stackoverflow.com/questions/9001509/how-can-i-sort-a-dictionary-by-key

	for key in sorted(degrees_counter):
		print "%s: %s" % (key, degrees_counter[key])
	(0, 1): 1
	(1, 0): 2
	(1, 2): 5
	(2, 0): 2
	(2, 2): 1


... re sorting complex key, see also:
-  http://stackoverflow.com/questions/13523070/python-complex-dictionary-keys
-  https://bytes.com/topic/python/answers/455645-create-dict-two-lists


## dyad census

http://igraph.org/python/doc/igraph.Graph-class.html#dyad_census



## triad census

Triad Census:

http://igraph.org/python/doc/igraph.datatypes.TriadCensus-class.html
http://files.eric.ed.gov/fulltext/ED024086.pdf
http://www.inside-r.org/packages/cran/igraph/docs/triad.census
See also Davis, J.A. and Leinhardt, S. (1972). The Structure of Positive Interpersonal Relations in Small Groups. In J. Berger (Ed.), Sociological Theories in Progress, Volume 2, 218-251. Boston: Houghton Mifflin.

More, and more recent, on networks:

Understanding Social Effects in Online Networks (2015)
http://corescholar.libraries.wright.edu/cgi/viewcontent.cgi?article=2427&context=knoesis


Demo:

	>>> from igraph import Graph
	>>> g=Graph.Erdos_Renyi(100, 0.2, directed=True)
	>>> tc=g.triad_census()
	>>> print tc.t003   
	42898
	>>> print tc["030C"] 
	1289
	>>> tc._remap
	{'201': 10, '021C': 5, '021D': 3, '210': 14, '120U': 12, '030C': 9, '003': 0, '300': 15, '012': 1, '021U': 4, '120D': 11, '102': 2, '111U': 7, '030T': 8, '120C': 13, '111D': 6}
	>>> 


tc = g.triad_census()
print tc.t003   
print tc["030C"] 
tc._remap
print tc
print g

	021D
	A<-B->C, the out-star.
	021U
	A->B<-C, the in-star.

	021C
	A->B->C, directed line.

The only 

	>>> print tc["021D"] 
	6
	>>> print tc["021U"] 
	3
	>>> print tc["021C"] 
	14
	>>> print tc.t021C
	14
	>>> tc
	TriadCensus((71, 71, 0, 6, 3, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	>>> print tc
	003 : 71 | 012 : 71 | 102 :  0 | 021D:  6
	021U:  3 | 021C: 14 | 111D:  0 | 111U:  0
	030T:  0 | 030C:  0 | 201 :  0 | 120D:  0
	120U:  0 | 120C:  0 | 210 :  0 | 300 :  0
	>>> print tc._remap
	{'201': 10, '021C': 5, '021D': 3, '210': 14, '120U': 12, '030C': 9, '003': 0, '300': 15, '012': 1, '021U': 4, '120D': 11, '102': 2, '111U': 7, '030T': 8, '120C': 13, '111D': 6}

Motif Detection:

Reference: S. Wernicke and F. Rasche: FANMOD: a tool for fast network motif detection, Bioinformatics 22(9), 1152--1153, 2006.


#### beyond triads -- motifs of size 4? 5+?

https://lists.nongnu.org/archive/html/igraph-help/2011-01/msg00101.html

	from igraph import *
	for i in xrange(11):
		print Graph.Isoclass(4, i)


### tgf import-export in python


Surprisingly, very little.

Found this simple tgf renderer CallGraphVisitor.to_tgf -- here https://github.com/davidfraser/pyan/blob/master/pyan.py
	
	def to_tgf(self, **kwargs):
	        draw_defines = ("draw_defines" in kwargs  and  kwargs["draw_defines"])
	        draw_uses = ("draw_uses" in kwargs  and  kwargs["draw_uses"])

	        s = ''
	        i = 1
	        id_map = {}
	        for name in self.nodes:
	            for n in self.nodes[name]:
	                if n.defined:
	                    s += """%d %s\n""" % (i, n.get_short_name())
	                    id_map[n] = i
	                    i += 1
	                #else:
	                #    print >>sys.stderr, "ignoring %s" % n
        
	        s += """#\n"""
        
	        if draw_defines:
	            for n in self.defines_edges:
	                for n2 in self.defines_edges[n]:
	                    if n2.defined and n2 != n:
	                        i1 = id_map[n]
	                        i2 = id_map[n2]
	                        s += """%d %d D\n""" % (i1, i2)

	        if draw_uses:
	            for n in self.uses_edges:
	                for n2 in self.uses_edges[n]:
	                    if n2.defined and n2 != n:
	                        i1 = id_map[n]
	                        i2 = id_map[n2]
	                        s += """%d %d U\n""" % (i1, i2)
	        return s
	


misc: http://finzi.psych.upenn.edu/library/comato/html/read.tgf.html

#### NEW -- adding edges by name for tgf import

-  http://stackoverflow.com/questions/29715837/python-igraph-vertex-indices
-  ... http://igraph.org/python/doc/igraph.Graph-class.html


#### draw nodes!

Rendering degree distribution images:

Aside: I looked at python turtle (`import turtle`) -- so fun, and so appropriate to my image set! But unfortunately, no graphics out capabilities other than EPS -- a total pain.

Okay, PyX looks like it will work -- "The result of a PyX run is an EPS (= Encapsulated PostScript) file, a PS (= PostScript) file, a PDF (= Portable Document Format) file or a SVG (= Scalable Vector Graphics) file, which can be viewed, printed or imported into other applications."

...but when I tried to install on Reason3 laptop in my "pathpattern" virtualenv:

	pip install pyx

	Collecting pyx
	  Downloading PyX-0.14.1.tar.gz (2.5MB)
	    100% |████████████████████████████████| 2.5MB 1.2MB/s 
	No files/directories in /private/var/folders/3_/lk019dw94q32s0rk9s3445j80000gn/T/pip-build-wgsZxT/pyx/pip-egg-info (from PKG-INFO)

...it turns out that "If you still need to run PyX with Python 2, you should use version 0.12.1 which is designed to run with Python 2.3 up to 2.7." [pyxFAQ](http://pyx.sourceforge.net/pyxfaq/general_aspects_pyx.html).

https://pypi.python.org/pypi/PyX/0.12.1

So, this worked:

    pip search pyx
    pip install pyx==0.12.1
	
okay:

	def add_indegree(canvas, count):


	def add_outdegree(canvas, count):

	

From:
-  http://pyx.sourceforge.net/examples/drawing/path.html
-  http://pyx.sourceforge.net/examples/drawing/pathitem.html


def degree_glyph(indegree, outdegree):
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

ins  = 4
outs = 4

top = 4
scale = 1.5

grid = canvas.canvas()

for i in range(ins):
	for o in range(outs):
		imgfilename = 'pyx_glyph_' + str(i) + str(o) + '.png'
		c = degree_glyph(i,o); c.writeGSfile(filename=imgfilename)
		grid.insert(c, [trafo.translate(i*scale, (top-o)*scale)])
		# grid.text(i*scale, (top-o)*scale+.5, str(i)+'x'+str(o), [text.size(-3)]) ## print label

grid.writeGSfile(filename='pyx_grid.png')

mypage = document.page(grid, margin=1)
mydocument = document.document(mypage)
mydocument.writeSVGfile(filename='pyx_doc.svg')

c = degree_glyph(2,2); c.writeGSfile(filename='pyx_glyph_22.png')
c = degree_glyph(2,1); c.writeGSfile(filename='pyx_glyph_21.png')



It would be really useful to have SVG functions, but they are Python 3 only -- but there is PNG and JPEG support -- from the old pyx 0.12.1 manual -- canvas.rst:

   If device is None, but a filename with suffix is given, PNG files will
   be written using the png16m device and JPG files using the jpeg device.

so, after drawing some stuff:

	>>> c.writeGSfile(filename='pyxtest.png')
	>>> c.writeGSfile(filename='pyxtest.jpg')


http://pyx.sourceforge.net/examples/drawing/path.html


## making graphs acyclic

### simplify

http://www.inside-r.org/packages/cran/igraph/docs/simplify

### feedback arc set

feedback_arc_set(weights=None, method="eades")
source code 
Calculates an approximately or exactly minimal feedback arc set.

A feedback arc set is a set of edges whose removal makes the graph acyclic. Since this is always possible by removing all the edges, we are in general interested in removing the smallest possible number of edges, or an edge set with as small total weight as possible. 



## SOMEDAY - pyunicorn

complex python network library, has some motif code in it.

-  http://pik-potsdam.de/~donges/pyunicorn/
-  https://github.com/pik-copan/pyunicorn
-  https://github.com/pik-copan/pyunicorn/blob/master/pyunicorn/core/network.py



## python reading notes

Core data -- tuples etc.:

-  passing around 2D lists, ranges, slices:
   -  https://gist.github.com/stenof/47d2e007371a657e93b0
   -  http://www.dotnetperls.com/2d-python
   -  http://stackoverflow.com/questions/16548668/iterating-over-a-2-dimensional-python-list
   -  https://www.codecademy.com/en/forum_questions/5080da8d8868280200001098
   -  http://stackoverflow.com/questions/31924150/python-passing-a-range-into-a-function
   -  https://docs.python.org/2/library/functions.html#slice
   -  http://stackoverflow.com/questions/28652976/passing-array-range-as-argument-to-a-function
   -  http://stackoverflow.com/questions/14048728/generate-list-of-range-tuples-with-given-boundaries-in-python

-  split string into tuples:
   -  http://stackoverflow.com/questions/11001247/fastest-way-to-split-a-concatenated-string-into-a-tuple-and-ignore-empty-strings
   -  http://stackoverflow.com/questions/8113782/split-string-on-whitespace-in-python

-  ...loops and tuples:
   -  http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/loopsandtuples.html

-  split, csv module
   -  http://www.dotnetperls.com/split-python
   -  http://www.dotnetperls.com/csv-python

-  text to string variable
   -  http://stackoverflow.com/questions/8369219/how-do-i-read-a-text-file-into-a-string-variable-in-python

-  pretty printing nested data: lists of lists of tuples etc.:
   -  https://djangosnippets.org/snippets/2773/
   -  https://docs.python.org/2/library/pprint.html
   -  http://stackoverflow.com/questions/3229419/pretty-printing-nested-dictionaries-in-python
   -  http://stackoverflow.com/questions/15550617/how-to-force-pprint-to-print-one-list-tuple-dict-element-per-line

Import / Export:

-  ncol
-  edgelist
-  trivial graph format
   -  https://en.wikipedia.org/wiki/Trivial_Graph_Format
   -  see "to_tgf" example in code: https://github.com/davidfraser/pyan/blob/master/pyan.py

Classes:

-  parameters, optional parameters -- param, *args, **kwargs
   -  http://stackoverflow.com/questions/12399803/how-to-check-if-a-key-in-kwargs-exists
   -  http://stackoverflow.com/questions/1098549/proper-way-to-use-kwargs-in-python
   -  ...and class constructors: http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
   -  http://www.diveintopython.net/power_of_introspection/optional_arguments.html
-  classes
   -  class constructors and defaults http://stackoverflow.com/questions/2164258/multiple-constructors-in-python

iGraph:

-  igraph general
   -  http://igraph.org/python/doc/tutorial/tutorial.html
-  igraph problem -- edgelist import
   -  ended up using Ncol instead, as per:
   -  http://stackoverflow.com/questions/32513650/can-import-edgelist-to-igraph-python
   -  http://igraph.org/python/doc/igraph-pysrc.html#GraphBase.Read_Edgelist
-  ...file-like objects, e.g. StreamIO
   -  originally interested because the igraph Ncol interface only took a filename, not any in-memory object. Didn't end up using, just wrote a new file then read it in.
   -  http://stackoverflow.com/questions/8240647/fast-data-move-from-file-to-some-stringio
   -  https://docs.python.org/2/library/stringio.html
   -  https://pymotw.com/2/StringIO/
   -  http://stackoverflow.com/questions/1883326/using-python-how-do-i-to-read-write-data-in-memory-like-i-would-with-a-file
   -  http://stackoverflow.com/questions/28368659/is-it-possible-to-rewind-a-python-stringio-in-memory-file
   -  http://stackoverflow.com/questions/1368261/python-file-like-buffer-object
-  ...file copy
   -  http://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python

General programming:

-  flow control -- if etc.
   -  https://docs.python.org/2/tutorial/controlflow.html
   -  http://stackoverflow.com/questions/181530/python-style-multiple-line-conditions-in-ifs
-  strings
   -  http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method

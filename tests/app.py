# -*- coding: utf-8 -*-

from .context import pathpattern
from pathpattern import *

import unittest
import logging
import sys

from igraph import Graph

class TestAppSuite(unittest.TestCase):
    """Rendering test cases."""

    log = logging.getLogger( "TestAppSuite.test_app" )
    

    def test_A_GlyphSet_tgfFile(self):
        """ """
        print "\n\n\ntest_A_GlyphSet_tgfFile\n\n"

        datafiles    = [ '../input/tgf/Lies_(Rick_Pryll).tgf'
                       , '../input/tgf/love is not CYOA.txt.tgf'
                       , '../input/tgf/Paper_Pong.tgf'                      # core.py 177: IndexError: list index out of range 
                       , '../input/tgf/Queneau_a-story-as-you-like-it.tgf'
                       , '../input/tgf/Sheldon_cookie.tgf'                  # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/Thrusts of Justice.tgf'              # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/TutorText0.tgf'
                       , '../input/tgf/jsayers.tgf'
                       , '../super_mario_bros/super_mario_bros-levels.tgf'
                       , '../input/tgf/Yorick.txt.tgf'
                       , '../input/tgf/CYOA_018.tgf'
                       , '../input/tgf/CYOA_112.tgf'
                       , '../input/tgf/Hopscotch_combined.tgf'
                       , '../input/tgf/Hopscotch_TOC1.tgf'
                       , '../input/tgf/Hopscotch_TOC2.tgf'
                       ]

        tests = zip(datafiles)

        for t in tests:

            ## SETUP GRAPH
            # print t
            tf = tgfFile(t[0])
            tfg = tf.to_graph()

            ## CREATE GLYPHSET
            gs = GlyphSet(graph=tfg, outdir='../output/pyx_glyphs/', prefix=filelabel(t[0]))
            print '  id:  ' + gs.id
            print gs
            # print gs.gcounts

            ## WRITE SIGNATURE IMAGE W/COUNT COLORS
            gs.write_signature()
            
            ## WIPE COUNT COLORS AND WRITE GLYPH IMAGES
            ## We could recreate the gs Glyphset with new settings -- but not necessary.
            gs.nocounts()      # set all counts to 1
            gs.write_glyphs()  # write the glyph images
            ## Update the file prefix to avoid overwriting the first sig
            gs.prefix = gs.prefix + 'nocounts_'
            gs.write_signature()

            # print tf
            # print gsl
            # print gs
            # print 'len(tf):  ' + str(len(tf) )
            # # print 'len(tfg): ' + str(len(tfg))
            # print 'len(gsl): ' + str(len(gsl))
            # print 'len(gs): ' + str(len(gs))
            
            # self.assertEqual( len(tf), len(tfg))
            # self.assertEqual( len(gsl), len(gs))
            # self.assertEqual( len(gs), len(tf))
            # self.assertEqual( len(gs), len(tfg))
            # self.assertEqual( len(gsl), len(tf))
            # self.assertEqual( len(gsl), len(tfg))


    def test_AA_GlyphSet_tgfFile_batch(self):
        """ Collect a set of graphs into one huge metagraph """
        print "\n\n\ntest_A_GlyphSet_tgfFile_batch\n\n"

        datafiles    = [ '../input/tgf/Lies_(Rick_Pryll).tgf'
                       , '../input/tgf/love is not CYOA.txt.tgf'
                       , '../input/tgf/Paper_Pong.tgf'                      # core.py 177: IndexError: list index out of range 
                       , '../input/tgf/Queneau_a-story-as-you-like-it.tgf'
                       , '../input/tgf/Sheldon_cookie.tgf'                  # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/Thrusts of Justice.tgf'              # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/TutorText0.tgf'
                       , '../input/tgf/jsayers.tgf'
                       , '../super_mario_bros/super_mario_bros-levels.tgf'
                       , '../input/tgf/Yorick.txt.tgf'
                       , '../input/tgf/CYOA_018.tgf'
                       , '../input/tgf/CYOA_112.tgf'
                       , '../input/tgf/Hopscotch_combined.tgf'
                       , '../input/tgf/Hopscotch_TOC1.tgf'
                       , '../input/tgf/Hopscotch_TOC2.tgf'
                       ]

        tests = zip(datafiles)

        metagraph = Graph(directed=True)

        for t in tests:
            ## SETUP GRAPH
            # print t
            tf = tgfFile(t[0])
            tfg = tf.to_graph()
            metagraph = metagraph.disjoint_union(tfg)
            ## each graph is added to the main graph, then the combined will be rendered as normal
            ## http://stackoverflow.com/questions/12058917/simple-python-igraph-usage
            ## http://igraph.org/python/doc/igraph.GraphBase-class.html#disjoint_union
            
        ## CREATE GLYPHSET
        gs = GlyphSet(graph=metagraph, outdir='../output/pyx_glyphs/', prefix=filelabel('metagraph'))
        print '  id:  ' + gs.id
        print gs
        # print gs.gcounts

        gs.write_signature()  # write sig image w/ counts
        gs.nocounts()         # set all counts to 1
        gs.write_glyphs()     # write glyph images w/ no counts
        gs.prefix = 'metagraph_nocounts_'
        gs.write_signature()  # write sig image w/ counts


    def test_AAA_GlyphSet_tgfFile_diff(self):
        """ Calculate the difference between GlyphSets """
        print "\n\n\ntest_A_GlyphSet_tgfFile_batch\n\n"

        datafiles0   = [ '../input/tgf/CYOA_018.tgf' 
                       , '../input/tgf/Hopscotch_TOC1.tgf'
                       ]

        datafiles1   = [ '../input/tgf/CYOA_112.tgf'      
                       , '../input/tgf/Hopscotch_TOC2.tgf'
                       ]

        tests = zip(datafiles0,datafiles1)

        for t in tests:
            tf0 = tgfFile(t[0])
            tfg0 = tf0.to_graph()
            gs0 = GlyphSet(graph=tfg0, outdir='../output/pyx_glyphs/', prefix=filelabel(t[0]))
            gs0.write_signature()
            
            tf1 = tgfFile(t[1])
            tfg1 = tf1.to_graph()
            gs1 = GlyphSet(graph=tfg1, outdir='../output/pyx_glyphs/', prefix=filelabel(t[1]))
            gs1.write_signature() 
            

            ## our comparisons will be thrown off if glyphs have count numbers, so wipe them first
            gs0.nocounts()         # set all counts to 1
            gs1.nocounts()         # set all counts to 1

            ## if we were adding the lists, we would use +:
            ##   gsL = gs0.glist+gs1.glist
            ## ...but we are getting the difference:
            ## http://stackoverflow.com/questions/3462143/get-difference-between-two-lists
            ## e.g. list(set(liA) - set(liB))
            gsL = list(set(gs0.glist) - set(gs1.glist))
            gs = GlyphSet(list=gsL, outdir='../output/pyx_glyphs/', prefix=filelabel(t[0])+filelabel(t[1]))

            ## currently combining initialized lists in a new object messes up counts and throws an error, as the counts are preserved from their individual lists...?
            ##   e.g.  if r<0 or r>1 or g<0 or g>1 or b<0 or b>1: raise ValueError            
            ## ...counts were already stripped above, but just for good measure in case that changes,
            ## ...I'll just strip counts for now
            gs.nocounts()         # set all counts to 1
            gs.write_glyphs()     # write glyph images w/ no counts
            gs.write_signature()  # write sig image w/ counts

            

    def test_B_tgfFile(self):
        """ """
        print "\n\n\ntest_B_tgfFile\n\n"
        datafiles    = [ 
                         '../input/tgf/Lies_(Rick_Pryll).tgf'
                       , '../input/tgf/love is not CYOA.txt.tgf'
                       , '../input/tgf/Paper_Pong.tgf'                    # core.py line 177: IndexError: list index out of range
                       , '../input/tgf/Queneau_a-story-as-you-like-it.tgf'
                       , '../input/tgf/Sheldon_cookie.tgf'                # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/Thrusts of Justice.tgf'            # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/TutorText0.tgf'
                       , '../input/tgf/jsayers.tgf'
                       , '../super_mario_bros/super_mario_bros-levels.tgf'
                       , '../input/tgf/Yorick.txt.tgf'
                       , '../input/tgf/CYOA_018.tgf'
                       , '../input/tgf/CYOA_112.tgf'
                       , '../input/tgf/Hopscotch_combined.tgf'
                       , '../input/tgf/Hopscotch_TOC1.tgf'
                       , '../input/tgf/Hopscotch_TOC2.tgf'
                       ]
        edgecounts   = [ 82,
                         184,
                         336,
                         38,
                         22,
                         202,
                         40,
                         42,
                         42,
                         22,
                         108,
                         92,
                         209,
                         55,
                         154
                       ]
        tests = zip(datafiles, edgecounts)
        
        for t in tests:
            print t
            tf = tgfFile(t[0])
            self.assertTrue(tf.nodelist)
            self.assertTrue(tf.nodeset)
            self.assertTrue(tf.nodedict)
            self.assertTrue(tf.edgelist)
            self.assertTrue(tf.filename)
            # print tf
            self.assertEqual(len(tf),t[1])
            ef = tf.write_edgefile()
            print '  saving:  ' + str(ef) + '\n'

    def test_C_GlyphSet_ranges(self):
        """ """
        print "\n\n\ntest_C_GlyphSet_ranges\n\n"
        ranges       = [ ((1,3),(2,4)),
                         ((0,2),(1,2)),
                         ((0,4,'indegree',1),(0,4,'outdegree',1)), # label and 'counts' args ignored for ranges
                         ((0,4),(0,4)),
                         ((0,5),(0,5))
                       ]
        expect_len   = [  4,
                          2,
                         16,
                         16,
                         25
                       ]
        tests = zip(ranges,expect_len)

        for t in tests:
            print t 
            gs = GlyphSet(range=t[0], outdir='../output/pyx_glyphs/', prefix='test_GS_range_')
            print gs.id
            print gs
            # self.log.debug( 'len: ' + str(len(gs)) + ' : ' + str(t[1]))
            self.assertEqual( len(gs), t[1])
            gs.write_glyphs()
            gs.write_signature()
            # print gs.gcounts
            print '\n'

    def test_D_GlyphSet_lists(self):
        """ """
        print "\n\n\ntest_D_GlyphSet_lists\n\n"

        lists        = [ [(0,1),(1,0),(1,1),(1,2)]
                       , [(0,1),(1,0),(1,1),(1,2),(2,1),(1,3)]
                       , [(0,0),(0,1),(1,0),(1,1),(1,2),(1,3),(2,1),(2,2)]
                       , [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
                       , [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
                       #, [(0,1,20),(1,0,99),(1,1,50),(1,2,17)] # counts? will fail because degree_glyph isn't dynamically setting the range
                       , [(0,1,1),(1,0,2),(1,1,3),(1,2,2)]
                       ]
        expect_len   = [ 4
                       , 6
                       , 8
                       , 9
					   , 16
                       , 4
                       ]
        
        tests = zip(lists,expect_len)

        for t in tests:
            print t
            gs = GlyphSet(list=t[0], outdir='../output/pyx_glyphs/', prefix='test_GS_list_')
            print gs.id
            print gs
            # self.log.debug( 'len: ' + str(len(gs)) + ' : ' + str(t[1]))
            self.assertEqual( len(gs), t[1])
            gs.write_glyphs()
            gs.write_signature()
            # print gs.gcounts
            print '\n'

    def test_E_pp_graph_stats(self):

        def tprint(*args):
            for a in args:
                print a

        g = Graph(directed=True)
        g.add_vertices(11)
        g.add_edges([(0,1), (1,2), (1,3), (2,4), (2,5), (3,5), (3,6), (4,7), (4,8), (5,8), (5,9), (6,9), (6,10)])

        a, b = pp_graph_stats(g)

        print 'parse arguments:'
        tprint(1,2,3)
        tprint(a)
        tprint(b)
        tprint(a[0])
        tprint(*a)
        tprint(*a[0])
        tprint(*a[0][0])



    def test_twineFile(self):
        """ """
        print "\n\n\ntest_twineFile\n\n"

        datafiles    = [ '../input/twine/twine_archive.html'
                       , '../input/twine/howlingdogs.html'
                       , '../input/twine/The_Temple_of_No.html'
                       ]

        formats      = [ 'archive'
                       , 'published'
                       , 'published'
                       ]

        tests = zip(datafiles, formats)

        for t in tests:
            print t
            tf = twineFile(t[0], format=t[1])
            print tf
            len(tf)
            tfg = tf.to_graph()
            gs = GlyphSet(graph=tfg, outdir='../output/pyx_glyphs/', prefix=filelabel(t[0]))
            print '\n'
            gs.write_glyphs()
            gs.write_signature()



























        

#    def test_app(self):
#        outpath = '../output/pyx_glyphs/'
#
#        log = logging.getLogger( "TestAppSuite.test_app" )
#        log.debug( "test_app" )
#
#        log.debug( "0a. glyph set" )
#        gs = GlyphSet( list = [(0,0),(0,1),(1,1),(1,2),(2,1),(1,3),(1,0)], width=2 )
#        gs = GlyphSet( range = ((0,4),(0,4)) )
#        print len(gs) # count of glyphs
#        print gs      # print glyph tuples by width
#        gs.write_glyph((0,1))
#        gs.write_glyphs()
#        
#        log.debug( "0b. signature template" )
#        signature_template = gs.signature()
#        signature_template.writeGSfile(filename= outpath + 'signature_template.png')
#        signature_template.writeGSfile(filename= outpath + 'signature_template.jpg')
#
#        log.debug( "1. work: import data")
#        tgffile_to_edgelist('../super_mario_bros/super_mario_bros-levels.tgf','../super_mario_bros/super_mario_bros-levels.el')
#        smb_graph = edgelistfile_to_graph('../super_mario_bros/super_mario_bros-levels.el')
#        print smb_graph
#
#        log.debug( "2. work: stats")
#        smb_stats = pp_graph_stats(smb_graph)
#        print smb_stats # custom print http://stackoverflow.com/questions/1535327/how-to-print-a-class-or-objects-of-class-using-print
#        
#        log.debug( "3. work: signature")
#        smb_signature = signature(smb_graph)
#        print smb_signature
#        smb_signature.writeGSfile(filename= outpath + 'smb_signature.jpg')
#        # smb_sig.dump('../super_mario_bros/super_mario_bros-levels.sig.png')
#
#        log.debug( "4. work: find motif")
#        #
#
#        log.debug( "5. corpus: import data")
#        # corpus_graph_set = tgfdir_to_graph_set('')
#
#        log.debug( "6. corpus: stats")
#        # corpus_stats = pp_stats_set(corpus_graph_set)
#
#        log.debug( "7. corpus: signature")
#        #
#
#        log.debug( "8. corpus: find motif")
#        
#        
#        log.debug( "9. work / corpus: comparison stats")
#        #
#
#        log.debug( "10. work / corpus: comparison signature")
#        #
#
#        log.debug( "11. work / corpus: comparison motif")
#        #

if __name__ == '__main__':
    # create logger
    # logging.basicConfig( stream=sys.stderr )
    # logging.basicConfig( stream=sys.stderr, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' )
    logging.basicConfig( stream=sys.stderr, format='--------------------\n%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n' )

    logging.getLogger( "TestAppSuite.test_app" ).setLevel( logging.DEBUG )

    unittest.main()

    
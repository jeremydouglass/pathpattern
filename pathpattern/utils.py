# -*- coding: utf-8 -*-

from os import path

def list_to_string(list_, **kwargs):
    """Convert list_ into string. Accepts keyword 'join', default linebreak."""
    ## http://www.decalage.info/en/python/print_list_
    ## http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python
    ## str.strip -- http://stackoverflow.com/questions/7984169/using-strip-on-lists
    results = ''
    jointoken = '\n'
    if ('join' in kwargs): # http://stackoverflow.com/questions/14017996/python-optional-parameter
        jointoken = kwargs['join']
    list_ = map(str, list_)       ## convert any ints into strings
    list_ = map(str.strip, list_) ## strip whitespace
    list_ = jointoken.join(list_)      ## join list items into multi-line string
    results = list_
    return results


def string_to_list(string_):
    """Convert string into list_."""
    results = []
    results = [x.strip() for x in string_.splitlines()]
    results = list(filter(None, results))  ## remove blank lines from list -- http://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
    return results


def txtfile_to_list(filename):
    """Load file contents into list_ of lines."""
    ## http://stackoverflow.com/questions/18448847/import-txt-file-and-having-each-line-as-a-list_    
    results = []
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'r') as inputfile:
            for line in inputfile:
                results.append(line.strip().replace(" ", ""))  ## replace all whitespace
                # results.append(line.strip())                 ## strip line end whitespace
                # results.append(line.strip().split(','))      ## strip and split on comma
    except OSError:
        print "File did not load."
    return results


def list_to_txtfile(list_, filename):
    """Save list_ of lines into text file."""
    ## http://stackoverflow.com/questions/899103/writing-a-list_-to-a-file-with-python
    if not list_: raise ValueError('No data to write.')
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'w') as outputfile:
            for item in list_:
                print>>outputfile, item
    except OSError:
        print "File not written."


def txtfile_to_string(filename):
    """ """
    ## http://stackoverflow.com/questions/8369219/how-do-i-read-a-text-file-into-a-string-variable-in-python
    results = ""
    if not filename: raise ValueError('No filename given.')
    with open(filename, 'r') as inputfile:
        results=inputfile.read()
        # results=inputfile.read().replace('\n', '')
    return results


def string_to_txtfile(string_, filename):
    """Save string into text file."""
    ## http://stackoverflow.com/questions/899103/writing-a-list_-to-a-file-with-python
    if not string_: raise ValueError('No data to write.')
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'w') as outputfile:
            print>>outputfile, string_
            # outputfile.write(string_)
    except OSError:
        print "File not written."


### STRING UTILS

def filelabel(fpath):

    ## filepath manipulation http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    f_path = path.basename(fpath)                   #  'love is not CYOA.txt.tgf'
    f_file, f_ext = path.splitext(f_path)  #  '../input/tgf/love is not CYOA.txt'  '.tgf'
    ## clean filename for prefix label -- pyx complains: ValueError: for security reasons, only characters, digits and the characters '_-./' are allowed in filenames
    ## addressing as per: http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
    f_label = f_file.strip().replace (' ', '_').replace('.','_')
    delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum() and not c=='_' and not c=='-')   
    f_label = f_label.translate(None, delchars) + '_'
    return f_label


def tlabel(lstr):
    ltxt = lstr.strip().replace(' ', '_').replace('.','_')
    delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum() and not c=='_')
    ltxt = ltxt.translate(None, delchars)
    return ltxt


### HTML UTILS


def html_wrap(html_string):
    """Add an html-head-body wrapper around an html string."""
    html_prefix="""<html>
        <head>
            <title>HTML CSS TESTS</title>
            <link rel="stylesheet" type="text/css" href="tests/manual html-css tests/html-css.css">
        </head>
        <body>"""
    html_postfix="""
    </body></html>
    """    
    return html_prefix + html_string + html_postfix


### JSON UTILS


def list_to_jsonfile(list_, filename):
    """Save list_ of lines into JSON file."""
    ## http://stackoverflow.com/questions/899103/writing-a-list_-to-a-file-with-python
    import json
    if not list_: raise ValueError('No data to write.')
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'w') as outputfile:
            json.dump(list_, outputfile)
    except OSError:
        print "File did not load."


def jsonfile_to_list(filename):
    """Load list_ of lines from JSON file."""
    ## http://stackoverflow.com/questions/899103/writing-a-list_-to-a-file-with-python
    import json
    if not filename: raise ValueError('No filename given.')
    results = []
    try:
        with open(filename, 'r') as inputfile:
            results = json.load(inputfile)
    except OSError:
        print "File did not load."
    return results


### PICKLE UTILS


def list_to_picklefile(list_, filename):
    """Save list_ of lines into pickle file."""
    ## https://docs.python.org/3/library/pickle.html
    ## http://stackoverflow.com/questions/899103/writing-a-list_-to-a-file-with-python
    import pickle
    if not list_: raise ValueError('No data to write.')
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'w') as outputfile:
            pickle.dump(list_, outputfile, pickle.HIGHEST_PROTOCOL)
    except OSError:
        print "File did not load."


def picklefile_to_list(filename):
    """Load list_ of lines from pickle file."""
    ## https://docs.python.org/3/library/pickle.html
    ## http://stackoverflow.com/questions/899103/writing-a-list_-to-a-file-with-python
    results = []
    import pickle
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'r') as inputfile:
            results = pickle.load(inputfile)
    except OSError:
        print "File did not load."
    return results


### TGF UTILS


def tgf_to_list(filename):
    """Load tgf file contents into two lists of nodes and of edges."""
    ## http://stackoverflow.com/questions/18448847/import-txt-file-and-having-each-line-as-a-list_    
    results = []
    tgf_nodes = []
    tgf_edges = []
    if not filename: raise ValueError('No filename given.')
    try:
        with open(filename, 'r') as inputfile:
            phase = 'nodes'
            for line in inputfile:
                if '#' in line.strip():
                    phase = 'edges'
                    continue
                if phase == 'nodes':
                    # print 'node: ' + str(line)
                    tgf_nodes.append(tuple(line.split()))
                if phase == 'edges':
                    # http://stackoverflow.com/questions/11001247/fastest-way-to-split-a-concatenated-string-into-a-tuple-and-ignore-empty-strings
                    # print 'edge' + str(line)
                    tgf_edges.append(tuple(line.split()))
    except OSError:
        print "File did not load."
    results.append(tgf_nodes)
    results.append(tgf_edges)
    return results


## JINJA2 UTILS



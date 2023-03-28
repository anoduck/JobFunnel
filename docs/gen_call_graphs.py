#! /usr/bin/env python3

# This file was created because of a bug in pyan3
# that prevents it from running in shell.
# NOTE: You will need to call this from the REPO root folder.

import pyan
import os


def write_file(FILE, FORMAT, callgraph):
    """
    Purpose: write graphs to file.
    """
    graph_dir = os.path.abspath('./call_graphs')
    basename = os.path.basename(FILE)
    filename = basename.replace('py', FORMAT)
    to_write = graph_dir + '/' + filename
    with open(to_write, 'w') as f:
        f.write(callgraph)
        print('Wrote file:' + to_write + '\n')
# end def


def gen_html(to_parse):
    """
    Purpose: Generate html files
    """
    FORMAT = 'html'
    for file in to_parse:
        FILE = file
        callgraph = pyan.create_callgraph(FILE, format=FORMAT, colored=True,
                                          draw_uses=True, nested_groups=True)
        write_file(FILE, FORMAT, callgraph)
        print('Completed:' + FORMAT + '\n')
# end def


def gen_dot(to_parse):
    """
    Purpose: Generate dot graphs
    """
    FORMAT = 'dot'
    for file in to_parse:
        FILE = file
        callgraph = pyan.create_callgraph(FILE, format=FORMAT, colored=True,
                                          draw_uses=True, nested_groups=True)
        write_file(FILE, FORMAT, callgraph)
        print('Completed:' + FORMAT + '\n')
# end def


def gen_svg(to_parse):
    """
    Purpose: Generate dot graphs
    """
    FORMAT = 'svg'
    for file in to_parse:
        FILE = file
        callgraph = pyan.create_callgraph(FILE, format=FORMAT, colored=True,
                                          draw_uses=True, nested_groups=True)
        write_file(FILE, FORMAT, callgraph)
        print('Completed:' + FORMAT + '\n')
# end def


def main():
    """
    Purpose: generate graphviz graphs in dot and html.
    """
    backend_dir = os.path.abspath('../jobfunnel/backend')
    filters_file = backend_dir + '/tools/filters.py'
    indeed_file = backend_dir + '/scrapers/indeed.py'
    jobfunnel_file = backend_dir + '/jobfunnel.py'
    to_parse = [filters_file, indeed_file, jobfunnel_file]
    dis_dir = os.path.basename(os.getcwd())
    if dis_dir == "docs":
        gen_dot(to_parse)
        gen_html(to_parse)
        gen_svg(to_parse)
        print('Graphs are Generated!')
    else:
        print('No, no... You are not executing this from the docs dir.')
        exit(1)
# end def


if __name__ == '__main__':
    main()

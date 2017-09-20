#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt

ifile = ""
tfile = ""

try:
        # sys.argv[1:]
	#	 - a argument list to be parsed.
        # 'hi:t:'
        #       - short_options, a list of strings with the names of the short options.
        #       - options that require an argument followed by a colon (':')
        # ['input = ', 'target = ']
	#	 - long_options, a list of strings with the names of the long options.
        # return value:
        #       opts - a list of (option, value) pairs;
        #       args - the list of program arguments left after the option list was stripped
        
        opts, args = getopt.getopt(sys.argv[1:], 'hi:t:', ['input = ', 'target = '])
        
except getopt.GetoptError:
        # This is raised when an unrecognized option is found in the argument list
        # or when an option requiring an argument is given none.
        
        print('./setCommandLineOptions.py -i <inputfile> -t <targetfile>')
        sys.exit()

for opt, arg in opts:
        if opt in ["-h", "--help"]:
                print("usage: ./setCommandLineOptions.py -i <inputfile> -t <targetfile>")
                sys.exit()
        elif opt in ["-i", "--input"]:
                ifile = arg
        elif opt in ["-t", "--target"]:
                tfile = arg

# check if get 
print("input file is ", ifile)
print("target file is ", tfile)

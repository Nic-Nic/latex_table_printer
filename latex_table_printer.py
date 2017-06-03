# -*- coding: utf-8 -*-

'''
LaTeX table printer v0.0.1

Copyright (C) 2017 Nicolàs Palacio

Contact: nicolaspe91@gmail.com

GNU-GLPv3:
This program is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
PARTICULAR PURPOSE. See the GNU General Public License for more details.

A full copy of the GNU General Public License can be found on file 
"LICENSE.md". If not, see <http://www.gnu.org/licenses/>.
'''

import sys

__all__ = ['print_latex_table']

def print_latex_table(filename, sep = '\t', rownames = True):
    '''
    This function reads a given table file and prints out the corresponding 
    LaTeX tabular environment.

    * Arguments:
        - filename [str]: The file name or path where the data is stored. It is 
          supposed that each line corresponds to a row of the table.
        - sep [str]: Optional, '\\t' (tab) by default. Separator between 
          entries/cells of the table. For instance, if the file is in .csv 
          format, the separator should be a comma (',').
        - rownames [bool]: Optional, True by default. Determines if the first 
          column (typically, where the row names are) of the table should be 
          included.
    '''

    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            row = line.split(sep) if rownames else line.split(sep)[1:]
            row[-1] = row[-1].rstrip()

            if i == 0:
                print '\\begin{tabular}{|%s}' %('c|' * len(row))

            print '\\hline'
            print '&'.join(row) + '\\\\'

        print '\\hline'
        print '\\end{tabular}'

if __name__ == '__main__':
    # Default args
    sep = '\t'; rownames = True

    for i, arg in enumerate(sys.argv):
        if i < 2: continue

        if arg == '-s' or arg == '--sep':
            sep = raw_input('Specify the separator character: ')
            print '\n'

        elif arg == '-r' or arg == '--rownames':
            rownames = False            

    print_latex_table(sys.argv[1], sep = sep, rownames = rownames)

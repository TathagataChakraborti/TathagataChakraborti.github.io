#!/usr/bin/env bash

'''
------
Auto-compile Webpages for ICAPS 2019 Homepage
------
Author :: Tathagata Chakraborti
Date   :: 10/10/2018
------
'''


'''
packages
'''

import openpyxl as xl
import argparse, sys, random

'''
global variables 
'''

data = {} 

'''
html templates
'''

with open('templates/index-template.html', 'r') as temp:
    index_template = temp.read()

with open('templates/cfp-template.html', 'r') as temp:
    cfp_template = temp.read()

with open('templates/header-template.html', 'r') as temp:
    header_template = temp.read()

with open('templates/navbar-template.html', 'r') as temp:
    navbar_template = temp.read()

with open('templates/dates-template.html', 'r') as temp:
    dates_template = temp.read()

with open('templates/quicklinks-template.html', 'r') as temp:
    quicklinks_template = temp.read()

'''
method :: cache data from xlxs file
'''
def cache(filename = 'data.xlsx'):

    global data

    wb = xl.load_workbook(filename)

    # print wb['topics'][1]   
    # for item in wb['topics'][1]   

    # keys = [str(item.value) for item in wb[sheet_name][1]][:max_col]

    # for row in wb[sheet_name].iter_rows(min_row=min_row, max_col=max_col, max_row=max_row):

    #   temp[str(row[0].value)] = {}
    #   for i in range(1, len(keys)):
    #       temp[str(row[0].value)][keys[i]] = str(row[i].value)

'''
method :: write index.html
'''
def write_file(args):

    global index_template, cfp_template

    # cache data
    print 'Reading data...'
    cache()

    # write problem file
    print 'Compiling index.html ...'

    # writing templates
    print 'Writing templates ...'

    index_template = index_template.replace('[HEADER]', header_template)    
    index_template = index_template.replace('[NAVBAR]', navbar_template)    
    index_template = index_template.replace('[DATES]', dates_template)    
    index_template = index_template.replace('[QUICKLINKS]', quicklinks_template)    

    index_template = index_template.replace('[INDEX]', '')
    index_template = index_template.replace('[CFP]', 'cfp.html')

    # write primary carousel section
    print 'Writing carousel ...'

    # write to output
    print 'Writing to file (../temp.html) ...'

    with open('../index.html', 'w') as output_file:
        output_file.write(index_template)

    # write problem file
    print 'Compiling CFP.html ...'

    # writing templates
    print 'Writing templates ...'

    cfp_template = cfp_template.replace('[HEADER]', header_template)    
    cfp_template = cfp_template.replace('[NAVBAR]', navbar_template)    
    cfp_template = cfp_template.replace('[DATES]', dates_template)    
    cfp_template = cfp_template.replace('[QUICKLINKS]', quicklinks_template)    

    cfp_template = cfp_template.replace('[INDEX]', 'index.html')
    cfp_template = cfp_template.replace('[CFP]', '')

    with open('../cfp.html', 'w') as output_file:
        output_file.write(cfp_template)

    print 'Done.'


'''
method :: main
'''
def main():

    parser = argparse.ArgumentParser(description='''Auto-compile Webpages of ICAPS 2019 Homepage.''', epilog='''Usage >> python compile_carousel.py''')
    args = parser.parse_args()

    if '-h' in sys.argv[1:]:
        print parser.print_help()
        sys.exit(1)
    else:
        write_file(args)


if __name__ == "__main__":
    main()

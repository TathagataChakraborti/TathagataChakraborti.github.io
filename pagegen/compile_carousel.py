#!/usr/bin/env bash

'''
------
Auto-compile carousel section for ICAPS 2019 homepage
------
Author :: Tathagata Chakraborti
Date   :: 01/01/2018
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
html blobs 
'''


'''
method :: cache data from xlxs file
'''
def cache(filename = 'data.xlsx'):

	global data

	wb = xl.load_workbook(filename)

	print wb['topics'][1]	
	# for item in wb['topics'][1]	

	# keys = [str(item.value) for item in wb[sheet_name][1]][:max_col]

	# for row in wb[sheet_name].iter_rows(min_row=min_row, max_col=max_col, max_row=max_row):

	# 	temp[str(row[0].value)] = {}
	# 	for i in range(1, len(keys)):
	# 		temp[str(row[0].value)][keys[i]] = str(row[i].value)

'''
method :: write index.html
'''
def write_file(dummy_option):

	# cache data
	print 'Reading data...'
	cache()

	# write problem file
	print 'Compiling index.html ...'

	with open('index_template.html', 'r') as index_template_file:
		index_template = index_template_file.read()

	# write primary carousel section
	print 'Writing primary carousel section ...'


	# write secondary carousel section
	print 'Writing secondary carousel section ...'

	# write to output
	print 'Writing to file (../temp.html) ...'

	with open('../temp.html', 'w') as output_file:
		output_file.write(index_template)

	print 'Done.'


'''
method :: main
'''
def main():

    parser = argparse.ArgumentParser(description='''Auto-compile carousel section of ICAPS 2019 Homepage.''', epilog='''Usage >> python compile_carousel.py''')

    parser.add_argument('-d', '--dummy', action='store_true', help="Make dummy carousel section.")

    args = parser.parse_args()

    if '-h' in sys.argv[1:]:
        print parser.print_help()
        sys.exit(1)
    else:
		write_file(args.dummy)    	


if __name__ == "__main__":
	main()
	   

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
import argparse, sys, random, copy

reload(sys)
sys.setdefaultencoding('utf-8')

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
carousel templates
'''

with open('templates/carousel-elements/carousel-template.html', 'r') as temp:
    carousel_template = temp.read()

with open('templates/carousel-elements/carousel-entry-template.html', 'r') as temp:
    carousel_entry_template = temp.read()

with open('templates/carousel-elements/carousel-entry-link-template.html', 'r') as temp:
    carousel_entry_link_template = temp.read()

with open('templates/carousel-elements/carousel-inner-template.html', 'r') as temp:
    carousel_inner_template = temp.read()

with open('templates/carousel-elements/carousel-indicators-template.html', 'r') as temp:
    carousel_indicators_template = temp.read()

'''
method :: cache data from xlxs file
'''
def cache(filename = 'data.xlsx'):

    global data

    wb = xl.load_workbook(filename)

    count = 0

    for item in wb['items']:

        new_entry = [str(elem.value) for elem in item]

        if not count: keys = new_entry
        else:

            data[count] = {}
            inner_count  = 0

            for key in keys:

                data[count][key] = new_entry[inner_count]
                inner_count += 1

        count += 1

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

    carousel_indicators = ''
    carousel_inner = ''
    carousel_entries = ''

    for key in data:

        carousel_indicator = copy.deepcopy(carousel_indicators_template) 
        carousel_indicator = carousel_indicator.replace('[NUMBER]', str(key))

        if key == 1:
            carousel_indicator = carousel_indicator.replace('class', 'class="active"')

        carousel_indicators += carousel_indicator

        local_carousel_inner = copy.deepcopy(carousel_inner_template)

        local_carousel_inner = local_carousel_inner.replace('[NUMBER]', str(key)) 
        local_carousel_inner = local_carousel_inner.replace('[Name]', data[key]['Name']) 
        local_carousel_inner = local_carousel_inner.replace('[Image]', data[key]['Image']) 

        carousel_inner += '\n\n' + local_carousel_inner

        carousel_entry = copy.deepcopy(carousel_entry_template) 
        carousel_entry = carousel_entry.replace('[NUMBER]', str(key))

        for inner_key in data[key]:

            new_entry = ""

            if inner_key == 'Links':

                link_list = data[key][inner_key].split(',')

                for link in link_list:

                    link_entry = copy.deepcopy(carousel_entry_link_template)
                    link_entry = link_entry.replace('[Link]', link)

                    new_entry += '\n' + link_entry

            else: new_entry = data[key][inner_key]

            carousel_entry = carousel_entry.replace('[{}]'.format(inner_key), new_entry)                

        carousel_entries += '\n\n' + carousel_entry

    local_carousel_template = copy.deepcopy(carousel_template)
    local_carousel_template = local_carousel_template.replace('[CAROUSEL-INDICATORS]', carousel_indicators)
    local_carousel_template = local_carousel_template.replace('[CAROUSEL-INNER]', carousel_inner)
    local_carousel_template = local_carousel_template.replace('[CAROUSEL-ELEMENTS]', carousel_entries)

    index_template = index_template.replace('[CAROUSEL]', local_carousel_template)

    # write to output
    print 'Writing to file (index.html) ...'

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

    # write to output
    print 'Writing to file (cfp.html) ...'

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

#!/usr/bin/env bash

'''
------
Auto-compile Webpages for ICAPS 2019
------
Author :: Tathagata Chakraborti
Date   :: 02/14/2019
------
'''


'''
packages
'''

import openpyxl as xl
import argparse, sys, random, copy


'''
global variables 
'''

data = {} 
pc_list = {}
paper_list = {}

'''
html templates
'''

with open('templates/index-template.html', 'r') as temp:
    index_template = temp.read()

with open('templates/cfp-template.html', 'r') as temp:
    cfp_template = temp.read()

with open('templates/workshop-template.html', 'r') as temp:
    workshop_template = temp.read()

with open('templates/header-template.html', 'r') as temp:
    header_template = temp.read()

with open('templates/navbar-template.html', 'r') as temp:
    navbar_template = temp.read()

with open('templates/dates-template.html', 'r') as temp:
    dates_template = temp.read()

with open('templates/quicklinks-template.html', 'r') as temp:
    quicklinks_template = temp.read()

with open('templates/program-template.html', 'r') as temp:
    program_template = temp.read()

with open('templates/track-paper-single.html', 'r') as temp:
    track_paper_single_template = temp.read()

with open('templates/organizing-team-template.html', 'r') as temp:
    organizing_team_template = temp.read()

with open('templates/track-table.html', 'r') as temp:
    track_table_template = temp.read()

with open('templates/track-table-single.html', 'r') as temp:
    track_table_single_template = temp.read()

'''
table stubs
'''

track_table_td = '<tr><td>[NAME]<span class="text-muted d-none"> &middot; [AFFILIATION]</span></td></tr>\n'
paper_table_td = '<tr><td>[TITLE]<span class="text-muted"> &bull; [AUTHORS] <span class="d-none">[Short Paper]</span></span></td></tr>\n'

''''''

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
method :: cache data from xlsx file
'''
def cache(filename = 'data.xlsx', pc_filename = 'icaps19_info/ICAPS-2019_PC.xlsx', papers_filename = 'icaps19_info/ICAPS-2019_accepted.xlsx'):

    global data, pc_list, paper_list

    print( 'Reading highlights...' )

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

    print( 'Reading PC list...' )

    wb = xl.load_workbook(pc_filename)

    for sheet_name in wb.sheetnames:

        dict_entry = {}

        for row in wb[sheet_name]:

            row_values = [str(item.value).strip() for item in row][:4]

            key   = row_values[3]
            entry = ["{} {}".format(row_values[0], row_values[1]), row_values[2]]

            if key in dict_entry:
                dict_entry[key].append(entry)
            else:
                dict_entry[key] = [entry]

        pc_list[str(sheet_name)] = dict_entry


    print( 'Reading Paper list...' )

    wb = xl.load_workbook(papers_filename)

    title_flag = False
    for row in wb["Accepted"]:

        if not title_flag:
            title_flag = True
        else:

            row_values = [str(item.value).strip() for item in row]

            key   = row_values[4]
            entry = row_values[1:4]

            if key in paper_list:
                paper_list[key].append(entry)
            else:
                paper_list[key] = [entry]


'''
method :: write index.html
'''
def write_file(args):

    global index_template, cfp_template, workshop_template, organizing_team_template, program_template

    # cache data
    print( 'Reading data...' )
    cache()

    # write problem file
    print( 'Compiling index.html ...' )

    # writing templates
    print( 'Writing templates ...' )

    index_template = index_template.replace('[HEADER]', header_template)    
    index_template = index_template.replace('[NAVBAR]', navbar_template)    
    index_template = index_template.replace('[DATES]', dates_template)    
    index_template = index_template.replace('[QUICKLINKS]', quicklinks_template)    

    index_template = index_template.replace('[INDEX]', '')
    index_template = index_template.replace('[CFP]', 'cfp.html')
    index_template = index_template.replace('[WORKSHOPS]', 'workshops.html')

    # write primary carousel section
    print( 'Writing carousel ...' )

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
    print( 'Writing to file (index.html) ...' )

    with open('../index.html', 'w') as output_file:
        output_file.write(index_template)

    # write cfp file
    print( 'Compiling cfp.html ...' )

    # writing templates
    print( 'Writing templates ...' )

    cfp_template = cfp_template.replace('[HEADER]', header_template)    
    cfp_template = cfp_template.replace('[NAVBAR]', navbar_template)    
    cfp_template = cfp_template.replace('[DATES]', dates_template)    
    cfp_template = cfp_template.replace('[QUICKLINKS]', quicklinks_template)    

    # write to output
    print( 'Writing to file (cfp.html) ...' )

    with open('../calls.html', 'w') as output_file:
        output_file.write(cfp_template)

    # write workshops file
    print( 'Compiling workshops.html ...' )

    # writing templates
    print( 'Writing templates ...' )

    workshop_template = workshop_template.replace('[HEADER]', header_template)    
    workshop_template = workshop_template.replace('[NAVBAR]', navbar_template)    
    workshop_template = workshop_template.replace('[DATES]', dates_template)    
    workshop_template = workshop_template.replace('[QUICKLINKS]', quicklinks_template)    

    # write to output
    print( 'Writing to file (workshops.html) ...' )

    with open('../workshops.html', 'w') as output_file:
        output_file.write(workshop_template)

    # write committees file
    print( 'Compiling organizing_team.html ...' )

    # writing templates
    print( 'Writing templates ...' )

    track_tables_stub = ""

    for track in pc_list:

        temp_track_table_template = copy.deepcopy(track_table_template).replace('[TRACK-NAME]', "{} Track".format(track))
        temp_table_stub = ""

        for role in pc_list[track]:

            temp_table_stub_single = ""

            for person in pc_list[track][role]:

                if person[1] != "None":
                    temp_table_stub_single += track_table_td.replace('[NAME]', person[0]).replace('[AFFILIATION]', person[1]).replace("d-none", "")
                else:
                    temp_table_stub_single += track_table_td.replace('[NAME]', person[0]).replace('[AFFILIATION]', "")

            temp_track_table_single_template = copy.deepcopy(track_table_single_template).replace('[ROLE]', role)
            temp_track_table_single_template = temp_track_table_single_template.replace('[ENTRIES]', temp_table_stub_single)

            temp_table_stub += "\n\n" + temp_track_table_single_template

        temp_track_table_template = temp_track_table_template.replace('[TRACK-TABLE]', temp_table_stub)
        track_tables_stub += "\n\n\n" + temp_track_table_template

    organizing_team_template = organizing_team_template.replace('[HEADER]', header_template)    
    organizing_team_template = organizing_team_template.replace('[NAVBAR]', navbar_template)    
    organizing_team_template = organizing_team_template.replace('[DATES]', dates_template)    
    organizing_team_template = organizing_team_template.replace('[QUICKLINKS]', quicklinks_template)    

    organizing_team_template = organizing_team_template.replace('[TRACK-TABLES]', track_tables_stub)

    # write to output
    print( 'Writing to file (organizing-team.html) ...' )

    with open('../organizing-team.html', 'wb') as output_file:
        output_file.write(organizing_team_template.encode("utf-8"))

    # write program file
    print( 'Compiling program.html ...' )

    # writing templates
    print( 'Writing templates ...' )

    paper_list_stub = ""

    track_order = ["Main Track", "Novel Applications Track", "Planning and Learning Track", "Robotics Track"]

    for track in track_order:

        temp_track_paper_single_template = copy.deepcopy(track_paper_single_template).replace('[TRACK]', track)

        temp_papers_list_stub = ""

        for paper in paper_list[track]:
            temp = paper_table_td.replace('[TITLE]', paper[1]).replace('[AUTHORS]', paper[0])

            if paper[2] == "Short":
                temp = temp.replace("d-none", "")

            temp_papers_list_stub += temp

        paper_list_stub += "\n\n" + temp_track_paper_single_template.replace('[ENTRIES]', temp_papers_list_stub)

    program_template = program_template.replace('[HEADER]', header_template)    
    program_template = program_template.replace('[NAVBAR]', navbar_template)    
    program_template = program_template.replace('[DATES]', dates_template)    
    program_template = program_template.replace('[QUICKLINKS]', quicklinks_template)    

    program_template = program_template.replace('[PAPERS]', paper_list_stub)

    # write to output
    print( 'Writing to file (program.html) ...' )

    with open('../program.html', 'wb') as output_file:
        output_file.write(program_template.encode("utf-8"))

    print( 'Done.' )


'''
method :: main
'''
def main():

    parser = argparse.ArgumentParser(description='''Auto-compile Webpages of ICAPS 2019 Homepage.''', epilog='''Usage >> python compile_carousel.py''')
    args = parser.parse_args()

    if '-h' in sys.argv[1:]:
        print( parser.print_help() )
        sys.exit(1)
    else:
        write_file(args)


if __name__ == "__main__":
    main()

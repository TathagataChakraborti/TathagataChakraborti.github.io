#!/usr/bin/env bash

import openpyxl as xl

total = 0
affiliation_data = {}

wb = xl.load_workbook('data.xlsx')

for row in wb["LOCATIONS"]:

    for item in row:

        item = str(item.value).strip()

        if item != 'None':
            total += 1

            if item in affiliation_data:
                affiliation_data[item] += 1
            else:
                affiliation_data[item] = 1

for key in affiliation_data:
    print('["{}", {}, {}],'.format(key, affiliation_data[key], 100*affiliation_data[key]/total))